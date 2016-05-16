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
    sql_str = "SELECT room_name FROM student_room WHERE id in (SELECT DISTINCT stu_room FROM student_info WHERE 1=1)"
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
def get_dis(page_start, info):
    sql_str = """SELECT * FROM apartment_discipline,student_info WHERE apartment_discipline.stu_id = student_info.stu_id"""
    sql_list = []

    if info['stu_sex'] != 0:
        sql_str += " and stu_sex = %s"
        sql_list.append(info['stu_sex'] == 1 and '男' or '女')

    if info['stu_id'] != 0:
        sql_str += " and apartment_discipline.stu_id = %s"
        sql_list.append(info['stu_id'])

    if info['stu_room'] != 0:
        sql_str += " and stu_room = %s"
        sql_list.append(info['stu_room'])

    if info['dis_type'] != 0:
        sql_str += " and dis_type = %s"
        sql_list.append(info['dis_type'])

    if info['dis_class'] != 0:
        sql_str += " and dis_class = %s"
        sql_list.append(info['dis_class'])

    if info['page_offset'] != 0:
        sql_str += " LIMIT %s,%s"
        sql_list.append(page_start)
        sql_list.append(info['page_offset'])

    sql_str += ";"
    sql_tuple = tuple(sql_list)

    cur = yield database.pool.execute(sql_str, params=sql_tuple)
    rs = database.cur_to_dict(cur)
    for i in rs:
        i['dis_date'] = "%s" % i['dis_date']
        if i['dis_type'] is 1:
            i['dis_class'] = helper_service.get_dis_item_by_num(i['dis_class'])
        elif i['dis_type'] is 2:
            i['dis_class'] = helper_service.get_dis_behavior_by_num(i['dis_class'])
        i['dis_type'] = helper_service.get_dis_type_by_num(i['dis_type'])

    raise gen.Return(rs)


@gen.coroutine
def count_dis():
    cur = yield database.pool.execute(
        """SELECT count(*) AS num FROM apartment_discipline;"""
    )
    rs = database.cur_to_dict(cur)
    raise gen.Return(rs)
