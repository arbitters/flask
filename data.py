import mysql.connector


def getToken():
    connection = mysql.connector.connect(
        host='containers-us-west-120.railway.app',
        port=6415,
        username='root',
        password='0en6pbybktiIE41UpRnu',
        database='railway'
    )
    cursor = connection.cursor(dictionary=True)
    table = 'Token'
    query = f'SELECT token FROM {table} WHERE id = {1}'
    cursor.execute(query)
    token = cursor.fetchall()
    cursor.close()
    connection.close()
    return [x['token'] for x in token].pop()


