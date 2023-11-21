def numeros(n1,n2,n3):
    if n1 > n2 and n1 > n3:
        return f"{n1} é o maior numero"
    elif n2 > n1 and n2 >n3:
        return f"{n2} é o maior numero"
    elif n3 > n1 and n3 > n2:
        return f"{n3} é o maior numero"

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))

print(numeros(num1,num2, num3))