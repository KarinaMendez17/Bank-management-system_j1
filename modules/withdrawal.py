import json
import os
from datetime import datetime
from modules.utilities import numb_criteria
from modules.utilities import greetings

def withdrawal():
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
                print("===RETIROS=== \n1. Cuenta de Ahorros. \n2. Cuenta Corriente. \n3. Tarjeta de Crédito. \n4. Disponer de fondos de Préstamos. \n5. Salir.")
                option = int(input(f"\n{greetings(client['gender'])} {client['name']}! \nSelecciona una opción: "))

                if option == 1:
                     wtdraw_debit(client, info, cc, account_type="savings_account", min_amount=10000, max_amount=350000)
                elif option == 2:
                     wtdraw_debit(client, info, cc, account_type="checking_account", min_amount=10000, max_amount=500000)
                elif option == 3:
                     w_loan(client, info, cc, account_type="credit_card", min_amount=100000, max_amount=150000)
                elif option == 4:
                     wd_loans(client, info, cc)
                elif option == 5:
                     return
            except (ValueError, KeyboardInterrupt) as sixth:
                print(f"Error {sixth}, Por favor ingrese una opción válida...")

#Loan withdrawal.
def w_loan(client, info, cc, account_type, min_amount=0, max_amount=0):
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        try:
            balances = client.get("loans", {}).get(account_type, {})
            current_balance = balances.get("balance", 0)
            account_number = balances.get("card_number", 0)
            account_names = {
                "credit_card": "Tarjeta de Crédito.",
                "any_ploan": "Préstamo de Libre Inversión.",
                "mortgage": "Crédito Hipotecario.",
                "vehicle_loan": "Crédito Automotriz."
            }
            print(f"Cuenta: {account_names[account_type]}")
            print(f"Número de cuenta: {account_number}")
            print(f"Saldo disponible: {current_balance}")

            if current_balance <= 0:
                print("Fondos insuficientes. No puede realizar retiros.")
                input("Presione Enter para continuar...")
                return
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Seleccione destino: \n1. Cuenta de Ahorros. \n2. Cuenta Corriente. \n3. Retiro en efectivo.")
                dest = int(input("Elige una opción: "))

                if dest == "1":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    savings_balance = client.get("debit_accounts", {}).get("balance", {}).get("savings_account")
                    if not savings_balance:
                        print("Usted no tiene una Cuenta de Ahorros registrada.")
                        input("Presione Enter para continuar...")
                        return
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        amount = int(input("Ingrese el monto a transferir: "))
                        if amount <= 0:
                            print("No se permiten retiros negativos o en cero.")
                            input("Presione Enter para continuar...")
                            continue
                        elif amount % 10000 != 0:
                            print("El monto debe ser múltiplo de 10000.")
                            input("Presione Enter para continuar...")
                            continue
                        elif amount < min_amount:
                            print(f"El monto mínimo a retirar es de: ${min_amount}")
                            input("Presione Enter para continuar...")
                            continue
                        elif amount > max_amount:
                            print(f"El monto máximo a retirar es de: ${max_amount}")
                            input("Presione Enter para continuar...")
                            continue
                        elif amount > current_balance:
                            print("Fondos insuficientes.")
                            input("Presione Enter para continuar...")
                            continue
                        else:
                            client["loans"][account_type]["balance"] -= amount
                            client["debit_accounts"]["balance"]["savings_account"] += amount
                            client["loans"][account_type]["debt"] = client["loans"][account_type].get("debt", 0) + amount
                            print(f"Transferencia exitosa por: ${amount}. \nNuevo balance de crédito: ${client['loans'][account_type]['balance']}")
                            input("Presione Enter para continuar...")
                elif dest == "2":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    checking_balance = client.get("debit_accounts", {}).get("balance", {}).get("checking_account")
                    if not checking_balance:
                        print("Usted no tiene una Cuenta Corriente registrada.")
                        input("Presione Enter para continuar...")
                        return
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        amount = int(input("Ingrese el monto a transferir: "))
                        if amount <= 0:
                            print("No se permiten retiros negativos o en cero.")
                            input("Presione Enter para continuar...")
                            continue
                        elif amount % 10000 != 0:
                            print("El monto debe ser múltiplo de 10000.")
                            input("Presione Enter para continuar...")
                            continue
                        elif amount < min_amount:
                            print(f"El monto mínimo a retirar es de: ${min_amount}")
                            input("Presione Enter para continuar...")
                            continue
                        elif amount > max_amount:
                            print(f"El monto máximo a retirar es de: ${max_amount}")
                            input("Presione Enter para continuar...")
                            continue
                        elif amount > current_balance:
                            print("Fondos insuficientes.")
                            input("Presione Enter para continuar...")
                            continue
                        else:
                            client["loans"][account_type]["balance"] -= amount
                            client["debit_accounts"]["balance"]["checking_account"] += amount
                            client["loans"][account_type]["debt"] = client["loans"][account_type].get("debt", 0) + amount
                            print(f"Transferencia exitosa por: ${amount}. \nNuevo balance de crédito: ${client['loans'][account_type]['balance']}")
                            input("Presione Enter para continuar...")

                elif dest == "3":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    amount = int(input("Ingrese el monto a retirar: "))

                    if amount <= 0:
                        print("No se permiten retiros negativos o en cero.")
                        input("Presione Enter para continuar...")
                        continue
                    elif amount % 10000 != 0:
                        print("El monto debe ser múltiplo de 10000.")
                        input("Presione Enter para continuar...")
                        continue
                    elif amount < min_amount:
                        print(f"El monto mínimo a retirar es de: ${min_amount}")
                        input("Presione Enter para continuar...")
                        continue
                    elif amount > max_amount:
                        print(f"El monto máximo a retirar es de: ${max_amount}")
                        input("Presione Enter para continuar...")
                        continue
                    elif amount > current_balance:
                        print("Fondos insuficientes.")
                        input("Presione Enter para continuar...")
                        continue
                    else:
                        client["loans"][account_type]["balance"] -= amount
                        client["loans"][account_type]["debt"] = client["loans"][account_type].get("debt", 0) + amount
                        print(f"Retiro éxitoso por: ${amount}. \nNuevo balance de crédito: ${client['loans'][account_type]['balance']}")
                        input("Presione Enter para continuar...")

                else:
                    print("Por favor, elige una opción válida...")
                    input("Presione Enter para continuar...")
                    continue

