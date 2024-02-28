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

precos = [8000]

with open("preços_roupas.txt", "a") as arquivo:
    for preco in precos:
        arquivo.write(str(preco) + '\n')
print(arquivo.closed)
