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
            "stu_parent_name_vice": stu_parent_name_bak,
            "stu_parent_relation_vice": stu_parent_relation_bak,
            "stu_parent_tel_vice": stu_parent_tel_bak
            "stu_adr_id": stu_adr_id
        }
    """
    try:
        cur = yield database.pool.execute("""
            INSERT INTO student_info(`stu_id`,`stu_name`,`stu_sex`,`stu_room`,`stu_cid`,
            `stu_tel`,`stu_nation`,`stu_adr_id`,stu_adr,`stu_class`,
            `stu_parent_name`,`stu_parent_relation`,`stu_parent_tel`,
            `stu_parent_name_vice`,`stu_parent_relation_vice`,`stu_parent_tel_vice`)
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
            """, (stu_info['stu_id'], stu_info['stu_name'],
                  stu_info['stu_sex'], stu_info['stu_room'], stu_info['stu_cid'], stu_info['stu_tel'],
                  stu_info['stu_nation'],
                  stu_info['stu_adr_id'], stu_info['stu_adr'], stu_info['stu_class'], stu_info['stu_parent_name'],
                  stu_info['stu_parent_relation'], stu_info['stu_parent_tel'], stu_info['stu_parent_name_vice'],
                  stu_info['stu_parent_relation_vice'], stu_info['stu_parent_tel_vice']
                  ))
    except IntegrityError:
        raise gen.Return('已有该学生')
    raise gen.Return('添加成功')


@gen.coroutine
def get_stu(stu_info):
    """

    :param stu_info:{
            "stu_id": int(stu_id),
            "stu_name": stu_name,
            "stu_sex": stu_sex,
            "stu_nation": stu_nation,
            "stu_tel": stu_tel,
            "stu_cid": stu_cid,
            "stu_adr": stu_adr,
            "stu_room": int(stu_room),
            "stu_class": int(stu_class),
            "stu_parent_name": stu_parent_name,
            "stu_parent_relation": stu_parent_relation,
            "stu_parent_tel": stu_parent_tel,
            "stu_parent_name_vice": stu_parent_name_vice,
            "stu_parent_relation_vice": stu_parent_relation_vice,
            "stu_parent_tel_vice": stu_parent_tel_vice
            "0" means no filter
        }
    :return: res: raised res of student
    """

    sql_str = 'SELECT  stu_name,stu_id,stu_sex,room_name AS stu_room,stu_room AS stu_room_id,stu_class AS stu_class_id,stu_cid,stu_tel, stu_nation, stu_adr_id ,stu_adr,class_name AS stu_class , stu_parent_name , stu_parent_relation , stu_parent_tel,stu_parent_name_vice ,stu_parent_relation_vice,stu_parent_tel_vice FROM `student_info` , `student_class`,`student_room` WHERE student_class.id = student_info.stu_class AND student_room.id = student_info.stu_room'
    for it in stu_info:
        if stu_info[it] != "0":
            sql_str += " AND (`"
            sql_str += it
            sql_str += '` LIKE "'
            sql_str += "%s" % stu_info[it]
            if it == 'stu_room' or it == 'stu_class':
                sql_str += '")'
            else:
                sql_str += '%")'

    sql_str += " ORDER BY stu_id;"
    cur = yield database.pool.execute(sql_str)
    res = database.cur_to_dict(cur)
    raise gen.Return(res)


@gen.coroutine
def edit_stu(id_change_flag, stu_info):
    if id_change_flag:
        yield database.pool.execute("DELETE FROM mee_stu_mgr.student_info WHERE stu_id=%s;",
                                    stu_info['old_stu_id'])
        add_stu(stu_info)
    else:
        yield database.pool.execute(
            """UPDATE `mee_stu_mgr`.`student_info` SET
                    `stu_name`=%s,
                    `stu_sex`=%s ,
                    `stu_room`=%s,
                    `stu_cid`=%s ,
                    `stu_tel`=%s ,
                    `stu_nation`=%s ,
                    `stu_adr_id`=%s,
                    `stu_adr`=%s ,
                    `stu_class`=%s,
                    `stu_parent_name`=%s ,
                    `stu_parent_tel`=%s,
                    `stu_parent_relation`=%s,
                    `stu_parent_name_vice`=%s,
                    `stu_parent_tel_vice`=%s,
                    `stu_parent_relation_vice`=%s
                    WHERE `stu_id`=%s;""",
            (stu_info['stu_name'], stu_info['stu_sex'], stu_info['stu_room'], stu_info['stu_cid'],
             stu_info['stu_tel'], stu_info['stu_nation'], stu_info['stu_adr_id'], stu_info['stu_adr'],
             stu_info['stu_class'], stu_info['stu_parent_name'], stu_info['stu_parent_tel'],
             stu_info['stu_parent_relation'], stu_info['stu_parent_name_vice'], stu_info['stu_parent_tel_vice'],
             stu_info['stu_parent_relation_vice'], stu_info['stu_id']))
    raise gen.Return()


@gen.coroutine
def del_stu(stu_id):
    database.pool.execute("DELETE FROM `mee_stu_mgr`.`student_info` WHERE `stu_id`=%s;", stu_id)
    raise gen.Return()
