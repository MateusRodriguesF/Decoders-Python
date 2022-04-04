print("""
   _   _   _   _   _   _     _   _   _   _   _   _   _   _  
  / \ / \ / \ / \ / \ / \   / \ / \ / \ / \ / \ / \ / \ / \ 
 ( P | y | t | h | o | n ) ( d | e | c | o | d | e | r | s )
  \_/ \_/ \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ 
""")
print("         Codado Por Mateus Rodrigues - 2017")
import base64
import hashlib
from time import sleep
option = 0
rodar = "s"
while rodar == "s" :
    while option != 6:
        print("""

 ____________________________________________________
|  ________________________________________________  |
| |                                                | |
| |                  __MENU__                      | |
| |                                                | |
| |        [ 1 ] BINÁRIO PARA HEXADECIMAL          | |
| |        [ 2 ] HEXADECIMAL PARA ASCII            | |
| |        [ 3 ] BASE-64 DECODER                   | |
| |        [ 4 ] BASE-64 ENCODER                   | |
| |        [ 5 ] MD5 ENCODER                       | |
| |                                                | |
| |                                                | |
| |                                                | |
| |                                                | |
| |________________________________________________| |
|____________________________________________________|




        """)
        option = int(input('Qual A Sua Opçao: \n'))
        if option == 1:
            binary_string = input ( "DIGITE UM NUMERO BINARIO: \n\n")
            
            print("CONSIDERE SÓ O VALOR DEPOIS DE 0x \n")
            decimal_representation = int(binary_string, 2)
            hexadecimal_string = hex(decimal_representation)
            print(binary_string + "CONVERTIDO PARA HEX É: \n" + hexadecimal_string)
            rodar = input("Deseja rodar novamente? s/n: \n")
        while rodar not in "sn":
            rodar = input("opçao invalida!!!Deseja rodar novamente? s/n: \n")
        if rodar == "n":
            print("Valew!")
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
            print("Valew!")
            break
        elif option == 3:
            base64_string = input("Entre com uma hash Base64: \n\n")
            base64_str_bytes = base64_string.encode('ascii')
            b64_str_bt = base64.b64decode(base64_str_bytes)
            base64_txt = b64_str_bt.decode('ascii')
            print(base64_txt)
            rodar = input("Deseja rodar novamente? s/n: \n")
        while rodar not in "sn":
            rodar = input("opçao invalida!!!Deseja rodar novamente? s/n: \n")
        if rodar == "n":
            print("Valew!")
            break
        elif option == 4:
            message = input("Insira Alguma Coisa: ")
            message_bytes = message.encode('ascii')
            base64_bytes = base64.b64encode(message_bytes)
            base64_message = base64_bytes.decode('ascii')
            print(base64_message)
            rodar = input("Deseja rodar novamente? s/n: \n")
        while rodar not in "sn":
            rodar = input("opçao invalida!!!Deseja rodar novamente? s/n: \n")
        if rodar == "n":
            print("Valew!")
            break
        elif option == 5:
            text_sum = input("Digite algo para verificar a Hash MD5: \n")
            print(hashlib.md5(text_sum.encode('utf-8')).hexdigest())
            rodar = input("Deseja rodar novamente? s/n: \n")
        while rodar not in "sn":
            rodar = input("opçao invalida!!!Deseja rodar novamente? s/n: \n")
        if rodar == "n":
            print("Valew!")
            break

