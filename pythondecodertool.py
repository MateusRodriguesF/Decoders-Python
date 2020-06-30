print("""
▒█▀▀▄ █▀▀ █▀▀ █▀▀█ █▀▀▄ █▀▀ █▀▀█ █▀▀ 　 █▀▀ █▀▄▀█ 　 ▒█▀▀█ █░░█ ▀▀█▀▀ █░░█ █▀▀█ █▀▀▄ 
▒█░▒█ █▀▀ █░░ █░░█ █░░█ █▀▀ █▄▄▀ ▀▀█ 　 █▀▀ █░▀░█ 　 ▒█▄▄█ █▄▄█ ░░█░░ █▀▀█ █░░█ █░░█ 
▒█▄▄▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀▀▀░ ▀▀▀ ▀░▀▀ ▀▀▀ 　 ▀▀▀ ▀░░░▀ 　 ▒█░░░ ▄▄▄█ ░░▀░░ ▀░░▀ ▀▀▀▀ ▀░░▀""")
print("Por Mateus Rodrigues - 2020")
option = 0
rodar = "s"
while rodar == "s" :
    while option != 6:
        print("""
        [ 1 ] BINÁRIO PARA HEXADECIMAL
        [ 2 ] HEXADECIMAL PARA ASCII
        """)
        option = int(input('Qual A Sua Opçao: \n'))
        if option == 1:
            binary_string = input ( "DIGITE UM NUMERO BINARIO: \n\n")
            
            print("CONSIDERE SO O VALOR DEPOIS DE 0x \n")
            decimal_representation = int(binary_string, 2)
            hexadecimal_string = hex(decimal_representation)
            print(binary_string + "CONVERTIDO PARA HEX É: \n" + hexadecimal_string)
            rodar = input("Deseja rodar novamente? s/n: \n")
        while rodar not in "sn":
            rodar = input("opçao invalida!!!Deseja rodar novamente? s/n: \n")
        if rodar == "n":
            break
        elif option == 2:
            hex_string = input("Digite um codigo hexadecimal: \n\n")[2:]
            bytes_object = bytes.fromhex(hex_string)
            ascii_string = bytes_object.decode("ASCII")
            print(hex_string + " convertido para ASCII é: \n" + ascii_string)
            rodar = input("Deseja rodar novamente? s/n: \n")
        while rodar not in "sn":
            rodar = input("opçao invalida!!!Deseja rodar novamente? s/n: \n")
        if rodar == "n":
             break
        print("obrigado por usar o programa!")
