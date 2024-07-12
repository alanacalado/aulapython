import time 
import os 

lista_cpf = ['111.222.333-24', '222.333.444-34', '333.444.555-45', '555.777.888-68']
lista_nome = ['Crementina', 'Judenilson', 'Claudete', 'Klodoaudo']
cont = 5 

os.system('cls')
while True:

    print(30*'=', 'BEM VINDO AO PYTHON CADASTRO', 30*'=')
    print('1. Cadastrar um novo usuário')
    print('2. Acessar o Sistema')
    print('3. Listar os usuários')
    print('4. Excluir o usuário')
    print('5. Sair')

  
    opcao = input('Digite sua opção: ')

    if opcao == '1':
        os.system('cls')
        novo_nome = input('Digite um novo nome que deseja cadastrar: ')
        novo_cpf = input('Digite um novo cpf: ')

        if novo_cpf in lista_cpf:
            print('CPF já está cadastrado')
            time.sleep(3)
        else:
            lista_cpf.append(novo_cpf)
            lista_nome.append(novo_nome)
            print(f'CPF cadastrado com sucesso!')
    elif opcao == '2':
        os.system('cls')
        cpf = input('Digite o seu cpf: ')

        if cpf in lista_cpf:
            print('Usuário logado com sucesso!')
            time.sleep(3)
        else:
            print('CPF invalido!')
    elif opcao == '3':
        os.system('cls')
        print('Lista de Usuários!')

        for i in lista_nome:
            print(f'Usuário: {i}')
    elif opcao == '4':
        os.system('cls')
        excluir_cpf = input('Digite o CPF que você deseja excluir: ')

        if excluir_cpf in lista_cpf:
            lista_cpf.remove('excluir_cpf')
            print('CPF excluido com sucesso!')
            time.sleep(3)
        else:
            print('CPF inválido!')
    elif opcao == '5':
        while cont >=0:
            os.system('cls') # Limpar o terminal
            print(f'Saindo do sistema. {cont}...')
            time.sleep(1) # atrasa o proximo comando
            cont -= 1
        break
    else:
        os.system('cls')
        print('Opção Invalida!')
        time.sleep(3)
        os.system('cls')
    
os.system('cls')
print('Você está fora do sistema!') 