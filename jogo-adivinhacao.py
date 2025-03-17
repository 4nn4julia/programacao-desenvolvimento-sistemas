def jogo1():


    import random

    print("____________________________________________")
    print("Seja bem-vindo ao jogo Teste de Adivinhação!")
    print("____________________________________________\n")
    print("Nesse jogo, você irá começar com 1000 pontos.")
    print("Quanto mais distante for o seu palpite do número a ser adivinhado, mais pontos você perde.")
    print("O objetivo é acertar o número secreto com a maior quantidade de pontos.\n")

    numero_secreto = random.randrange(1, 10)
    tentativas = 0
    pontos = 1000

    # Configuração dos níveis de dificuldade.
    print("Em qual nível de dificuldade você gostaria de jogar?")
    print("[1] Fácil / [2] Médio / [3] Difícil\n")

    dificuldade = int(input("Selecione o nível de dificuldade: "))

    if (dificuldade == 1):
        print("Você selecionou a dificuldade fácil, com 20 tentativas.")
        tentativas = 20
    elif (dificuldade == 2):
        print("Você selecionou a dificuldade médio, com 10 tentativas.")
        tentativas = 10
    else:
        dificuldade = 3
        print("Você selecionou a dificuldade difícil, com 5 tentativas. Que coragem, boa sorte!")
        tentativas = 5

    # Configuração das rodadas
    for rodada in range(1, tentativas + 1):
        print("Tentativa {} de {}".format(rodada, tentativas))
        palpite = input("Digite o seu palpite numérico entre 1 e 10: ")
        print("Você digitou o número: ", palpite)
        palpite_correto = int(palpite)

        if (palpite_correto < 1 or palpite_correto > 10):
            print("Por favor, digite um número entre 1 e 10!")
            continue

        # Verificação da proximidade de acerto.
        acertou = palpite_correto == numero_secreto
        palpite_maior = palpite_correto > numero_secreto
        palpite_menor = palpite_correto < numero_secreto

        if (acertou):
            print("Parabens! Você achou o número correto e finalizou o jogo  com {}".format(pontos))
            break
        else:
            if (palpite_maior):
                print("Que pena, você errou! Seu palpite foi maior que o número a ser adivinhado. Tenta novamente!")
            elif (palpite_menor):
                print("Que pena, você errou! Seu palpite foi menor que o número a ser adivinhado. Tenta novamente!")

            pontos_perdidos = abs(numero_secreto - palpite_correto)
            pontos = pontos - pontos_perdidos

        # Alertas de última rodada.
        if (rodada == 19 and tentativas == 20):
            print("Atenção! Essa é sua última tentativa. Boa sorte.")
        elif (rodada == 9 and tentativas == 10):
            print("Atenção! Essa é sua última tentativa. Boa sorte.")
        elif (rodada == 4 and tentativas == 5):
            print("Atenção! Essa é sua última tentativa. Boa sorte.")

    print("Fim da partida! Você terminou o jogo com {} pontos.\n".format(pontos))

    recomeco = int(input("Você gostaria de jogar novamente? [1] para SIM ou [2] para NÃO\n"))
    if (recomeco == 1):
        jogo1()
    elif (recomeco == 2):
        print("Obrigado por jogar!")
        exit()
    else:
        exit()

# Fim do código base e comando para rodar.
if (__name__ == "__main__"):
    jogo1()
        