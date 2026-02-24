from argon2 import PasswordHasher

# Create Argon2 hasher
ph = PasswordHasher()

# Original password
password = "Riddhi@2026"

# Hash the password
hashed_password = ph.hash(password)

print("Original Password:", password)
print("Argon2 Hashed Password:", hashed_password)

# Verifying password
try:
    ph.verify(hashed_password, password)
    print("Password Verification: SUCCESS")
except:
    print("Password Verification: FAILED")