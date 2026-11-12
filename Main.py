# Namor Jesús - Alés Armando
# Tema 3 — Gestión de socios de un gimnasio

import os

# funciones de carga y modificacion de archivos
# cambiar segun quien lo tenga
# probar
# aca levantamos el archivo obteniendo la ruta, importante clonar el repo para probar


def cargarRutaArchivo(archivo: str = 'socios.txt'):
    
    carpeta = os.path.dirname(os.path.abspath(__file__))
    ruta = os.path.join(carpeta, archivo)
    
    return ruta


def devolverDiccionarioSocios(archivo: str = 'socios.txt'):
    """
    carga los socios y usa el DNI como clave
    pasa las lineas incorrectas y nos devuelve cuantas encontro
    """

    ruta = cargarRutaArchivo(archivo)

    socios = {}
    errores = 0

    try:
        with open(file=ruta, mode='r', encoding='utf-8') as f:

            for linea in f:

                try:
                    datos = linea.strip().split(';')

                    if len(datos) != 5:
                        raise ValueError

                    dni = datos[0].strip()
                    nombre = datos[1].strip()
                    plan = datos[2].strip().lower().replace('ó', 'o')
                    ultimo_mes_pago = int(datos[3])
                    asistencias = int(datos[4])

                    if (not dni or not nombre or dni in socios or
                        plan not in ['musculacion', 'funcional', 'pileta'] or
                        ultimo_mes_pago < 1 or ultimo_mes_pago > 12 or
                        asistencias < 0):
                        raise ValueError

                    socios[dni] = {
                        'nombre': nombre,
                        'plan': plan,
                        'ultimo_mes_pago': ultimo_mes_pago,
                        'asistencias': asistencias
                    }

                except ValueError:
                    errores += 1

        print('lineas con errores:', errores)

    except FileNotFoundError:
        print('no existe el archivo')

    return socios


# def devolverListaSocios(archivo: str = 'socios.txt'):
#     ruta = cargarRutaArchivo(archivo)
    
#     listasocios = []
    
    
#     with open(file = ruta, mode = 'r', encoding= 'utf-8') as f:
#         lineas = f.readlines()
        
#         for linea in lineas:
            
#             datos = linea.strip().split(';')
            
#             try:

#                 socio = {"dni": datos[0],
#                         "nombre": datos[1],
#                         "entrenamiento": (datos[2]),
#                         "ultimaC": int(datos[3]),
#                         'asistencia': int(datos[4])}
                
                
#                 listasocios.append(socio)            

            
#             except Exception as e:
#                 print("error en el dni: ", e)
#                 continue
    
#     f.close()
#     return listasocios                


def printearSocios(dni: str, socio: dict):
    """
    printea los datos del socio
    """

    print("--------------------")
    print("dni:", dni)
    print("nombre:", socio["nombre"])
    print("plan:", socio["plan"])
    print("ultimo mes pago:", socio["ultimo_mes_pago"])
    print("asistencias:", socio["asistencias"])
    print("--------------------")


def verSocios(socios: dict):
    """
    muestra los socios registrados
    """

    for dni, socio in socios.items():
        printearSocios(dni, socio)



# def verSocios(archivo: str = 'socios.txt'):

#     listaSocios = devolverListaSocios(archivo)

#     for socio in listaSocios:
#         printearSocios(socio)


def verMorosos(mes: int, socios: dict):
    """
    muestra socios que no pagaron atnes de mes ingresado
    """

    if mes < 1 or mes > 12:
        print('!!!ERROR, el mes debe estar entre 1 y 12')
        return

    encontro = False

    for dni, socio in socios.items():

        if socio['ultimo_mes_pago'] < mes:

            printearSocios(dni, socio)
            encontro = True

    if not encontro:
        print('no hay socios morosos')


# def verMorosos(mes: int, archivo: str = 'socios.txt', ):
    
#     if mes < 1:
#         print("error, no pueden haber meses negativos ni menores a uno")
    
#     else:

#         listaSocios = devolverListaSocios(archivo)
        
#         for socio in listaSocios:
#             if socio['ultimaC'] != mes:
#                 printearSocios(socio)


def diccionariosEntrenamientosYCantidad(socios: dict):
    """
    cuenta los socios y suma las asistencias de cada plan
    """

    entrenamientos = {}
    asistencias = {}

    for socio in socios.values():

        plan = socio['plan']

        if plan not in entrenamientos:
            entrenamientos[plan] = 0
            asistencias[plan] = 0

        entrenamientos[plan] += 1
        asistencias[plan] += socio['asistencias']

    return entrenamientos, asistencias


# def diccionariosEntrenamientosYCantidad(archivo: str = 'socios.txt'):
#         listaSocios = devolverListaSocios(archivo= archivo)
#         entrenamientos = {}
    
#         for socio in listaSocios:
        
