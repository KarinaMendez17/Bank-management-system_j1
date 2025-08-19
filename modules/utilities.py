#Number verification.
def numb_criteria(txt, min=None, max=None, lngt=None):
    while True:
        try:
            valor = int(input(txt))

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
        except (ValueError, KeyboardInterrupt):
            print("Ingrese un número válido...")

#Email verification.
def email_criteria(txt):
    while True:
        try:
            email = input(txt).strip()
            if "@" not in email:
                print("Email inválido: falta '@'")
                continue
            if not any(email.endswith(dom) for dom in [".com", ".es", ".co", ".net"]):
                print("Email inválido: debe terminar en un dominio válido (.com, .es, .co, .net)")
                continue
            return email
        except (ValueError, KeyboardInterrupt):
            print("Ingrese un email válido...")

#Personalized greetings.
def greetings(gender):

    if gender == "M":
        p_greet = "¡Bienvenido"
    elif gender == "F":
        p_greet = "¡Bienvenida"
    else:
        p_greet = "¡Bienvenidx"
    return p_greet