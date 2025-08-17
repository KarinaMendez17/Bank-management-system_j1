import json
from modules.utilities import numb_criteria

#Main menu option 1.
def create_account():
    print("===CREAR CUENTA=== \n1. Cuenta de Ahorros. \n2. Cuenta Corriente.")
    option = int(input("Selecciona el tipo de cuenta a crear: "))

#New savings account.
    if option == 1:
        create_ca()

#New checking account.
    elif option == 2:
        create_cc()
    
    else:
        print("Opción inválida...")


#New account suboptions.
def create_ca():
    cc = int(input("Ingrese su número de cédula: ", lngt = 10)).strip()

def create_cc():
    cc = int(input("Ingrese su número de cédula: ", lngt = 10)).strip()