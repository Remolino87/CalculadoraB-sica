# Función para sumar dos números
def sumar(a, b):
    return a + b

# Función para restar dos números
def restar(a, b):
    return a - b

# Función para multiplicar dos números
def multiplecar(a, b):
    return a * b

# Función para dividir dos números
def dividir(a, b):
    if b == 0:
        return "Error: Division por cero no es permitida."
    return a / b

def calculadora():
    print("Seleccione la operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    while True:
        # Recibir la entrads del usuario
        eleccion = input("Ingrese su elección (1/2/3/4): ")

        if eleccion in ["1", "2", "3", "4"]:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrse el segundo número: "))

            if eleccion == "1":
                print(f"Resultado: {num1} + {num2} = {sumar(num1, num2)}")

            elif eleccion == "2":
                print(f"Resultado: {num1} - {num2} = {restar(num1, num2)}")
            
            elif eleccion == "3":
                print(f"Resultado: {num1} * {num2} =  {multiplecar(num1, num2)}")
            
            elif eleccion == "4":
                print(f"Resultado: {num1} / {num2} =  {dividir(num1, num2)}")
            
            # preguntar si el usuario quiere realizar otra operación
            siguiente_calculo = input("¿Quieres realizar otra operación? (s/n): ")
            if siguiente_calculo.lower() != "s":
                break
        else:
            print("Entrada inválida, por favor ingrese una opción valida.")

if __name__ == "__main__":
    calculadora()