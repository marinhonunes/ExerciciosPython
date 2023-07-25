# Exemplo com os dados do arquivo texto notas_estudantes.dat:
# jose 10 5 2 3 4
# pedro 3 6 9 2
# suzana 8 2 7 4 3 7 4 1 2 9 1 7
# gisela 2 8 2 10 6 7
# joao 4 3 5 7 6

# Usando o arquivo texto acima, escreva uma função para cada um dos itens abaixo que serão implementados:
# a) imprime o nome dos estudantes que têm menos de cinco notas;
# b) calcula a média das notas de cada estudante e imprime o nome e a média de cada um;
# c) calcula a nota maior e a nota menor de cada estudante e imprime o nome junto com as suas respectivas notas;
# d) exibir os nomes dos estudantes que tiraram nota 10.

# MARIO VINICIUS DE AZEVEDO NUNES - R.A 10482223211
# PAULO VITOR SANTOS DA SILVA - R.A 10482223392

# a) imprime o nome dos estudantes que têm menos de cinco notas;
def nao_tem_cinco_notas():
    arquivo = open("notas_estudantes.dat", "r", encoding="utf-8") # abre o arquivo. 
    conteudo_arquivo = arquivo.readlines() #faz a leitura e armazena na variável 'conteudo_arquivo'.
    for i in conteudo_arquivo: #percorre cada linha do arquivo.
        lista = i.split() #divide a linha em uma lista de strings separadas por espaço. (cria lista com o nome 'lista')
        aluno = lista[0] #armazena o primeiro elemento da lista que é o nome do aluno.
        qtd_notas = lista[1:] #refaz a lista com o nome numero_notas, ignorando o indince[0]
        if len(qtd_notas) < 5: #verifica a quantidade de elementos, se for menor que 5 notas (elementos).
            print(f"O aluno {aluno} não tem 5 notas.")
            print("____________________________________________________________________")
            print()
    arquivo.close() #fecha o arquivo.

# b) calcula a média das notas de cada estudante e imprime o nome e a média de cada um;
def nome_e_media():
    arquivo = open("notas_estudantes.dat", "r", encoding="utf-8")
    conteudo_arquivo = arquivo.readlines()
    for i in conteudo_arquivo:
        lista = i.split()
        aluno = lista[0] # mesma lógica da primeira função até aqui...
        notas = [int(i) for i in lista[1:]] # cria var notas e percorre toda a lista do indice 1 em diante e armazena no formato int.
        somatoria = 0 # variavel para armazenar a soma das notas
        for i in notas: #percorre as notas
            somatoria += i #soma cada nota com o valor armazenado na var somatoria
        media = somatoria / len(notas) #var media, divide o valor da somatoria anterior pelo numero de notas no aluno.
        print(f"A nota média de: {aluno}, foi de: {media: .2f}") # printa nome e nota, limitando para 2 casas depois do '.'
        print("____________________________________________________________________")
        print()
    arquivo.close()

# c) calcula a nota maior e a nota menor de cada estudante e imprime o nome junto com as suas respectivas notas;

def maior_e_menor_nota():
    arquivo = open("notas_estudantes.dat", "r", encoding="utf-8")
    conteudo_arquivo = arquivo.readlines()
    for i in conteudo_arquivo:
        lista = i.split()
        aluno = lista[0] 
        notas = [int(i) for i in lista[1:]] # mesma lógica até aqui...
        maior_nota = max(notas) #utilizando o operador max para ver o maior valor entre as notas(elementos)
        menor_nota = min(notas) #utilizando o operador min para ver o menor valor entre as notas(elementos)
        print(f"A maior nota de: {aluno}, foi de {maior_nota} Pontos e a menor nota foi de: {menor_nota} Pontos.")
        print("________________________________________________________________________")
        print()
    arquivo.close()

# d) exibir os nomes dos estudantes que tiraram nota 10.

def aluno_nota_maxima():
    arquivo = open("notas_estudantes.dat", "r", encoding="utf-8")
    conteudo_arquivo = arquivo.readlines()
    for i in conteudo_arquivo:
        lista = i.split()
        aluno = lista[0] 
        notas = [int(i) for i in lista[1:]] # mesma lógica até aqui...
        if 10 in notas: #verifica se entre os elementos existe o 10
            print(f"O Aluno: {aluno} tirou a nota 10!")
            print("____________________________________________________________________")
            print()
    arquivo.close()
    
resposta = 0

while resposta != 5:
    menu = input('''
        SEJA BEM-VINDO AO SISTEMA DE NOTAS

    FAVOR SELECIONAR UMA DAS OPÇÕES A SEGUIR:
    
(digite o número para acessar a função desejada)

    1 - Alunos que têm menos de 5 notas.
    2 - Nota média.
    3 - Maior e menor nota.
    4 - Alunos que tiraram nota 10.
    5 - Encerrar sistema.

''')

    resposta = int(menu)

    if resposta == 1:
        nao_tem_cinco_notas()
        input("pressione enter para continuar.")
    elif resposta == 2:
        nome_e_media()
        input("pressione enter para continuar.")
    elif resposta == 3:
        maior_e_menor_nota()
        input("pressione enter para continuar.")
    elif resposta == 4:
        aluno_nota_maxima()
        input("pressione enter para continuar.")
    elif resposta == 5:
        print("Sistema encerrado.")
    else:
        print("Opção inválida.")