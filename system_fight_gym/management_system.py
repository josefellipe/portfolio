import pandas as pd

import datetime as dt

cadastro_dataframe = pd.read_excel("cadastro.xlsx")
cabacalho_cadastros = list(cadastro_dataframe.columns)
# ID_MATRICULA | NOME | MODALIDADE | FAIXA | GRAU | DATA DE VENCIMENTO | VALOR DA MENSALIDADE | SITUAÇÃO | DÉBITOS
financeiro_dataframe = pd.read_excel("financeiro.xlsx")
cabecalho_financeiro = list(financeiro_dataframe.columns)
# ID | DIA | MÊS | ANO | TIPO | DESCRIÇÃO | VALOR | DESCONTO | JUROS | SITUAÇÃO | MATRÍCULA
lancamento_mensalidades = pd.read_excel("lancamentos_mensalidades.xlsx")
cabecalho_lancamento_mensalidade = list(lancamento_mensalidades.columns)
# ID_MENSALIDADE | MATRICULA | DIA DE REFERÊNCIA | MÊS DE REFERÊNCIA | ANO DE REFERÊNCIA
hoje = dt.date.today()
dia = hoje.day
mes = hoje.month
ano = hoje.year


def atualizar_debitos(dados_cadastro, dados_lancamentos):
    for aluno in dados_cadastro:
        for lancamento in dados_lancamentos:
            if aluno[0] == lancamento[1] and lancamento[6] != "PG" and lancamento[6] != "LANCADO":
                aluno[8] = int(aluno[8]) + int(aluno[6])
                lancamento[6] = "LANCADO"
    salvar(dados_cadastro, 'cadastro.xlsx', "aluno")
    salvar(dados_lancamentos, 'lancamentos_mensalidades.xlsx',
           "lancamentos_mensalidades")


def dar_baixa_mensalidade(dados_financeiro, dados_cadastro, dados_lancamento):
    matricula = input("Qual a matricula do aluno?")
    mes_referencia = input("Qual o mes que vence esta mensalidade?")
    for aluno in dados_cadastro:
        if int(matricula) == int(aluno[0]):
            pagamento = input("Qual o valor pago?")
            for lancamento in dados_lancamento:
                if int(matricula) == int(lancamento[1]) and int(lancamento[3]) == int(mes_referencia):
                    lancamento[5] = "PG"
            primary_key = criar_primary_key(dados_financeiro)
            aux = []
            aux.append(primary_key)
            aux.append(dia)
            aux.append(mes_referencia)
            aux.append(ano)
            aux.append("MENSALIDADE")
            aux.append(input("Descrição:   "))
            aux.append(pagamento)
            desconto = input("Desconto:  ")
            aux.append(desconto)
            juros = input("Juros:  ")
            aux.append(juros)
            aux.append("PG")
            aux.append(matricula)
            aux.append(aluno[1])
            aluno[8] = aluno[8] - int(pagamento) + int(desconto) - int(juros)
            dados_financeiro.append(aux)
            salvar(dados_financeiro, 'financeiro.xlsx', "financeiro")
    salvar(dados_cadastro, 'cadastro.xlsx', "aluno")


def checagem_mensalidades(dados_cadastro, dados_lancamentos):
    for aluno in dados_cadastro:
        if aluno[7] == "ATIVO":
            cont = 0
            for lancamento in dados_lancamentos:
                dados_referencia = dt.date(
                    int(lancamento[4]), int(lancamento[3]), int(lancamento[2]))
                mes_referencia = dados_referencia.month
                ano_referencia = dados_referencia.year
                if aluno[0] == lancamento[1] and int(lancamento[3]) == int(mes_referencia) and int(lancamento[4] == int(ano_referencia)):
                    cont += 1
            if cont == 0:
                if int(aluno[5]) < dia:
                    adicionar_mensalidade_lancamentos(dados_lancamentos, aluno)


def adicionar_mensalidade_lancamentos(dados, aluno):
    aux = []
    aux.append(criar_primary_key(dados))
    aux.append(aluno[0])
    aux.append(aluno[5])
    aux.append(mes)
    aux.append(ano)
    aux.append(hoje)
    aux.append("")
    dados.append(aux)
    salvar(dados, "lancamentos_mensalidades.xlsx", "lancamentos_mensalidades")


def transformar_dataframe_em_array(dados):
    aux = []
    for i in range(len(dados)):
        aux.append(list(dados.loc[i]))
    return aux


def transformar_array_em_dataframe(dados, menu_escolha):
    if menu_escolha == "aluno":
        header = cabacalho_cadastros
    if menu_escolha == "financeiro":
        header = cabecalho_financeiro
    if menu_escolha == "lancamentos_mensalidades":
        header = cabecalho_lancamento_mensalidade
    dataFrame = pd.DataFrame(dados, columns=header)
    return dataFrame


def salvar(dados, local, menu_escolha):
    data_frame = transformar_array_em_dataframe(dados, menu_escolha)
    data_frame.to_excel(local, index=False)


