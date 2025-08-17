#To validate numbers.
def numb_criteria(mensaje, min=None, max=None, lngt=None):
    while True:
        try:
            valor = int(input(mensaje))

            if min is not None and valor < min:
                print(f"El valor debe ser mayor o igual a {min}.")
                continue
            if max is not None and valor > max:
                print(f"El valor debe ser menor o igual a {max}.")
                continue
            if lngt is not None and len(str(valor)) != lngt:
                print(f"El número debe tener exactamente {lngt} dígitos.")
                continue

            return valor
        except ValueError:
            print("Ingrese un número válido.")
