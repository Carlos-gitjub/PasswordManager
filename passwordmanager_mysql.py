import mysql.connector                                     #conector a MySQL
from bullet import VerticalPrompt, Input, Password         #oculta contraseña al escribirla

cli = Password(prompt="Introduce contraseña para password_manager_3000: ", hidden = "*")
result = cli.launch()

#conexión a base de datos
try:
  db =  mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=result,
        database="password_manager_3000")
except mysql.connector.Error as err:
  print("Something went wrong: {}".format(err))
  raise                                                    #"raise" lo he puesto para que el programa no sga ejecutandose si hay un error

#definición de funciones
def sacar_contrasenia():
    name = input("introduce el nombre de la app en minusculas: ")
    cursor = db.cursor()
    cursor.execute("SELECT password FROM cuentas WHERE app_name = '" + name +"';")
    r = cursor.fetchall()
    print(r)
    db.close()
def insertar_datos_cuenta():
    pwd = Password(prompt="contraseña: ",hidden = "*")
    result_pwd = pwd.launch()
    email = input("email: ")
    nombre_app = input("nombre app: ")

    cursor = db.cursor()
    cursor.execute = "INSERT INTO cuentas VALUES ('"+ result_pwd +"','"+ email +"','"+ nombre_app +"');" 
    db.close()

#Menú
print("""
1. Insertar datos de nueva cuenta
2. Sacar contraseña
""")
opcion= int(input("Ingresa una opcion: "))

if opcion==1:
    insertar_datos_cuenta()
elif opcion ==2:
    sacar_contrasenia()
else: 
    print("No has introducido ninguna opcion")

