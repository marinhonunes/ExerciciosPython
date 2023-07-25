# Atividade 3 - Manipulação de caracteres (Strings) (PODE SER FEITO EM DUPLAS!!).

# 1) [Strings, listas, módulos] Jogo da palavra embaralhada. Desenvolva um jogo em que o jogador tenha que adivinhar uma palavra 
# que será mostrada na tela com as letras embaralhadas. 

#No programa deverá possuir funções para:
# - preencher uma lista de palavras (contendo no mínimo 10 palavras!);
# - escolher uma das palavras da lista aleatoriamente (função recebe uma lista e retorna o índice da palavra selecionada na lista 
# para o jogador adivinhar);
# - embaralhar as letras uma palavra passada por parâmetro – o critério de embaralhar deve ser criado pelo desenvolvedor (a função
#  recebe a palavra que foi escolhida com a grafia correta e retorna a palavra embaralhada);
# - jogar, onde o jogador terá sete tentativas para adivinhar a palavra (recebe a palavra escolhida com a grafia correta por
#  parâmetro e retorna o resultado true (se o jogador venceu) ou false (se o jogador perdeu)).

# Quando iniciar o jogo, o programa escolherá uma das palavras da lista (aletoriamente) e a exibirá embaralhada ao jogador. 
# O jogador terá sete tentativas para adivinhar a palavra. Ao final, a palavra com a grafia correta deve ser mostrada na tela, 
# informando se o jogador ganhou ou perdeu o jogo.

# Para sortear uma das palavras existentes na lista deverá utilizar uma das funções que geram números de forma randômica
#  (para indicar o índice da lista correspondente à palavra sorteada), observe as funções indicadas abaixo:
# A função random() retorna um float x tal que 0 <= x < 1.
# A função uniform(10,20) retorna um float x tal que 10 <= x < 20.
# A função randint(100,1000) retorna um inteiro x tal que 100 <= x < 1000.
# A função randrange(100,1000,2) retorna um inteiro x tal que 100 <= x < 1000 e x é par (ou seja, passo 2)

# 10482223211 - MARIO VINICIUS DE AZEVEDO NUNES
# 10482223392 - PAULO VITOR SANTOS DA SILVA

import random

def preencher_palavras ():
    lista = ['tigre', 'panda', 'golfinho', 'melancia', 'jabuticaba', 'laranja', 'gorila', 'esquilo', 'abacaxi', 'morango']
    return lista

lista_preenchida = preencher_palavras()

def escolher_palavra (lista):
    indice = random.randint(0, len(lista_preenchida) -1)
    escolhido = lista_preenchida[indice]
    return escolhido

escolhido = escolher_palavra(lista_preenchida)

def embaralhar_palavra (palavra):
    palavra_lista = []
    for i in palavra:
        palavra_lista.append(i)
    random.shuffle(palavra_lista)
    palavra_embaralhada = ' '.join(palavra_lista)
    return palavra_embaralhada

embaralhada = embaralhar_palavra(escolhido)

print(embaralhada)

# def jogar ():              