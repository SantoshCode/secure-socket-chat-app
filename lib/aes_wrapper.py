"""AES WRAPPER."""
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

import pyaes


class AESWrapper:
    """
    AESWrapper class provides an implementation for AES encryption and
    decryption.

    The class is initialized with a key used for encryption and decryption. If
    a key is not provided, a random key is generated. The encrypt method
    encrypts the message and returns the ciphertext. The decrypt
    method decrypts the ciphertext and returns the original
    message.

    Attributes:
    key (bytes): The encryption key.

    Methods:
    encrypt(message: str) -> bytes
    Encrypts the message and returns the ciphertext

    decrypt(ciphertext: bytes) -> bytes:
    Decrypts the ciphertext and returns the original message.
    """

    def __init__(self, key=None):
        """Initialize class with the key used for encryption and decryption.

        Args:
            key (str, optional): The encryption key. If not provided, a random
            key will be generated
        """
        self.iv = '56402407815369799606473313783365152726939209028133773258453508982544031147012'
        if key is None:
            temp_key = get_random_bytes(AES.block_size)
            self.key = temp_key

        else:
            self.key = key

    def encrypt(self, message):
        """
        Encrypts the message using AES encryption

        Args:
        message (str): The plain text message to be encrypted.

        Returns:
        ciphertext: Ciphertext
        """
        aes = pyaes.AESModeOfOperationCTR(
            self.key, pyaes.Counter(int(self.iv)))
        ciphertext = aes.encrypt(message)
        return ciphertext

    def decrypt(self,  ciphertext):
        """
        Decrypts the ciphertext using AES encryption

        Args:
        ciphertext (bytes): The encrypted message in bytes format.

        Returns:
        bytes: The decrypted message in bytes format.
        """
        aes = pyaes.AESModeOfOperationCTR(
            self.key, pyaes.Counter(int(self.iv)))
        decrypted = aes.decrypt(ciphertext)
        return decrypted