def criar_primary_key(dados):
    primary_key = 0
    if dados != []:
        for item in dados:
            if int(item[0]) >= primary_key:
                primary_key = int(item[0]) + 1
    return primary_key


def menu(n, dados_financeiro, dados_aluno, dados_lancamento):
    resposta = n
    while resposta == "aluno":
        resposta = menu_aluno(dados_aluno)
    while resposta == "financeiro":
        resposta = menu_financeiro(
            dados_financeiro, dados_aluno, dados_lancamento)
    return resposta


def menu_aluno(dados):
    menu_escolha = "aluno"
    escolha = input(
        "\n\nALUNO\n\n1 - Consultar\n2 - Editar\n3 - Matricular\n4 - Excluir\n5 - Sair\n")
    if escolha == "1":
        filtro_debito = input("\n\n1 - Todos\n2 - Mensalidade em Aberto\n3 - Mensalidade em Dia\n")
        if filtro_debito == "1":
            aux = []
            aux2 = []
            for cadastro in dados:
                aux.append(cadastro[1])
                aux = sorted(aux)
            for nome in aux:
                for cadastro in dados:
                    if nome == cadastro[1]:
                        aux2.append(cadastro)
        if filtro_debito == "2":
            aux2 = []
            for cadastro in dados:
                if cadastro[6] == "ATIVO" and int(cadastro[7]) != 0:
                    aux2.append(cadastro)
        if filtro_debito == "3":
            aux2 = []
            for cadastro in dados:
                if cadastro[6] == "ATIVO" and int(cadastro[7]) == 0:
                    aux2.append(cadastro)
        print(transformar_array_em_dataframe(aux2, menu_escolha))
    if escolha == "2":
        editar_aluno(dados)
    if escolha == "3":
        add_aluno(dados)
    if escolha == "4":
        delete_item(dados, menu_escolha)
    if escolha == "5":
        menu_escolha = "9"
    return menu_escolha


def menu_financeiro(dados_financeiro, dados_cadastro, dados_lancamento):
    menu_escolha = "financeiro"
    escolha = input(
        "\n\nFINANCEIRO\n\n1 - Consultar\n2 - Editar\n3 - Adicionar\n4 - Excluir\n5 - Resumo\n6 - Sair\n")
    if escolha == "1":
        print(transformar_array_em_dataframe(dados_financeiro, menu_escolha))
    if escolha == "2":
        edit_financeiro(dados_financeiro)
    if escolha == "3":
        add_financeiro(dados_financeiro, dados_cadastro, dados_lancamento)
    if escolha == "4":
        delete_item(dados_financeiro, menu_escolha)
    if escolha == "5":
        resumo_financeiro_mes(dados_financeiro)
    if escolha == "6":
        menu_escolha = "9"
    return menu_escolha


def resumo_financeiro_mes(dados):
    aux = []
    balanco = 0
    mes = input("\nQual o mês do resumo?\n")
    for item in dados:
        if int(item[2]) == int(mes):
            aux.append(item)
            if item[4] == "MENSALIDADE":
                balanco += int(item[6])
            else:
                balanco = balanco - int(item[6])
    print(f'\n\nO faturamento do mês {mes} foi de:  R${balanco},00\n\n')
    relatorio = transformar_array_em_dataframe(aux,"financeiro")
    print(relatorio)
    guardar = input("\n\nDeseja salvar esse relatório?\n1 - Sim\n2 - Não\n")
    if guardar == "1":
        local = f'relatorio_mes_{mes}.xlsx'
        salvar(relatorio,local,"financeiro")


def add_aluno(dados):
    novo_aluno = "1"
    while novo_aluno == "1":
        primary_key = criar_primary_key(dados)
        aux = []
        aux.append(primary_key)
        aux.append(input("Nome:  "))
        aux.append(input("Modalidade:  "))
        aux.append(input("Faixa:  "))
        aux.append(input("Grau:  "))
        aux.append(input("Data de Vencimento:  "))
        aux.append(input("Valor Mensalidade:  "))
        aux.append("ATIVO")
        aux.append(0)
        dados.append(aux)
        salvar(dados, 'cadastro.xlsx', "aluno")
        novo_aluno = input(
            "\nDeseja cadastrar mais um aluno?\n1 - Sim\n2 - Não\n")


def add_financeiro(dados_financeiro, dados_cadastro, dados_lancamento):
    novo_financeiro = "1"
    while novo_financeiro == "1":
        tipo = input(
            "\n\nPagamento de mensalidade ou outros tipos?\n1 - Mensalidade\n2 - Outros\n")
        if tipo == "1":
            dar_baixa_mensalidade(
                dados_financeiro, dados_cadastro, dados_lancamento)
        else:
            primary_key = criar_primary_key(dados_financeiro)
            aux = []
            aux.append(primary_key)
            aux.append(dia)
            aux.append(input("Qual o mês de vencimento?"))
            aux.append(ano)
            aux.append(input("Tipo:  "))
            aux.append(input("Descrição:  "))
            aux.append(input("Valor:  "))
            aux.append(input("Desconto:  "))
            aux.append(input("Juros:  "))
            situacao = input("Situação:\n1 - PAGO\n2 - EM ABERTO\n")
            if situacao == "1":
                situacao = "PAGO"
            if situacao == "2":
                situacao = "EM ABERTO"
            aux.append(situacao)
            aux.append(" ")
            aux.append(" ")
            dados_financeiro.append(aux)
            salvar(dados_financeiro, 'financeiro.xlsx', "financeiro")
        novo_financeiro = input(
            "\nDeseja cadastrar mais uma conta?\n1 - Sim\n2 - Não\n")


