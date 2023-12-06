import os

def perguntar_borda(sabor):
    borda = input(f'Você gostaria de adicionar borda à sua pizza {sabor}? (s/n): ')
    return 'com borda' if borda.lower() == 's' else 'sem borda'

def processar_resposta(resposta, nome, endereco):
    if resposta == '1':
        borda = perguntar_borda('Margherita')
        print(f'{os.linesep}{nome}, sua pizza Margherita {borda} está sendo preparada! Será entregue em: {endereco}{os.linesep}')
    elif resposta == '2':
        borda = perguntar_borda('Pepperoni')
        print(f'{os.linesep}{nome}, sua pizza Pepperoni {borda} está a caminho! Será entregue em: {endereco}{os.linesep}')
    elif resposta == '3':
        borda = perguntar_borda('Frango com Catupiry')
        print(f'{os.linesep}{nome}, sua pizza de Frango com Catupiry {borda} será entregue em breve! Será entregue em: {endereco}{os.linesep}')
    else:
        print('Por favor, escolha 1, 2 ou 3 para fazer um pedido.')

    # Adicione uma mensagem de agradecimento ao final do pedido
    print(f'{os.linesep}Obrigado pelo seu pedido, {nome}! Apreciamos a sua preferência. Bom apetite!{os.linesep}')

def start():
    # Apresentar o bot da pizzaria
    print('Olá! Bem-vindo à Bill Pizzaria.')
    # Pedir o nome
    nome = input('Digite seu nome: ')
    # Pedir o endereço
    endereco = input('Digite seu endereço: ')
    # Oferecer o menu de opções
    resposta = input(
        f'O que você gostaria de pedir hoje, {nome}?{os.linesep}[1] - Pizza Margherita{os.linesep}[2] - Pizza Pepperoni{os.linesep}[3] - Pizza de Frango com Catupiry{os.linesep}')
    # Processar a resposta enviada
    processar_resposta(resposta, nome, endereco)

if __name__ == '__main__':
    start()
