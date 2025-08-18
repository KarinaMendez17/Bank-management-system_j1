#Libraries
import os
import time
import modules.debitAccount as da
import modules.creditAccount as ca
import modules.deposits as dp
import modules.withdrawal as wd
import modules.payments as pm
import modules.deleteAccount as dt
def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            print("""===SISTEMA DE GESTIÓN BANCARIO=== \n1. Crear cuenta. \n2. Depósitos. \n3. Solicitar Crédito. \n4. Retirar efectivo. \n5. Pago cuota de crédito. \n6. Cancelar cuenta. \n7. Salir.""")
            option = int(input("Selecciona una opción: "))

            match option:
                case 1:
                    da.create_debitAcc()
                case 2:
                    dp.deposit()
                case 3:
                    ca.create_creditAcc()
                case 4:
                    wd.withdrawal()
                case 5:
                    pm.payments()
                case 6:
                    dt.terminate_account()
                case 7:
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
