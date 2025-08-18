import json
import random
from modules.utilities import numb_criteria
from modules.utilities import email_criteria
from modules.utilities import greetings

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
    print("===Nueva Cuenta de Ahorros.===")
    with open("data/clients.json", "r") as am:
        info = json.load(am)
    cc = numb_criteria("Ingrese su número de cédula: ", lngt = 10)
# convertir cc a string para buscar en las llaves del diccionario
    if str(cc) in info["clients"]:
        client = info["clients"][str(cc)]
        new_acc = "savings"
        if client["debit_accounts"][new_acc + "_account"] is not None:
            print("Ya tiene una cuenta de ahorros.")
            input("Presione Enter para continuar...")
        
        else:
            existing_numbers = [user.get("savings_account") for user in info["clients"].values()]
            savings_account = random.randint(1000, 9999)
            while savings_account in existing_numbers:
                savings_account = random.randint(1000, 9999)
            
            client["debit_accounts"][new_acc + "_account"] = savings_account
            with open("data/clients.json", "w") as am:
                json.dump(info, am, indent=4)

        print(f"Su Cuenta de Ahorros fue creada éxitosamente, con el número: {savings_account}.")
        input("Presione Enter para continuar...")
    else:
#User information.
        name = input("Ingrese su nombre: ").strip().title()
        age = numb_criteria("Ingrese su edad: ", min = 18, max = 120)
        gender = input("Ingrese su género (M/F/O): ").strip().upper()
        email = email_criteria("Ingrese su email: ").strip()
        mobile = numb_criteria("Ingrese su número de teléfono móvil: ", lngt = 10)
        landline = None
        add_landline = input("¿Desea agregar un teléfono fijo? (s/n): ").strip().lower()
        if add_landline == "s":
            landline = numb_criteria("Ingrese su número de teléfono fijo: ", lngt = 10)

#User location.
        country = input("Ingrese su país de residencia: ").strip().capitalize()
        department = input("Ingrese su departamento de residencia: ").strip().capitalize()
        city = input("Ingrese su ciudad de residencia: ").strip().capitalize()
        address = input("Ingrese su dirección actual: ").strip().title()
        
#Random account number
        existing_numbers = [user.get("savings_account") for user in info["clients"].values()]
        savings_account = random.randint(10000, 9999)
        while savings_account in existing_numbers:
            savings_account = random.randint(1000, 9999)

#After data collection
        info["clients"][str(cc)] = {
            "name": name,
            "age": age,
            "gender": gender,
            "email": email,
            "contact_info": {
                "mobile": mobile,
                "landline": landline  #It'll be "Null" if no data is provided
            },
            "location": {
                "country": country,
                "department": department,
                "city": city,
                "address": address
            },
            "debit_accounts": {
                "savings_account": savings_account,
                "checking_account": None,
            },
#The account starts with zero loans, but the option remains there if the client wants to apply for one in the future.
            "loans": {
                "credit_card": None,
                "any_ploan": None,
                "mortgage": None,
                "vehicle_loan": None
            }
}
        
#Save everything in the Json file
        with open("data/clients.json", "w") as am:
            json.dump(info, am, indent=4)

        print(f"Su cuenta fue creada éxitosamente, con el número: {savings_account}. {greetings(gender)}, {name}.")
    input("Presione Enter para continuar...")



def create_cc():
    print("===Nueva Cuenta Corriente.===")
    with open("data/clients.json", "r") as am:
        info = json.load(am)
    cc = numb_criteria("Ingrese su número de cédula: ", lngt = 10)
    if str(cc) in info["clients"]:
        client = info["clients"][str(cc)]
        new_acc = "checking"
        if client["debit_accounts"][new_acc + "_account"] is not None:
            print("Ya tiene una cuenta corriente.")
            input("Presione Enter para continuar...")
        else:
            existing_numbers = [user.get("checking_account") for user in info["clients"].values()]
            checking_account = random.randint(10000, 99999)
            while checking_account in existing_numbers:
                checking_account = random.randint(10000, 99999)
    
            client["debit_accounts"][new_acc + "_account"] = checking_account

            with open("data/clients.json", "w") as am:
                json.dump(info, am, indent=4)
            print(f"Su Cuenta Corriente fue creada éxitosamente, con el número: {checking_account}.")
            input("Presione Enter para continuar...")

    else:
#User information.
        name = input("Ingrese su nombre: ").strip().title()
        age = numb_criteria("Ingrese su edad: ", min = 18, max = 120)
        gender = input("Ingrese su género (M/F/O): ").strip().upper()
        email = email_criteria("Ingrese su email: ").strip()
        mobile = numb_criteria("Ingrese su número de teléfono móvil: ", lngt = 10)
        landline = None
        add_landline = input("¿Desea agregar un teléfono fijo? (s/n): ").strip().lower()
        if add_landline == "s":
            landline = numb_criteria("Ingrese su número de teléfono fijo: ", lngt = 10)

#User location.
        country = input("Ingrese su país de residencia: ").strip().capitalize()
        department = input("Ingrese su departamento de residencia: ").strip().capitalize()
        city = input("Ingrese su ciudad de residencia: ").strip().capitalize()
        address = input("Ingrese su dirección actual: ").strip().title()
        
#Random account number
        existing_numbers = [user.get("checking_account") for user in info["clients"].values()]
        checking_account = random.randint(10000, 99999)
        while checking_account in existing_numbers:
            checking_account = random.randint(10000, 99999)

#After data collection
        info["clients"][str(cc)] = {
            "name": name,
            "age": age,
            "gender": gender,
            "email": email,
            "contact_info": {
                "mobile": mobile,
                "landline": landline  #It'll be "Null" if no data is provided
            },
            "location": {
                "country": country,
                "department": department,
                "city": city,
                "address": address
            },
            "debit_accounts": {
                "savings_account": None,
                "checking_account": checking_account,
            },
#The account starts with zero loans, but the option remains there if the client wants to apply for one in the future.
            "loans": {
                "credit_card": None,
                "any_ploan": None,
                "mortgage": None,
                "vehicle_loan": None
            }
}
        
#Save everything in the Json file
        with open("data/clients.json", "w") as am:
            json.dump(info, am, indent=4)

        print(f"Su cuenta fue creada éxitosamente, con el número: {checking_account}. {greetings(gender)}, {name}.")
    input("Presione Enter para continuar...")