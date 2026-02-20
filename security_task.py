import hashlib
from cryptography.fernet import Fernet

# --- TASK 1: THE PROBLEM (THREAT ANALYSIS) ---
# We analyze that plain text passwords are dangerous.
def analyze_threat():
    print("--- TASK 1: THREAT ANALYSIS ---")
    print("Finding: Storing passwords as 'Riddhi123' is a HIGH VULNERABILITY.")
    print("Risk: If the database is stolen, accounts are compromised immediately.\n")

# --- TASK 2: THE SOLUTION (SECURE IMPLEMENTATION) ---
def implement_defense(user_password):
    print("--- TASK 2: SECURE IMPLEMENTATION ---")
    
    # 1. Hashing (for Credentials)
    # This turns your password into a 64-character 'code'
    hashed = hashlib.sha256(user_password.encode()).hexdigest()
    print(f"Original Password: {user_password}")
    print(f"Secure Hashed Version: {hashed}")

    # 2. Encryption (for Sensitive Files)
    key = Fernet.generate_key()
    cipher = Fernet(key)
    secret_note = "Confidential: HackWeHub Internship Project"
    encrypted = cipher.encrypt(secret_note.encode())
    print(f"\nEncrypted Project File Content: {encrypted}")
    print("Status: System Hardened Successfully.")

# RUN THE SIMULATION
analyze_threat()
implement_defense("Riddhi@2025")import hashlib
from cryptography.fernet import Fernet

# --- TASK 1: THE PROBLEM (THREAT ANALYSIS) ---
# We analyze that plain text passwords are dangerous.
def analyze_threat():
    print("--- TASK 1: THREAT ANALYSIS ---")
    print("Finding: Storing passwords as 'Riddhi123' is a HIGH VULNERABILITY.")
    print("Risk: If the database is stolen, accounts are compromised immediately.\n")

# --- TASK 2: THE SOLUTION (SECURE IMPLEMENTATION) ---
def implement_defense(user_password):
    print("--- TASK 2: SECURE IMPLEMENTATION ---")
    
    # 1. Hashing (for Credentials)
    # This turns your password into a 64-character 'code'
    hashed = hashlib.sha256(user_password.encode()).hexdigest()
    print(f"Original Password: {user_password}")
    print(f"Secure Hashed Version: {hashed}")

    # 2. Encryption (for Sensitive Files)
    key = Fernet.generate_key()
    cipher = Fernet(key)
    secret_note = "Confidential: HackWeHub Internship Project"
    encrypted = cipher.encrypt(secret_note.encode())
    print(f"\nEncrypted Project File Content: {encrypted}")
    print("Status: System Hardened Successfully.")

# RUN THE SIMULATION
analyze_threat()
implement_defense("Riddhi@2025")
