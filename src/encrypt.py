from cryptography.fernet import Fernet

def generate_key():
    """
    generates a key for symmetric encryption and saves it to a file 'secret.key'
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    """
    loads the key named "secret.key" from the current directory
    """
    return open("secret.key", "rb").read()


def encrypt_message(message):
    key = load_key()
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)

    print(encrypted_message)
    return encrypted_message


def decrypt_message(encrypted_message):
    """
    decrypts a message
    """
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)

    print(decrypted_message.decode())


if __name__ == "__main__":
    generate_key()
    encrypted_msg = encrypt_message("here's the tea, encrypt this shit!")
    print()
    print()
    decrypt_message(encrypted_msg)
