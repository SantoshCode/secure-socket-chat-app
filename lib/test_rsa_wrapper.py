"""RSA WRAPPER TEST."""
import os
import unittest
import rsa

from rsa_wrapper import RSAWrapper


class TestRSAWrapper(unittest.TestCase):
    def setUp(self):
        self.rsa_wrapper = RSAWrapper()
        self.message = "This is a secret message."
        self.rsa_wrapper.generate("client")

    def test_generate(self):
        self.assertTrue(os.path.exists(
            os.path.join('keys', 'client.private.pem')))
        self.assertTrue(os.path.exists(
            os.path.join('keys', 'client.public.pem')))

    def test_encrypt_decrypt(self):
        with open(os.path.join('keys', 'client.public.pem'), 'rb') as f:
            public_key = rsa.PublicKey.load_pkcs1(f.read())
        with open(os.path.join('keys', 'client.private.pem'), 'rb') as f:
            private_key = rsa.PrivateKey.load_pkcs1(f.read())

        encrypted_message = self.rsa_wrapper.encrypt(
            public_key, self.message.encode())
        decrypted_message = self.rsa_wrapper.decrypt(
            private_key, encrypted_message)
        self.assertEqual(self.message.encode(), decrypted_message)

    def test_init_load_server_keys(self):
        self.rsa_wrapper.init_load_server_keys()
        self.assertIsInstance(self.rsa_wrapper.server_pub, rsa.PublicKey)
        self.assertIsInstance(self.rsa_wrapper.server_private, rsa.PrivateKey)


if __name__ == '__main__':
    unittest.main()
