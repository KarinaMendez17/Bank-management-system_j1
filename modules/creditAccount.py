import json
import random
import os
from datetime import datetime
from modules.utilities import numb_criteria
from modules.utilities import greetings

def create_creditAcc():
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
                print(F"===SOLICITAR CRÉDITO=== \n1. Tarjeta de crédito. \n2. Crédito de Libre Inversión. \n3. Crédito Hipotecario. \n4. Crédito Automotriz. \n5. Salir.")
                option = int(input(f"\n{greetings(client['gender'])} {client['name']}! \nElige una opción: "))

#Credit options.
                if option == 1: 
                    tdc(client, info, cc)
                elif option == 2:
                    aploan(client, info, cc)
                elif option == 3:
                    mortgage(client, info, cc)
                elif option == 4:
                    cloan(client, info, cc)
                elif option == 5:
                    return
                else:
                    print("Por favor, elige una opción válida...")
                    continue
            except(ValueError, KeyboardInterrupt) as sixth:
                print(f"Error: {sixth}, elige una opción válida...")

#Credit card.
def tdc(client, info, cc):
    os.system('cls' if os.name == 'nt' else 'clear')
    if "loans" not in client:
        client["loans"] = {}
    elif "credit_card" in client["loans"]:
        print("Lo sentimos, ya posee una tarjeta de crédito. En este momento no puede solicitar otra.")
        input("Presione Enter para continuar...")
        return
    total_balance, approved = validate_funds(client, min_balance=100000)
    if not approved:
        input("Presione Enter para continuar...")
    else:
#Random Credit Card number generator.
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            tdc_number = str(random.randint(100000, 999999))
            exists = False
            for user in info["clients"].values():
                if "loans" in user and "credit_card" in user["loans"]:
                    if user["loans"]["credit_card"]["card_number"] == tdc_number:
                        exists = True
                        break
            if not exists:
                break

    #Credit Crd limit will be 5 times the total ammount of the balance in deb accounts.
        credit_limit = total_balance * 5
        today = datetime.today()
        expiration_date = today.replace(year=today.year + 8)

        client["loans"]["credit_card"] = {
            "card_number": tdc_number,
            "balance": credit_limit,
            "limit": credit_limit,
            "debt": 0,
            "creation_date": today.strftime("%Y-%m-%d"),
            "expiration_date": expiration_date.strftime("%Y-%m-%d"),
            "payment_day": 13
        }

        info["clients"][str(cc)] = client
        with open("data/clients.json", "w") as am:
            json.dump(info, am, indent=4)

        print(f"Tarjeta de crédito creada con número: {tdc_number}")
        print(f"Límite aprobado: ${credit_limit}")
        print(f"Fecha de creación: {today.strftime("%Y-%m-%d")}")
        print(f"Fecha de expiración: {expiration_date.strftime('%Y-%m-%d')}")
        print("Su fecha de pago es el día 13 de cada mes.")
        input("Presione Enter para continuar...")

#Any Purpose Loan.
def aploan(client, info, cc):
    os.system('cls' if os.name == 'nt' else 'clear')
    if "loans" not in client:
        client["loans"] = {}
    elif "any_ploan" in client["loans"]:
        print("Lo sentimos, ya posee un Préstamo de Libre Inversión. En este momento no puede solicitar otro.")
        input("Presione Enter para continuar...")
        return
#To validate if the client has funds enough.
    total_balance, approved = validate_funds(client, min_balance=50000)
    if not approved:
        input("Presione Enter para continuar...")
    else:
#Random Loan number generator.
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            apl_number = str(random.randint(100, 999))
            exists = False
            for user in info["clients"].values():
                if "loans" in user and "any_ploan" in user["loans"]:
                    if user["loans"]["any_ploan"]["ploan_number"] == apl_number:
                        exists = True
                        break
            if not exists:
                break
#Loan max amount will be 3 times the total amount of the balance in deb accounts.
        credit_limit = total_balance * 3
        today = datetime.today()
        expiration_date = today.replace(year=today.year + 2)

        client["loans"]["any_ploan"] = {
            "ploan_number": apl_number,
            "balance": credit_limit,
            "limit": credit_limit,
            "debt": 0,
            "creation_date": today.strftime("%Y-%m-%d"),
            "expiration_date": expiration_date.strftime("%Y-%m-%d"),
            "payment_day": 15
        }

        info["clients"][str(cc)] = client
        with open("data/clients.json", "w") as am:
            json.dump(info, am, indent=4)

        print(f"Felicitaciones, su Préstamo de Libre Inversión fue aprobado, con el número: {apl_number}")
        print(f"Límite aprobado: ${credit_limit}")
        print(f"Fecha de creación: {today.strftime("%Y-%m-%d")}")
        print(f"Fecha de expiración: {expiration_date.strftime('%Y-%m-%d')}")
        print("Su fecha de pago es el día 15 de cada mes.")
        input("Presione Enter para continuar...")

