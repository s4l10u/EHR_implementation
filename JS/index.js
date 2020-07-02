const IPFS = require('ipfs')
const { globSource } = IPFS

const ipfs = await IPFS.create()

//options specific to globSource
const globSourceOptions = {
  recursive: true
};

//example options to pass to IPFS
const addOptions = {
  pin: true,
  wrapWithDirectory: true,
  timeout: 10000
};

for await (const file of ipfs.add(globSource('./docs', globSourceOptions), addOptions)) {
  console.log(file)
}


