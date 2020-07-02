
echo '+++++++++++++++++++++++++++++++++++++++++++++++'
echo '++++Generate swark key for private network ++++'
echo '+++++++++++++++++++++++++++++++++++++++++++++++'

# Test if git is installed 

if ! [ -x "$(command -v git)" ]; then
  echo 'I require foo but it s not installed.' >&2
  $(sudo apt-get install git)
fi
if ! [ -x "$(command -v ipfs)" ]; then
  echo 'ipfs is requiered please install  https://docs.ipfs.io/install/  ....' >&2
  exit;
fi

if ! [ -x "$(command -v go)" ]; then
  echo 'Go is requiered, please install go  https://golang.org/doc/install ....' >&2
  exit;
fi


$(export PATH=$PATH:/usr/local/go/bin)

$(go get -u github.com/Kubuxu/go-ipfs-swarm-key-gen/ipfs-swarm-key-gen)
echo " swarm key generated  and is located in the directory ~/go/bin !"

echo 'Copy the generated swarm file to the .ipfs directory of each nodes.'

$(./go/bin/ipfs-swarm-key-gen > ~/.ipfs/swarm.key)


echo 'Successful execution'
