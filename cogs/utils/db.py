import pymysql
import config


def get_all_prefixes():
    db = pymysql.connect(config.db_ip, config.db_user, config.db_pass, config.db_name)
    cur = db.cursor()
    cur.execute(f'SELECT * FROM settings')
    results = cur.fetchall()
    d = dict()
    for row in results:
        d[str(row[0])] = row[1]
    db.close()
    return d