#Libraries
import os
import time
import modules.debitAccount as cr

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            print("""===SISTEMA DE GESTIÓN BANCARIO=== \n1. Crear cuenta. \n2. Depósitos. \n3. Solicitar Crédito. \n4. Retirar efectivo. \n5. Pago cuota de crédito. \n6. Cancelar cuenta. \n7. Salir.""")
            option = int(input("Selecciona una opción: "))

            match option:
                case 1:
                    cr.create_account()
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
                case 6:
                    pass
                case 7:
                    pass
                case _:
                    print("Por favor, ingrese una opción válida...")
                    time.sleep(2)
                    continue
        except (ValueError, KeyboardInterrupt):
            print("Ingrese un número válido...")
            time.sleep(1)
        
if __name__=="__main__":
    main()
