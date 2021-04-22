import mysql.connector                                     #conector a MySQL
from bullet import VerticalPrompt, Input, Password         #oculta contraseña al escribirla

cli = Password(prompt="Introduce contraseña para password_manager_3000: ", hidden = "*")
result = cli.launch()




try:
  db =  mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=result,
        database="password_manager_3000")

except mysql.connector.Error as err:
  print("Something went wrong: {}".format(err))
  raise

print("""
1. Insertar datos de nueva cuenta
2. Sacar contraseña
""")
opcion= int(input("Ingresa una opcion: "))


if opcion == 1:                                                      #insert option doesnt seem to work dont know why
    pwd = Password(prompt="contraseña: ",hidden = "*")
    result_pwd = pwd.launch()
    email = input("email: ")
    nombre_app = input("nombre app: ")

    cursor = db.cursor()
    cursor.execute = "INSERT INTO cuentas VALUES ('"+ result_pwd +"','"+ email +"','"+ nombre_app +"');" 
    db.close() 




         
elif opcion == 2:
    name = input("introduce el nombre de la app en minusculas: ")
    cursor = db.cursor()
    cursor.execute("SELECT password FROM cuentas WHERE app_name = '" + name +"';")
    r = cursor.fetchall()
    print(r)
    db.close()

else:
    print("No  has tecleado ninguna")


