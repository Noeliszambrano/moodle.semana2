#Función para validar una calificación individual e imprimir si aprobó o no
def Resultado_de_Calificacion():
    while True:
        try:
            calificacion_Estudiante = int(input("\nIngresa una calificación numérica (0 a 100): "))
#Validación de rango
            if 100 >= calificacion_Estudiante > 49:
                print("\nEl estudiante aprobó.")
            elif calificacion_Estudiante < 0:
                print("\nLa calificación no puede ser menor a 0. Intente nuevamente.")
                continue
            elif calificacion_Estudiante > 100:
                print("\nLa calificación no puede ser mayor a 100. Intente nuevamente.")
                continue
            else:
                print("\nEl estudiante reprobó.")
            break  # Salimos del ciclo si la calificación es válida
        except ValueError:
            print("\nLa calificación debe ser un número entero. Intente nuevamente.")
#Función para calcular el promedio de las calificaciones
def Calcular_Promedio(lista_de_Calificaciones):
    promedio = sum(lista_de_Calificaciones) / len(lista_de_Calificaciones)
    print(f"\nEl promedio de las calificaciones es de: {promedio:.2f}")
#Función que cuenta cuántas calificaciones son mayores a un valor dado
def Contar_Calificaciones_Mayores(lista_de_Calificaciones):
    try:
        valor = int(input("\nIngresa un valor para comparar las notas que sean mayores a ese valor: "))
        cantidad = sum(1 for nota in lista_de_Calificaciones if nota > valor)
        print(f"\nCantidad de calificaciones mayores al valor dado: {cantidad}")
    except ValueError:
        print("\nDebes ingresar un número entero.")
#Función que verifica cuántas veces se repite una calificación específica
def Verificar_Contar_CalificacionesEspecificas(listaCalificaciones):
    try:
        Validar_Calificacion = int(input("\nIngrese la calificación a validar: "))
        conteo = listaCalificaciones.count(Validar_Calificacion)

        if conteo > 0:
            print(f"\nLa calificación {Validar_Calificacion} aparece {conteo} veces en las notas.")
        else:
            print(f"\nLa calificación {Validar_Calificacion} no aparece en las notas.")
    except ValueError:
        print("\nDebes ingresar un número entero.")
#Menú principal para interactuar con el usuario
def Mostrar_Menu(listaCalificaciones):
 while True:
        print("\n--- Menú de opciones ---")
        print("1. Calcular el promedio de las calificaciones")
        print("2. Contar las calificaciones mayores a un valor")
        print("3. Verificar y contar cuántas veces se repite una calificación")
        print("4. Salir")

        opcion = input("Selecciona una opción (1, 2, 3 o 4): ").strip()

        # Opciones del menú
        if opcion == '1':
            if listaCalificaciones:
                Calcular_Promedio(listaCalificaciones)
            else:
                print("\nNo hay calificaciones para calcular el promedio.")
        elif opcion == '2':
            if listaCalificaciones:
                Contar_Calificaciones_Mayores(listaCalificaciones)
            else:
                print("\nNo hay calificaciones para comparar.")
        elif opcion == '3':
            if listaCalificaciones:
                Verificar_Contar_CalificacionesEspecificas(listaCalificaciones)
            else:
                print("\nNo hay calificaciones para verificar.")
        elif opcion == '4':
            print("\n¡Hasta luego!")
            break
        else:
            print("\nOpción no válida, por favor selecciona una opción correcta.")
#
def main():
    print("\n--- Bienvenido al sistema de calificaciones ---")

    while True:
        opcionInicial = input("\n¿Qué deseas hacer?\n1. Ingresar una sola calificación\n2. Ingresar una lista de calificaciones\nSelecciona 1 o 2: ").strip()

        if opcionInicial == '1':
            Resultado_de_Calificacion()
            break
        elif opcionInicial == '2':
            calificaciones = input("Ingresa las calificaciones separadas por comas: ")
            try:
                # Se convierten las entradas en enteros y se valida que no estén vacías
                listaCalificaciones = [int(n.strip()) for n in calificaciones.split(',') if n.strip() != '']
                if Mostrar_Menu(listaCalificaciones) :
                    print("calificaciones agregadas. ")                 
                else:                              
                    print("\nNo se ingresaron calificaciones válidas.")
                break
            except ValueError:
                print("\nPor favor asegúrate de ingresar solo números enteros separados por comas.")
        else:
            print("\nOpción no válida. Intenta nuevamente.")
#Llamamos a la función principal (jajaja, esta vez no se me olvido.)
main()