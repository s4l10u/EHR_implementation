# Print the usage message
function Help() {
  echo "Usage: "
  echo "  ehr.sh <Mode> [Flags]"
  echo "    <Mode>"
  echo "      - 'add'        - add a new EHRs file, it can be pdf, jpeg, xml, text,..  "
  echo "      - 'retrieve'   - retrive file from Off-chain"
  echo "      - 'genkey'     - Genete user keys( private and public)"
  echo "      - 'enc'        - Encrypt a given file and store it localy"
  echo "      - 'dec'        - Decrypt a given file and store it localy"
  echo "      - 'gen-re-key' - Create an re-encryption key for a given public key"
  echo "      - 're-enc'     - re-encrypt a given for "
 
  echo
  echo "    Flags:"
  echo
  echo "   -h <Help> -  "
  echo
  echo "    -n <Name> -  Name of the file"
  echo
  echo "    -o <Output> - output path )"
  echo
  echo "    -pk <Path public key> - public key  path "
  echo
  echo "    -i < ID> - EHR Identifier "
  echo
  echo "    -c < ID> - Capsule  "
  echo
  echo "    -N < Kfrag > - the total number of kfrags "
  echo
  echo "    -t < threshold > - the minimum number of kfrags needed to activate a capsule "
  echo
  echo "    -w < WALLET > - Folder for generated keys"
  echo
  echo "    -f < FOR > - Owner of re-encrtyption key "
  echo
  echo "    -dpk <DELEGER PUBKEY > - Deleger public keys"
  echo
  echo "    -vpk < DELEGER VERIFYKEY > - Deleger verifying keys "
  echo
  
  echo " Possible Mode and flags"
  echo
  echo "  ehr.sh add -n  -o "
  echo
  echo "  ehr.sh retrieve -i -o "
  echo
  echo "  ehr.sh gen-re-key -pk -N -t -o "

  echo
  echo " Examples:"
  echo
  echo "  ./ehr.sh add -n Parasitological.pdf -o ~/my/ehr/folder"
  echo
  echo "  ./ehr.sh gen-re-key -pk public_key.cert -t 10 -N 20 -o ~/my/ehr/re-keys"
  echo
  echo "  ./ehr.sh enc  -n scan.jpeg  -w Alice"
  echo
  echo " ./ehr.sh gen-re-key -w Jean -t 10 -N 15 -f Bob -pk keys/Bob/public_key.cert"
  echo
  echo "./ehr.sh re-enc -f Bob -dpk keys/Jean/public_key.cert -dvk keys/Jean/verifying_key.cert -c Encrypted/Jean/scan.jpeg.cap -pk keys/Bob/public_key.cert "
  echo
  echo " ./ehr.sh dec   -n Encrypted/Alice/scan.jpeg.enc  -c Encrypted/Alice/scan.jpeg.cap  -w Alice -o scan.jpeg"
}
export N=1
export THRESHOLD=1

## Parse mode
# # Local .env
# source <(sed -E -n 's/[^#]+/export &/ p' .env)

if [[ $# -lt 1 ]] ; then
  Help
  exit 0
else
  export MODE=$1
  shift
fi

# parse flags

while [[ $# -ge 1 ]] ; do
  key="$1"
  case $key in
  -h )
    Help
    exit 0
    ;;
    -n )
    export NAME="$2"
    shift
    ;;
    -c )
    export CAPSULE="$2"
    shift
    ;;
  -o )
    export OUTPUT_PATH="$2"
    shift
    ;;
  -pk )
    export PK_PATH="$2"
    shift
    ;;
  -dpk )
    export DELEGERPK="$2"
    shift
    ;;
  -dvk )
    export DELEGERVK="$2"
    shift
    ;;
  -t )
    export THRESHOLD="$2"
    shift
    ;;

  -N )
    export N="$2"
    shift
    ;;
  -i )
    export ID="$2"
    shift
    ;;
  -f)
    export FOR="$2"
    shift
    ;;
  -w )
    export WALLET="$2"
    shift
    ;;
  * )
    echo
    echo "Unknown flag: $key"
    echo
    Help
    exit 1
    ;;
  esac
  shift
done



function Add_EHR(){
    echo 'EHR'
}

function Retrieve_EHR(){
    echo 'EHR'
}

function Genkey(){
    cd keys
    [ ! -d "$WALLET" ] && mkdir -p "$WALLET"
    cd ..
    python genkey.py
}



function Encrypt(){
  cd Encrypted
  [ ! -d "$WALLET" ] && mkdir -p "$WALLET"
  cd ..
  #cp  -u $NAME  docs
  python Encrypt.py
}


function Decrypt(){
    cd Decrypted
    [ ! -d "$WALLET" ] && mkdir -p "$WALLET"
    cd ..
    python Decrypt.py
}

function GenReKey(){
   cd Ursulas
   [ ! -d "$FOR" ] && mkdir -p "$FOR"
   cd ..
   python genrekey.py
}

function ReEncrypt(){
  cd Re-encrypted
  [ ! -d "$FOR" ] && mkdir -p "$FOR"
  cd ..
  python re-encrypt.py
}
# Determine mode of operation and printing out what we asked for
if [ "$MODE" == "add" ]; then
  echo
  Add_EHR
  echo " + Encrypt  file"
  echo
  echo " + Store encrypted file and the capsule  to IPFS "
  echo 
  echo " + Retrive the hash file from IPFS"
  echo
  echo " + Connect to an organisation peer"
  echo
  echo " + Invok the chaincode"
  echo
  echo " + Create an update transaction"
  echo
  echo " + Add a new asset to the blockchain  "
  echo 
  Add_EHR

elif [ "$MODE" == "retrieve" ]; then
  echo
  Retrieve
  echo
  echo " + Query $ID EHR asset from the ledger      "
  echo
  echo " + Revieve the  $ID EHR asset file form IPFS   "
  echo
  echo " + Decrypt   $ID EHR"
  echo
  echo " + Store the derypted file to $OUTPUT_PATH  "
  echo

  echo

elif [ "$MODE" == "genkey" ]; then
  echo
  Genkey
  echo " + Setting a default curve"
  echo
  echo " + Genete private and public key"
   echo
  echo " + Genete signing and verifying key"
  echo
  echo " + Store keys  to $WALLET WALLET"
  echo

elif [ "$MODE" == "enc" ]; then
  
  echo
  Encrypt
  echo " + Encrypt  file"
  echo
  echo " + Store encrypted file and the capsule  to $OUTPUT_PATH"
  echo

elif [ "$MODE" == "dec" ]; then
  echo
  Decrypt
  echo
  echo " + Decrypt  file"
  echo
  echo " + Store decrypted file and the capsule  to $OUTPUT_PATH +"
  echo
 


elif [ "$MODE" == "gen-re-key" ]; then
  echo
  GenReKey
  echo
  echo " + creates re-encryption key"
  echo
  echo " + fragments the re-encryption key to $N kfrag"
  echo
  echo " + Send kfrag to $N proxies or Ursulas"
  echo

elif [ "$MODE" == "re-enc" ]; then
  echo
  ReEncrypt
  echo " + Retrieve kfrags from proxies"
  echo
  echo " + perform re-encryption"
  echo
  echo " + Store the re-encrypted capsule to IPFS"
  echo

else
  Help
  exit 1
fi


