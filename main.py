'''arquivo = open("Texto.txt", "r")
print(arquivo.read())
print(arquivo.tell())
arquivo.close()
print(arquivo.closed)'''

'''arquivo = open("novo.txt", "w")
arquivo.write("Arquivo de escrita")
arquivo.close()
print(arquivo.closed)'''

'''arquivo = open("frutas.txt", "w")
arquivo.write("Bananas" + '\n')
arquivo.write("Uvas" + '\n')
arquivo.write("Mamao" + '\n')
arquivo.close()
print(arquivo.closed)'''

'''precos = [20,100,500,600]

with open("preços_roupas.txt", "w") as arquivo:
    for preco in precos:
        arquivo.write(str(preco) + '\n')
print(arquivo.closed)'''

'''precos = [8000]

with open("preços_roupas.txt", "a") as arquivo:
    for preco in precos:
        arquivo.write(str(preco) + '\n')
print(arquivo.closed)'''

'''disciplinas = ["Rad \n", "introdução a C \n", "Programação 1 \n"]
with open("disciplinas.txt", "w") as file:
    file.write("Relação de disciplinas \n")
    file.writelines(disciplinas)

with open("disciplinas.txt", "r") as file:
    print(file.read())'''

'''with open("Texto.txt", "r") as arquivo:
    print("Representação original da linha")
    for linha in arquivo:
        print(repr(linha))

with open("texto.txt", "r") as arquivo:
    print("conteúdo da linha")
    for linha in arquivo:
        linha = linha.strip()
        print(repr(linha_))'''

'''minha_lista = ["Arroz", "Feijão", "Carne"]
lista_ = '.'.join(minha_lista)

with open("texto.txt", "r") as arquivo:
    arquivo.write(lista_)'''

'''try:
    with open("arquivo_texto.txt", "r") as arquivo:
        print(arquivo.read())
except FileNotFoundError:
    print("Arquivo inexistente")'''

'''import os
try:
    os.remove("teste.txt")
    print("Arquivo foi removido")
except FileNotFoundError as erro:
    print("Arquivo inexistente")
    print("descrição", erro)'''

try:
    f = open("novo2.txt", "r")
    f.write("write")
except IOError as erro:
    print("O erro foi", erro)
