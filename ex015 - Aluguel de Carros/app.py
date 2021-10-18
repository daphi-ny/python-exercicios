d = int(input('por quantos dias este carro será alugado? '))
km = float(input('quantos KM pretende percorrer com o carro? '))
dia = d * 60
kms = km * 0.15
soma = dia + kms
print('o valor será de {}'.format(soma))