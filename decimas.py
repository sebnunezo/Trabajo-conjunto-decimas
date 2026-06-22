import os
import time

reservas =[]

def limpiar_pantalla(): 
    os.system('cls')

def calcular_categoria(total):
    if total < 200000:
        return "Economica"
    elif total <= 500000:
        return "Estandar"
    else:
        return "Premium"
    
def validar_codigo(codigo):
    return codigo.isdigit() and int(codigo) > 0 

def validar_nombre(nombre):
    return len(nombre.strip()) >=3 and nombre.replace("", "").isalpha()

def validar_noches(noches):
    return noches.isdigit () and int (noches) > 0

def validar_valor(valor):
    return valor.isdigit() and int (valor) > 0

def validar_total(total):
    return total > 0

def validar_categoria(categoria):
    return categoria in ["Economica","Estandar","Premium"]

def buscar_reserva(lista, codigo):
    for r in reservas:
        if r["codigo"] == codigo:
            return r
    return None

def registrar_reserva(lista):
    try:
        codigo = input("Codigo: ")
        if not validar_codigo(codigo) or buscar_reserva(codigo):
            print("Codigo invalido o ya existe")
            return
        
        nombre = input    ("Nombre : ").strip()
        noches = int(input("Noches: "))
        valor = int (input("Valor por noche: "))

        total = noches * valor 
        categoria = calcular_categoria(total)

        reserva = {"codigo": codigo, "nombre": nombre, "noches": noches,
                   "valor": valor, "total": total, "categoria": categoria}
        reservas.append(reserva)
        print(f"Listo! Total: ${total}, Categoria: {categoria}")
    except ValueError:
        print("ERROR: ingrese solo numeros donde corresponde ")

#PARTE SEBA
def salir_sistema():
    print("Gracias por usar el sistema, Saliendo....")
    return True

def menu():
    while True:
        limpiar_pantalla()
        print("1. Registrar reserva")
        print("2. Buscar reserva")
        print("3. Actualizar reserva")
        print("4. Eliminar reserva")
        print("5. Mostrar reservas")
        print("6. Mostrar estadísticas")
        print("7. Salir")

        opcion = input("Ingrese una Opcion: ")

        if opcion == "1":
            registrar_reserva(reservas)
        elif opcion == "2":
            buscar_reserva_menu(reservas)
        elif opcion == "3":
            actualizar_reserva(reservas)
        elif opcion == "4":
            eliminar_reserva(reservas)
        elif opcion == "5":
            mostrar_reservas(reservas)
        elif opcion == "6":
            mostrar_estadisticas(reservas)
        elif opcion == "7":
            if salir_sistema():
                break
        else: 
            print("Invalido")
menu()
