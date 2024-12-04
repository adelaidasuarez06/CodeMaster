def pedir_nota(materia):
    nota = -1
    while nota < 0 or nota > 5:  # Repetir mientras la nota no sea válida
        nota = float(input(f"Ingresa la nota de {materia}: "))
        if nota < 0 or nota > 5:
            print("Error: La nota debe estar entre 0 y 5. Inténtalo de nuevo.")
    return nota

print("Ingresa las notas de las 3 materias:")
matematicas = pedir_nota("Matemáticas")
ciencia = pedir_nota("Ciencia")
lenguaje = pedir_nota("Lenguaje")

promedio = (matematicas + ciencia + lenguaje) / 3

if promedio >= 4.5:
    mensaje = "Excelente, aprobado con honores."
elif promedio >= 3.0:
    mensaje = "Aprobado."
elif promedio >= 2.0:
    mensaje = "En recuperación, necesitas mejorar."
else:
    mensaje = "Reprobado."

print(f"\nPromedio: {promedio:.2f}")
print(mensaje)
