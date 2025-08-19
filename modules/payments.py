import json
import os
import time
from modules.utilities import numb_criteria
from modules.utilities import greetings

def payments():
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
                debit_accounts = client.get("debit_accounts", {})
                if not debit_accounts:
                    print("No tiene cuentas de débito para realizar pagos.")
                    input("Presione Enter para continuar...")
                    return

                print("===PAGAR CRÉDITO=== \n1. Tarjeta de Crédito. \n2. Préstamo de Libre Inversión. \n3. Crédito Hipotecario. \n4. Crédito Automotriz. \n5. Salir.")
                option = int(input(f"\n{greetings(client['gender'])} {client['name']} \nElige una opción: "))
                if option == 1:
                    pay_credit(client, cc, credit_type="credit_card", credit_name="Tarjeta de Crédito.")
                elif option == 2:
                    pay_credit(client, cc, credit_type="any_ploan", credit_name="Préstamo de Libre Inversión.")
                elif option == 3:
                    pay_credit(client, cc, credit_type="mortgage", credit_name="Crédito Hipotecario.")
                elif option == 4:
                    pay_credit(client, cc, credit_type="vehicle_loan", credit_name="Crédito Automotriz.")
                elif option == 5:
                    return
                else:
                    print("Por favor, elige una opción válida...")
                    time.sleep(1)
                    continue
            except (ValueError, KeyboardInterrupt) as sixth:
                print(f"Error: {sixth}. Por favor, ingrese una opción válida...")


def pay_credit(client, cc, credit_type, credit_name):
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        try:
            loans = client.get("loans", {})
            credit = loans.get(credit_type)
            
            if not credit or credit.get("debt", 0) <=0:
                print(f"No tiene deuda activa en {credit_name}.")
                input("Presione Enter para continuar...")
                return

            debit_accounts = client.get("debit_accounts", {})
            balance = debit_accounts.get("balance", {})
            
            print(f"===PAGO DE {credit_name.upper()}===\nTotal deuda: ${credit['debt']}\nSaldo actual: ${credit['balance']}\nLímite de crédito: ${credit['limit']}")
            print("Opciones de pago:")
            print("1. Pago mínimo")
            print("2. Pago total")
            print("3. Pago parcial")
            
            choice = int(input("Seleccione opción: "))
            
            if choice == 1:
                amount = credit.get("minimum", 1000)
                print(f"Monto mínimo a pagar: ${amount}")
            elif choice == 2:
                amount = credit.get("debt", 0)
                print(f"Monto total a pagar: ${amount}")
            elif choice == 3:
                amount = float(input("Ingrese el monto que desea pagar: "))
                if amount <= 0:
                    print("Monto inválido.")
                    return
                if amount > credit.get("debt", 0):
                    amount = credit["debt"]
                    print(f"El monto ingresado supera la deuda, se ajustará a ${amount}")
            else:
                print("Por favor, elige una opción válida...")
                continue
            
#Choose account
            print("\nSeleccione la cuenta desde la que desea pagar:")
            print(f"1. Cuenta de Ahorros - Saldo: ${balance.get('savings_account', 0)}")
            print(f"2. Cuenta Corriente - Saldo: ${balance.get('checking_account', 0)}")
            choice = int(input("Opción: "))
            if choice == 1:
                acc_type = "savings_account"
            else:
                acc_type= "checking_account"
            
            if amount > balance.get(acc_type, 0):

                print("Fondos insuficientes en la cuenta seleccionada.")
                input("Presione Enter para continuar...")
                continue

#Apply payment
            balance[acc_type] -= amount
            credit["debt"] -= amount
            
#Save changes
            debit_accounts["balance"] = balance
            client["debit_accounts"] = debit_accounts
            loans[credit_type] = credit
            client["loans"] = loans
            
            with open("data/clients.json", "r") as f:
                info = json.load(f)
            info["clients"][str(cc)] = client
            with open("data/clients.json", "w") as f:
                json.dump(info, f, indent=4)
            
            print(f"Pago de ${amount} aplicado a {credit_name}. Deuda restante: ${credit['debt']}")
            input("Presione Enter para continuar...")
            return
        except (ValueError, KeyboardInterrupt) as sixth:
                print(f"Error: {sixth}. Por favor, ingrese una opción válida...")