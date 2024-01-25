import psycopg2

# Crear objecto de conexion
con = psycopg2.connect(
    host="ec2-50-17-37-172.compute-1.amazonaws.com",
    database="d2a6f6ik93fsj6",
    user="gguzman",
    password="p394a126d55e12096219d2fe53431aff619f3d86fa36697a76f32bf57f19ced06"
)

# Crear cursor
cursor = con.cursor()

# Mysql
# show tables

try:
    query = '''
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = 'public'
    '''

    cursor.execute(query)

    tablas = cursor.fetchall()

    for t in tablas:
        print(t[0])
except psycopg2.Error as e:
    print(f'Un error en la conexion {e}')
finally:
    cursor.close()
    con.close()

