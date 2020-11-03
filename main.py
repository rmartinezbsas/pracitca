import csv
import os.path

def cargar(archivo, campos):
    formato='w'
     

    guardar = "si"
    lista_empleados = []
    while guardar == "si":
        empleado = []

        for campo in campos:
            empleado.append(input(f"Ingrese {campo} del empleado: "))
        lista_empleados.append(empleado)
        guardar = input("Desea seguir cargando empleados? Si/No")

    try:
        formato='w'
        archivo_usuario=(input("Ingrese el nombre del archivo"))  
        if archivo==archivo_usuario:
           formato=(input("Desea modificarlo o sobreescribirlo? Modificarlo - a sobreescribirlo- w     a/w"))
          
        else:
          print("El archivo no existe, se creara uno nuevo")
          archivo=archivo_usuario


        with open(archivo, formato, newline='') as file:
            file_guarda = csv.writer(file)
            file_guarda.writerows(lista_empleados)
            print("se guardo correctamente")
            return
    except IOError:
        print("Ocurrio un error con el archivo")

def informar(archivo,archivo2):
    
      legajo_i=(input("Ingrese el numero de legajo")) 
     
      with open(archivo2,'r', newline='') as file:
            lectura_csv = csv.reader(file)
            count=0
            j=0
            for j in lectura_csv:
              if (legajo_i==j[0]):
                  count= count+1
            
                   
            print(count)


      with open(archivo,'r', newline='') as f:
            saldo_vacaciones=0
            lecturae_csv = csv.reader(f)
            for n in lecturae_csv:
              if (legajo_i==n[0]):
            
                 saldo_vacaciones=(n[3])
                 saldo_final= int(saldo_vacaciones)-count
                 
      
      
                 print(f"{n[0]} {n[1]} {n[2]} Saldo", saldo_final)
           
         





def menu():
    ARCHIVO = "empleados.csv"
    ARCHIVO2 ="registro.csv"
    CAMPOS = ['Legajo', 'Apellido', 'Nombre', 'Total_vacaciones']

    while True:
        print("Elija una opcion: \n 1.Guardar datos \n 2.Mostar total de vacaciones \n 3.Salir")
        opcion = input("")
                 
        if opcion == "1":
           cargar(ARCHIVO, CAMPOS)
        if opcion == "2":
           informar(ARCHIVO,ARCHIVO2)
           #mostrar(ARCHIVO)
        if opcion == "3":
            exit()
        else:
            print("Por favor elija una opcion valida")

menu()