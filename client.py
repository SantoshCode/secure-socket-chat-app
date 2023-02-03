"""CLIENT."""
import socket

from lib.rsa_wrapper import RSAWrapper
from lib.aes_wrapper import AESWrapper

rsa_wrapper = RSAWrapper()

rsa_wrapper.init_load_server_keys()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 7634

s.connect((host, port))
while True:
    # FIRST STEP RECEIVING AES KEY
    encrypted_aes_key = s.recv(1024)
    print('Received encrypted AES key from server 🔑 ✅')

    decrypted_aes_key = rsa_wrapper.decrypt(
        rsa_wrapper.server_private, encrypted_aes_key
    )

    aes_wrapper = AESWrapper(decrypted_aes_key)

    print("Waiting for response... ⌛️")
    encrypted_server_message = s.recv(1024)

    decrypted_server_message = aes_wrapper.decrypt(
        encrypted_server_message
    )

    print("Message from server: 📩", decrypted_server_message.decode())

    client_message = input("Send message to server: ")

    encrypted_client_message = aes_wrapper.encrypt(
        client_message.encode()
    )

    s.send(encrypted_client_message)
