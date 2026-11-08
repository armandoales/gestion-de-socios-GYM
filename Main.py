import os

# funciones de carga y modificacion de archivos
# cambiar segun quien lo tenga
# probar
# aca levantamos el archivo obteniendo la ruta, importante clonar el repo para probar
def cargarRutaArchivo(archivo: str = 'socios.txt'):
    
    carpeta = os.path.dirname(os.path.abspath(__file__))
    ruta = os.path.join(carpeta, archivo)
    
    return ruta


def devolverListaSocios(archivo: str = 'socios.txt'):
    ruta = cargarRutaArchivo(archivo)
    
    listasocios = []
    
    
    with open(file = ruta, mode = 'r', encoding= 'utf-8') as f:
        lineas = f.readlines()
        
        for linea in lineas:
            
            datos = linea.strip().split(';')
            
            try:

                socio = {"dni": datos[0],
                        "nombre": datos[1],
                        "entrenamiento": (datos[2]),
                        "ultimaC": int(datos[3]),
                        'asistencia': int(datos[4])}
                
                
                listasocios.append(socio)            

            
            except Exception as e:
                print("error en el dni: ", e)
                continue
    
    f.close()
    return listasocios                


def printearSocios(socio: dict):
    print("--------------------")
    print("dni: ", socio["dni"])
    print('nombre:', socio['nombre'])
    print("entrenamiento: ", socio["entrenamiento"])
    print("ultimaC: ", socio["ultimaC"])
    print("asistencia: ", socio["asistencia"])
    print('--------------------')


def verSocios(archivo: str = 'socios.txt'):

    listaSocios = devolverListaSocios(archivo)
    
    for socio in listaSocios:
        printearSocios(socio)


def verMorosos(mes: int, archivo: str = 'socios.txt', ):
    
    if mes < 1:
        print("error, no pueden haber meses negativos ni menores a uno")
    
    else:

        listaSocios = devolverListaSocios(archivo)
        
        for socio in listaSocios:
            if socio['ultimaC'] != mes:
                printearSocios(socio)
                

def diccionariosEntrenamientosYCantidad(archivo: str = 'socios.txt'):
        listaSocios = devolverListaSocios(archivo= archivo)
        entrenamientos = {}
    
        for socio in listaSocios:
        
            if socio['entrenamiento'] not in entrenamientos:
                entrenamientos[str(socio['entrenamiento'])] = 1
            else:
                entrenamientos[str(socio['entrenamiento'])] += 1
        
        return entrenamientos, listaSocios


def verCantSocios(archivo: str = 'socios.txt'):
    
    entrenamientos, listaSocios = diccionariosEntrenamientosYCantidad(archivo= archivo)
    
    print("entrenamientos y su cantidad")
    for entrenamiento, cantidad in entrenamientos.items():
        print(f'{entrenamiento}: {cantidad} de personas')
        
    print("total: ", len(listaSocios))
    
    
def promedioAsistencia(archivo: str = 'socios.txt'):

    entrenamientos, listaSocios = diccionariosEntrenamientosYCantidad(archivo= archivo)
            
    totalParticipantes = len(listaSocios)
    
    print("entrenamientos y procedimientos")
    
    for entrenamiento, cantidad in entrenamientos.items():
        print(f'{entrenamiento}: {(cantidad * 100) / totalParticipantes}%')            


def aniadirCliente(archivo: str = 'socios.txt'):

    try:
        nombre = str(input('dame el nombre: '))
        dni = str(input("dame el dni: "))
        entrenamiento= str(input("dame el entrenamiento que realizara: "))
        mes = int(input('que mes pago? numero solo: '))

        
        ruta = cargarRutaArchivo(archivo= archivo)
        
        with open(file= ruta, mode= "a", encode = 'utf-8') as f:
            f.write(
                f'{dni};{nombre};{entrenamiento};{mes};0'
            )
            f.close()

        print('cliente añadido!!!!!')
    
    except Exception:
        print("no se puede aniadir ningun cliente, problema fatal")


# cosas basicas del main y handlers
def opciones():
    print("1. ver socios morosos (ingresar numero de mes actual)") # hecho
    print("2. ver cantidad de socios") # hecho
    print("3. ver promedio de asistencias por plan") # hecho
    print("4. Reporte: morosos y sus deudas")
    print("5. añadir cliente") #hecho 
    print("7. eliminar cliente")
    print("8. ver todos los socios") # hecho
    print("9. registrar el pago del mes")
    print("10. registrar asistencia")
    print("0. salir") # hecho


# aca van a ir las llamadas a funcion segun se requiera
def handlerOpciones(opcion: int, archivo: str = 'socios.txt'):
    match opcion:
        
        case 1:
            try:
                mes = int(input("dame el numero del mes"))
                verMorosos(mes= mes, archivo= archivo)
            
            except Exception:
                print(' no fue correcto introducido')
        
        
        case 2:
            verCantSocios(archivo= archivo)
        
        case 3:
            promedioAsistencia(archivo= archivo)
        
        case 5:
            aniadirCliente(archivo= archivo)
        
        case 8:
            verSocios(archivo= archivo)

    
# main, dejarlo lo mas bobo que se pueda
def main():
    
    while True:
        
        try:
            opcion = int(input("selecciona una opcion: "))

            if opcion == 0:
                print("adios!!!!")
                break
            
            else:
                handlerOpciones(opcion)    
        
        except ValueError:
            print("selecciona un numero!!!")
            
main()