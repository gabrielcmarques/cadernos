listOfMacs = []

with open("D:\Gabriel\Desktop\Python Pequenos Projetos\parser_csv\mac_ip_converter\mac_ip_snippets.txt", "r")as reader:
    for line in reader.readlines():
        listOfMacs.append(line)

print(listOfMacs)
print("\n" * 2)

RemoveDash = []
RemoveLine = []
NewMacs = []


# Trocando linhas por dois pontos
for mac in listOfMacs:
    dashRemoved = mac.replace("-", ":")
    RemoveDash.append(dashRemoved)

print(RemoveDash)
print("\n" * 2)


# Removendo \n do texto
for mac in RemoveDash:
    lineRemoved = mac.replace("\n", "")
    RemoveLine.append(lineRemoved)

print(RemoveLine)
print("\n" * 2)


# Convertendo minusculo
for mac in RemoveLine:
    lowerCase = mac.lower()
    NewMacs.append(lowerCase)

print(NewMacs)
print("\n" * 2)
