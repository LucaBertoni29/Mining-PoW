import hashlib

"""Il target rappresenta la difficoltà che viene quantificata in base al numero di zeri iniziali
più zeri sono richiesti più la difficoltà è alta"""

target = int(input("Inserire numero di 0 richiesti per accettare il blocco: "))

check_target = "0" * target

nonce = 0

print ("Nonce |  Hash")
print ("---------------------------------------------------------------------------")

while True :
    block = "Bob invia 1 BTC a Alice"
    block = (block+str(nonce))
    hash = hashlib.sha256(block.encode('utf-8')).hexdigest()
    hash = hashlib.sha256(hash.encode('utf-8')).hexdigest()

    print (nonce, "\t", hash)

    if (hash[:target] == check_target):
            break

    nonce += 1

print ("\t", "^" * target)