#Save changes and overwrite data.
            info["clients"][str(cc)] = client
            with open("data/clients.json", "w") as am:
                json.dump(info, am, indent=4)
            return
        except(ValueError, KeyboardInterrupt) as sixth:
            print(f"Error: {sixth}, elige una opción válida...")


#Withdrawings from debit accounts.
def wtdraw_debit(client, info, cc, account_type, min_amount=0, max_amount=0):
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        try:
            balances = client.get("debit_accounts", {}).get("balance", {})
            current_balance = balances.get(account_type, 0)
            account_number = client.get("debit accounts", {}).get(account_type)
            account_names = {
                "savings_account": "Cuenta de Ahorros.",
                "checking_account": "Cuenta Corriente."
            }

            print(f"Cuenta: {account_names[account_type]}")
            print(f"Número de cuenta: {account_number}")
            print(f"Saldo disponible: {current_balance}")

            if current_balance <= 0:
                print("Fondos insuficientes. No puede realizar retiros.")
                input("Presione Enter para continuar...")
                return
            
            else:
                amount = int(input(f"Ingrese el monto a retirar: "))
#Withdrawal validations.
                if amount <= 0:
                    print("No se permiten retiros negativos o en cero.")
                    input("Presione Enter para continuar...")
                    continue
                elif amount % 10000 != 0:
                    print("El monto debe ser múltiplo de 10000.")
                    input("Presione Enter para continuar...")
                    continue
                elif amount < min_amount:
                    print(f"El monto mínimo a retirar es de: ${min_amount}")
                    input("Presione Enter para continuar...")
                    continue
                elif amount > max_amount:
                     print(f"El monto máximo a retirar es de: ${max_amount}")
                     input("Presione Enter para continuar...")
                     continue
                elif amount > current_balance:
                    print("Fondos insuficientes.")
                    input("Presione Enter para continuar...")
                    continue
                else:
                    client["debit_accounts"]["balance"][account_type] -= amount

#Save changes and overwrite data.
                    info["clients"][str(cc)] = client
                    with open("data/clients.json", "w") as am:
                        json.dump(info, am, indent=4)

                    print(f"\nRetiro exitoso por la cantidad de: ${amount}.")
                    print(f"Saldo restante: ${client['debit_accounts']['balance'][account_type]}")
                    input("Presione Enter para continuar...")
                    return
        except(ValueError, KeyboardInterrupt) as sixth:
                print(f"Error: {sixth}, elige una opción válida...")

#The rest of available loans are here.
def wd_loans(client, info, cc):
    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("===RETIRO DE PRÉSTAMOS===. \n1. Préstamo de Libre Inversión. \n2. Crédito Hipotecario. \n3. Crédito Automotriz. \n4. Salir.")
            choice = int(input("Elige una opción: "))
            if choice == 1:
                w_loan(client, info, cc, account_type="any_ploan", min_amount=10000, max_amount=1000000)
            if choice == 2:
                w_loan(client, info, cc, account_type="mortgage", min_amount=10000, max_amount=1000000)
            if choice == 3:
                w_loan(client, info, cc, account_type="vehicle_loan", min_amount=10000, max_amount=1000000)
            if choice == 4:
                return
        except(ValueError, KeyboardInterrupt) as sixth:
                print(f"Error: {sixth}, elige una opción válida...")