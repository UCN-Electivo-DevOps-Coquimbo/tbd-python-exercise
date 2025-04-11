# Trunk-Based Development

Este es un ejercicio para el electivo "Introducción a DevOps", donde deberán aplicar Trunk-Based Development para integrar código.

# Actividad

Los estudiantes deberán agruparse de a dos o tres integrantes. Luego, deberán crear una o más de las siguientes funcionalidades a la aplicación.

- [ ] Calcular el promedio de un listado de valores.
- [X] Encontrar el valor máximo dentro de un listado de valores.
- [X] Calcular el área de un círculo dado el radio correspondiente.
- [X] Obtener el factorial de un número según un input dado.
- [ ] Comprobar si el número entregado por input es primo.
- [ ] Comprobar si una cadena de caracteres es un palíndromo.
- [X] Ordenar un listado de valores.
- [ ] Obtener la frecuencia de los valores de una lista entregada.
- [X] Obtener todos las palabras de un texto y colocarlas en una lista.

Cada una de estas funcionalidades debe imprimir su resultado por consola en inglés.

# Instrucciones

1. Se debe generar un archivo con su funcionalidad en la carpeta `functionalities`. Debe llevar por nombre `<nombreFuncion>.py`.
2. En el archivo `__init__.py` de la funcionalidad, deberá agregar el nombre del archivo en la lista de la variable `__all__` entre comillas dobles.
3. Se debe generar una función execute en dicho archivo donde desarrollará el problema asignado.
4. Se debe usar la función execute en el código principal (`main.py`).
5. Probar la aplicación y verificar que todo este funcionando correctamente.

# Estándares

- Todos los commits deben estar en inglés.
- Los commits deben realizarse usando conventional commits (feat:, bug:, etc.).
- Los PR's deben llevar una descripción de lo que se fusionará.
- Los PR's no deben tener más de 3 archivos
- Los PR's deben ser aprobados por al menos 1 persona de su equipo y una persona de otro equipo

# Ejecución

Para iniciar la aplicación, debe ejecutar lo siguiente en la linea de comandos:

```bash
$ python3 src/main.py
```
