def calcular_nota_necesaria_examen(nota_presentacion, peso_presentacion=0.60):
    try:
        nota_presentacion = float(nota_presentacion)
        nota_minima_final = 4.0
        nota_necesaria_examen = (
            nota_minima_final - (nota_presentacion * peso_presentacion)) / (1 - peso_presentacion)
        return max(0, nota_necesaria_examen)
    except ValueError:
        return "Entrada inválida. Por favor, ingrese un número."


def calcular_promedio_final(nota_presentacion, nota_examen, peso_presentacion=0.60):
    try:
        nota_presentacion = float(nota_presentacion)
        nota_examen = float(nota_examen)
        promedio_final = (nota_presentacion * peso_presentacion) + \
            (nota_examen * (1 - peso_presentacion))
        return promedio_final
    except ValueError:
        return "Entrada inválida. Por favor, ingrese un número."


while True:
    print("\nOpciones:")
    print("a) Calcular nota necesaria en el examen.")
    print("b) Calcular promedio final de la asignatura.")
    print("e) Salir.")
    opcion = input("Seleccione una opción: ")

    if opcion == 'e':
        print("Saliendo del programa.")
        break
    elif opcion == 'a':
        nota_presentacion_usuario = input("Ingrese su nota de presentación: ")
        resultado = calcular_nota_necesaria_examen(nota_presentacion_usuario)
        print(f"Nota necesaria en el examen: {
              resultado:.2f}" if isinstance(resultado, float) else resultado)
    elif opcion == 'b':
        nota_presentacion_usuario = input("Ingrese su nota de presentación: ")
        nota_examen_usuario = input("Ingrese su nota del examen: ")
        resultado = calcular_promedio_final(
            nota_presentacion_usuario, nota_examen_usuario)
        print(f"Promedio final de la asignatura: {
              resultado:.2f}" if isinstance(resultado, float) else resultado)
    else:
        print("Opción no válida. Intente nuevamente.")
