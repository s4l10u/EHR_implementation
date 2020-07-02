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


# class private():
#     def __init__(self):
#         self.private_key = keys.UmbralPrivateKey.gen_key()
      
#     def __repr__(self):
#         return self.private_key

# k = private()
# dill.pickles(k, open('mypicklefile', 'wb'))

# key generation and persistence storage

private_key = keys.UmbralPrivateKey.gen_key()
private_key_byte=keys.UmbralPrivateKey.to_bytes(private_key)
outfile = open('keys/'+ os.getenv("WALLET")+'/private_key.pem','wb')
pickle.dump(private_key_byte,outfile)
outfile.close()

public_key= private_key.get_pubkey()
public_key_byte= keys.UmbralPublicKey.to_bytes(public_key)
outfile = open('keys/'+ os.getenv("WALLET")+'/public_key.cert','wb')
pickle.dump(public_key_byte,outfile)
outfile.close()

