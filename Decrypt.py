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
import dill

project_folder = os.getcwd()
load_dotenv(os.path.join(project_folder, '.env'))

ciphertext = pickle.load(open(os.getenv("NAME"), 'rb'))

capsule_byte= pickle.load(open(os.getenv("CAPSULE"), 'rb'))

#capsule = keys.UmbralPrivateKey.from_bytes(capsule_byte)

capsule = pre.Capsule.from_bytes(capsule_byte,params)


private_key_byte= pickle.load(open('keys/'+os.getenv("WALLET") +'/private_key.pem', 'rb'))

private_key= keys.UmbralPrivateKey.from_bytes(private_key_byte)

cleartext = pre.decrypt(ciphertext=ciphertext,capsule=capsule,decrypting_key=private_key)


output_file = open('Encrpted/'+os.getenv("WALLET"), "wb")
output_file.write(cleartext)
output_file.close()

#pickle.dump(cleartext,open("Med_Doc/decrypted_file.jpeg", "wb")  )
print(os.getenv("OUTPUT_PATH"))
#+os.getenv("NAME")