# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite ingresar tres valores de temperatura
De las temperaturas ingresadas por consola determinar:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?

En cada caso imprimir en pantalla el resultado

IMPORTANTE: Para ordenar las temperatuas debe utilizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido. Recomendamos pensar bien este problema de lógica con un lápiz y papel.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

temperatura_1 = float(input("ingerese la temperatura"))
temperatura_2 = float(input("ingerese la temperatura"))
temperatura_3 = float(input("ingerese la temperatura"))

#temperatura maxima
if (temperatura_1 > temperatura_2 and temperatura_3 < temperatura_2):
    print (temperatura_1, "tiene la temperatura maxima")
elif (temperatura_2 > temperatura_1 and temperatura_3 < temperatura_1):
    print (temperatura_2, "tiene la temperatura maxima")
else:
    print (temperatura_3, "tiene la temperatura maxima")

#temperatura minima
if (temperatura_1 < temperatura_2 and temperatura_3 > temperatura_2):
    print (temperatura_1, "tiene la temperatura minima")
elif (temperatura_2 < temperatura_1 and temperatura_3 > temperatura_1):
    print (temperatura_2, "tiene la temperatura minima")
else: 
    print (temperatura_3, "tiene la temperatura minima")

#promedio temperaturas
promedio = (temperatura_1 + temperatura_2 + temperatura_3) / 3
print ("el promedio de las temperaturs es:", promedio)

