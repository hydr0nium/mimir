from mimir.util.constants import PACKAGE_MANAGERS, INSTALLED_DB
import sqlite3
from mimir.util.output import debug



def add_installed_package(package_name, installed_name, package_manager):
    conn = sqlite3.connect(INSTALLED_DB)
    cur= conn.cursor()
    
    query = "INSERT INTO installed_packages (name, installed_name, installed_with) VALUES (?,?,?)"
    cur.execute(query, (package_name, installed_name, package_manager))
    conn.commit()


def get_installed_packages():
    conn = sqlite3.connect(INSTALLED_DB)
    cur= conn.cursor()
    
    query = "SELECT name,installed_name,installed_with FROM installed_packages"
    res = cur.execute(query)
    res = res.fetchall()
    conn.commit()
    return res

def check_install(package_name):
    conn = sqlite3.connect(INSTALLED_DB)
    cur= conn.cursor()
    query = "SELECT name FROM installed_packages WHERE name == (?)"
    res = cur.execute(query, (package_name,))
    res = res.fetchall()
    conn.commit()
    return len(res)==1

def get_installed_package(package_name):
    conn = sqlite3.connect(INSTALLED_DB)
    cur= conn.cursor()
    query = "SELECT installed_name,installed_with FROM installed_packages WHERE name == (?)"
    res = cur.execute(query, (package_name,))
    res = res.fetchone()
    debug(res)
    conn.commit()
    return res

def remove_package_from_db(package_name):
    conn = sqlite3.connect(INSTALLED_DB)
    cur= conn.cursor()
    query = "DELETE FROM installed_packages WHERE name == (?)"
    cur.execute(query, (package_name,))
    conn.commit()

def create_db():
    stms = ['''
    CREATE TABLE IF NOT EXISTS installed_packages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name text NOT NULL,
    installed_name text NOT NULL,
    installed_with text NOT NULL
    );
    '''
    ]
    conn = sqlite3.connect(INSTALLED_DB)
    cursor = conn.cursor()
    for stm in stms:
        cursor.execute(stm)
    conn.commit()