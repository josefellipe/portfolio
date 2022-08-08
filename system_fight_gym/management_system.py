from re import A
import pandas as pd


enroll_dataframe = pd.read_excel("cadastro.xlsx")
header_cadastros = list(enroll_dataframe.columns)
# MATRICULA | NOME | FAIXA | GRAU | DATA DE VENCIMENTO | VALOR DA MENSALIDADE | SITUAÇÃO | DÉBITOS
financial_dataframe = pd.read_excel("financeiro.xlsx")
header_financeiro = list(financial_dataframe.columns)
# ID | DATA | TIPO | DESCRIÇÃO | VALOR | DESCONTO | JUROS | SITUAÇÃO


def transform_dataframe_into_array(data):
    aux = []
    for i in range(len(data)):
        aux.append(list(data.loc[i]))
    return aux


def transform_array_into_dataframe(data, menu_choice):
    if menu_choice == "student":
        header = header_cadastros
    if menu_choice == "financial":
        header = header_financeiro
    dataFrame = pd.DataFrame(data, columns=header)
    return dataFrame


def salve(data, local, menu_choice):
    data_frame = transform_array_into_dataframe(data,menu_choice)
    data_frame.to_excel(local, index=False)


def create_primary_key(data):
    primary_key = 0
    if data != []:
        for item in data:
            if int(item[0]) >= primary_key:
                primary_key = int(item[0]) + 1
    return primary_key


def menu(n, data_student, data_financial):
    resposta = n
    while resposta == "student":
        resposta = menu_student(data_student)
    while resposta == "financial":
        resposta = menu_financial(data_financial)
    return resposta


def menu_student(data):
    menu_choice = "student"
    choice = input(
            "\n1 - Consultar\n2 - Editar\n3 - Matricular\n4 - Excluir\n5 - Sair\n")
    if choice == "1":
        print(transform_array_into_dataframe(data,menu_choice))
    if choice == "2":
        edit_student(data)
    if choice == "3":
        add_student(data)
    if choice == "4":
        delete_item(data,menu_choice)
    if choice == "5":
        menu_choice = "9"
    return menu_choice


def menu_financial(data):
    menu_choice = "financial"
    choice = input(
            "\n1 - Consultar\n2 - Editar\n3 - Adicionar\n4 - Excluir\n5 - Sair\n")
    if choice == "1":
        print(transform_array_into_dataframe(data,menu_choice))
    if choice == "2":
        edit_financial(data)
    if choice == "3":
        add_financial(data)
    if choice == "4":
        delete_item(data,menu_choice)
    if choice == "5":
        menu_choice = "9"
    return menu_choice



def add_student(data):
    new_student = "1"
    while new_student == "1":
        primary_key = create_primary_key(data)
        aux = []
        aux.append(primary_key)
        aux.append(input("Name:  "))
        aux.append(input("Belt:  "))
        aux.append(input("Degree:  "))
        aux.append(input("Due date:  "))
        aux.append(input("Monthly fee:  "))
        aux.append("ATIVO")
        aux.append(0)
        data.append(aux)
        salve(data,'cadastro.xlsx',"student")
        new_student = input(
                "\nDeseja cadastrar mais um aluno?\n1 - Sim\n2 - Não\n")


def add_financial(data):
    new_financial = "1"
    while new_financial == "1":
        primary_key = create_primary_key(data)
        aux = []
        aux.append(primary_key)
        aux.append(input("Date:  "))
        aux.append(input("Type:  "))
        aux.append(input("Descrition:  "))
        aux.append(input("Value:  "))
        aux.append(input("Descount:  "))
        aux.append(input("Fees:  "))
        aux.append(input("Situation:  "))
        data.append(aux)
        salve(data,'financeiro.xlsx', "financial")
        new_financial = input(
                "\nDeseja cadastrar mais uma conta?\n1 - Sim\n2 - Não\n")


def edit_student(data):
    primary_key_student = input("\nWhat is the student's enrollment?")
    for student in data:
        if int(student[0]) == int(primary_key_student):
            edit = input("Do you wnat to change the name?\n1 - Yes\n2 - No\n")
            if edit == "1":
                student[1] = input("\nWhat is the new name?\n")
            edit = input("Do you wnat to change the Belt?\n1 - Yes\n2 - No\n")
            if edit == "1":
                student[2] = input("\nWhat is the new Belt?\n")
            edit = input("Do you wnat to change the Degree?\n1 - Yes\n2 - No\n")
            if edit == "1":
                student[3] = input("\nWhat is the new Degree?\n")
            edit = input("Do you wnat to change the Due Date?\n1 - Yes\n2 - No\n")
            if edit == "1":
                student[4] = input("\nWhat is the new Due Date?\n")
            edit = input("Do you wnat to change the Monthly Fee?\n1 - Yes\n2 - No\n")
            if edit == "1":
                student[5] = input("\nWhat is the new Monthly Fee?\n")
            edit = input("Do you wnat to change the Status?\n1 - Yes\n2 - No\n")
            if edit == "1":
                student[6] = input("\nWhat is the new Status?\n")
    salve(data,'cadastro.xlsx', "student")


def edit_financial(data):
    primary_key_financial = input("\nWhat is the financial ID?")
    for conta in data:
    # ID | DATA | TIPO | DESCRIÇÃO | VALOR | DESCONTO | JUROS | SITUAÇÃO
        if int(conta[0]) == int(primary_key_financial):
            edit = input("Do you wnat to change the date?\n1 - Yes\n2 - No\n")
            if edit == "1":
                conta[1] = input("\nWhat is the new date?\n")
            edit = input("Do you wnat to change the Type?\n1 - Yes\n2 - No\n")
            if edit == "1":
                conta[2] = input("\nWhat is the new Type?\n")
            edit = input("Do you wnat to change the Descrition?\n1 - Yes\n2 - No\n")
            if edit == "1":
                conta[3] = input("\nWhat is the new Descrition?\n")
            edit = input("Do you wnat to change the Value?\n1 - Yes\n2 - No\n")
            if edit == "1":
                conta[4] = input("\nWhat is the new Value?\n")
            edit = input("Do you wnat to change the Descount?\n1 - Yes\n2 - No\n")
            if edit == "1":
                conta[5] = input("\nWhat is the new Descount?\n")
            edit = input("Do you wnat to change the Fees?\n1 - Yes\n2 - No\n")
            if edit == "1":
                conta[6] = input("\nWhat is the new Fees?\n")
            edit = input("Do you wnat to change the Situation?\n1 - Yes\n2 - No\n")
            if edit == "1":
                conta[7] = input("\nWhat is the new Situation?\n")
    salve(data,'financeiro.xlsx', "financial")


def delete_item(data, setor):
    if setor == "student":
        local = "cadastro.xlsx"
    elif setor == "financial":
        local = "financeiro.xlsx"
    primary_key_student = input("\nWhat is the student's enrollment or financial's ID?")
    for item in data:
        if int(item[0]) == int(primary_key_student):
            data.remove(item)
    salve(data, local, setor)




# Tratamento de dados
enroll = transform_dataframe_into_array(enroll_dataframe)
financial = transform_dataframe_into_array(financial_dataframe)

# Menu
m = "9"
while m == "9":
    m = input("\n1 - Students\n2 - Financial\n")
    if m == "1":
        m = "student"
    elif m == "2":
        m = "financial"
    while m == "student" or m == "financial":
        m = menu(m, enroll, financial)

