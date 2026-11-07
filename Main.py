# creacion del menu 


def opciones():
    print("1. ver socios morosos (anterior al mes que ingresa el usuario.)")
    print("2. ver cantidad de socios")
    print("3. ver promedio de asistencias por plan")
    print("4. Reporte: morosos y sus deudas")
    print("0. salir")


# aca van a ir las llamadas a funcion segun se requiera
def handlerOpciones(opcion: int):
    pass
    

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