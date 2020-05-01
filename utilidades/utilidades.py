import requests
import string

def Recebe(token):

    r = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token='+token)
    saida=r.json()
    print(saida)
    with open('answer.json','wb') as file:
        file.write(r.content)


    #with open('./answer.json', 'r') as json_file:
    #    dados = json.load(json_file)

def Decifra(entrada,casas):
    abcdario = list(string.ascii_lowercase)
    #print("Iniciando a localizacao")
    try:
        if entrada in abcdario:
            nposicao=abcdario.index(entrada) - casas
            #print(abcdario[nposicao])
            return(abcdario[nposicao])
 
        else:
            #print("Estou fora da lista")
            return(entrada)
    except:
        print("Erro")

#saida=Decifra("w",4) # se for 4, deve retornar b
#print(saida)

def EnviaResposta(token):
    files = {'answer': open('answer.json', 'rb')}
    #headers = {'Content-type': 'multipart/form-data'}
    r = requests.post('https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token='+token,files=files)
    saida=r.headers
    print(saida)
    print(r.status_code)
    print(r.text)
