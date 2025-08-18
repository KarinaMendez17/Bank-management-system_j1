import json
import time
import os
from modules.utilities import numb_criteria
from modules.utilities import greetings


#One must be a client to be able to use this function.
def deposit():
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
            os.system('cls' if os.name == 'nt' else 'clear')
            try:
                print(f"===DEPÓSITOS.=== \n{greetings(client['gender'])} {client['name']}!")
                print("1. Mis Cuentas.\n2. Depositar a otra cuenta. \n3. Salir.")
                option = int(input("Elige a quién deseas depositar: "))

#My products.
                if option == 1:
                    my_products(client, cc)
#Someone else.
                elif option == 2:
                    other_acc()
#Return to main menu.
                elif option == 3:
                    return
                else:
                    print("Por favor, elige una opción válida...")
                    time.sleep(1)
                    continue
            except(ValueError, KeyboardInterrupt) as sixth:
                print(f"Error: {sixth}, elige una opción válida...")

#Option 1:
def my_products(client, cc):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            print("===Mis Cuentas===")
            accounts = client["debit_accounts"]

            if accounts.get("savings_account") and accounts.get("checking_account"):
                print(f"\n1. Cuenta de Ahorros ({accounts['savings_account']}) \n2. Cuenta Corriente ({accounts['checking_account']}) \n3. Volver")
                choice = int(input("Elige la cuenta a la que deseas depositar: "))
                if choice == 1:
                    deposit_ca(client, cc)
                elif choice == 2:
                    deposit_cc(client, cc)
                elif choice == 3:
                    return
                else:
                    print("Opción inválida, intenta de nuevo.")
                    time.sleep(1)
        except(ValueError, KeyboardInterrupt) as sixth:
            print(f"Error: {sixth}, elige una opción válida...")

#Option 1: SB 1: Deposit to savings account.
def deposit_ca(client, cc):
            os.system('cls' if os.name == 'nt' else 'clear')
            amount = float(input("Monto a depositar en Cuenta de Ahorros: "))
            client["debit_accounts"]["balance"]["savings_account"] += amount
            accounts = client["debit_accounts"]

#Save new balance in Json.
            with open("data/clients.json", "r") as am:
                info = json.load(am)
            info["clients"][str(cc)] = client
            with open("data/clients.json", "w") as am:
                json.dump(info, am, indent=4)

            print(f"Depósito exitoso en su cuenta ({accounts['savings_account']}). \nNuevo saldo de Ahorros: {client['debit_accounts']['balance']['savings_account']}")
            input("Presione Enter para continuar...")
                      
#Option 1: SB 2: Deposit to checking account.
def deposit_cc(client, cc):
    os.system('cls' if os.name == 'nt' else 'clear')
    amount = float(input("Monto a depositar en Cuenta Corriente: "))
    client["debit_accounts"]["balance"]["checking_account"] += amount
    accounts = client["debit_accounts"]

#Save new balance in Json.
    with open("data/clients.json", "r") as am:
        info = json.load(am)
    info["clients"][str(cc)] = client
    with open("data/clients.json", "w") as am:
        json.dump(info, am, indent=4)

    print(f"Depósito exitoso en su cuenta ({accounts['checking_account']}). \nNuevo saldo de Cuenta Corriente: {client['debit_accounts']['balance']['checking_account']}")
    input("Presione Enter para continuar...")

#Option 2:
def other_acc():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        try:
            with open("data/clients.json", "r") as am:
                info = json.load(am)

            acc_number = int(input("Ingresa el número de cuenta destino: "))
            
#Search for the client's account.
            found_client = None
            acc_type = None
            for cc, client in info["clients"].items():
                accounts = client["debit_accounts"]
                if accounts.get("savings_account") == acc_number:
                    found_client = client
                    acc_type = "savings_account"
                    break
                elif accounts.get("checking_account") == acc_number:
                    found_client = client
                    acc_type = "checking_account"
                    break
            if not found_client:
                print("Cuenta no encontrada.")
                input("Presione Enter para continuar...")
                return
            
            account_names = {
                "savings_account": "Cuenta de Ahorros",
                "checking_account": "Cuenta Corriente"
            }

#Ask for the amount.
            amount = float(input(f"Monto a depositar en la {account_names[acc_type]}: "))
            found_client["debit_accounts"]["balance"][acc_type] += amount


#Saves the new balance in the client's information.
            info["clients"][cc] = found_client
            with open("data/clients.json", "w") as am:
                json.dump(info, am, indent=4)

            print(f"Depósito exitoso por la cantidad de: ${amount} a la cuenta de {found_client['name']} con terminación {str(acc_number)[-2:]}")
            input("Presione Enter para continuar...")
            return
        except(ValueError, KeyboardInterrupt) as sixth:
            print(f"Error: {sixth}, elige una opción válida...")