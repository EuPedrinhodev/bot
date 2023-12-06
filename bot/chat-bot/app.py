import os

def processar_resposta(resposta, nome, endereco):
    if resposta == '1':
        borda = input('Você gostaria de adicionar borda à sua pizza Margherita? (s/n): ')
        borda = 'com borda' if borda.lower() == 's' else 'sem borda'
        print(f'{os.linesep}{nome}, sua pizza Margherita {borda} está sendo preparada! Será entregue em: {endereco}{os.linesep}')
    elif resposta == '2':
        borda = input('Você gostaria de adicionar borda à sua pizza Pepperoni? (s/n): ')
        borda = 'com borda' if borda.lower() == 's' else 'sem borda'
        print(f'{os.linesep}{nome}, sua pizza Pepperoni {borda} está a caminho! Será entregue em: {endereco}{os.linesep}')
    elif resposta == '3':
        borda = input('Você gostaria de adicionar borda à sua pizza de Frango com Catupiry? (s/n): ')
        borda = 'com borda' if borda.lower() == 's' else 'sem borda'
        print(f'{os.linesep}{nome}, sua pizza de Frango com Catupiry {borda} será entregue em breve! Será entregue em: {endereco}{os.linesep}')
    else:
        print('Por favor, escolha 1, 2 ou 3 para fazer um pedido.')

    # Adicione uma mensagem de agradecimento ao final do pedido
    print(f'{os.linesep}Obrigado pelo seu pedido, {nome}! Apreciamos a sua preferência. Bom apetite!{os.linesep}')

def start():
    # Apresentar o bot da pizzaria
    print('Olá! Bem-vindo à Pizzaria Bot.')
    # Pedir o nome
    nome = input('Digite seu nome: ')
    # Pedir o endereço
    endereco = input('Digite seu endereço: ')
    while True:
        # Oferecer o menu de opções
        resposta = input(
            f'O que você gostaria de pedir hoje, {nome}?{os.linesep}[1] - Pizza Margherita{os.linesep}[2] - Pizza Pepperoni{os.linesep}[3] - Pizza de Frango com Catupiry{os.linesep}')
        # Processar a resposta enviada
        processar_resposta(resposta, nome, endereco)

if __name__ == '__main__':
    start()
