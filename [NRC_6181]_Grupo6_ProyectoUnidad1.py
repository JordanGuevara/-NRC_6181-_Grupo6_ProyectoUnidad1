# Controlador de la fecha y hora
from msilib.schema import Control
# Esto es usada para poder llevar un registro de exacto de la hora y fecha de ingreso del cliente 
from calendar import c
# Esta importacion ayuda para mostrar y asignarle numeros randoms a nuestras variables
import random
from datetime import date
import datetime
from datetime import datetime


"""
Para poder solventar el problema que presente Cooperativa con el registro de sus nuevos vehiculos y choferes esto
ayudara a la cooperativa a poder llevar un registro de los vehiculos y choferes nuevos que trabajan. A su vez poder registrar
a clientes nuevos y llevar un control de lo clientes que solicitan el sevicio.
Para poder solventar la primera parte del problema se crea una clase la cual tiene como nombre clientes, esta clase tendra las variables 
nombre, apellido y edad, esto ayudara a recompilar los datos principales de cada cliente que se ha registrado. 
"""

"""
Esta clase sirve para el control del registro de clientes
"""
class clientes():
    # Constructor de objeto para nuestros clientes
    def __init__(self, nombre, apellido, telefono):
        self.nombre=nombre
        self.apellido=apellido
        self.telefono=telefono
"""
la  clase VehiculosChoferes contiene las variables para el registro de los vehiculos y choferes  nuevos
"""
class VehiculosChoferes:
    #Constructor de objeto de nuestros choferes
    def __init__(self, matricula, marca, cedulap, nombres, apellidos, edad):
        self.matricula=matricula
        self.marca=marca
        self.cedulap=cedulap
        self.nombres=nombres
        self.apellidos=apellidos
        self.edad=edad

