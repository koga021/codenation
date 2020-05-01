import requests
import string

def Recebe(token):

    r = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token='+token)
    saida=r.json()
    print(saida)
    with open('./answer.json','wb') as file:
        file.write(r.content)


    #with open('./answer.json', 'r') as json_file:
    #    dados = json.load(json_file)

def Decifra(entrada,casas):
    abcdario = list(string.ascii_lowercase)
    #print("Iniciando a localizacao")
    try:
        if entrada in abcdario:
            #print("A String existe dentro do ABCDARIO")
            #print("String de entrada: ",entrada,"Posicao: ",abcdario.index(entrada))
            #return(abcdario[abcdario.index(entrada)+casas])
            if abcdario.index(entrada)+casas >= 26:
                #print("Fora do Array de ABCDARIO")
                nposicao=abcdario.index(entrada)+casas - 26
                #print("String de saida: ",abcdario[nposicao],"Posicao: ",nposicao)
                return(abcdario[nposicao])
            else:
                #print("Dentro do Array de ABCDARIO")
                return(abcdario[abcdario.index(entrada)+casas])


        else:
            #print("Estou fora da lista")
            return(entrada)
    except:
        print("Erro")

#saida=Decifra("w",4) # se for 4, deve retornar b
#print(saida)

def EnviaResposta(token):
    files = {'answer': ('answer.json', open('./answer.json', 'rb'))}
    headers = {'Content-type': 'multipart/form-data'}
    r = requests.post('https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token='+token,files=files,headers=headers)
    saida=r.headers
    print(saida)
