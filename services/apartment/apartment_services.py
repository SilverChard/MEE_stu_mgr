# coding=utf-8
from tornado import gen

import database
from services import helper_service


@gen.coroutine
def insert_dis(dis_data):
    """
    dis_data = {
            "stu_id": stu_id,
            "type": dis_type,
            "dis_class": dis_2,
            "others": others
        }

    """

    cur = yield database.pool.execute(
        """INSERT INTO apartment_discipline (`dis_type`, `dis_class`, `others`, `stu_id`, `dis_date`) VALUES (%s, %s, %s,%s,%s);"""
        , (dis_data['type'], dis_data['dis_class'], dis_data['others'], dis_data['stu_id'], dis_data['dis_date']))
    rs = database.cur_to_dict(cur)
    raise gen.Return(rs)


@gen.coroutine
def get_room(info):
    sql_str = "SELECT room_name FROM student_room WHERE id IN (SELECT DISTINCT stu_room FROM student_info WHERE 1=1)"
    sql_list = []
    if info['stu_sex'] != 0:
        sql_str += " and stu_sex = %s"
        sql_list.append(info['stu_sex'] == 1 and '男' or '女')

    if info['stu_id'] != 0:
        sql_str += " and stu_id = %s"
        sql_list.append(info['stu_id'])

    if info['dis_type'] != 0:
        sql_str += " and dis_type = %s"
        sql_list.append(info['dis_type'])

    if info['dis_class'] != 0:
        sql_str += " and dis_class = %s"
        sql_list.append(info['dis_class'])

    sql_str += ";"
    sql_tuple = tuple(sql_list)
    cur = yield database.pool.execute(sql_str, params=sql_tuple)
    rs = database.cur_to_dict(cur)
    raise gen.Return(rs)


@gen.coroutine
def get_dis(info):
    sql_str = """SELECT DISTINCT
    apartment_discipline.id AS id,
    student_info.stu_name AS stu_name,
    student_info.stu_sex AS stu_sex,
    student_info.stu_id AS stu_id,
    student_room.room_name AS stu_room,
    apartment_discipline.dis_type AS dis_type,
    apartment_discipline.dis_class AS dis_class,
    apartment_discipline.dis_date AS dis_date,
    apartment_discipline.others AS others,
    IF(dis_type = 1,
        dis_behavior.dis_class_name,
        dis_item.dis_class_name) AS dis_class
FROM
    apartment_discipline,
    student_info,
    student_room,
    dis_behavior,
    dis_item
WHERE
    (apartment_discipline.stu_id = student_info.stu_id)
        AND (student_info.stu_room = student_room.id)
        AND IF(apartment_discipline.dis_type = 1,
        (apartment_discipline.dis_class = dis_behavior.id),
        (apartment_discipline.dis_class = dis_item.id))"""
    sql_list = []

    if info['stu_sex'] != "":
        sql_str += " AND (`student_info`.`stu_sex` = %s)"
        sql_list.append(info['stu_sex'])

    if info['stu_id'] != "":
        sql_str += ' AND (`student_info`.`stu_id` LIKE "%s%%%%") ' % info['stu_id']

    if info['stu_room'] != "":
        sql_str += " AND (`student_info`.`stu_room` = %s)"
        sql_list.append(info['stu_room'])

    if info['dis_type'] != "":
        sql_str += " AND (`apartment_discipline`.`dis_type` = %s)"
        sql_list.append(info['dis_type'])

    if info['dis_class'] != "":
        sql_str += " AND (`apartment_discipline`.`dis_class` = %s)"
        sql_list.append(info['dis_class'])

    sql_str += "ORDER BY `apartment_discipline`.`id`;"
    sql_tuple = tuple(sql_list)

    cur = yield database.pool.execute(sql_str, params=sql_tuple)
    rs = database.cur_to_dict(cur)
    for i in rs:
        i['dis_date'] = "%s" % i['dis_date']
    raise gen.Return(rs)


@gen.coroutine
def get_dis_class_by_type(dis_type):
    if dis_type == '1':
        table_name = 'dis_behavior'
    if dis_type == '2':
        table_name = 'dis_item'
    cur = yield database.pool.execute(query=("SELECT * FROM `mee_stu_mgr`.%s;" % table_name))
    rs = database.cur_to_dict(cur)
    raise gen.Return(rs)


@gen.coroutine
def update_dis(info):
    database.pool.execute(
        "UPDATE `mee_stu_mgr`.`apartment_discipline` SET `dis_type` = %s, `dis_class` = %s, `others` = %s,`stu_id` = %s, `dis_date` = %s WHERE `id` = %s;",
        (info['dis_type'], info['dis_class'], info['dis_others'], info['stu_id'], info['dis_date'], info['dis_id']))


@gen.coroutine
def del_dis(dis_id):
    database.pool.execute("DELETE FROM `mee_stu_mgr`.`apartment_discipline` WHERE `apartment_discipline`.`id`=%s;",
                          dis_id)
