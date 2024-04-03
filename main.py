def calcular_minimo_comun_divisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Función para verificar si el número ingresado es un entero positivo
def verificar_entero_positivo(num):
    try:
        num = int(num)
        if num <= 0:
            return False
        return True
    except ValueError:
        return False

# Solicitar al usuario que ingrese los dos números
while True:
    num1 = input("Ingrese el primer número entero positivo: ")
    if verificar_entero_positivo(num1):
        break
    else:
        print("Error: Debe ingresar un entero positivo.")

while True:
    num2 = input("Ingrese el segundo número entero positivo: ")
    if verificar_entero_positivo(num2):
        break
    else:
        print("Error: Debe ingresar un entero positivo.")

# Convertir los números ingresados a enteros
num1 = int(num1)
num2 = int(num2)

# Calcular el MCD
mcd = calcular_minimo_comun_divisor(num1, num2)

# Mostrar el resultado
print("El máximo común divisor (MCD) de", num1, "y", num2, "es:", mcd)