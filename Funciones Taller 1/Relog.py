def angulos(horas:int, min:int):
    Angulo_horas = horas*30+min*0.5
    Angulo_min = min*6
    Angulo_mas_pequeño = Angulo_horas - Angulo_min
    if Angulo_mas_pequeño > 180:
        return 360-Angulo_mas_pequeño
    return Angulo_mas_pequeño
H = int(input("Ingrese las horas: "))
M = int(input("Ingrese los minutos: "))
print(f"El angulo más pequeño es {angulos(H,M)}°")