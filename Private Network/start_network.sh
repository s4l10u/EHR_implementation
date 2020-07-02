
#!/bin/bash

echo '++++++++++++++++++++++++++++++++++++++++++++++++'
echo '++++++++ Build a private IPFS network ++++++++++'
echo '++++++++++++++++++++++++++++++++++++++++++++++++'

STATUS='y'

if ! [ -x "$(command -v ipfs)" ]; then
  echo 'ipfs is requiered please install  https://docs.ipfs.io/install/  ....' >&2
  exit;
fi

if ! [ -x "$(command -v go)" ]; then
  echo 'Go is requiered, please install go  https://golang.org/doc/install ....' >&2
  exit;
fi


echo '++++++++++++++++++Requierement++++++++++++++++++'
echo 'IP adress of all node in private network'
echo 'Identity of each IPFS node'



echo '++++++++++++++++++++++++++++++++++++++++++++++++'
echo '+++++++++++++++ Start the network ++++++++++++++'
echo '++++++++++++++++++++++++++++++++++++++++++++++++'


export LIBP2P_FORCE_PNET=1 && IPFS_PATH=~/.ipfs ipfs daemon