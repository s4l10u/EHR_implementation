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
echo '+++++++++++++++ Add Bootstrap Node +++++++++++++'
echo '++++++++++++++++++++++++++++++++++++++++++++++++'



while [[ $STATUS == 'y' ]]; do

read -p 'Please enter host IP address ' ip

echo ' run this following command for IPFS_PATH=~/.ipfs ipfs config show | grep "PeerID" '

read -p 'Please enter identity of the node  ' id

IPFS_PATH=~/.ipfs ipfs bootstrap add /ip4/$ip/tcp/4001/ipfs/$id

read  -p 'Add a other bootstrap node ( Y / N) ' STATUS

done

IPFS_PATH=~/.ipfs ipfs config show