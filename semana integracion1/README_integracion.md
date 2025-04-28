# Conversor de Sistemas Numéricos - trabajoGrupal.py

# Grupo
Nicolas Pagola y Matias Orellana

## Objetivo
El programa `trabajoGrupal.py` es un conversor numérico interactivo que permite transformar números decimales ingresados por el usuario a otros sistemas numéricos: binario, octal o hexadecimal. La ejecución se mantiene en un ciclo hasta que el usuario ingrese el comando "F" para finalizar.

## Validaciones de Entrada

### Selección del Sistema Numérico
1. El programa solicita al usuario que elija el sistema numérico de destino
2. Realiza las siguientes validaciones:
   - Elimina espacios en blanco y convierte la entrada a mayúsculas
   - Verifica que la opción ingresada sea válida (entre las disponibles)
   - Muestra mensajes de error descriptivos para entradas inválidas

### Ingreso del Número Decimal
1. Una vez seleccionado el sistema objetivo, se solicita el número decimal a convertir
2. Validaciones implementadas:
   - Confirma que la entrada sea un número decimal válido
   - Verifica que cumpla con los parámetros establecidos
   - En caso de error, detiene la ejecución e informa al usuario

## Proceso de Conversión
1. Según la opción seleccionada por el usuario, realiza la conversión a:
   - Binario (base 2)
   - Octal (base 8)
   - Hexadecimal (base 16)
   - Opción para mostrar todas las conversiones simultáneamente

2. El resultado se muestra formateado en la terminal con el formato:
########################################
"Sistema numérico": "Valor convertido"
########################################

3. Finalizada la conversión, el programa:
- Muestra el resultado claramente formateado
- Termina la ejecución o reinicia el ciclo según la acción del usuario