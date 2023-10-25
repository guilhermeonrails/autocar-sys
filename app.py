import os
import json

def exibir_nome_do_programa():
    os.system('clear')
    print('''
▄▀█ █░█ ▀█▀ █▀█ ▄█▄
█▀█ █▄█ ░█░ █▄█ ░▀░
''')

def carregar_dados():
    try:
        with open('carros.json', 'r') as arquivo:
            dados = json.load(arquivo)
            return dados # Retorna um dicionário vazio se o arquivo não existir
    except:
        return {}

def listar_veiculos():
    os.system('clear')
    print('Listando todos os carros\n')
    lista_de_veiculos = carregar_dados()
    print(f'{"-" * 35}')
    for _, informacao in lista_de_veiculos.items():
        print(f"{informacao['marca']} | {informacao['modelo']} | {informacao['ano']} | {informacao['preco']:.2f}")
        print(f'{"-" * 35}')
    input('\nPressione enter para voltar ao menu de opções ')
    main()

def cadastrar_novo_veiculo():
    os.system('clear')
    print('Cadastrar novo veículo\n')
    marca_do_veiculo = input('Digite a marca do veículo: ')
    modelo_do_veiculo = input('Digite o modelo do veículo: ')
    ano_do_veiculo = input('Digite o ano do veículo: ')
    preco_do_veiculo = input('Digite o preço do veículo: ')
    lista_de_veiculos = carregar_dados()
    novo_veiculo = {
        f"carro{len(lista_de_veiculos) + 1}": {
            "marca": marca_do_veiculo,
            "modelo": modelo_do_veiculo,
            "ano": ano_do_veiculo,
            "preco": float(preco_do_veiculo)
        }
    }
    lista_de_veiculos.update(novo_veiculo)
    salvar(lista_de_veiculos)  
    input('\nVeículo cadastrado com sucesso! Pressione enter para voltar ao menu')
    main()

def salvar(lista_de_veiculos):
    with open('carros.json', 'w') as arquivo:
        json.dump(lista_de_veiculos, arquivo, indent=4)

def sair():
    os.system('clear')
    print('\nFinalizando a aplicação\n')

def exibir_quantidade_de_carros_cadastrados():
    lista_de_carros = carregar_dados()
    os.system('clear')
    print('Carros cadastrados\n')
    print(f'Existem {len(lista_de_carros)} cadastrados neste momento.')
    input('\nPressione enter para voltar ao menu ')
    main()

opcoes = {
    1: listar_veiculos,
    2: cadastrar_novo_veiculo,
    3:exibir_quantidade_de_carros_cadastrados,
    4: sair
}

def menu_de_opcoes():
    print('⇾ 1. Listar veículos')
    print('⇾ 2. Cadastrar novo veículo')
    print('⇾ 3. Quantidade de carros cadastrados')
    print('⇾ 4. Sair\n')

def escolher_opcao():
    opcao = verifica_se_opcao_e_valida()
    if opcao in opcoes:
        opcoes[opcao]()
    else:
        opcao_invalida()

def opcao_invalida():
    cor_vermelha = "\033[41m"
    cor_padrao = "\033[0m"
    input(f'\n{cor_vermelha}Opção inválida! Pressione enter e escolha uma opção válida{cor_padrao}')
    return main()

def verifica_se_opcao_e_valida():
    try:
        opcao = int(input('Digite a opção desejada: '))
        return opcao
    except ValueError:
        opcao_invalida()

def main():
    exibir_nome_do_programa()
    menu_de_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()