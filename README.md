Socket client-server communication through AES & RSA encryption
================================================================

Description
------------

This project implements secure socket communication between a client and server through the use of the Advanced Encryption Standard (AES) and the Rivest-Shamir-Adleman (RSA) encryption algorithms.

The server generates a public-private key pair using RSA and shares the public key with the client. The server then uses this public key to encrypt an AES key, which is sent to the client for use in further communication. All subsequent messages exchanged between the client and server are encrypted using the AES key, ensuring the confidentiality and privacy of the communication.

This project serves as a demonstration of the implementation of secure socket communication and the use of encryption algorithms to protect sensitive information in communication.

Setup
-------

```sh
$ git clone https://github.com/SantoshCode/secure-socket-chat-app.git
$ cd secure-socket-chat-app
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Terminal session 1
```sh
$ python3 server.py
```

Terminal session 2
```sh
$ python3 client.py
```
