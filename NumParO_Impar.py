def NumPar_impar():
    while True:
        print("Verificador de numero par o impar.")
        try:
            num = int(input("Digite un numero: "))
            if num % 2 == 0:
                print(f"{num} es un numero par")
            else:
                print(f"{num} es un numero impar.")
        except ValueError:
            print("Error, Digite un número válido.")
NumPar_impar()