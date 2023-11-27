# Patrones Estructurales

Mi dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/lauralardies/patrones_estructurales)
https://github.com/lauralardies/patrones_estructurales


## Enunciados

En este repositorio trabajamos sobre dos ejercicios diferentes:

### Ejercicio 1

Tras el éxito inicial de su plataforma digital de creación y gestión de pizzas gourmet personalizadas, la cadena "Delizioso" desea llevar su propuesta al siguiente nivel. Ahora, aparte de permitir la personalización individual de pizzas, quiere ofrecer a sus clientes la posibilidad de combinar sus creaciones en menús personalizados, que podrían incluir entradas, bebidas, pizzas y postres. Estos menús pueden ser creados tanto por el cliente como por el equipo culinario de "Delizioso", con opciones preestablecidas que representan la esencia de la marca.

**Objetivos:**
1. Desarrollo de Menús Personalizados:
   - Introducir la noción de un "menú", que puede contener varios elementos: entradas, bebidas, pizzas (que ya han sido definidas previamente con su sistema de creación de pizzas) y postres.
   - Un "menú" puede ser simple (contener elementos básicos) o compuesto (incluir otros menús más pequeños, como un "Combo Pareja" que incluye dos menús individuales).
   - Cada "menú" tendrá un código único y un precio, que se determina como la suma de los precios de sus elementos, con un descuento según la promoción aplicada.
2. Patrones de Diseño:
   - Implementar el patrón Composite para modelar la relación entre los elementos y menús, facilitando la creación, modificación y cálculo de precios de menús compuestos.
   - Continuar utilizando el patrón Builder para la creación detallada de las pizzas.
3. Interacción con CSV:
   - Ampliar el sistema de almacenamiento en CSV para incluir los menús personalizados, de forma que se pueda registrar y recuperar la información de menús individuales y compuestos.
   - Permitir que, a partir de un menú almacenado, se pueda reconstruir toda la estructura del menú con sus elementos individuales y precios.
4. Restricciones:
   - Las librerías estándar de Python para la interacción con archivos CSV están permitidas.
   - Se espera un diseño modular y orientado a objetos, con una clara separación de responsabilidades.
   - La implementación del cálculo del precio de un "menú" debe hacerse en tiempo de ejecución y ser eficiente.

**Entrega:**
- Un diagrama UML detallando las clases, relaciones y métodos.
- Código Python correspondiente a la implementación.
- Un breve informe que justifique las decisiones de diseño tomadas y explique cómo se han aplicado los patrones de diseño.
- Un conjunto de pruebas unitarias que demuestren la correcta funcionalidad del sistema.
 
### Ejercicio 2

## Archivos

## Código

### Ejercicio 1

#### 
