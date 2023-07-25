# # Atividade 2 - Implementação de um jogo com uso de modularização (PODE SER FEITO EM DUPLAS!!).

# # Faça um programa em Python que implemente um Jogo de Dados com as regras a seguir.
# # *Deve utilizar modularização na implementação do programa.

# #            O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 9, você um "sortudo" e ganhou. 
# Se você tirar 2, 4 ou 12 na primeira jogada, que "azar"!! E você perdeu. Se, na primeira jogada, você fez um 3, 5, 6, 8, 10 ou 11, este é seu "Ponto".
# # Seu objetivo agora, da segunda jogada em diante, é continuar jogando os dados até tirar este número ("Ponto") novamente. Você perde, no entanto, 
# # se tirar um 7 antes de tirar este "Ponto" novamente.
# # Para gerar os números dos dados que foram lançados deverá utilizar uma das funções que geram números de forma randômica, observe as funções indicadas abaixo:
# # A função random() retorna um float x tal que 0 <= x < 1.
# # A função uniform(10,20) retorna um float x tal que 10 <= x < 20.
# # A função randint(100,1000) retorna um inteiro x tal que 100 <= x < 1000.
# # A função randrange(100,1000,2) retorna um inteiro x tal que 100 <= x < 1000 e x é par (ou seja, passo 2)

# # MARIO VINICIUS DE AZEVEDO NUNES - R.A 10482223211
# # PAULO VITOR SANTOS DA SILVA - R.A 10482223392


ponto = 0
contador = 1

def jogo():
    from random import randint

    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    soma_dados = dado1 + dado2
    global contador
    print('A soma dos dado foi ', soma_dados)


    if soma_dados == 7 or soma_dados == 9:
        if contador == 1:
            print('Sortudo, você ganhou o jogo na primeira rodada e a partida acabou !!!!')
        elif contador == 2 and soma_dados == 7:
            print('Voce perdeu !!!')
        else:
            print('Sortudo, você ganhou o jogo e a partida acabou !!!!')

    elif soma_dados == 2 or soma_dados == 4 or soma_dados == 12:
        print('Que azar, você perdeu e o jogo acabou')


    elif soma_dados == 3 or soma_dados == 5 or soma_dados == 6 or soma_dados == 8 or soma_dados == 10 or soma_dados == 11:
        global ponto
        ponto += soma_dados
        print('vc esta na', contador, 'rodada')
        contador += 1
        print("Voce está com ",ponto ,"pontos")
        print('---' * 30)

        continuar = input('Deseja jogar o dado novamente ? [S/N] ').upper()

        if continuar == 'S':
            jogo()

        elif continuar == 'N':
            print('Acabou a partida e você ficou com ', ponto, 'pontos ')

        else:
            print('Resposta inválida')
            continuar = input('Deseja jogar o dado novamente ? [S/N] ').upper()

            if continuar == 'S':
                jogo()
            else:
                print('Acabou a partida e você ficou com ', ponto, 'pontos ')




if __name__ == '__main__':
    print("Bem-vindo ao jogo de dados!")
    jogo()