def editar_aluno(dados):
    primary_key_aluno = input("\n\nQual é a matrícula do aluno?\n")
    for aluno in dados:
        if int(aluno[0]) == int(primary_key_aluno):
            continuar = "1"
            while continuar == "1":
                editar = input(f'\nVocê deseja alterar qual item?\n'
                f'1 - Nome\n'
                f'2 - Modalidade\n'
                f'3 - Faixa\n'
                f'4 - Grau\n'
                f'5 - Data de vencimento\n'
                f'6 - Valor da mensalidade\n'
                f'7 - Status\n')
                if editar == "1":
                    aluno[1] = input("\nQual o novo nome?\n")
                if editar == "2":
                    aluno[2] = input("\nQual a nova Modalidade?\n")
                if editar == "3":
                    aluno[3] = input("\nQual a nova faixa?\n")
                if editar == "4":
                    aluno[4] = input("\nQual o novo grau?\n")
                if editar == "5":
                    aluno[5] = input("\nQual a nova data de vencimento?\n")
                if editar == "6":
                    aluno[6] = input("\nQual o novo valor da mensalidade?\n")
                if editar == "7":
                    aluno[7] = input("\nQual o novo status?\n")
                continuar = input("\nDeseja alterar outro item?\n1 - Sim\n2 - Não\n")
    salvar(dados, 'cadastro.xlsx', "aluno")


def edit_financeiro(dados):
    primary_key_financeiro = input("\nWhat is the financeiro ID?")
    for conta in dados:
        if int(conta[0]) == int(primary_key_financeiro):
            continuar = "1"
            while continuar == "1":
                editar = input(f'\nVocê deseja alterar qual item?\n'
                f'1 - Dia\n'
                f'2 - Mês\n'
                f'3 - Ano\n'
                f'4 - Tipo\n'
                f'5 - Descrição\n'
                f'6 - Valor\n'
                f'7 - Desconto\n'
                f'8 - Juros\n'
                f'9 - Situação\n'
                f'10- Matrícula\n')
                if editar == "1":
                    conta[1] = input("\nQual o novo Dia?\n")
                if editar == "2":
                    conta[2] = input("\nQual o novo Mês?\n")
                if editar == "3":
                    conta[3] = input("\nQual o novo Ano?\n")
                if editar == "4":
                    conta[4] = input("\nQual o novo tipo?\n")
                if editar == "5":
                    conta[5] = input("\nQual a nova descrição?\n")
                if editar == "6":
                    conta[6] = input("\nQual o novo valor?\n")
                if editar == "7":
                    conta[7] = input("\nQual a nova desconto?\n")
                if editar == "8":
                    conta[8] = input("\nQual o novo juros?\n")
                if editar == "9":
                    situacao = input("Nova situação:\n1 - PG\n2 - EM ABERTO\n")
                    if situacao == "1":
                        situacao = "PAGO"
                    if situacao == "2":
                        situacao = "EM ABERTO"
                    conta[9] = situacao
                if editar == "10":
                    conta[10] = input("\nQual a nova matrícula\n")
                continuar = input("\nDeseja alterar outro item?\n1 - Sim\n2 - Não\n")
    salvar(dados, 'financeiro.xlsx', "financeiro")


def delete_item(dados, setor):
    if setor == "aluno":
        local = "cadastro.xlsx"
        txt = "Qual a matrícula do aluno"
    elif setor == "financeiro":
        local = "financeiro.xlsx"
        txt = "Qual o ID do item?"
    primary_key = input(txt)
    for item in dados:
        if int(item[0]) == int(primary_key):
            dados.remove(item)
    salvar(dados, local, setor)


def atualizar_lancamentos(cadastro, lancamento):
    checagem_mensalidades(cadastro, lancamento)
    salvar(lancamento, "lancamentos_mensalidades.xlsx",
           "lancamentos_mensalidades")
    atualizar_debitos(cadastro, lancamento)


# Tratamento de dados
cadastro_array = transformar_dataframe_em_array(cadastro_dataframe)
financeiro_array = transformar_dataframe_em_array(financeiro_dataframe)
lancamento_array = transformar_dataframe_em_array(lancamento_mensalidades)


# Menu
m = "9"
while m == "9":
    atualizar_lancamentos(cadastro_array, lancamento_array)
    m = input("\nMENU PRINCIPAL\n\n1 - alunos\n2 - Financeiro\n")
    if m == "1":
        m = "aluno"
    elif m == "2":
        m = "financeiro"
    while m == "aluno" or m == "financeiro":
        m = menu(m, financeiro_array, cadastro_array, lancamento_array)
