while True:
    comando = input("Digite sair para fechar o programa: \n").strip().lower()
   
    print(comando)

    if comando == 'sair':
        print("Até logo! \n")
        break
    else:
        print(f"Você digitou o valor: {comando} \n")