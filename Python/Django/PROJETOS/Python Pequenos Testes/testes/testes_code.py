# print("Inicio")
# assert 1 < 2
# print("FIM")

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

import requests

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
requisicao_dic = requisicao.json()

cotacao = requisicao_dic["USDBRL"]["bid"]
cotacao = float(cotacao)
print(cotacao)

preco_produto = 100
faturamento = preco_produto * cotacao 
print(faturamento)