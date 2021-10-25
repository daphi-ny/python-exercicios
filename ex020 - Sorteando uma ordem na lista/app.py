import random
n1 = str(input('aluno 1: '))
n2 = str(input('aluno 2: '))
n3 = str(input('aluno 3: '))
n4 = str(input('aluno 4: '))
n5 = str(input('aluno 5: '))
lista = [n1, n2, n3, n4, n5]
random.shuffle(lista)
print('a nova ordem será: ')
print('{}'.format(lista))