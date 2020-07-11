import umbral
from umbral import config
from umbral.curve import SECP256K1
config.set_default_curve(SECP256K1)
from umbral import keys, signing
from umbral import pre
from umbral.kfrags import KFrag
from umbral.config import default_params
params = default_params()
import os
from dotenv import load_dotenv
import pickle
import marshal
import random
import json
project_folder = os.getcwd()
load_dotenv(os.path.join(project_folder, '.env'))

#kfrags_byte= pickle.load(open('Ursulas/'+ os.getenv("FOR") + '/kfrag.cert', 'rb'))


capsule_byte= pickle.load(open(os.getenv("CAPSULE"), 'rb'))
capsule = pre.Capsule.from_bytes(capsule_byte,params)

# file = open(os.getenv("CAPSULE"), 'rb')  # The "rb" clause tells the open method to read the file as bytes
# capsule_byte = file.read()
# capsule = pre.Capsule.from_bytes(capsule_byte,params)

public_key_byte= pickle.load(open(os.getenv("DELEGERPK"), 'rb'))
public_key= keys.UmbralPublicKey.from_bytes(public_key_byte)

verifying_key_byte= pickle.load(open(os.getenv("DELEGERVK"), 'rb'))
verifying_key= keys.UmbralPublicKey.from_bytes(verifying_key_byte)

Bob_public_key_byte= pickle.load(open(os.getenv("PK_PATH"), 'rb'))
Bob_public_key= keys.UmbralPublicKey.from_bytes(Bob_public_key_byte)

kfrags_byte= pickle.load(open('Ursulas/'+ os.getenv("FOR") +'/kfrag.cert', 'rb'))

kfrags=[ KFrag.from_bytes(kfrag)  for kfrag in kfrags_byte]

kfrags_info= pickle.load(open('Ursulas/'+ os.getenv("FOR") +'/kfrags.info', 'rb'))

kfrags = random.sample(kfrags, int(kfrags_info['N']))  

correctness=capsule.set_correctness_keys(delegating=public_key,receiving=Bob_public_key,verifying=verifying_key)

cfrags = list()  
if False in correctness:
    print ('Verification error')
    exit() 
else:              
    for kfrag in kfrags:
        cfrag = pre.reencrypt(kfrag=kfrag, capsule=capsule )
        cfrags.append(cfrag)       



cfrags_byte=[umbral.cfrags.CapsuleFrag.to_bytes(cfrag) for cfrag in cfrags]
pickle.dump(cfrags_byte,open('Re-encrypted/'+os.getenv("FOR")+'/cfrags','wb'))

