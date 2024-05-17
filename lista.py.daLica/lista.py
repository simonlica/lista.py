# Criando um lita de fruta
frutas = ["maça", "banana", "lrnja", "uva", "manga"]

# Exibindo a lista complta de frutas
print("Lista de frutas:", frutas)

# Adicionando uma nova fruta a lista
frutas.append("abacaxi")
print("depois de adicionar abacaxi:", frutas)

# Removendo uma fruta a lista
frutas.remove("banana")
print("Depoi d remover banana:", frutas)

# Acessando uma fruta específica (a primeira fruta)
primeira_fruta = frutas[0]
print("A primeira ruta é:", primeira_fruta)

# Percorrendo a lista de frutas
print("Todas as frutas:")
for fruta in frutas:
    print(fruta)

# Veriicando se uma fruta esta na lista     
    if "manga" in frutas: 
        print("Manga esta na lista de frutas.")
    else:
        print("Manga não esta na lista e frutas.")   

# Ordenando a lista de frutas
frutas.sort()
print("Lista de frutas ordenada:", frutas)

# Contando o número de frutas
numero_de_frutas = len(frutas)
print("Número de frutas na lista:", numero_de_frutas)