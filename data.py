import mysql.connector

def getToken():
    connection = mysql.connector.connect(
        host='containers-us-west-201.railway.app',
        port=7627,
        username='root',
        password='oJe5zg9UekxFFybq4BsA',
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

def createTables():
    connection = mysql.connector.connect(
        host='containers-us-west-201.railway.app',
        port=7627,
        username='root',
        password='oJe5zg9UekxFFybq4BsA',
        database='railway'
    )
    cursor = connection.cursor()
    create_league_table = """
        CREATE TABLE IF NOT EXISTS league (
            id INT AUTO_INCREMENT PRIMARY KEY,
            discord_user VARCHAR(255) UNIQUE,
            league_user VARCHAR(255),
            wallet_address VARCHAR(255),
            league_server VARCHAR(255)
        )
    """
    create_counter_table = """
        CREATE TABLE IF NOT EXISTS counter (
            id INT AUTO_INCREMENT PRIMARY KEY,
            discord_user VARCHAR(255) UNIQUE,
            counter_user VARCHAR(255),
            wallet_address VARCHAR(255),
            counter_server VARCHAR(255)
        )
    """
    cursor.execute(create_league_table)
    cursor.execute(create_counter_table)
    connection.commit()
    cursor.close()
    connection.close()


def getLeagueUser(user):
    connection = mysql.connector.connect(
        host='containers-us-west-201.railway.app',
        port=7627,
        username='root',
        password='oJe5zg9UekxFFybq4BsA',
        database='railway'
    )

    cursor = connection.cursor(dictionary=True)
    table = 'league'
    query = f"SELECT discord_user FROM {table} WHERE discord_user = %s"
    cursor.execute(query, (user,))
    user_exists = cursor.fetchone() is not None
    cursor.close()
    connection.close()
    return user_exists

def getCounterUser(user):
    connection = mysql.connector.connect(
        host='containers-us-west-201.railway.app',
        port=7627,
        username='root',
        password='oJe5zg9UekxFFybq4BsA',
        database='railway'
    )

    cursor = connection.cursor(dictionary=True)
    table = 'counter'
    query = f"SELECT discord_user FROM {table} WHERE discord_user = %s"
    cursor.execute(query, (user,))
    user_exists = cursor.fetchone() is not None
    cursor.close()
    connection.close()
    return user_exists


def insertLeagueUser(discordUser, leagueUser, walletAddress, leagueServer):
    connection = mysql.connector.connect(
        host='containers-us-west-201.railway.app',
        port=7627,
        username='root',
        password='oJe5zg9UekxFFybq4BsA',
        database='railway'
    )

    cursor = connection.cursor()
    table = 'league'

    insert_query = """
        INSERT INTO {} (discord_user, league_user, wallet_address, league_server)
        VALUES (%s, %s, %s, %s)
    """.format(table)
    values = (discordUser, leagueUser, walletAddress, leagueServer)
    cursor.execute(insert_query, values)
    connection.commit()
    cursor.close()
    connection.close()

def insertCounterUser(discordUser, counterUser, walletAddress, counterServer):
    connection = mysql.connector.connect(
        host='containers-us-west-201.railway.app',
        port=7627,
        username='root',
        password='oJe5zg9UekxFFybq4BsA',
        database='railway'
    )

    cursor = connection.cursor()
    table = 'counter'

    insert_query = """
        INSERT INTO {} (discord_user, counter_user, wallet_address, counter_server)
        VALUES (%s, %s, %s, %s)
    """.format(table)
    values = (discordUser, counterUser, walletAddress, counterServer)
    cursor.execute(insert_query, values)
    connection.commit()
    cursor.close()
    connection.close()
