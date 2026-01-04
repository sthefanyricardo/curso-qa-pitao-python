def mostra_nome(nome):
    print(nome)

mostra_nome("Sthefany Albuquerque Ricardo")

print("Sthefany Albuquerque Ricardo")


def converter_para_real(valor_em_dolar):
    cotacao = 5.50
    resultado = valor_em_dolar * cotacao
    return resultado

valor_convertido = converter_para_real(100)

print(valor_convertido)


def criar_email_corporativo(nome, empresa):
    email = f"{nome}@{empresa}.com.br"
    return email.lower()

email_formatado = criar_email_corporativo('sthefany.ricardo', 'qapitao')
print(email_formatado)

email_formatado = criar_email_corporativo('sthefany.qapitao', 'python')
print(email_formatado)

email_formatado = criar_email_corporativo('sthefany.python', 'qapitão')
print(email_formatado)
