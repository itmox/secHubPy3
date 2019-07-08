import sqlite3

def connect(dbName):
    # If no db name is given secHub.db is used. If a sqlite name is given (config) then the custom DB name/ Custom DB is taken
    if dbName =="" or not dbName:
        conn = sqlite3.connect('secHub.db');
    else:
        conn = conn = sqlite3.connect(dbName);
    return conn


def createTables(conn):
    c = conn.cursor()
    # Create basic/standard tables
    c.execute('''CREATE TABLE user(userId Username text, passwort text''')
    c.execute('''CREATE TABLE session(userId text, sessionId text, token text''')
    c.execute('''CREATE TABLE role(Username text, passwort text''')
    c.execute('''CREATE TABLE userInfo(Username text, passwort text''')
    c.execute('''CREATE TABLE persistentInput(session, passwort text''')
    c.execute('''CREATE TABLE (Username text, passwort text''')
    conn.commit()


def destroyDB(conn):
    conn.close()

