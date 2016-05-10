# coding=utf-8
from tornado import gen
from tornado_mysql import IntegrityError

import database


@gen.coroutine
def add_room(stu_room):
    cur = yield database.pool.execute("INSERT INTO student_room (`room_name`) VALUE (%s);SELECT @@IDENTITY AS id;",
                                      stu_room)
    res = database.cur_to_dict(cur)
    raise gen.Return(res)


@gen.coroutine
def add_class(stu_class):
    cur = yield database.pool.execute("INSERT INTO student_class (`class_name`) VALUE (%s);SELECT @@IDENTITY AS id;",
                                      stu_class)
    res = database.cur_to_dict(cur)
    raise gen.Return(res)


@gen.coroutine
def add_stu(stu_info):
    """
    :argument stu_info:{
            "stu_id": stu_id,
            "stu_name": stu_name,
            "stu_sex": stu_sex,
            "stu_nation": stu_nation,
            "stu_tel": stu_tel,
            "stu_cid": stu_cid,
            "stu_adr": stu_adr,
            "stu_room": stu_room,
            "stu_class": stu_class,
            "stu_parent_name": stu_parent_name,
            "stu_parent_relation": stu_parent_relation,
            "stu_parent_tel": stu_parent_tel,
            "stu_parent_name_bak": stu_parent_name_bak,
            "stu_parent_relation_bak": stu_parent_relation_bak,
            "stu_parent_tel_bak": stu_parent_tel_bak
        }
    """
    try:
        cur = yield database.pool.execute("""
            INSERT INTO student_info(`stu_id`,`stu_name`,`stu_sex`,`stu_room`,`stu_cid`,
            `stu_tel`,`stu_nation`,stu_adr,`stu_class`,
            `stu_parent_name`,`stu_parent_relation`,`stu_parent_tel`,
            `stu_parent_name_vice`,`stu_parent_relation_vice`,`stu_parent_tel_vice`)
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
            """, (stu_info['stu_id'], stu_info['stu_name'],
                  stu_info['stu_sex'], stu_info['stu_room'], stu_info['stu_cid'], stu_info['stu_tel'],
                  stu_info['stu_nation'],
                  stu_info['stu_adr'], stu_info['stu_class'], stu_info['stu_parent_name'],
                  stu_info['stu_parent_relation'], stu_info[
                                                                'stu_parent_tel'], stu_info['stu_parent_name_vice'],
                  stu_info['stu_parent_relation_vice'], stu_info['stu_parent_tel_vice']
                  ))
    except IntegrityError:
        raise gen.Return('已有该学生')
    raise gen.Return('添加成功')


@gen.coroutine
def get_stu(stu_info):
    for it in stu_info:
        if stu_info[it] != "0":
            stu_info[it]
            it
