from cryptography.fernet import Fernet

def encrypt(password):
    key=load_key()
    cipher=Fernet(key)
    encrypted=cipher.encrypt(password.encode())
    return encrypted.decode()

def decrypt(ciphertext):
    key=load_key()
    cipher=Fernet(key)
    decrypted=cipher.decrypt(ciphertext.encode())
    return decrypted.decode()

def generate_key():
    key=Fernet.generate_key()
    with open('secret.key', 'wb') as file:
        file.write(key)

def load_key():
    with open('secret.key', 'rb') as file:
        key=file.read()
    return key
