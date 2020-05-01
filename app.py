import os
import requests
import hashlib
import json
import string

from utilidades import *


token=os.environ['TOKEN_CODENATION']
#print(hashlib.sha512(b'Testando tudo').hexdigest())

#utilidades.Recebe(token)


with open('./answer.json', 'r') as json_file:
    dados = json.load(json_file)

#abcdario = list(string.ascii_lowercase)
#print(abcdario)


#print(dados['cifrado'])
frase=''
for i in dados['cifrado']:
    #print(i)
    saida=utilidades.Decifra(i,dados['numero_casas'])
    #print(saida)
    frase=frase + saida

#print(dados)
#print(dados['cifrado'])
#print(frase)
dados['decifrado']=frase
#print(dados)

d512=hashlib.sha512(frase.encode('utf-8')).hexdigest()
#print(d512)
dados['resumo_criptografico']=d512

#print(dados)
#print(type(dados))
with open('./answer.json','w') as file:
    #file.write(dados)
    json.dump(dados, file)

utilidades.EnviaResposta(token)