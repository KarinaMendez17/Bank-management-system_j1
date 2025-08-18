import json
import random
from modules.utilities import numb_criteria
from modules.utilities import email_criteria
from modules.utilities import greetings

def create_creditAcc():
    while True:
        try:
            with open("data/clients.json", "r") as am:
                info = json.load(am)
            cc = numb_criteria("Ingrese su número de cédula: ", lngt=10)
            client = info["clients"].get(str(cc))
            if not client:
                print("Cliente no encontrado.")
                input("Presione Enter para continuar...")
                return
        except(ValueError, KeyboardInterrupt) as sixth:
            print(f"Error: {sixth}, elige una opción válida...")

        while True:
            try:
                print(F"===SOLICITAR CRÉDITO=== \n{greetings(client['gender'])} {client['name']}! \n1. Tarjeta de crédito. \n.2 Crédito de Libre Inversión. \n3. Crédito Hipotecario. \n4. Crédito Automotriz. \n5. Salir.")
                option = int(input("Elige una opción: "))

#TDC.
                if option == 1:
                    pass
                elif option == 2:
                    pass
                elif option == 3:
                    pass
                elif option == 4:
                    pass
                elif option == 5:
                    return
                else:
                    print("Por favor, elige una opción válida...")
                    continue
            except(ValueError, KeyboardInterrupt) as sixth:
                print(f"Error: {sixth}, elige una opción válida...")