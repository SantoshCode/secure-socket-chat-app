"""RSA WRAPPER."""

import os
import rsa


class RSAWrapper:
    """
    A wrapper class for RSA encryption.

    The RSAWrapper class provides a convenient wrapper around the RSA
    encryption algorithm.
    It can be used to generate, store and retrieve RSA public and private keys,
    and perform encryption and decryption operations using these keys.
    """

    def __init__(self):
        """
        Initialize the instance variables for the RSAWrapper class.

        Attributes:
        - NBITS (int): Represents the number of bits in the RSA key,
          initialized as 1024.
        - server_pub (None or object): Represents the server's public key,
          initialized as None.
        - server_private (None or object): Represents the server's private key,
          initialized as None.
        """
        self.NBITS = 1024
        self.server_pub = None
        self.server_private = None

    def init_load_server_keys(self):
        """Load server keys."""
        print('Loading keys ....')
        with open(
            os.path.join('keys', 'server.public.pem'), 'rb'
        ) as f:
            self.server_pub = rsa.PublicKey.load_pkcs1(f.read())
        with open(
            os.path.join('keys', 'server.private.pem'), 'rb'
        ) as f:
            self.server_private = rsa.PrivateKey.load_pkcs1(f.read())
        print('Loading keys success ✅')

    def generate(self, machine):
        """Generate public key and private key.

        Args:
            direction (str): Define client or server
        """
        print(f'Generating public and private key for {machine}')
        public_key, private_key = rsa.newkeys(self.NBITS)

        with open(
            os.path.join('keys',
                         machine + '.private.pem'), 'wb'
        ) as f:
            f.write(private_key.save_pkcs1("PEM"))
        with open(
            os.path.join('keys',
                         machine + '.public.pem'), 'wb'
        ) as f:
            f.write(public_key.save_pkcs1("PEM"))

    def encrypt(self, public_key, message: str):
        """Encrypt message using public.

        Args:
            public_key (str): Public key
            message (str): Message to encrypt

        Returns:
            str: Decoded message
        """
        encrypted_message = rsa.encrypt(message, public_key)
        return encrypted_message

    def decrypt(self, private_key, encrypted_message):
        """Decrypt encrypted message using private key.

        Args:
            encrypted_message (str): Encrypted message

        Returns:
            str: Decrypted message
        """
        decrypted_message = rsa.decrypt(encrypted_message, private_key)
        return decrypted_message
