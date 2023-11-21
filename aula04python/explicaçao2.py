# def maior(n1,n2,n3):
#   if n1 >= n2 and n1 >= n3:
#     return n1
#   elif n2 >= n1 and n2 >= n3:
#     return n2
#   elif n3 >= n1 and n3 >= n2:
#     return n3
  
# lista_de_numeros = []
# for i in range(1,4):
#   numero = int(input(f"Digite o {i}º número: "))
#   lista_de_numeros.append(numero)

# print(maior(lista_de_numeros[0], lista_de_numeros[1], lista_de_numeros[2]))


# ===============================================================


# def maior(lista):
#   maior_numero = 0
#   for numero in lista:
#     if numero > maior_numero:
#       maior_numero = numero
#   return maior_numero


# lista_de_numeros = []
# for i in range(1,4):
#   numero = int(input(f"Digite o {i}º número: "))
#   lista_de_numeros.append(numero)

# print(maior(lista_de_numeros))

# ==============================================================

# def maior(lista):
#   maior_numero = 0
#   for numero in lista:
#     if numero > maior_numero:
#       maior_numero = numero
#   if maior_numero == 0:
#     return "Digite números positivos"
#   else:
#     return maior_numero


# lista_de_numeros = []
# for i in range(1,4):
#   numero = int(input(f"Digite o {i}º número: "))
#   lista_de_numeros.append(numero)

# print(maior(lista_de_numeros))

# ==============================================================

# infinito = float("inf")
# infinito_negativo = -float("inf")

# ==============================================================


# def saudacao(nome:str, hora:int):
#   if hora >= 5 and hora <= 12:
#     return f"bom dia {nome}"
#   elif hora > 12 and hora <= 18:
#     return f"boa tarde {nome}"
#   else:
#     return f"boa noite {nome}"
  

# print(saudacao(hora=18, nome="Abel"))


# ============================================================



# def saudacao(nome:str, hora:int):
#   if hora >= 5 and hora <= 12:
#     return f"bom dia {nome}"
#   elif hora > 12 and hora <= 18:
#     return f"boa tarde {nome}"
#   else:
#     return f"boa noite {nome}"
  
# name = str(input("Digite seu nome: "))
# hr = int(input("Digite a hora:"))

# print(saudacao(hora=hr, nome=name))