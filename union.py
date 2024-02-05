import pyodbc

def conexion_sql_server():
    try:
        connection = pyodbc.connect(
            trusted_connection='Yes',
            driver='{SQL Server Native Client}',
            server='C:\\Program Files\\Microsoft SQL Server\\MSSQL13.MSSQLSERVER\\MSSQL',
            database='SG-STEAMCONTROL',
        )
        print('Conexion exitosa')
        return connection
    except pyodbc.Error as e:
        print(f'Error connecting to SQL Server: {e}')
        return None
