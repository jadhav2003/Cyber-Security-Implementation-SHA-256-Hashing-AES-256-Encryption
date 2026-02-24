import hashlib
from cryptography.fernet import Fernet

# -------- TASK 1: Identify the Problem --------
print("----- TASK 1: THREAT ANALYSIS -----")
print("Plaintext password storage is a security risk.")
print("If the database is breached, user credentials are exposed.\n")

# -------- TASK 2: Implement the Solution --------
print("----- TASK 2: SECURE IMPLEMENTATION -----")

# Step 1: Hash the password
password = "Riddhi@2026"
hashed_password = hashlib.sha256(password.encode()).hexdigest()

print("Original Password:", password)
print("Hashed Password (SHA-256):", hashed_password)

# Step 2: Encrypt sensitive data
key = Fernet.generate_key()
cipher = Fernet(key)

data = "Confidential Internship Project File"
encrypted_data = cipher.encrypt(data.encode())

print("\nOriginal File Data:", data)
print("Encrypted Ciphertext:", encrypted_data)

print("\nSystem Secured Successfully.")