import os
import json 

def load_tasks():
    try:
        with open('tarefas.json' ,'r') as arquivo:
            return json.load(arquivo)       
    except FileNotFoundError:
        return []

task_list = load_tasks()

def save_tasks():
    with open('tarefas.json', 'w') as arquivo:
        json.dump(task_list, arquivo)

def show_banner():
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

def show_menu():
    print('.Menu de opções.')
    print('\n1. Adicionar tarefa')
    print('2. Lista de tarefas')
    print('3. Atualizar tarefas / Concluir tarefa')
    print('4. Deletar tarefa')
    print('5. Sair do programa\n')
    

def get_choice():
    try:
        opicao = int (input('Escolha uma opção: '))
        if opicao == 1:
            add_task()
        elif opicao == 2:
            show_tasks()
        elif opicao == 3:
            update_list()
        elif opicao == 4:
            delete_task()
        elif opicao == 5:
            print('Saindo...')
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print('Opção inválida')
            invalid_option()
    except ValueError:
        invalid_option()
        return 0
    return opicao

def invalid_option():
    input('Opção inválida. Pressione qualquer tecla para voltar.')

def add_task():
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

    task_list.append(nova)
    save_tasks()
    input('Tarefa adicionada com sucesso')

def show_tasks():
    print('Lista de tarefas')

    for i, item in enumerate(task_list):
        estado = "✔" if item["concluida"] else "✘"
        print(i, f'{item["tarefa"]} [{estado}]')

    input('Pressione qualquer tecla para sair.')

def mark_as_done():
    if not task_list:
        input('Lista vazia!')
        return

    while True:
        try:
            print('Número das tarefas atuais: ')
            for i , tarefa in enumerate(task_list):
                print(i, tarefa['tarefa'])
                
            qual = int(input('Qual tarefa foi concluída: '))

            if qual < 0 or qual >= len(task_list):
                print('Número inválido!')
                continue
            
            task_list[qual]["concluida"] = True
            save_tasks()

            print('Tarefa concluída ✔')
            break
             
        except ValueError:
            print('Somente números.')

def edit_task():
    if not task_list:
        input('Lista vazia!')
        return

    while True:
        try:
            print('Número das tarefas atuais: ')
            
            for i, tarefa in enumerate(task_list):
                print(i, tarefa['tarefa'])

            qual_o_numero = int(input('Qual tarefa deve ser mudada: '))

            if qual_o_numero < 0 or qual_o_numero >= len(task_list):
                print('Número inválido!')
                continue
            break

        except ValueError:
            print('Somente números!')
        
    nova_tarefa = input('Qual é o nome da nova tarefa: ')

    task_list[qual_o_numero]['tarefa'] = nova_tarefa

    print('\nNova lista:')
    for item in task_list:
        status = "✔" if item["concluida"] else "✘"
        print(f'{item["tarefa"]} [{status}]')
    
    save_tasks()
    input('\nPressione qualquer tecla...')

def update_list():
    try:
        print('1. Trocar item da lista')
        print('2. Marcar como concluído')
        
        opicao = int(input('O que deseja alterar: '))
        
        if opicao == 1:
            edit_task()
        elif opicao == 2:
            mark_as_done()
        else:
            print('Opção inválida')
    except ValueError:
        print('Só número!')

def delete_task():
    if not task_list:
        input('Lista vazia!')
        return

    while True:
        try:
            print('Qual você deseja deletar: ')
            for i, tarefa in enumerate(task_list):
                print(i , tarefa['tarefa'])

            deletar = int(input('Qual o número da tarefa a ser deletada: '))

            if deletar < 0 or deletar >= len(task_list):
                print('Número inválido!')
                continue
            break   

        except ValueError: 
            print('Só números!!')
            
    task_list.pop(deletar)

    print('Item removido')
    print('Nova lista')

    for i , lista in enumerate(task_list):
        print(i , lista['tarefa'])

    save_tasks()

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        show_banner()
        show_menu()
        opicao = get_choice()
        if opicao == 5:
            break

main()