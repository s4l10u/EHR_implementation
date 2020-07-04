import umbral
from umbral import config
from umbral.curve import SECP256K1
config.set_default_curve(SECP256K1)
from umbral import keys, signing
from umbral import pre
from umbral.kfrags import KFrag
import os
from dotenv import load_dotenv
import pickle
import marshal
import dill
import random
import json
project_folder = os.getcwd()
load_dotenv(os.path.join(project_folder, '.env'))

#kfrags_byte= pickle.load(open('Ursulas/'+ os.getenv("FOR") + '/kfrag.cert', 'rb'))
kfrags_byte= pickle.load(open('Ursulas/Bob/kfrag.cert', 'rb'))

kfrags=[ KFrag.from_bytes(kfrag)  for kfrag in kfrags_byte['kfrags']]
print(kfrags)

# kfrags = random.sample(kfrags, N)  

# correctness=capsule.set_correctness_keys(delegating=os.getenv("DELEGERPK"),receiving=os.getenv("PK_PATH"),verifying=os.getenv("DELEGERVK"))

# if False correctness:
#     Print ('Verification error')
#     break 
# else:
#     cfrags = list()                 
#     for kfrag in kfrags:
#         cfrag = pre.reencrypt(kfrag=kfrag, capsule=open(os.getenv("CAPSULE"))
#         cfrags.append(cfrag)       
