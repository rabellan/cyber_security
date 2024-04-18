import hashlib

def hash_password(password):
    # Create a new SHA-1 hash object
    sha1 = hashlib.sha1() # WARNING insecure hashing algo
    
    # Update the hash object with the bytes of the string
    sha1.update(password.encode())
    
    # Get the hexadecimal representation of the digest
    hash_digest = sha1.hexdigest()
    
    return hash_digest

# Example usage
password = "IWantEmployment"
hashed_password = hash_password(password)
print("SHA-1 Hashed Password:", hashed_password)