#             if socio['entrenamiento'] not in entrenamientos:
#                 entrenamientos[str(socio['entrenamiento'])] = 1
#             else:
#                 entrenamientos[str(socio['entrenamiento'])] += 1
        
#         return entrenamientos, listaSocios


def verCantSocios(socios: dict):
    """
    muestra la cantidad de socios por plan
    """

    entrenamientos, asistencias = diccionariosEntrenamientosYCantidad(socios)

    print("planes y su cantidad de socios")

    for entrenamiento, cantidad in entrenamientos.items():
        print(f'{entrenamiento}: {cantidad} personas')

    print("total: ", len(socios))

# def verCantSocios(archivo: str = 'socios.txt'):
    
#     entrenamientos, listaSocios = diccionariosEntrenamientosYCantidad(archivo= archivo)
    
#     print("entrenamientos y su cantidad")
#     for entrenamiento, cantidad in entrenamientos.items():
#         print(f'{entrenamiento}: {cantidad} de personas')
        
#     print("total: ", len(listaSocios))
    

def promedioAsistencia(socios: dict):
    """
    calcula promedio de asistencias por plan.
    """

    entrenamientos, asistencias = diccionariosEntrenamientosYCantidad(socios)

    print("promedio de asistencias por plan")

    for entrenamiento, cantidad in entrenamientos.items():

        promedio = asistencias[entrenamiento] / cantidad

        print(f'{entrenamiento}: {promedio:.2f} asistencias por socio')


# def promedioAsistencia(archivo: str = 'socios.txt'):

#     entrenamientos, listaSocios = diccionariosEntrenamientosYCantidad(archivo= archivo)
            
#     totalParticipantes = len(listaSocios)
    
#     print("entrenamientos y procedimientos")
    
#     for entrenamiento, cantidad in entrenamientos.items():
#         print(f'{entrenamiento}: {(cantidad * 100) / totalParticipantes}%')            


def aniadirCliente(socios: dict, archivo: str = 'socios.txt'):
    """
    añade un nuevo socio al diccionario y guarda los cambios
    """

    nombre = input('dame el nombre: ')
    dni = input('dame el dni: ')

    if not dni or dni in socios:
        print('DNI vacio o ya existe')
        return

    plan = input('dame el plan: ').lower().replace('ó', 'o')

    if plan not in ['musculacion', 'funcional', 'pileta']:
        print('plan no valido')
        return

    try:
        mes = int(input('que mes pago? numero solo: '))

        if mes < 1 or mes > 12:
            print('mes no valido')
            return

    except ValueError:
        print('debe ingresar un numero')
        return

    if not nombre.strip():
        print('nombre no valido')
        return

    socios[dni] = {
        'nombre': nombre.strip(),
        'plan': plan,
        'ultimo_mes_pago': mes,
        'asistencias': 0
    }

    guardarSocios(socios, archivo)

    print('cliente añadid')


# def aniadirCliente(archivo: str = 'socios.txt'):

#     try:
#         nombre = str(input('dame el nombre: '))
#         dni = str(input("dame el dni: "))
#         entrenamiento= str(input("dame el entrenamiento que realizara: "))
#         mes = int(input('que mes pago? numero solo: '))

        
#         ruta = cargarRutaArchivo(archivo= archivo)
        
#         with open(file= ruta, mode= "a", encoding= 'utf-8') as f:
#             f.write(
#                 f'{dni};{nombre};{entrenamiento};{mes};0\n'
#             )
#             f.close()

#         print('cliente añadido!!!!!')
    
#     except Exception:
#         print("no se puede aniadir ningun cliente, problema fatal")


def buscarCliente(socios: dict, dni: str):
    """
    busca un socio mediante su DNI
    """

    try:
        socio = socios[dni]

        printearSocios(dni, socio)

        return True

    except KeyError:
        print('no se encontro ningun socio con ese DNI')
        return False


def modificarCliente(socios: dict, archivo: str = 'socios.txt'):
    """
    modifica el nombre o el plan de un socio
    """

    dni = input('ingrese el DNI del socio: ')

    if buscarCliente(socios, dni):

        nombre = input('nuevo nombre (Enter para mantener): ')
        plan = input('nuevo plan (Enter para mantener): ')

        if plan:
            plan = plan.lower().replace('ó', 'o')

            if plan not in ['musculacion', 'funcional', 'pileta']:
                print('plan no valido')
                return

        if not nombre and not plan:
            print('no se realizaron modificaciones')
            return

        try:
            if nombre.strip():
                socios[dni]['nombre'] = nombre.strip()

            if plan:
                socios[dni]['plan'] = plan

            guardarSocios(socios, archivo)

            print('datos modificados!!')

        except KeyError:
            print('no se encontro el socio')


