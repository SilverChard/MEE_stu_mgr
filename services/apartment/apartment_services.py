# coding=utf-8
from tornado import gen

import database


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
