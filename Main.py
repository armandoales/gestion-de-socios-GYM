import os

# funciones de carga y modificacion de archivos
# cambiar segun quien lo tenga
def verSocios(archivo: str = 'socios.txt'):

    carpeta = os.path.dirname(os.path.abspath(__file__))
    ruta = os.path.join(carpeta, archivo)
    
    with open(file= ruta, mode= 'r', encoding= "utf-8") as f:
        
        lineas = f.readlines()
        
        for linea in lineas:
            print(linea)
   


# cosas basicas del main y handlers
def opciones():
    print("1. ver socios morosos (anterior al mes que ingresa el usuario)")
    print("2. ver cantidad de socios")
    print("3. ver promedio de asistencias por plan")
    print("4. Reporte: morosos y sus deudas")
    print("5. aniadir cliente") # corregir aniadir enie
    print("7. eliminar cliente")
    print("8. ver todos los socios")
    print("9. registrar el pago del mes")
    print("10. registrar asistencia")
    print("0. salir")


# aca van a ir las llamadas a funcion segun se requiera
def handlerOpciones(opcion: int):
    match opcion:
        case 6:
            print("entro la funcion y el case funciona")
            verSocios()

    
#main, dejarlo lo mas bobo que se pueda
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