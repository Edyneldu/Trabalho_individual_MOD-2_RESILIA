# Função para exibir um título
def titulo(msg):
    print('\n')
    print(msg)
# Função para exibir a lista de candidatos
def listaCandidato(candidato):
    titulo('Lista de Candidatos:')
    for i, c in enumerate(candidato):
        print(f'{i+1}° Candidato: e{c[0]}_t{c[1]}_p{c[2]}_s{c[3]}')
# Função para exibir os candidatos aprovados
def aprovados(criterios, candidato):
    # Lista para armazenar os candidatos aprovados
    listaAprovados = [f'{j+1}° Candidato e_{c[0]}_t{c[1]}_p{c[2]}_s{c[3]}' for j, c in enumerate(candidato) if all(0 < criterios[i] <= c[i] for i in range(4))]
    titulo('Aprovados:')
    # Verifica se não há candidatos aprovados
    if len(listaAprovados) == 0:
        print('\n_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX_\n')
        print('_______________________________________________________________Nenhum Aprovado! _______________________________________________________')
        print('\n_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX_\n')
    else:
        # Exibe os candidatos aprovados
        for ap in listaAprovados:
            print(f'{ap[:13]:.<18}{ap[13:]}')
# Função para obter uma nota digitada pelo usuário
def obterNota(rotulo):
    while True:
        try:
            nota = int(input(f'Digite a nota do Canditato para: {rotulo}: '))
            return nota
        except ValueError:
            print('\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Atenção !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
            print('Por favor, digite um número válido!!!')
            print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Warming !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
# Função para obter a resposta do usuário (s/n)
def obterResposta():
    while True:
        print('\n\n_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_?_\n')
        resposta = input('Deseja adicionar mais algum candidato à lista? ["s" para "sim" ou "n" para "não"]: ').lower()
        if resposta == 's' or resposta == 'n':
            return resposta
        else:
            print('\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Atenção !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
            print('Por favor, digite uma resposta válida ("s" para "sim" ou "n" para "não")!!!')
            print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! WarminG !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
# Lista para armazenar os candidatos
candidato = []
pos = 1
# Início do programa
print('\n_________________________________________________________________ Início ______________________________________________________________\n')
# Exibe o título para inserção das notas
titulo('Insira as notas do Candidato abaixo:')
while True:
    print(f'{pos}° Candidato:') 
    # Obtém as notas do candidato
    notas = [obterNota(rotulo) for rotulo in ['Entrevista', 'Teste Teórico', 'Teste Prático', 'Soft Skill']]
    candidato.append(notas)
    # Obtém a resposta do usuário para adicionar mais candidatos
    resposta = obterResposta()
    if resposta == 'n':
        break
    pos += 1
# Exibe o título para inserção dos critérios
titulo('Quais são os Critérios:')
# Obtém os critérios de avaliação
criterios = [obterNota(rotulo) for rotulo in ['e_ Entrevista', 't_ Teste Teórico', 'p_ Teste Prático', 's_ Soft Skill']]
# Exibe a lista de candidatos
listaCandidato(candidato)
# Verifica e exibe os candidatos aprovados
aprovados(criterios, candidato)
print('\n___________________________________________________________________ FIM ________________________________________________________________\n')
#°2023 - Edineudo Sampaio - Resília/iFood
