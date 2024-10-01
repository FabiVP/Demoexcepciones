# Demo excepciones
## Ejercicio natural
Respecto al código, int(input()) solicita al usuario un número entero, mientras que raise ValueError() lanza un error si el número ingresado no es mayor a cero. 
El bloque try-except-finally gestiona las excepciones: intenta ejecutar el código, captura errores como un valor no válido, y siempre muestra un mensaje en el bloque
finally para indicar que se está validando la entrada. Luego, el bucle for i in range() calcula los divisores del número ingresado y print() se encarga de mostrar tanto 
los resultados como cualquier error capturado. Esto asegura un proceso robusto de validación y cálculo.