def eliminarCliente(socios: dict, archivo: str = 'socios.txt'):
    """
    elimina un socio mediante su DNI y guarda los cambios.
    """

    dni = input('ingrese el DNI del socio que desea eliminar: ')

    if buscarCliente(socios, dni):

        try:
            del socios[dni]

            guardarSocios(socios, archivo)

            print('socio eliminado correctamente')

        except KeyError:
            print('no se encontro el socio')


def registrarPago(socios: dict, archivo: str = 'socios.txt'):
    """
    registra el pago de un mes para un socio
    """

    dni = input('ingrese el DNI del socio: ')

    if buscarCliente(socios, dni):

        try:
            mes = int(input('ingrese el mes que pago: '))

            if mes < 1 or mes > 12:
                print('mes no valido')
                return

            socios[dni]['ultimo_mes_pago'] = mes

            guardarSocios(socios, archivo)

            print('pago registrado correctamente')

        except ValueError:
            print('debe ingresar un numero')

        except KeyError:
            print('no se encontro el socio')


def registrarAsistencia(socios: dict, archivo: str = 'socios.txt'):
    """
    registra una nueva asistencia de un socio
    """

    dni = input('ingrese el DNI del socio: ')

    if buscarCliente(socios, dni):

        try:
            socios[dni]['asistencias'] += 1

            guardarSocios(socios, archivo)

            print('asistencia registrada')

        except KeyError:
            print('no se encontro el socio')


def reporteMorosos(socios: dict, mes: int):
    """
    genera un archivo txt con los socios morosos y sus meses adeudados
    """

    ruta = cargarRutaArchivo('reporte_morosos.txt')

    if mes < 1 or mes > 12:
        print('mes no valido')
        return

    encontro = False

    with open(file=ruta, mode='w', encoding='utf-8') as f:

        f.write('REPORTE DE SOCIOS MOROSOS\n\n')

        for dni, socio in socios.items():

            if socio['ultimo_mes_pago'] < mes:

                mesesAdeudados = mes - socio['ultimo_mes_pago']

                f.write(
                    f"DNI: {dni}\n"
                    f"Nombre: {socio['nombre']}\n"
                    f"Meses adeudados: {mesesAdeudados}\n"
                    "--------------------\n"
                )

                encontro = True

        if not encontro:
            f.write('no hay socios morosos')

    print('reporte generado correctamente')


def guardarSocios(socios: dict, archivo: str = 'socios.txt'):
    """
    guada todos los socios del diccionario en el txt
    """

    ruta = cargarRutaArchivo(archivo)

    with open(file=ruta, mode='w', encoding='utf-8') as f:

        for dni, socio in socios.items():

            f.write(
                f"{dni};{socio['nombre']};{socio['plan']};"
                f"{socio['ultimo_mes_pago']};"
                f"{socio['asistencias']}\n"
            )

# cosas basicas del main y handlers
def opciones():

    print("1. Ver socios morosos") #hecho
    print("2. Ver cantidad de socios") #hecho
    print("3. Ver promedio de asistencias por plan") #hecho
    print("4. Reporte de morosos y sus deudas") #hecho
    print("5. Añadir cliente") #hecho
    print("6. Modificar datos de un socio") #hecho
    print("7. Eliminar cliente") #hecho
    print("8. Ver todos los socios") #hecho
    print("9. Registrar el pago del mes") #hecho
    print("10. Registrar asistencia") #hecho
    print("11. Buscar socio") #hecho
    print("0. Salir") #hecho


# aca van a ir las llamadas a funcion segun se requiera
def handlerOpciones(opcion: int, socios: dict, archivo: str = 'socios.txt'):
    
    match opcion:

        case 1:
            try:
                mes = int(input("numero del mes: "))
                verMorosos(mes, socios)

            except ValueError:
                print("tenes que ingresar un numero")

        case 2:
            verCantSocios(socios)

        case 3:
            promedioAsistencia(socios)

        case 4:
            try:
                mes = int(input("mes actual: "))
                reporteMorosos(socios, mes)

            except ValueError:
                print("tenes que ingresar un numero")

        case 5:
            aniadirCliente(socios, archivo)

        case 6:
            modificarCliente(socios, archivo)

        case 7:
            eliminarCliente(socios, archivo)

        case 8:
            verSocios(socios)

        case 9:
            registrarPago(socios, archivo)

        case 10:
            registrarAsistencia(socios, archivo)

        case 11:
            dni = input("DNI del socio: ")
            buscarCliente(socios, dni)

        case _:
            print("opcion no valida")

    
# main, dejarlo lo mas bobo que se pueda
def main():
  
    socios = devolverDiccionarioSocios()

    while True:

        opciones()

        try:
            opcion = int(input("Selecciona una opcion: "))

            if opcion == 0:
                print("Adios!!!!")
                break

            handlerOpciones(opcion, socios)

        except ValueError:
            print("Selecciona un numero!!!")


if __name__ == '__main__':
    main()