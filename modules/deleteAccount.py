import json
import os
from modules.utilities import numb_criteria
from modules.utilities import greetings

#Terminate Account menu.
def terminate_account():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
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
                print("===ELIMINAR CUENTA.=== \n1. Cuenta de Ahorros. \n2. Cuenta Corriente \n3. Tarjeta de Crédito. \n4. Préstamo de Libre Inversión. \n5. Crédito Hipotecario. \n6. Crédito Automotriz. \n7. Salir.")
                option = int(input(f"\n{greetings(client['gender'])} {client['name']}! \nElige el tipo de cuenta a eliminar: "))

                if option == 1:
                    dt_cAhorros(client, cc)
                elif option == 2:
                    dt_cCorriente(client, cc)
                elif option == 3:
                    dt_tdc(client, cc)
                elif option == 4:
                    dt_pLoan(client, cc)
                elif option == 5:
                    dt_mortgage(client, cc)
                elif option == 6:
                    dt_cLoan(client, cc)
                elif option == 7:
                    return
                else:
                    print("Por favor, ingrese una opción válida...")
                    continue
            except(ValueError, KeyboardInterrupt) as sixth:
                print(f"Error: {sixth}, elige una opción válida...")

def dt_cAhorros(client, cc):
    os.system('cls' if os.name == 'nt' else 'clear')
    accounts = client["debit_accounts"]
    balances = accounts.get("balance", {})

    savings_balance = balances.get("savings_account", 0)
    checking_account = accounts.get("checking_account")

    if savings_balance > 0:

        if checking_account not in (None, 0):
            balances["checking_account"] = (balances.get("checking_account", 0) or 0) + savings_balance
            print(f"Se han transferido ${savings_balance} de la Cuenta de Ahorros a la Cuenta Corriente.")
        else:
            print(f"Lamentamos verle partir, su cheque por la cantidad de ${savings_balance} estará disponible en 7 días hábiles, en su sucursal bancaria más cercana.")
            input("Presione Enter para continuar...")
        
    balances.pop("savings_account", None)
    accounts.pop("savings_account", None)
    accounts["balance"] = balances
    client["debit_accounts"] = accounts

#Overwrite data in Json
    with open("data/clients.json", "r") as am:
        info = json.load(am)
    info["clients"][str(cc)] = client
    with open("data/clients.json", "w") as am:
        json.dump(info, am, indent=4)

    print("Cuenta de Ahorros eliminada con éxito.")
    input("Presione Enter para continuar...")
    return

def dt_cCorriente(client, cc):
    os.system('cls' if os.name == 'nt' else 'clear')
    accounts = client["debit_accounts"]
    balances = accounts.get("balance", {})

    checking_balance = balances.get("checking_account", 0)
    savings_account = accounts.get("savings_account")

    if checking_balance > 0:

        if savings_account not in (None, 0):
            balances["checking_account"] = (balances.get("checking_account", 0) or 0) + checking_balance
            print(f"Se han transferido ${checking_balance} de la Cuenta de Ahorros a la Cuenta Corriente.")
        else:
            print(f"Lamentamos verle partir, su cheque por la cantidad de ${checking_balance} estará disponible en 7 días hábiles, en su sucursal bancaria más cercana.")
            input("Presione Enter para continuar...")
    
    balances.pop("checking_account", None)
    accounts.pop("checking_account", None)
    accounts["balance"] = balances
    client["debit_accounts"] = accounts

#Overwrite data in Json.
    with open("data/clients.json", "r") as am:
        info = json.load(am)
    info["clients"][str(cc)] = client
    with open("data/clients.json", "w") as am:
        json.dump(info, am, indent=4)

    print("Cuenta Corriente eliminada con éxito.")
    input("Presione Enter para continuar...")
    return

def dt_tdc(client, cc):
    os.system('cls' if os.name == 'nt' else 'clear')
    loans = client.get("loans", {})
    credit = loans.get("credit_card")

    if not credit:
        print("No tiene tarjeta de crédito registrada.")
        input("Presione Enter para continuar...")
        return

    if credit.get("debt", 0) > 0:
        print(f"No puede eliminar la Tarjeta de Crédito. Deuda pendiente: ${credit['debt']}")
        input("Presione Enter para continuar...")
        return

    loans.pop("credit_card")
    client["loans"] = loans

#Overwrite data in Json.
    with open("data/clients.json", "r") as am:
        info = json.load(am)
    info["clients"][str(cc)] = client
    with open("data/clients.json", "w") as am:
        json.dump(info, am, indent=4)

    print("Tarjeta de Crédito eliminada con éxito.")
    input("Presione Enter para continuar...")

def dt_pLoan(client, cc):
    os.system('cls' if os.name == 'nt' else 'clear')
    loans = client.get("loans", {})
    credit = loans.get("any_ploan")

    if not credit:
        print("No tiene ningún Préstamo de Libre Inversión activo.")
        input("Presione Enter para continuar...")
        return

    if credit.get("debt", 0) > 0:
        print(f"No puede eliminar el Préstamo de Libre Inversión. Deuda pendiente: ${credit['debt']}")
        input("Presione Enter para continuar...")
        return

    loans.pop("any_ploan")
    client["loans"] = loans

#Overwrite data in Json.
    with open("data/clients.json", "r") as am:
        info = json.load(am)
    info["clients"][str(cc)] = client
    with open("data/clients.json", "w") as am:
        json.dump(info, am, indent=4)

    print("Préstamo de Libre Inversión eliminado con éxito.")
    input("Presione Enter para continuar...")

#Mortgage
def dt_mortgage(client, cc):
    os.system('cls' if os.name == 'nt' else 'clear')
    loans = client.get("loans", {})
    credit = loans.get("mortgage")

    if not credit:
        print("No tiene ningún Crédito Hipotecario activo.")
        input("Presione Enter para continuar...")
        return

    if credit.get("debt", 0) > 0:
        print(f"No puede eliminar el Crédito Hipotecario. Deuda pendiente: ${credit['debt']}")
        input("Presione Enter para continuar...")
        return

    loans.pop("mortgage")
    client["loans"] = loans

#Overwrite data in Json.
    with open("data/clients.json", "r") as am:
        info = json.load(am)
    info["clients"][str(cc)] = client
    with open("data/clients.json", "w") as am:
        json.dump(info, am, indent=4)

    print("Crédito Hipotecario eliminado con éxito.")
    input("Presione Enter para continuar...")

#Vehicle loan.
def dt_cLoan(client, cc):
    os.system('cls' if os.name == 'nt' else 'clear')
    loans = client.get("loans", {})
    credit = loans.get("vehicle_loan")

    if not credit:
        print("No tiene ningún Crédito Automotriz activo.")
        input("Presione Enter para continuar...")
        return

    if credit.get("debt", 0) > 0:
        print(f"No puede eliminar el Crédito Automotriz. Deuda pendiente: ${credit['debt']}")
        input("Presione Enter para continuar...")
        return

    loans.pop("vehicle_loan")
    client["loans"] = loans

#Overwrite data in Json.
    with open("data/clients.json", "r") as am:
        info = json.load(am)
    info["clients"][str(cc)] = client
    with open("data/clients.json", "w") as am:
        json.dump(info, am, indent=4)

    print("Crédito Automotriz eliminado con éxito.")
    input("Presione Enter para continuar...")