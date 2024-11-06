def convertir_tiempo():
    unidad1 = input("Escribe la unidad de tiempo (segundos, minutos o horas): ")
    valor_1 = float(input(f"Escribe el valor en {unidad1}: "))
    unidad2 = input("Escribe la unidad de tiempo a la que quieres convertir (segundos, minutos o horas): ")

    if unidad1 == "segundos":
        if unidad2 == "minutos":
            valor_f = valor_1 / 60
        elif unidad2 == "horas": 
            valor_f = valor_1 / 3600
        else:
            print(f"Unidad inválida {unidad2}")

    elif unidad1 == "minutos":
        if unidad2 == "segundos":
            valor_f = valor_1 * 60
        elif unidad2 == "horas":
            valor_f = valor_1 / 60
        else:
            print(f"Unidad inválida {unidad2}")

    elif unidad1 == "horas":
        if unidad2 == "segundos":
            valor_f = valor_1 * 3600
        elif unidad2 == "minutos":
            valor_f = valor_1 * 60
        else:
            print(f"Unidad inválida {unidad2}")
    else:
        print(f"Unidad inválida {unidad1}")
    print(f"{valor_1} {unidad1} es igual a {valor_f} {unidad2}")
convertir_tiempo()
