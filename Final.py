print("BIENVENIDO A ***SolidMix***")
print(f"----------------------------------")
print("Por favor ingrese sus datos:")
nombre = input("Nombre y Apellido: ")
dni = input("DNI: ")
direccion = input("Dirección: ")
print(f"----------------------------------")
with open('agenda.txt', 'a') as file:
    file.write(f"----------------------------------\n")
    file.write(f"SolidMix - DATOS DEL USUARIO\n")
    file.write("Nombre y apellido: " + nombre + "\n")
    file.write("DNI: " + dni + "\n")
    file.write("dirección: " + direccion + "\n")
    file.write(f"----------------------------------\n")

while True:
    print("Ingrese la unidad de medida que desea utilizar\n1- En caso de metros\n2- En caso de centímetros\n3- En caso de pies")

    unidad_a_utilizar = 0

    while unidad_a_utilizar not in [1, 2, 3]:
        try:
            unidad_a_utilizar = int(input("Ingrese el número correspondiente: "))
            if unidad_a_utilizar not in [1, 2, 3]:
                print("Error: Ingrese un número válido (1, 2 o 3).")
        except ValueError:
            print("Error: Ingrese un número válido (1, 2 o 3).")

    while True:
        ancho = float(input("Ingrese el ancho: "))
        if ancho > 0:
            break
        else:
            print("El ancho debe ser un número positivo mayor que cero. Por favor, inténtelo de nuevo.")

    while True:
        largo = float(input("Ingrese el largo: "))
        if largo > 0:
            break
        else:
            print("El largo debe ser un número positivo mayor que cero. Por favor, inténtelo de nuevo.")

    while True:
        espesor = float(input("Ingrese el espesor: "))
        if espesor > 0:
            break
        else:
            print("El espesor debe ser un número positivo mayor que cero. Por favor, inténtelo de nuevo.")

    volumen = 0

    if unidad_a_utilizar == 1:
        volumen = largo * ancho * espesor
    elif unidad_a_utilizar == 2:
        volumen = (largo / 100) * (ancho / 100) * (espesor / 100)
    elif unidad_a_utilizar == 3:
        volumen = (largo / 3.28084) * (ancho / 3.28084) * (espesor / 3.28084)

    tipo_Deconcreto = ["1:2:2","1:2:3","1:2:4","1:3:4","1:3:6"]
    while True:
        tipo_concreto = input(f"{tipo_Deconcreto}\nCual el tipo de concreto que desea: ")

        if tipo_concreto in tipo_Deconcreto:
            break
        else:
            print("Opción no válida. Por favor, elija una opción de la lista.")

    cemento = 0
    grava = 0
    arena = 0
    agua = 0
    if tipo_concreto == "1:2:2":
        print("*********CALCULOS REALIZADOS*********")
        print (f"Necesitará la siguiente cantidad de materiales")
        cemento = (volumen * 8.4) * 1.05
        arena = volumen * 0.67
        grava = volumen * 0.67
        agua = volumen * 220
        print(f" {round(cemento, 2)} bolsas de 50 kg,\n {round(arena, 2)} kg de arena,\n {round(grava, 2)} kg de grava,\n {round(agua, 1)} litros de agua.")
    elif tipo_concreto == "1:2:3":
        print("*********CALCULOS REALIZADOS*********")
        print (f"Necesitará la siguiente cantidad de materiales")
        cemento = (volumen * 7) * 1.05
        arena = volumen * 0.56
        grava = volumen * 0.84
        agua = volumen * 180
        print(f" {round(cemento, 2)} bolsas de 50 kg,\n {round(arena, 2)} kg de arena,\n {round(grava, 2)} kg de grava,\n {round(agua, 1)} litros de agua.")
    elif tipo_concreto == "1:2:4":
        print("*********CALCULOS REALIZADOS*********")
        print(f"Necesitará la siguiente cantidad de materiales")
        cemento = (volumen * 6) * 1.05
        arena = volumen * 0.48
        grava = volumen * 0.96
        agua = volumen * 170
        print(f" {round(cemento, 2)} bolsas de 50 kg,\n {round(arena, 2)} kg de arena,\n {round(grava, 2)} kg de grava,\n {round(agua, 1)} litros de agua.")
    elif tipo_concreto == "1:3:4":
        print("*********CALCULOS REALIZADOS*********")
        print(f"Necesitará la siguiente cantidad de materiales")
        cemento = (volumen * 5.2) * 1.05
        arena = volumen * 0.63
        grava = volumen * 0.84
        agua = volumen * 170
        print(f" {round(cemento, 2)} bolsas de 50 kg,\n {round(arena, 2)} kg de arena,\n {round(grava, 2)} kg de grava,\n {round(agua, 1)} litros de agua.")
    elif tipo_concreto == "1:3:6":
        print("*********CALCULOS REALIZADOS*********")
        print(f"Necesitará la siguiente cantidad de materiales")
        cemento = (volumen * 4.2) * 1.05
        arena = volumen * 0.5
        grava = volumen * 1
        agua = volumen * 160
        print(f" {round(cemento, 2)} bolsas de 50 kg,\n {round(arena, 2)} kg de arena,\n {round(grava, 2)} kg de grava,\n {round(agua, 1)} litros de agua.")

    with open('ticket.txt', 'w') as file:
        file.write(f"***TICKET DE TRABAJO***\n")
        file.write(f"Cantidad de hormigón(volumen): {volumen} m^3\n")
        file.write(f"Tipo de Concreto: {tipo_concreto}\n")
        file.write(f"Cantidad de Materiales:\n")
        file.write(f"Cemento: {round(cemento, 2)} bolsas de 50 kg\n")
        file.write(f"Arena: {round(arena, 2)} kg\n")
        file.write(f"Grava: {round(grava, 2)} kg\n")
        file.write(f"Agua: {round(agua, 1)} litros\n")
        file.write(f"----------------------------------")

    with open("venta.txt", "w") as file:
        file.write(f"----------------------------------\n")
        file.write(f"***********SolidMix***********\n")
        file.write(f"DATOS DEL USUARIO\n")
        file.write("Nombre y apellido: "+ nombre + "\n")
        file.write("DNI: "+ dni+ "\n")
        file.write("dirección: "+ direccion + "\n")
        file.write(f"----------------------------------\n")
        file.write(f"Cantidad de hormigón(volumen): {volumen} m^3\n")
        file.write(f"Tipo de Concreto: {tipo_concreto}\n")
        file.write(f"Cantidad de Materiales:\n")
        file.write(f"Cemento: {round(cemento, 2)} bolsas de 50 kg\n")
        file.write(f"Arena: {round(arena, 2)} kg\n")
        file.write(f"Grava: {round(grava, 2)} kg\n")
        file.write(f"Agua: {round(agua, 1)} litros\n")
        file.write(f"----------------------------------")



    respuesta = input("¿Desea calcular otro volumen? (si/no): ")
    if respuesta.lower() != "si":
        print("Gracias por elegir SolidMix")
        break