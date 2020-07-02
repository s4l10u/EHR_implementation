import umbral
from umbral import config
from umbral.curve import SECP256K1
config.set_default_curve(SECP256K1)
from umbral import keys, signing
from umbral import pre
import os
from dotenv import load_dotenv
import pickle
import marshal
import dill
project_folder = os.getcwd()
load_dotenv(os.path.join(project_folder, '.env'))


# Read the file
file = open(os.getenv("NAME"), "rb")  
plaintext = file.read()

# Encrypt it
alices_public_key_byte= pickle.load(open('keys/public_key.cert', 'rb'))

alices_public_key= keys.UmbralPublicKey.from_bytes(alices_public_key_byte)

ciphertext, capsule = pre.encrypt(alices_public_key, plaintext)

#os.environ["capsule"]=capsule
#os.getenv("capsule")


# save the cipher and capsule

pickle.dump(ciphertext, open(os.getenv("OUTPUT_PATH"), "wb") )

capsule_byte = pre.Capsule.to_bytes(capsule)

#print (  pre.Capsule.from_bytes(capsule_byte))

pickle.dump(capsule_byte,open('Capsule_' + os.getenv("NAME"),'wb'))
