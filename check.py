import os
import sqlite3


def delete_all_in_db():
    """
    This function connects to database 'db/database'
    then delete all elements
    :return: None
    """
    db = sqlite3.connect('db/database.db')
    query = "DELETE FROM urls"
    cursor = db.cursor()
    cursor.execute(query)
    db.commit()


def add_element_in_db(lst):
    """
    This function connects to database 'db/database'
    then add break servers
    :param lst: [list] 'break_servers'
    :return: None
    """
    db = sqlite3.connect('db/database.db')
    cursor = db.cursor()
    for server in lst:
        cursor.execute("INSERT INTO urls(name) VALUES(?)", (server,))
        db.commit()


def check(lst):
    """
    This function pings servers from the [list] 'servers' by os console
    if server is break add hostname in [list] 'break_servers'
    :return: None
    """
    for server in lst:
        if os.system("ping -c 1 " + server) != 0:
            break_servers.append(server)


break_servers = []

servers = [
    "call4life.vn",
    "mmi.call4life.vn",
    "call4.life",
    "diary.call4.life",
    "mmi.call4.life",
    "call4life.am",
    "landing.call4life.am",
    "land.call4life.am",
    "mmi.call4life.am",
    "mmibot.online",
    "service.mmibot.online",
    "anamnesis.call4life.net",
    "anamnesis.call4life.ru",
    "call4life.net",
    "landing.call4life.net",
    "land.call4life.net",
    "update.call4life.net",
    "mmi.call4life.net",
    "mmi-ios.call4life.net",
    "pinoyloan.ph",
    "206.189.40.124",
    "167.172.190.171",
    "207.154.215.211",
    "46.101.242.39",
    "138.197.184.201",
]

break_servers.clear()
delete_all_in_db()
check(servers)
if break_servers:
    add_element_in_db(break_servers)
