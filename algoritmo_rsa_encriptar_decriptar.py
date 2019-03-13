import rsa

def sign(message, privkey):
    hash = rsa.compute_hash(message, 'SHA-1')
    signature = rsa.sign_hash(hash, privkey, 'SHA-1')
    return signature

def verify(message, signature, pubkey):
    verificacao = rsa.verify(message, signature, pubkey)
    if verificacao == 'SHA-1':
        return True
    return False

#Criar par de chaves
(pub, priv) = rsa.newkeys(512)


message = 'Go left at the blue tree'.encode('utf8')

crypto = rsa.encrypt(message, pub)

print('Mensagem encriptada: \n',crypto)

message = rsa.decrypt(crypto, priv)

print('Mensagem decriptada: \n',message.decode('utf8'))


########################## ASSINATURA ###################

signature = sign(message,priv)

# verify signature
print(verify(message, signature, pub))



