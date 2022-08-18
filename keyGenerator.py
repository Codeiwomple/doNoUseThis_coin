import hashlib

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.exceptions import InvalidSignature
"""
alice_private_key = ec.generate_private_key(ec.SECP256K1(), default_backend())
alice_public_key = alice_private_key.public_key()

bob_private_key = ec.generate_private_key(ec.SECP256K1(), default_backend())
bob_public_key = bob_private_key.public_key()


alice_addr = alice_public_key.public_bytes(
    encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)


print(alice_addr.decode())

print(alice_addr == alice_public_key.public_bytes(
    encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo))

print("Alice public: ", alice_public_key)
print("Bob public: ", bob_public_key)

data = bytes("This is the data I will sign", 'utf-8')

alice_signature = alice_private_key.sign(data, ec.ECDSA(hashes.SHA256()))
bob_signature = bob_private_key.sign(data, ec.ECDSA(hashes.SHA256()))

# print(signature)

#data += b'1'

# Verify for alice
try:
    alice_public_key.verify(alice_signature, data, ec.ECDSA(hashes.SHA256()))
    print("Alice signature verified with her key")
except InvalidSignature:
    print("Signature verifcation failed AA")
except:
    print("Somthing went wrong...")

try:
    bob_public_key.verify(bob_signature, data, ec.ECDSA(hashes.SHA256()))
    print("Bob signature verified with his key")
except InvalidSignature:
    print("Signature verifcation failed BB")
except:
    print("Somthing went wrong...")

try:
    bob_public_key.verify(alice_signature, data, ec.ECDSA(hashes.SHA256()))
    print("Alice signature verified with Bob key")
except InvalidSignature:
    print("Signature verifcation failed AB")
except:
    print("Somthing went wrong...")

if bob_private_key.public_key() != bob_public_key:
    raise Exception("You cannot sign transactions for other people")
else:
    signingKey.sign(data, ec.ECDSA(hashes.SHA256()))
    print("DONE")


digest = hashes.Hash(hashes.SHA256())
digest.update(data)
# digest.finalize()

print("Digest", digest.finalize().hex())
"""

# Create keys
alice_private_key = ec.generate_private_key(ec.SECP256K1(), default_backend())
alice_public_key = alice_private_key.public_key()

# Data for signing
data = bytes("This is the data I will sign", 'utf-8')

# Sign data
alice_signature = alice_private_key.sign(data, ec.ECDSA(hashes.SHA256()))

# Verify signature
alice_public_key.verify(alice_signature, data, ec.ECDSA(hashes.SHA256()))

# Serialise
alice_addr = alice_public_key.public_bytes(
    encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)

print("Alice address: ", alice_addr.decode())

# Create key from serialised data
newKey = serialization.load_pem_public_key(alice_addr)

# Verify with new key
newKey.verify(alice_signature, data, ec.ECDSA(hashes.SHA256()))
