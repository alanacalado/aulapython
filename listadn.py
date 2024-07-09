lista = ['gomes', 'jojo', 'gigi', 'ruth', 'carminha', 'jordania']

print(f'O primeiro nome da lista é: {lista[0]}')
print(f'O segundo nome da lista é: {lista[1]}')
print(f'O terceiro nome da lista é: {lista[2]}')
print(f'O quarto nome da lista é: {lista[3]}')

for i in range(5):  
    print(f'{i + 1}° nome: {lista[i]}')
print()
for i in range(len(lista)):  
    print(f'{i + 1}° nome: {lista[i]}') 


print(60*'=')
x = int(input('Digite um número inteiro:'))

for num in range(1, 11):
    print(f'{x} X {num} = {x * num}')