import hashlib

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.exceptions import InvalidSignature

private_key = ec.generate_private_key(ec.SECP256K1(), default_backend())
public_key = private_key.public_key()

data = bytes("This is the data I will sign", 'utf-8')


digest = hashes.Hash(hashes.SHA256())
digest.update(data)
# digest.finalize()

print("Digest", digest.finalize().hex())


signature = private_key.sign(data, ec.ECDSA(hashes.SHA256()))

# print(signature)

#data += b'1'
try:
    public_key.verify(signature, data, ec.ECDSA(hashes.SHA256()))
    print("Signature verified")
except InvalidSignature:
    print("Signature verifcation failed")
except:
    print("Somthing went wrong...")
