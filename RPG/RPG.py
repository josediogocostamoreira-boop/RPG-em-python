# Dungeon dos Tesouros

salas = {
    "Entrada": {"inimigo": None, "tesouro": 0, "dano": 0, "visitada": False},
    "Sala Sombria": {"inimigo": "Goblin", "tesouro": 50, "dano": 10, "visitada": False},
    "Sala do Dragão": {"inimigo": "Dragão", "tesouro": 200, "dano": 60, "visitada": False},
    "Fonte da Vida": {"inimigo": None, "tesouro": 0, "dano": -30, "visitada": False},
    "Tesouro Escondido": {"inimigo": None, "tesouro": 100, "dano": 0, "visitada": False}
}

jogador = {
    "nome": "",
    "vida": 100,
    "pontos": 0,
    "sala": "Entrada"
}

# Começa o jogo
print("Bem-vindo à Dungeon dos Tesouros!")
nome = input("Qual é o teu nome? : ")
jogador["nome"] = nome
print(f"Olá {nome}! Boa sorte...\n")

while True:
    print("\nO que queres fazer?")
    print("1 → Ver como estás")
    print("2 → Explorar a sala onde estás")
    print("3 → Ir para outra sala")
    print("4 → Sair do jogo")

    escolha = input("Escolhe (1-4): ")

    # 1 - Ver estado
    if escolha == "1":
        print(f"\nNome:   {jogador['nome']}")
        print(f"Vida:   {jogador['vida']}")
        print(f"Pontos: {jogador['pontos']}")
        print(f"Sala:   {jogador['sala']}")

    # 2 - Explorar sala atual
    elif escolha == "2":
        sala_atual = salas[jogador["sala"]]

        if sala_atual["visitada"]:
            print("Já estiveste aqui! Não há mais nada para fazer.")
        else:
            print(f"\nEstás a explorar: {jogador['sala']}")

            # Inimigo?
            if sala_atual["inimigo"] != None:
                print(f"Aiii! Apareceu um {sala_atual['inimigo']}!")
                jogador["vida"] = jogador["vida"] - sala_atual["dano"]
                print(f"Perdeste {sala_atual['dano']} de vida")

            # Tesouro ou cura?
            if sala_atual["tesouro"] > 0:
                print(f"Encontraste {sala_atual['tesouro']} pontos!")
                jogador["pontos"] = jogador["pontos"] + sala_atual["tesouro"]

            if sala_atual["dano"] < 0:
                cura = -sala_atual["dano"]
                print(f"Recuperaste {cura} de vida!")
                jogador["vida"] = jogador["vida"] + cura

            sala_atual["visitada"] = True

            print(f"Agora tens {jogador['vida']} de vida e {jogador['pontos']} pontos")

    # 3 - Mudar de sala
    elif escolha == "3":
        print("\nSalas que existem:")
        numero = 1
        for nome_sala in salas:
            print(f"{numero} - {nome_sala}")
            numero = numero + 1

        opcao = input("Para qual sala queres ir? (número): ")
        try:
            numero_escolhido = int(opcao)
            lista_salas = list(salas.keys())
            if 1 <= numero_escolhido <= len(lista_salas):
                nova_sala = lista_salas[numero_escolhido - 1]
                jogador["sala"] = nova_sala
                print(f"Ok! Agora estás na {nova_sala}")
            else:
                print("Número errado...")
        except:
            print("Tens de escrever um número!")

    # 4 - Sair
    elif escolha == "4":
        print("\nAdeus! Saíste da dungeon.")
        break

    else:
        print("Escolhe um número entre 1 e 4, por favor.")

    # Verifica se morreu
    if jogador["vida"] <= 0:
        print("\nPerdeste toda a vida... FIM DE JOGO!")
        print(f"Conseguiste {jogador['pontos']} pontos")
        break

print("\nObrigado por jogar!")
print(f"Pontuação final: {jogador['pontos']}")

#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⣠⣴⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀ ⢀⣴⣾⠟⢹⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣤⣤⣤⣤⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀  ⣠⣶⡿⠋⠁⠀⢸⣿⣿⣿⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⡿⠿⠛⠛⠋⠉⣿⣿⣿⣿⣿⣿⣿⣶⣤⡀⠀⠀⠀
# ⢀⣴⡿⠟⠁⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⠀⠀⣴⣿⠟⠁⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀
#⠐⠿⣿⣤⡀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⣾⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄
#⠀⠀⠀⣿⣿⣷⣄⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⣿⣇⣀⣠⠴⠶⠟⠛⠛⠛⠛⠛⠛⠛⠛⠛⠻⠿⠿⣿⣿⣿⡿⠇
#⠀⠀⠀⣿⣿⣿⣿⣿⣦⡀⢸⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⢰⠀⠀⠀⠀⠀⠀⠀⠙⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠛⠛⠛⠛⠛⠛⠿⣿⣿⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠒⠒⢲⠀