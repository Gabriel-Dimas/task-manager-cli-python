import os
import json 

def caregar_tarefas():
    try:
        with open('tarefas.json' ,'r') as arquivo:
            return json.load(arquivo)       
    except FileNotFoundError:
        return []

lista_de_tarefas = caregar_tarefas()

def salvar_tarefas():
    with open('tarefas.json', 'w') as arquivo:
        json.dump(lista_de_tarefas, arquivo)

def nome_do_programa():
    print(""" 

    ██╗░░░░░██╗░██████╗████████╗░█████╗░  ██████╗░███████╗
    ██║░░░░░██║██╔════╝╚══██╔══╝██╔══██╗  ██╔══██╗██╔════╝
    ██║░░░░░██║╚█████╗░░░░██║░░░███████║  ██║░░██║█████╗░░
    ██║░░░░░██║░╚═══██╗░░░██║░░░██╔══██║  ██║░░██║██╔══╝░░
    ███████╗██║██████╔╝░░░██║░░░██║░░██║  ██████╔╝███████╗
    ╚══════╝╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝  ╚═════╝░╚══════╝
    ████████╗░█████╗░██████╗░███████╗███████╗░█████╗░░██████╗
    ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗██╔════╝
    ░░░██║░░░███████║██████╔╝█████╗░░█████╗░░███████║╚█████╗░
    ░░░██║░░░██╔══██║██╔══██╗██╔══╝░░██╔══╝░░██╔══██║░╚═══██╗
    ░░░██║░░░██║░░██║██║░░██║███████╗██║░░░░░██║░░██║██████╔╝
    ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░
""")

def listar_opicao():
    print('.Menu de opções.')
    print('\n1. Adicionar tarefa')
    print('2. Lista de tarefas')
    print('3. Atualizar tarefas')
    print('4. Deletar tarefa')
    print('5. Sair do programa\n')
    

def opicao_escolida():
    try:
        opicao = int (input('Escolha uma opção: '))
        if opicao == 1:
            adicionar_tarefa()
        elif opicao == 2:
            mostar_tarefas()
        elif opicao == 3:
            atualizar_lista()
        elif opicao == 4:
            apagar_da_lista()
        elif opicao == 5:
            print('Saindo...')
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print('Opção inválida')
            opicao_inavlida()
    except ValueError:
        opicao_inavlida()
        return 0
    return opicao

def opicao_inavlida():
    input('Opção inválida. Pressione qualquer tecla para voltar.')

def adicionar_tarefa():
    while True:
        tarefa = input('Qual tarefa você deseja adicionar? ')
        if not tarefa.strip():
            print('Tarefa vazia, tente novamente!!')
        else:
            break
    
    nova = {
        'tarefa': tarefa,
        'concluida': False
    }

    lista_de_tarefas.append(nova)
    salvar_tarefas()
    input('Tarefa adicionada com sucesso')

def mostar_tarefas():
    print('Lista de tarefas')

    for i, item in enumerate(lista_de_tarefas):
        estado = "✔" if item["concluida"] else "✘"
        print(i, f'{item["tarefa"]} [{estado}]')

    input('Pressione qualquer tecla para sair.')

def marca_tarefa_concluida():
    if not lista_de_tarefas:
        input('Lista vazia!')
        return

    while True:
        try:
            print('Número das tarefas atuais: ')
            for i , tarefa in enumerate(lista_de_tarefas):
                print(i, tarefa['tarefa'])
                
            qual = int(input('Qual tarefa foi concluída: '))

            if qual < 0 or qual >= len(lista_de_tarefas):
                print('Número inválido!')
                continue
            
            lista_de_tarefas[qual]["concluida"] = True
            salvar_tarefas()

            print('Tarefa concluída ✔')
            break
             
        except ValueError:
            print('Somente números.')

def auterar_lista():
    if not lista_de_tarefas:
        input('Lista vazia!')
        return

    while True:
        try:
            print('Número das tarefas atuais: ')
            
            for i, tarefa in enumerate(lista_de_tarefas):
                print(i, tarefa['tarefa'])

            qual_o_numero = int(input('Qual tarefa deve ser mudada: '))

            if qual_o_numero < 0 or qual_o_numero >= len(lista_de_tarefas):
                print('Número inválido!')
                continue
            break

        except ValueError:
            print('Somente números!')
        
    nova_tarefa = input('Qual é o nome da nova tarefa: ')

    lista_de_tarefas[qual_o_numero]['tarefa'] = nova_tarefa

    print('\nNova lista:')
    for item in lista_de_tarefas:
        status = "✔" if item["concluida"] else "✘"
        print(f'{item["tarefa"]} [{status}]')
    
    salvar_tarefas()
    input('\nPressione qualquer tecla...')

def atualizar_lista():
    try:
        print('1. Trocar item da lista')
        print('2. Marcar como concluído')
        
        opicao = int(input('O que deseja alterar: '))
        
        if opicao == 1:
            auterar_lista()
        elif opicao == 2:
            marca_tarefa_concluida()
        else:
            print('Opção inválida')
    except ValueError:
        print('Só número!')

def apagar_da_lista():
    if not lista_de_tarefas:
        input('Lista vazia!')
        return

    while True:
        try:
            print('Qual você deseja deletar: ')
            for i, tarefa in enumerate(lista_de_tarefas):
                print(i , tarefa['tarefa'])

            deletar = int(input('Qual o número da tarefa a ser deletada: '))

            if deletar < 0 or deletar >= len(lista_de_tarefas):
                print('Número inválido!')
                continue
            break   

        except ValueError: 
            print('Só números!!')
            
    lista_de_tarefas.pop(deletar)

    print('Item removido')
    print('Nova lista')

    for i , lista in enumerate(lista_de_tarefas):
        print(i , lista['tarefa'])

    salvar_tarefas()

def men():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        nome_do_programa()
        listar_opicao()
        opicao = opicao_escolida()
        if opicao == 5:
            break

men()

