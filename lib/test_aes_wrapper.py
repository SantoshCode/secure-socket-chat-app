"""AES WRAPPER TEST."""
import unittest

from aes_wrapper import AESWrapper


class TestAESWrapper(unittest.TestCase):
    def setUp(self):
        self.key = b"1234567890123456"
        self.aes_wrapper = AESWrapper(self.key)
        self.message = "This is a secret message."

    def test_key_type(self):
        self.assertIsInstance(self.key, bytes)

    def test_encrypt_decrypt(self):
        encrypted = self.aes_wrapper.encrypt(self.message.encode())
        decrypted = self.aes_wrapper.decrypt(encrypted).decode()
        self.assertEqual(self.message, decrypted)

    def test_encrypt_decrypt_random_key(self):
        aes_wrapper = AESWrapper()
        encrypted = aes_wrapper.encrypt(self.message.encode())
        decrypted = aes_wrapper.decrypt(encrypted).decode()
        self.assertEqual(self.message, decrypted)


if __name__ == '__main__':
    unittest.main()
