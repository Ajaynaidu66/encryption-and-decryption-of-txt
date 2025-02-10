from cryptography.fernet import Fernet

# Generate and store a key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("✅ Secret key generated and saved as 'secret.key'")

# Load the secret key
def load_key():
    return open("secret.key", "rb").read()

# Encrypt text
def encrypt_text(text):
    key = load_key()
    fernet = Fernet(key)
    encrypted_text = fernet.encrypt(text.encode())
    return encrypted_text.decode()  # Convert bytes to string

# Decrypt text
def decrypt_text(encrypted_text):
    key = load_key()
    fernet = Fernet(key)
    decrypted_text = fernet.decrypt(encrypted_text.encode())
    return decrypted_text.decode()  # Convert bytes to string

# Main Program
if __name__ == "__main__":
    print("🔐 Text Encryption/Decryption Tool")
    print("1️⃣ Generate Key")
    print("2️⃣ Encrypt Text")
    print("3️⃣ Decrypt Text")
    
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        generate_key()
    
    elif choice == "2":
        text = input("Enter text to encrypt: ")
        encrypted = encrypt_text(text)
        print(f"🔒 Encrypted Text: {encrypted}")

    elif choice == "3":
        encrypted_text = input("Enter encrypted text: ")
        decrypted = decrypt_text(encrypted_text)
        print(f"🔓 Decrypted Text: {decrypted}")

    else:
        print("❌ Invalid choice! Please enter 1, 2, or 3.")
