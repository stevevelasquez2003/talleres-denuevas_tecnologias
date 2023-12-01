"""
Crea Función Calcular Max y Min: recibe una lista de enteros y
devuelve el máximo y el mínimo de los números guardados en la
lista.

"""
# maxymin=[700,1,24,5,6,7,46,80]


# def calcular_max(maxymin):
#  max = maxymin[0]
#  for i in maxymin:
#    if i > max :
#      max = i
#  return max
  

# def calcular_min(maxymin):
#  min = maxymin[0]
#  for i in maxymin:
#    if i < min :
#      min = i
#  return min
   
# print(calcular_max(maxymin))
# print(calcular_min(maxymin))
"""

Usa la función MaxMin que recibe una lista con valores
numéricos y devuelve el valor máximo y el mínimo creada
anteriormente y crea un programa que pida números por teclado
y muestre el máximo y el mínimo, utilizando la función anterior.
"""
# cantidad_de_numeros =int(input("cuantos numeros desea en la lista"))
# lista_numeros=[]
# for i in range(cantidad_de_numeros):
#   ingresa = int(input(f"favor ingrese un numero{i+1}"))
#   lista_numeros.append(ingresa)

# print(f"el numeromaximo es: {calcular_max(lista_numeros)}  y el numero minimo es: {calcular_min(lista_numeros)}")

"""
TERCER PUNTO
Solicitar al usuario que ingrese su dirección email. Imprimir un
mensaje indicando si la dirección es válida o no, valiéndose de
una función para decidirlo. Una dirección se considerará válida si
contiene el símbolo "@".


def ingresar_correo_electronico(email):
  return '@' in email
correo_electronico = input("favor ingresa tu dirección de correo electrónico ")
if ingresar_correo_electronico(correo_electronico):
    print("el correo electronico que ha ingresado es correcto")
else:
    print("El correo ingresado no es correcto Favor agregale  el '@'")

  """
"""" 
PUNTO5
def calcular_cubos(muestra):
    
    cubos = [numero ** 3 for numero in muestra]
    return cubos


numeros = [1, 2, 3, 4, 5]
cubos_resultantes = calcular_cubos(numeros)

print("Muestra original:", numeros)
print("Cubos resultantes:", cubos_resultantes)
"""
"""
PUNTO4
def es_primo(numero):
  

    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True


numero_ingresado = input("Ingrese un número entero para verificar si es primo: ")


if numero_ingresado.isdigit():
    numero_ingresado = int(numero_ingresado)
    if es_primo(numero_ingresado):
        print(f"{numero_ingresado} es un número primo.")
    else:
        print(f"{numero_ingresado} no es un número primo.")
else:
    print("Por favor, ingrese un número entero válido.")

"""
