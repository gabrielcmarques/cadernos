from tqdm import tqdm
import time
import requests

# for i in tqdm(range(10)):
#     time.sleep(1)

#//##//##//##//##//##//##//##//##//##//##//##//#

# lista = [1, 2, 3, 10, 15]

# for item in tqdm(lista):
#     time.sleep(1)

#//##//##//##//##//##//##//##//##//##//##//##//#

# with tqdm(total=50) as barra_progresso:
#     for i in range(10):
#         time.sleep(1)
#         barra_progresso.update(5)

#//##//##//##//##//##//##//##//##//##//##//##//#

# link = 'https://cep.awesomeapi.com.br/json/05424020'
# requisicao = requests.get(link)
# print(requisicao.json())

#//##//##//##//##//##//##//##//##//##//##//##//#

# path = "outros/barra_progresso/ceps.txt"

# with open(path, "r") as arquivo:
#     ceps = arquivo.read()
# ceps = ceps.split("\n") 
# print(ceps)           

#//##//##//##//## Barra normal://##//##//##//##//##//##//##//#


# path = "outros/barra_progresso/ceps.txt"

# with open(path, "r") as arquivo:
#     ceps = arquivo.read()
# ceps = ceps.split("\n") 

# for cep in tqdm(ceps):
#     link = f'https://cep.awesomeapi.com.br/json/{cep}'
#     requisicao = requests.get(link)
#     resposta = requisicao.json()
#     cidade = resposta['city']
#     bairro = resposta['district']
#     if cidade == "Rio de Janeiro":
#         print(cep, bairro)

#//##//##//##//## Alternativa://##//##//##//##//##//##//##//#

path = "outros/barra_progresso/ceps.txt"

with open(path, "r") as arquivo:
    ceps = arquivo.read()
ceps = ceps.split("\n") 

enderecos_entrega = []
for cep in tqdm(ceps):
    link = f'https://cep.awesomeapi.com.br/json/{cep}'
    requisicao = requests.get(link)
    resposta = requisicao.json()
    cidade = resposta['city']
    bairro = resposta['district']
    if cidade == "Rio de Janeiro":
        enderecos_entrega.append((cep, bairro))
print(enderecos_entrega)

