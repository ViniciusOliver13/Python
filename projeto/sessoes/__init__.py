from os import system

def adiconar_Sessao(sessao):
    """
    """
    system('cls')
    
    nome = str(input('Digite o nome da sessão: '))

    if nome in [sessao['nome'] for sessao in sessao]:
        print('Sessão já cadastrada!')
        return None
    
    else:
        descricao = str(input('Digite a descrisão da sessão: '))

        sessao.append({'nome': nome, 'descricao': descricao, 'acessorios': []})

        print('Sessão adicionada com sucesso!')


def adiconar_Acessorios_Sessao(sessao, acessorios):

    """
    """
    system('cls')

    busca = str(input('Qual o nome da sessao? '))


    if len(sessao) == 0:
        print('Nenhuma sessão cadastrada!') 

    else:
        for sessoes in sessao:
            if busca == sessoes['nome']:
                print('Sessão encontrada!')

                busca = str(input('Informe o nome do acessório: '))

                for acessorio in acessorios:

                    if busca == acessorio['nome']:
                        print('Acessório encontrado!')
                
                        sessoes['acessorios'].append(acessorio)
                        print(f'Acessório "{busca}" adicionado com sucesso a "{sessoes["nome"]}"!')                         
                        return None

                    print('Acessório não foi cadastrado!')
                    return None 
            
        print('Sessão não encontrada!')

