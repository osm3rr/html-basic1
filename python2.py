# Condicionales anidados
# Validar el ingreso a una discoteca
# La disco está abierta, viernes y sábado, a partir de las 20H,y 
# solo pueden pasar los mayores de 18 años
name = input("Ingrese su nombre: ")
print(f"Hola {name}")

week_day = input(" Ingrese el día de la semana: ")

if week_day == "viernes":
    # validación de la hora
    hour = input("Ingese la hora: ")
    hour = int(hour)
    if hour >= 20:
        # validación de la edad
        age = int(input("Ingrese su edad: "))
        if age >= 18:
            print("Es viernes, son más de las 08:00 PM y eres mayor de edad")
        else:
            print("fuera de aquí menor!")
    else:
        print("CERRADO! Abre a partir de las 08:00 PM")
else:
    print("CERRADO! Abre viernes y sábado")
