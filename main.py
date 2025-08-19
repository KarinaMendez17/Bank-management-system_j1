#Libraries
import os
import time
import modules.debitAccount as da
import modules.accountInfo as ai
import modules.creditAccount as ca
import modules.deposits as dp
import modules.withdrawal as wd
import modules.payments as pm
import modules.deleteAccount as dt
def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            print("===SISTEMA DE GESTIÓN BANCARIO=== \n1. Crear cuenta. \n2. Información de la cuenta. \n3. Depósitos. \n4. Solicitar Crédito. \n5. Retirar efectivo. \n6. Pago cuota de crédito. \n7. Cancelar cuenta. \n8. Salir.")
            option = int(input("Selecciona una opción: "))

            match option:
                case 1:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    da.create_debitAcc()
                case 2:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    ai.account_info()
                case 3:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    dp.deposit()
                case 4:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    ca.create_creditAcc()
                case 5:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    wd.withdrawal()
                case 6:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    pm.payments()
                case 7:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    dt.terminate_account()
                case 8:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Hasta pronto...")
                    break
                case _:
                    print("Por favor, ingrese una opción válida...")
                    time.sleep(2)
                    continue
        except (ValueError, KeyboardInterrupt):
            print("Ingrese un número válido...")
            time.sleep(1)
        
if __name__=="__main__":
    main()
