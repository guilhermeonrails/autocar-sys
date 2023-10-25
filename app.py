import os

def exibir_nome_do_programa():
    os.system('clear')
    print('''
▄▀█ █░█ ▀█▀ █▀█ ▄█▄
█▀█ █▄█ ░█░ █▄█ ░▀░
''')


def listar_veiculos():
    os.system('clear')
    print('Listando todos os carros')

def cadastrar_novo_veiculo():
    pass

def salvar():
    pass

def sair():
    pass

opcoes = {
    1:listar_veiculos,
    2:cadastrar_novo_veiculo,
    3:salvar,
    4:sair
}

def menu_de_opcoes():
    print('⇾ 1. Listar veículos')
    print('⇾ 2. Cadastrar novo veículo')
    print('⇾ 3. Salvar veículos')
    print('⇾ 4. Sair\n')

def escolher_opcao():
    opcao = verifica_se_opcao_e_valida()
    if opcao in opcoes:
        opcoes[opcao]()
    else:
        input('Opção inválida! Pressione enter e escolha uma opção válida')
    
def verifica_se_opcao_e_valida():
    try:
        opcao = int(input('Digite a opção desejava: '))
        return opcao
        
    except:
        input('Opção inválida! Pressione enter e escolha uma opção válida')
        return main()


def main():
    exibir_nome_do_programa()
    menu_de_opcoes()
    escolher_opcao()
    
if __name__ == '__main__':
    main()