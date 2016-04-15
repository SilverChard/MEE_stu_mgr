# coding=utf-8
from tornado import gen
from tornado_mysql import pools

from settings import mysql_db_host, mysql_db_port, mysql_db_user, mysql_db_pass, mysql_db_database

pool = pools.Pool(
    dict(host=mysql_db_host, port=mysql_db_port, user=mysql_db_user, passwd=mysql_db_pass, db=mysql_db_database,
         charset='utf8'),
    max_idle_connections=5,
    max_recycle_sec=3,
    max_open_connections=100)


def cur_to_dict(cur):
    rows = cur._rows
    keys = [item[0] for item in cur.description]
    return [dict(zip(keys, row)) for row in rows]
