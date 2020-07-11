import umbral
from umbral import config
from umbral.curve import SECP256K1
config.set_default_curve(SECP256K1)
from umbral import keys, signing
from umbral import pre

from umbral.curve import Curve
from umbral.params import UmbralParameters

from umbral.config import default_params
params = default_params()

#curve = default_curve()


import os
from dotenv import load_dotenv

import pickle
import marshal

project_folder = os.getcwd()
load_dotenv(os.path.join(project_folder, '.env'))

file = open(os.getenv("NAME"), 'rb')  # The "rb" clause tells the open method to read the file as bytes
ciphertext = file.read()

# file = open(os.getenv("CAPSULE"), 'rb')  # The "rb" clause tells the open method to read the file as bytes
# capsule_byte = file.read()


capsule_byte= pickle.load(open(os.getenv("CAPSULE"), 'rb'))
capsule = pre.Capsule.from_bytes(capsule_byte,params)


private_key_byte= pickle.load(open('keys/' + os.getenv("WALLET") +'/private_key.pem', 'rb'))

private_key= keys.UmbralPrivateKey.from_bytes(private_key_byte)

cfrags_byte=pickle.load(open('Re-encrypted/'+os.getenv("WALLET")+'/cfrags', 'rb'))
cfrags=[umbral.cfrags.CapsuleFrag.from_bytes(cfrag) for cfrag in cfrags_byte]


public_key_byte= pickle.load(open(os.getenv("DELEGERPK"), 'rb'))
public_key= keys.UmbralPublicKey.from_bytes(public_key_byte)

verifying_key_byte= pickle.load(open(os.getenv("DELEGERVK"), 'rb'))
verifying_key= keys.UmbralPublicKey.from_bytes(verifying_key_byte)

Bob_public_key_byte= pickle.load(open(os.getenv("PK_PATH"), 'rb'))
Bob_public_key= keys.UmbralPublicKey.from_bytes(Bob_public_key_byte)


correctness=capsule.set_correctness_keys(delegating=public_key,receiving=Bob_public_key,verifying=verifying_key)

for cfrag in cfrags:
    capsule.attach_cfrag(cfrag)


cleartext = pre.decrypt(ciphertext=ciphertext,capsule=capsule,decrypting_key=private_key)


output_file = open('Re-decrypted/'+ os.getenv("WALLET")+'/'+os.getenv("OUTPUT_PATH"), "wb")
output_file.write(cleartext)
output_file.close()

#pickle.dump(cleartext,open('Re-decrypted/'+ os.getenv("WALLET")+'/'+os.getenv("OUTPUT_PATH"), "wb"))
