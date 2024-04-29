import secrets
from Crypto.Cipher import AES
from cryptography.fernet import Fernet
from Crypto.Util.Padding import pad, unpad


FERNET_KEY = b"lWnYSCR3uolMu6rshe-Zx1MrP2jIoaqUMcKsOSIPBJE="


class DataSecurity:

    @staticmethod
    def save_file(stream: bytes) -> tuple[str, bytes, bytes]:
        """
        :return:
            file name
            aes key
            iv
        """
        file_name = secrets.token_hex(24)
        aes_key = secrets.token_bytes(32)
        iv = secrets.token_bytes(16)

        cipher = AES.new(aes_key, AES.MODE_CBC, iv=iv)

        with open("./files/" + file_name, "wb") as f:
            f.write(cipher.encrypt(pad(stream, 16)))

        return (file_name, aes_key, iv)

    @staticmethod
    def get_file(aes_key: bytes, iv: bytes, file: str) -> bytes:
        """
        :return:
            decrypted data
        """
        cipher = AES.new(aes_key, AES.MODE_CBC, iv=iv)
        with open("./files/" + file, "rb") as f:
            data = f.read()

        return unpad(cipher.decrypt(data), 16)

    @staticmethod
    def encrypt_key(key: bytes, iv: bytes) -> str:
        """
        :return:
            encrypted data
        """
        return Fernet(FERNET_KEY).encrypt(key + iv)[8:].decode()

    @staticmethod
    def decrypt_key(data: str) -> tuple:
        """
        :return:
            aes key
            aes iv
        """
        fernet = Fernet(FERNET_KEY).decrypt(b"gAAAAABm" + data.encode())

        return fernet[:32], fernet[32:]