#Morgage
def mortgage(client, info, cc):
    os.system('cls' if os.name == 'nt' else 'clear')
    if "loans" not in client:
        client["loans"] = {}
    elif "mortgage" in client["loans"]:
        print("Lo sentimos, ya posee un Crédito Hipotecario. En este momento no puede solicitar otro.")
        input("Presione Enter para continuar...")
        return
#To validate if the client has funds enough.
    total_balance, approved = validate_funds(client, min_balance=5000000)
    if not approved:
        input("Presione Enter para continuar...")
    else:
#Random Loan number generator.
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            mrtg_number = str(random.randint(1000000, 9999999))
            exists = False
            for user in info["clients"].values():
                if "loans" in user and "mortgage" in user["loans"]:
                    if user["loans"]["morgage"]["mortgage_number"] == mrtg_number:
                        exists = True
                        break
            if not exists:
                break
#Loan max amount will be 20 times the total amount of the balance in deb accounts.
        credit_limit = total_balance * 20
        today = datetime.today()
        expiration_date = today.replace(year=today.year + 30)

        client["loans"]["mortgage"] = {
            "mortgage_number": mrtg_number,
            "balance": credit_limit,
            "limit": credit_limit,
            "debt": 0,
            "creation_date": today.strftime("%Y-%m-%d"),
            "expiration_date": expiration_date.strftime("%Y-%m-%d"),
            "payment_day": 30
        }

        info["clients"][str(cc)] = client
        with open("data/clients.json", "w") as am:
            json.dump(info, am, indent=4)

        print(f"Felicitaciones, su Crédito Hipotecario fue aprobado, con el número: {mrtg_number}")
        print(f"Límite aprobado: ${credit_limit}")
        print(f"Fecha de creación: {today.strftime("%Y-%m-%d")}")
        print(f"Fecha de expiración: {expiration_date.strftime('%Y-%m-%d')}")
        print("Su fecha de pago es el día 30 de cada mes.")
        input("Presione Enter para continuar...")

#Vehicle Loan
def cloan(client, info, cc):
    os.system('cls' if os.name == 'nt' else 'clear')
    if "loans" not in client:
        client["loans"] = {}
    elif "vehicle_loan" in client["loans"]:
        print("Lo sentimos, ya posee un Crédito Automotriz. En este momento no puede solicitar otro.")
        input("Presione Enter para continuar...")
        return
    
#To validate if the client has funds enough.
    total_balance, approved = validate_funds(client, min_balance=2000000)
    if not approved:
        input("Presione Enter para continuar...")
    else:
#Random Loan number generator.
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            vloan_number = str(random.randint(10000000, 99999999))
            exists = False
            for user in info["clients"].values():
                if "loans" in user and "vehicle_loan" in user["loans"]:
                    if user["loans"]["vehicle_loan"]["vloan_number"] == vloan_number:
                        exists = True
                        break
            if not exists:
                break
#Loan max amount will be 20 times the total amount of the balance in deb accounts.
        credit_limit = total_balance * 10
        today = datetime.today()
        expiration_date = today.replace(year=today.year + 10)

        client["loans"]["vehicle_loan"] = {
            "vloan_number": vloan_number,
            "balance": credit_limit,
            "limit": credit_limit,
            "debt": 0,
            "creation_date": today.strftime("%Y-%m-%d"),
            "expiration_date": expiration_date.strftime("%Y-%m-%d"),
            "payment_day": 20
        }

        info["clients"][str(cc)] = client
        with open("data/clients.json", "w") as am:
            json.dump(info, am, indent=4)

        print(f"Felicitaciones, su Crédito Automotriz fue aprobado, con el número: {vloan_number}")
        print(f"Límite aprobado: ${credit_limit}")
        print(f"Fecha de creación: {today.strftime("%Y-%m-%d")}")
        print(f"Fecha de expiración: {expiration_date.strftime('%Y-%m-%d')}")
        print("Su fecha de pago es el día 20 de cada mes.")
        input("Presione Enter para continuar...")


#To validate if the client has funds enough.
def validate_funds(client, min_balance=0):
    balances = client.get("debit_accounts", {}).get("balance", {})
    savings = balances.get("savings_account", 0)
    checking = balances.get("checking_account", 0)
    total_balance = savings + checking

    if total_balance < min_balance:
        print("Su solicitud está siendo validada. En un plazo de 7 días tendrá respuesta...")
        return total_balance, False
    return total_balance, True