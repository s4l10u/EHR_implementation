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
import json
project_folder = os.getcwd()
load_dotenv(os.path.join(project_folder, '.env'))


private_key_byte= pickle.load(open('keys/'+ os.getenv("WALLET") + '/private_key.pem', 'rb'))

private_key= keys.UmbralPrivateKey.from_bytes(private_key_byte)

signing_key_byte= pickle.load(open('keys/'+ os.getenv("WALLET") + '/signing_key.pem', 'rb'))

signing_key= keys.UmbralPrivateKey.from_bytes(signing_key_byte)

Signer = signing.Signer(private_key=signing_key)

public_key_byte= pickle.load(open(os.getenv("PK_PATH"), 'rb'))

public_key= keys.UmbralPublicKey.from_bytes(public_key_byte)

kfrags = pre.generate_kfrags(delegating_privkey=private_key,signer = Signer,receiving_pubkey=public_key,threshold= int(os.getenv("THRESHOLD")),N= int(os.getenv("N")))

kfrags_dict = {} 
kfrags_dict["kfrags"] = [ KFrag.to_bytes(kfrag)  for kfrag in kfrags]
kfrags_dict["FOR"]= os.getenv("FOR")
kfrags_dict["THRESHOLD"]= os.getenv("THRESHOLD")
kfrags_dict["N"]= os.getenv("N")
outfile=open('Ursulas/'+ os.getenv("FOR") +'/kfrag.cert','wb')
pickle.dump(kfrags_dict,outfile)
outfile.close()









# s=json.dumps(variables)
# variables2=json.loads(s)
# assert(variables==variables2)










# outfile.write(str(kfrags))
# outfile.close()

# outfile = open('Ursulas/'+ os.getenv("FOR") +'/kfrag.cert','wb')
# kfrags_dict = {} 
# kfrags_dict[os.getenv("FOR")] = kfrags
# # pickle.dump(kfrags_dict,outfile)



# # with open('Ursulas/'+ os.getenv("FOR") +'/kfrag.cert','wb') as f:
# #     pickle.dump(kfrags, f)


# with open('Ursulas/'+ os.getenv("FOR") +'/kfrag.cert','wb') as handle:
#     pickle.dump(kfrags_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
