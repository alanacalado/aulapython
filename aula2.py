print ( 'ola mundo')


'''
comento
blocos
de codigo
'''
# comentario de linha

nome = "alanaa"
print(nome)
peso = 0.0
altura = 1.65
instrutor = True
print(peso)
print(altura)
print(instrutor)
print(peso,type(peso)) 
print(instrutor,type(instrutor))


valor = 15
print(valor, type(valor))
valor = str(valor)
print(type(valor))

#nome = input("digite seu nome: ")
#idade = int(input("digite a sua idade: "))

#print('ola,meu nome é '+ nome + '! Tenho ' + str(idade) + ' de idade')

#print('ola, meu nome é ', nome, 'Tenho ', idade, 'anos de idade!')

#print(f'Ola, meu nome é {nome}, tenho {idade} de idade. Atualmente peso {peso}, e tenho {altura} de altura.')

'''
Criar um sistema para receber o nome, idade, peso, altura
Converter a idade para receber somente numeros inteiros
Imprimir os tipos de dados
Imprimir todas as informações concatenadas usando f string
'''
#variaveis para receber os inputs


nome = input("digite seu nome :  ")
idade = int(input ('digite sua idade: '))
peso = float(input('digite seu peso: '))
altura = float (input ('digite sua altura: '))

print(f'Ola, meu nome é {nome}, \nTenho {idade} anos de idade. \nAtualmente peso {peso}, e tenho {altura} de altura.')
print(type(nome))
print(type(idade))
print(type(peso))
print(type(altura))