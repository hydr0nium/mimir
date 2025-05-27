from mimir.util.constants import PACKAGE_MANAGERS, INSTALLED_DB
import sqlite3




def add_installed_package(package_name):
    raise NotImplementedError

def create_db():
    stms = ['''
    CREATE TABLE IF NOT EXISTS installed_packages (
    id INTEGER PRIMARY KEY,
    name text NOT NULL,
    installed_with text NOT NULL
    );
    '''
    ]
    conn = sqlite3.connect(INSTALLED_DB)
    cursor = conn.cursor()
    for stm in stms:
        cursor.execute(stm)
    conn.commit()