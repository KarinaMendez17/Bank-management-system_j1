import json
from modules.utilities import numb_criteria

#Terminate Account menu.
def terminate_account():
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

            accounts = client["debit_accounts"]
            balances = accounts.get("balance", {})

            print("===Eliminar Cuenta.=== \n1. Cuenta de Ahorros. \n2. Cuenta Corriente \n3. Tarjeta de Crédito. \n4. Préstamo de Libre Inversión. \n5. Crédito Hipotecario. \n6. Crédito Automotriz. \n7. Salir.")
            option = int(input("Elige el tipo de cuenta a eliminar: "))

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

#Delete savings account.
    accounts["savings_account"] = None
    balances["savings_account"] = 0
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

    pass
def dt_cCorriente(client, cc):
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

#Delete savings account.
    accounts["savings_account"] = None
    balances["savings_account"] = 0
    accounts["balance"] = balances
    client["debit_accounts"] = accounts

    # Guardar cambios en JSON
    with open("data/clients.json", "r") as am:
        info = json.load(am)
    info["clients"][str(cc)] = client
    with open("data/clients.json", "w") as am:
        json.dump(info, am, indent=4)

    print("Cuenta Corriente eliminada con éxito.")
    input("Presione Enter para continuar...")
    return

def dt_tdc():
    pass
def dt_pLoan():
    pass
def dt_mortgage():
    pass
def dt_cLoan():
    pass