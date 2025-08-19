import json
import os
from modules.utilities import numb_criteria
from modules.utilities import greetings
from datetime import datetime

def account_info():
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
            print(f"\n{greetings(client['gender'])} {client['name']}! \nA continuacuón se desglosa la información de tus cuentas:")

            print("\n=== INFORMACIÓN DEL CLIENTE ===")
            print(f"Nombre: {client['name']}")
            print(f"Edad: {client['age']}")
            print(f"Género: {client['gender']}")
            print(f"Email: {client['email']}")
            
            contact = client["contact_info"]
            print(f"Teléfono móvil: {contact['mobile']}")
            print(f"Teléfono fijo: {contact['landline']}")
            
            location = client["location"]
            print(f"País: {location['country']}")
            print(f"Departamento: {location['department']}")
            print(f"Ciudad: {location['city']}")
            print(f"Dirección: {location['address']}")

#Debit accounts information.
            debit_accounts = client["debit_accounts"]
            balances = debit_accounts["balance"]
            print("\n=== CUENTAS DE DÉBITO ===")
            print(f"Cuenta de Ahorros: {debit_accounts['savings_account']} - Saldo: {balances['savings_account']}")
            print(f"Cuenta Corriente: {debit_accounts['checking_account']} - Saldo: {balances['checking_account']}")

            loans = client.get("loans", {})
            account_names = {
                "credit_card": "Tarjeta de Crédito",
                "any_ploan": "Préstamo de Libre Inversión",
                "mortgage": "Crédito Hipotecario",
                "vehicle_loan": "Crédito Automotriz"
            }
            print("\n=== PRÉSTAMOS / CRÉDITOS ===")

            for loan_type, loan_info in loans.items():
                print(f"{account_names.get(loan_type, loan_type)}:")

                number = loan_info.get("card_number") or loan_info.get("ploan_number") \
                        or loan_info.get("mortgage_number") or loan_info.get("vloan_number")
                print(f"  Número: {number}")

#Credit information.
                print(f"  Saldo disponible: {loan_info['balance']}")
                print(f"  Límite: {loan_info['limit']}")
                print(f"  Deuda: {loan_info['debt']}")
                print(f"  Fecha de creación: {loan_info['creation_date']}")
                print(f"  Fecha de expiración: {loan_info['expiration_date']}")
                print(f"  Día de pago: {loan_info['payment_day']}")

#To verify the loan status.
                exp_date = datetime.strptime(loan_info['expiration_date'], "%Y-%m-%d")
                status = "Activo" if exp_date >= datetime.today() else "Vencido"
                print(f"  Estado: {status}\n")
                
            input("Presione Enter para continuar...")
            return

        except(ValueError, KeyboardInterrupt) as sixth:
            print(f"Error: {sixth}, elige una opción válida...")
