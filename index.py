import hashlib

#This is the public key
publicKey = '041e7bcc70c72770dbb72fea022e8a6d07f814d2ebe4de9ae3f7af75bf706902a7b73ff919898c836396a6b0c96812c3213b99372050853bd1678da0ead14487d7'

#The public key is currently in hex format, the hash input needs it to be in a bytearray.
publicKeyAsbyteArr = bytearray.fromhex(publicKey)

#Below we are perfroming the first sha256 hash. The digest() converts the output to a bytearray format.
#If this was changed to .hexdigest() the output would be readable and come out in hex.
firstHash = hashlib.sha256(publicKeyAsbyteArr).digest()

#This line of code will apply ripemd160 hash to the first hash and output the result as a hexdigest.
#The reason we need the output in the form of a hexdigest instead of a byte array is because it is easier to append the prefix.
rm160 = hashlib.new('ripemd160', firstHash).hexdigest()

#The prefix tells us what the address represents, 00 means it is a main-net public key address.
r1 = '00' + rm160

#convert r1 to a byte array so that we can use it to perform a checksum.
r1Asbyte = bytearray.fromhex(r1)

#Here we perform a double hash and output the result as hex. This is the checksum.
dh = hashlib.sha256(hashlib.sha256(r1Asbyte).digest()).hexdigest()

#We then take the first four bytes of the cheksum and append it to 'r1'
address = (r1 + dh[0:8])

#This is the address


