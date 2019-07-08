#this class is used to abstract the other connector classes from access
import sqlite_connector

database = "";

#select the database sqlite Database from the getDatabase Switcher
def sqlite():
    return sqlite_connector;

def getDatabase(argument):
    switcher = {
        1: sqlite,
        2: sqlite,
        3: sqlite,
        4: sqlite,
        5: sqlite,
        6: sqlite,
        7: sqlite,
        8: sqlite,
        9: sqlite,
        10: sqlite,
    }

    func = switcher.get(argument, lambda: "Invalid database Type.")
    # Execute the function
    func()



