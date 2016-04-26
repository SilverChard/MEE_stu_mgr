# coding=utf-8

from tornado import gen

import database


@gen.coroutine
def get_stu_info_by_id(stu_id):
    cur = yield database.pool.execute("SELECT stu_name,stu_sex FROM  student_info WHERE stu_id=%s ;", stu_id)
    rs = database.cur_to_dict(cur)
    raise gen.Return(rs)


@gen.coroutine
def get_room_info():
    cur = yield database.pool.execute("SELECT * FROM student_room;")
    rs = database.cur_to_dict(cur)
    raise gen.Return(rs)


def get_dis_item_by_num(num):
    item = None
    if num == 1:
        item = '烟'
    elif num == 2:
        item = "酒"
    elif num == 3:
        item = "打火机"
    elif num == 4:
        item = "管制刀具"
    elif num == 5:
        item = "违规电器"
    elif num == 10:
        item = "其他违规物品"
    return item


def get_dis_behavior_by_num(num):
    behavior = None
    if num == 1:
        behavior = '早归'
    elif num == 2:
        behavior = "晚归"
    elif num == 3:
        behavior = "夜不归宿"
    elif num == 4:
        behavior = "私开小卖部"
    elif num == 5:
        behavior = "聚众打麻将"
    elif num == 6:
        behavior = "私养宠物"
    elif num == 7:
        behavior = "宿舍打架"
    elif num == 10:
        behavior = "其他违纪行为"
    return behavior


def get_dis_type_by_num(num):
    dis_type = None
    if num == 1:
        dis_type = "宿舍违纪物品"
    elif num == 2:
        dis_type = "宿舍行为违纪"
    return dis_type
