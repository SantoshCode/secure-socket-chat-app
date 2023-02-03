"""SERVER."""
import socket

from lib.rsa_wrapper import RSAWrapper
from lib.aes_wrapper import AESWrapper

rsa_wrapper = RSAWrapper()
aes_wrapper = AESWrapper()

rsa_wrapper.generate('server')
rsa_wrapper.init_load_server_keys()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 7634

s.bind((host, port))
s.listen(1)

con, addr = s.accept()
print("connected with", addr)
while True:
    # FIRST STEP SENDING AES KEY
    print('Sending encrypted AES key to client 🔑')
    encrypted_key = rsa_wrapper.encrypt(
        rsa_wrapper.server_pub, aes_wrapper.key
    )
    con.send(encrypted_key)

    messg = input("Send encrypted message to client: ")

    ciphertext = aes_wrapper.encrypt(messg)

    con.send(ciphertext)

    print("Waiting for response... ⌛️")

    encrypted_client_message = con.recv(1024)

    decrypted_client_message = aes_wrapper.decrypt(
        encrypted_client_message
    )

    print("Message from client: 📩", decrypted_client_message.decode())
