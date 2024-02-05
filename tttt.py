import pyodbc

# Configuración de la conexión
server = 'SAP (SQL Server 13.0.4259.0 -SAP/AuxiliarSistemas)'  # Reemplaza con el nombre de tu servidor SQL Server
database = 'SG-STEAMCONTROL'  # Reemplaza con el nombre de tu base de datos
username = 'INTERFAZ'  # Reemplaza con tu nombre de usuario
password = '123456*'  # Reemplaza con tu contraseña
driver = '{ODBC Driver 17 for SQL Server}'  # Asegúrate de tener el controlador correcto instalado

# Cadena de conexión
connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

try:
    # Intenta establecer la conexión
    connection = pyodbc.connect(connection_string)
    print('Conexión exitosa')

    # Aquí puedes realizar operaciones en la base de datos, como consultas, inserciones, actualizaciones, etc.

    # Por ejemplo, puedes ejecutar una consulta
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM TuTabla")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    # No olvides cerrar el cursor y la conexión cuando hayas terminado
    cursor.close()
    connection.close()

except Exception as e:
    print(f'Error al intentar conectar: {e}')