# Banderas para detener el condicional while con sus repectivos casos
condicion1=True
condicion2=True 
condicion3=True
condicion4=True
# Asiganara y mostrara la fecha actual 
fecha=datetime.today().strftime('%m-%d')  
# Asignacion de variables con sus valores especificos   
"""
Fechas de los dias festivos
"""
añoNuevo="06-10"
carnaval="03-28"
viernesSanto="04-15"
diaTrabajo="05-02"
batallaPichincha="05-23"
diaDifuntos="11-04"
indCuenca="11-03"
navidad="12-31"
"""
Este sera  el menu principal el cual le de las dos opciones que posee el codigo, el menu principal se veria  asi:
=============================== 
COOPERATIVA "LA FAMILIA"
=============================== 
1:CLIENTES
2:AGENCIA
3:SALIR 
=============================== 
INGRESE UNA OPCION:
"""
# Menu que podremos seleccionar nuestras opciones para el problema que se tiene planteado en separ en subproblemas
while condicion1==True:
    # Ingreso para asiganrle un valor a nuestra variable para seleccionar que orden queremos hacer
    menuPrincipal=int(input("\n=============================== \nCOOPERATIVA °LA FAMILIA°: \n=============================== \n 1:CLIENTES \n 2:AGENCIA \n 3:SALIR \n=============================== \n INGRESE UNA OPCION:  "))
    if menuPrincipal ==1:
        """
        Al momento de selccionar la opcion 1, se desplegara un submenu el cual  ledara dos opciones al cliente la primera un registro y la
        segundael ingreso de sesión, en el ingreso de sesión el cliente podra solicitar el servicio
        ======================================= 
        COOPERATIVA "LA FAMILIA"
        ======================================= 
        1:REGISTRATE, SI ERES CLIENTE NUEVO
        2:INICIA SESIÓN, SI YA ERES  USUARIO
        3:SALIR 
        ======================================= 
        INGRESE UNA OPCION:
        """
        
        while condicion2 ==True:
            #Submenu para las acciones que se hara para los clientes
            subCliente=int(input("\n======================================= \nCOOPERATIVA °LA FAMILIA°: \n======================================= \n 1:REGISTRATE, SI ERES CLIENTE NUEVO \n 2:INICIA SESIÓN, SI YA ERES  USUARIO \n 3:VOLVER AL MENU PRINCIPAL \n======================================= \n INGRESE UNA OPCION:  "))
            if subCliente ==1:
                print ("====================================================================")
                print ("            ERES CLIENTE NUEVO REGISTRATE Y VIAJA SEGURO ")
                print ("====================================================================") 
                """
                En la opcion 1 desplegara el regiustro primero se le pedira aL usuario que ingrese sus datos principales esto ayudara 
                a la compañia al momento de hacer una carrera, 
                """
                """
                En esta seccion se le pedira al nuevo usuario que ingrese sus datos para haci poder disponer del servicio, el usuario para 
                poder regitrarse debera ingresar su nombre, apellido, edad (si el usuario es menor de 16 años, se le permitira el registro pero
                con supervisión de los padres, asi  mismo si es mayor de 75 serasolo bajo supervision de un familiar), cedula y telefono, ejemplo
                INGRESE SUS NOMBRE: GREGORY
                INGRESE SUS APELLIDO: CHEVEZ
                INGRES SU EDAD: 20
                EDAD PERMITIDA
                INGRESA TU NUMERO DE CEDULA O PASAPORTE: 0952799708
                INGRESA TU NUMERO DE TELFONA PARA PODER ESTAR EN CONTACTO CONTIGO A LO QUELLEGEEL CHOFER: 0975781238
                """
                # Asignacion de variables a usar en nuestro codigo
                nombre=str(input("INGRESE SUS NOMBRE: "))
                apellido=str(input("INGRESE SUS APELLIDO: "))
                edad=int(input("INGRES SU EDAD: "))
                #se validara la edad en caso de ser menor de edad saldra edad negada y si es mayor de 65 igualmente sera negada
                if edad>=15 and edad<=75 :
                    print ("EDAD PERMITIDA")
                    cedula=str(input("INGRESA TU NUMERO DE CEDULA O PASAPORTE: "))
                    telefono=str(input("INGRESA TU NUMERO PARA ESTAR EN CONTACTO: "))
                    # Creacion de un archivo txt para el guardado de los datos
                    arch=open('Registro.txt','w')
                    arch.write("|   NOMBRE   |   APELLIDO   |   EDAD   |      CEDULA     |     TELEFONO     |"+'\n')
                    arch.write('    '+ nombre + '       '+ apellido + '       ' + str(edad) + '            ' + cedula+ '              ' + telefono )
                    arch.close() 
                    
                else:
                    print("EDAD NO PERMITIDA POR SER MENOR DE EDAD, VUELVA A INGRESAR")
                    print ("==================================================================================")  
                    print ("!!QUE BIEN YA PERTENECES A UNA DE LAS MEJORES COOPERATIVAS DE TAXIS DEL PAIS¡¡ ")
                    print ("==================================================================================") 


                
            elif subCliente ==2:
                print ("====================================================================")
                print ("          HOLA VIAJERO QUE SE SIENTE VIAJAR SEGURO DE NUEVO ")
                print ("====================================================================")
                """
                Al seleccionar la opcion 2 desplegara el inicio de seción del usuario solicitando su nombre como usuario y su numero de cedula 
                como contraseña, EJEMPLO:
                INGRESE SU USUARIO O NOMBRE REGISTRADO: GREGORY
                INGRESE SU CONTRASEÑA: 0952799708
                """
                usuario=str(input("INGRESE SU USUARIO O NOMBRE REGISTRADO: "))
                passw=str(input("INGRESE SU CONTRASEÑA: "))
                # Verificacion del usuario y la contraseña
                if usuario==nombre and passw==cedula:
                    print("LOS DATOS INGRESADOS SON CORRECTOS")
                    """
                    Una vez que el usuario verifique sus datos sele pedira que ingrese su lugar de recogida, referencia del  sector
                    de regida y lugar de llegada
                    INGRESE EL LUGAR DE RECOGIDA: MUCHO LOTE MZ.2624
                    INGRESE UNA REFERENCIA DEL SECTOR: DETRAS DE LA  FERIA DE CARROS
                    INGRESE EL LUGAR DE LLEGADA: CIUDADELA LA FAE
                    """
                    print ("====================================================================") 
                    lugarI=str(input("INGRESE EL LUGAR DE RECOGIDA: "))
                    referencia=str(input("INGRESE UNA REFERENCIA DEL SECTOR: "))
                    lugarFi=str(input("INGRESE EL LUGAR DE LLEGADA: "))
                    #fecha1=datetime.datetime.now()
                    #fecha2=datetime.datetime.strftime(fecha1, '%b %d %Y %H:%M:%S')
                    print ("====================================================================") 
                    g=clientes(nombre,apellido,telefono)
                    print ("====================================================================")
                    print ("         SOLICITUD FUE REALIZADA EXITOSAMENTE")
                    print ("====================================================================")
                    print("NOMBRE DEL CLIENTE: ",g.nombre)
                    print("APELLIDO DEL CLIENTE: ",g.apellido)
                    print("TELEFONO DE CONTACTO: " ,g.telefono)
                    print("LUGAR DE PARTIDA: ",lugarI)
                    print("REFERENCIA DEL  LUGAR DE RECOGIDA: ",referencia) 
                    print("LUGAR DE LLEGADA: ",lugarFi)
                    print("FECHA DE SOLICITUD: 2022-"+str(fecha))
                    print ("====================================================================")
                    print ("       AVISO: SE HARA UN DESCUENTO DEL 25% POR FERIADO")
                    print ("====================================================================")
 
                else:
                    print("LOS DATOS INGRESADOS SON INCORRECTOS, VUELVA A INGRESAR:")
                    print ("====================================================================")
            elif subCliente ==3:
                print("REGRESANDO AL MENU PRNCIPAL......... ")
                condicion2=False
            else:
                print("LA OPCION INGRESA ES INCORRECTA VUELVA A INGRESAR: ")      
                print("====================================================================")

    elif menuPrincipal ==2:
        while condicion3==True:
            # Menu para el administrador de la Cooperativa de taxi
            subAdmin=int(input("\n======================================= \nCOOPERATIVA °LA FAMILIA°: \n======================================= \n 1:REGISTRO DE TAXIS, SOLO ADMINISTRADORES \n 2:SOLICITUDES HECHAS \n 3:VOLVER AL MENU PRINCIPAL \n======================================= \n INGRESE UNA OPCION:  "))
            if subAdmin ==1:
                """
                En la opcion 1 desplegara el inicio de seción el cual solo tendra el administrador al momento de registrar algun nuevo vehiculo o chofer
                esto hara que el programa se seguro al momento de que el cliente o alguna persona mala intente ingresar.
                Para poder ingresar esta seccion, el administrador solo tiene acceso a ella la cual el usuario y la contraseña son:
                admin=("jordan")
                contra=("losrapidos")
                """
                admin=("jordan")
                contra=("losrapidos")
                print ("====================================================================")
                usuario=str(input("INGRESE EL EL USUARIO: "))
                contrasena=str(input("INGRESE LA CONTRASEÑA: "))
                if usuario==admin and contrasena==contra:
                    print("LOS DATOS INGRESADOS SON CORRECTOS")
                    print ("====================================================================")
                    print ("             REGISTRO DE VEHICULOS Y CHOFERES ")
                    print ("====================================================================")
                    VCHnuevos=int
                    """  
                    El while nos ayudara a poder verificar que se ha llegado a la cantidad prevista de taxistas a registrar
                    """ 

                    while condicion4==True: 
                        VCHnuevos=int(input("INGRESE LA CANIDAD DE TAXISTAS QUE VAN HACER REGISTRADOS: "))  
                        """    
                        El for servira para hacer el bucle del ingreso de los nuevos taxis, si ingresa 2 se repitira 2 veces permitiendo el ingreso de 
                        taxistas de la cantidad indicada
                        """  
                        if VCHnuevos<=3:
                            for i in range(VCHnuevos):
                                        """
                                        En estas lineas de codigo el administrador de la cooperativa podra ingresar los nuevos vehiculos y choferes que trabajaran en
                                        la cooperativa esto seria  un ejemplo de como se registra:
                                        INGRESE LA MATRICULA DEL VEHICULO: GRM-1504
                                        INGRESE EL MODELO Y LA MARCA DEL VEHICULO: CHEVROLET "CAMARO 2022"
                                        INGRESE EL NUMERO DE CEDULA DEL USUARIO: 0952799708
                                        INGRESE LOS NOMBRES DEL CONDUCTOR: KARLOS GREGORY
                                        INGRSE LOS APELLIDOS DEL CONDUCTOR: CHEVEZ BAZAN
                                        INGRESE EL TIPO DE LICENCIA DEL CONDUCTOR: TIPO C
                                        """
                                        print ("====================================================================")
                                        print ("             REGISTRO DE VEHICULOS  ")
                                        print ("====================================================================")
                                        matricula=str(input("INGRESE LA MATRICULA DEL VEHICULO: "))
                                        marca=str(input("INGRESE EL MODELO Y LA MARCA DEL VEHICULO: "))
                                        cedulap=int(input("INGRESE EL NUMERO DE CEDULA DEL USUARIO: "))
                            for i in range(VCHnuevos):
                                        print ("====================================================================")
                                        print ("             REGISTRO DE CHOFERES  ")
                                        print ("====================================================================")
                                        nombres=str(input("INGRESE LOS NOMBRES DEL CONDUCTOR: "))
                                        apellidos=str(input("INGRSE LOS APELLIDOS DEL CONDUCTOR: "))
                                        tipoLic=str(input("INGRESE EL TIPO DE LICENCIA DEL CONDUCTOR: "))
                                        print ("====================================================================")
                            condicion4=False
                        else: 
                            print(" INGRESE CORRECTAMENTE EL NUMERO DE TAXISTAS A REGISTRAR")
                else:
                        print("LOS DATOS INGRESADOS SON INCORRECTOS, VUELVA A INGRESAR:")
                        print ("====================================================================")
            elif subAdmin ==2:
                """
                En la opcion dos el administrador podra observar que personas han solicitado un pedido, adicional a esto se le reflejara
                que dias tendra un descuento, esto dias son los dias festivos, entos dias los clientes tendra un descuento el cual sera
                de 25% para cualquier carrera
                """
                g=clientes(nombre, apellido, telefono )
                print ("====================================================================")
                print ("         SOLICITUD FUE REALIZADA EXITOSAMENTE")
                print ("====================================================================")
                print("NOMBRE DEL CLIENTE: ",g.nombre)
                print("APELLIDO DEL CLIENTE: ",g.apellido)
                print("TELEFONO DE CONTACTO: " ,g.telefono)
                print("LUGAR DE PARTIDA: ",lugarI)
                print("REFERENCIA DEL  LUGAR DE RECOGIDA: ",referencia) 
                print("LUGAR DE LLEGADA: ",lugarFi)
                print("FECHA EN LA QUE REALIZASTES LA SOLICITUD DEL DERVICIO "+str(fecha))
                print ("====================================================================")
                print ("         AVISO: SE HARA UN DESCUENTO DEL 25% POR FERIADO")
                print ("====================================================================")
                # Asignacion de variable con un numero random decimal con su limitante
                pago=random.uniform(1,5)
                """
                Estos datos sobre los feriados suceden durante el año en unos internacionales y otros nacionales en el Ecuador fueron encontrados 
                por este medio https://www.eluniverso.com/noticias/ecuador/los-dias-que-son-feriados-en-ecuador-para-este-2022
                -nota/#:~:text=En%20Ecuador%20anualmente%20se%20cuenta,obligatorio%20para%20todos%20los%20ecuatorianos. gracias a esta información existente 
                pudimos armar nuestro codigo de forma veridica.
                """
                if fecha==añoNuevo:
                    print("EL CLIENTE PAGO : ",round(pago,2))
                    descuento=(pago*25)/100
                    print("DESCUENTO POR SER AÑO NUEVO, SE LE HA COBRADO: ",round(descuento,2))
                elif fecha==viernesSanto:
                    print("EL CLIENTE PAGO : ",round(pago,2))
                    descuento=(pago*25)/100
                    print("DESCUENTO POR SER VIERNES SANTO, SE LE HA COBRADO: ",round(descuento,2))
                elif fecha==diaTrabajo:
                    print("EL CLIENTE PAGO : ",round(pago,2))
                    descuento=(pago*25)/100
                    print("DESCUENTO POR SER DIA  DEL TRABAJO, SE LE HA COBRADO: ",round(descuento,2))
                elif fecha==batallaPichincha:
                    print("EL CLIENTE PAGO : ",round(pago,2))
                    descuento=(pago*25)/100
                    print("DESCUENTO POR EL DIA DE LA BATALLA DE PICHINCHA, SE LE HA COBRADO: ",round(descuento,2))
                elif fecha==diaDifuntos:
                    print("EL CLIENTE PAGO : ",round(pago,2))
                    descuento=(pago*25)/100
                    print("DESCUENTO POR DIA DE LOS DIFUNTOS, SE LE HA COBRADO: ",round(descuento,2))
                elif fecha==indCuenca:
                    print("EL CLIENTE PAGO : ",round(pago,2))
                    descuento=(pago*25)/100
                    print("DESCUENTO POR SER DIA DE LA INDEPENDENCIA DE CUENCA, SE LE HA COBRADO: ",round(descuento,2))
                elif fecha==navidad:
                    print("EL CLIENTE PAGO : ",round(pago,2))
                    descuento=(pago*25)/100
                    print("DESCUENTO POR SER NAVIDAD, SE LE HA COBRADO: ",round(descuento,2))
                else: 
                    print(" POR EL MOMENTO, HOY NO ES UN DIA FERIADO")
                    print("====================================================================")
                print("====================================================================")
            elif subAdmin ==3:
                print ("REGRESAR AL MENU PRNCIPAL ")
                condicion3=False       
            else:
                print("LA OPCION INGRESA ES INCORRECTA VUELVA A INGRESAR: ")           
    elif menuPrincipal ==3:
        print ("GRACIAS POR SU VISITA")
        condicion1=False
    else:
        print("LA OPCION INGRESA ES INCORRECTA VUELVA A INGRESAR ")
                