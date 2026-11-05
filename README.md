# gestion-de-socios-GYM
UM pyhon integrador informatica 1

debemos seguir los siguientes lineamientos
# menu:
Bucle while con opciones numeradas y opción Salir; una opción inválida muestra un mensaje y vuelve al menú

# carga desde archivo
Al iniciar, se lee el archivo de datos con with open. Si no existe, el programa arranca vacío y lo informa. Las líneas mal formadas se omiten y se informa cuántas fueron

# Diccionario como estructura principal	Clave única (código, DNI, legajo o nombre) → diccionario con los campos del registro
Clave única (código, DNI, legajo o nombre) → diccionario con los campos del registro

# Altas, bajas, modificaciones y búsqueda
No se permiten claves duplicadas; buscar o borrar una clave inexistente muestra un mensaje y no rompe el programa

# Dos consultas propias del tema

# Reporte exportado

# Guardado
de cambios

# Validación de entradas
try/except con excepciones concretas (ValueError, FileNotFoundError, KeyError); el programa no se interrumpe por un dato mal ingresado

# Funciones

# Datos de prueba	Archivo con al menos 15 registros válidos y 2 líneas mal formadas a propósito
Archivo con al menos 15 registros válidos y 2 líneas mal formadas a propósito

# RESTRICCIONES
* Solo Python estándar y lo visto en la materia. No se permiten pandas, csv, json ni otras librerías, salvo que el par lo justifique en la declaración de IA y pueda explicarlo en la defensa.
*	Nada de variables globales modificadas dentro de funciones: los datos se pasan como parámetros.
* El formato de archivo es texto plano con campos separados por ;, una línea por registro.
* Se puede hacer uso de la IA para encontrar errores u optimizar el código pero debe declararse.

# # # TEMA # # #
Gestión de socios de un gimnasio
Diccionario dni → {"nombre", "plan", "ultimo_mes_pago", "asistencias"}. Los planes son musculación, funcional y pileta.

30111222;Laura Gómez;funcional;10;12
28999000;Martín Ruiz;pileta;8;3
35444555;Sofía Díaz;musculacion;10;20

*	Operaciones extra: registrar una asistencia y registrar el pago de un mes.
*	Consulta 1: socios morosos, es decir, con ultimo_mes_pago anterior al mes que ingresa el usuario.
*	Consulta 2: cantidad de socios y promedio de asistencias por plan, armando un diccionario plan → contador.
*	Reporte: lista de morosos con los meses que adeuda cada uno.

