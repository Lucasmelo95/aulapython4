# def somar(n1,n2):
#   return n1 + n2

def somar(n1,n2):
  return n1 + n2

resultado = somar(5,8)
media = resultado / 2

print(media)


def checarNota(nota):
  if nota >=0 and nota <= 10:
    return "válido"
  else:
    return "inválido"
  
print(checarNota(5))
print(checarNota(-5))
print(checarNota(50))
print(checarNota(9))
