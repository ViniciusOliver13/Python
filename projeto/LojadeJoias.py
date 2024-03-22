from projeto import menu
from projeto.acessorios import adicionar_Acessorio, ver_Acessorios
from projeto.sessoes import adiconar_Sessao, adiconar_Acessorios_Sessao

Acessorios = []
Sessoes = []
choice = 0

while True:
    choice = menu()

    if choice == 1:
        adicionar_Acessorio(Acessorios)
    
    elif choice == 2:
        adiconar_Sessao(Sessoes)
    
    elif choice == 3:
        adiconar_Acessorios_Sessao(Sessoes, Acessorios)

    elif choice == 4:
        ver_Acessorios(Acessorios)

    elif choice == 5:
        break

    else:
        print('Opção inválida!')


