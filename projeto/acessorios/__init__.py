from os import system

def adicionar_Acessorio(acessorios):
    """
    """
    system('cls')
    
    tipos = ('Joia', 'Bijuteria')
    
    nome = str(input('Digite o nome do acessório: '))

    if nome in [acessorios['nome'] for acessorios in acessorios]:
        print('Acessório já cadastrado!')
        return None
    
    else:
        tipo = int(input('Digite o tipo do acessório\n[1] Joia\n[2] Bijuteria\n>>> '))
        tipo = tipos[tipo - 1]
        preco = float(input('Digite o preço do acessório: R$'))
        quantidade = int(input('Informe a quantidade no estoque: '))

    print('Acessório adicionado com sucesso!')

    acessorios.append({'nome': nome, 'tipo': tipo, 'preco': preco, 'quantidade': quantidade})


def ver_Acessorios(acessorios):
    """
    """
    system('cls')

    for acessorio in acessorios:
        print(f'Nome: {acessorio["nome"]}\nTipo: {acessorio["tipo"]}\nPreço: R${acessorio["preco"]}\nQuantidade: {acessorio["quantidade"]}\n')

