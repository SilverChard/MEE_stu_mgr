# coding=utf-8
import collections

import tornado
from tornado import gen, web
import xlwt
import StringIO
from handlers.base import BaseHandler
from services import helper_service
from services.student import student_service
from services.student.student_service import get_stu


class StudentIndexHandler(BaseHandler):
    @gen.coroutine
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render("/student/index.html")


class AddStudentHandler(BaseHandler):
    @gen.coroutine
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render("/student/stu_add.html")


class ShowStudentHandler(BaseHandler):
    @gen.coroutine
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render("/student/stu_show.html")


class EditStudentInfoHandler(BaseHandler):
    @gen.coroutine
    @tornado.web.authenticated
    def post(self, *args, **kwargs):
        """
            old_stu_id:                 旧学号 用于判断学号是否被修改
            stu_id:                     新学号
            stu_name:                   姓名
            stu_sex:                    性别
            stu_room:                   宿舍号(id)
            stu_cid:                    身份证号
            stu_tel:                    电话号码
            stu_nation:                 民族
            stu_adr_id:                 地址_区位号
            stu_adr:                    地址
            stu_class:                  班级
            stu_parent_name:            监护人姓名
            stu_parent_tel:             监护人电话
            stu_parent_relation:        监护人关系
            stu_parent_name_vice:       备用监护人姓名
            stu_parent_tel_vice:        备用监护人电话
            stu_parent_relation_vice:   备用监护人关系
        """
        id_change_flag = True
        if self.get_argument('old_stu_id') == self.get_argument('stu_id'):
            id_change_flag = False
        stu_info = {
            'old_stu_id': self.get_argument('old_stu_id'),
            'stu_id': self.get_argument('stu_id'),
            'stu_name': self.get_argument('stu_name'),
            'stu_sex': self.get_argument('stu_sex'),
            'stu_room': self.get_argument('stu_room'),
            'stu_cid': self.get_argument('stu_cid'),
            'stu_tel': self.get_argument('stu_tel'),
            'stu_nation': self.get_argument('stu_nation'),
            'stu_adr_id': self.get_argument('stu_adr_id'),
            'stu_adr': self.get_argument('stu_adr'),
            'stu_class': self.get_argument('stu_class'),
            'stu_parent_name': self.get_argument('stu_parent_name'),
            'stu_parent_tel': self.get_argument('stu_parent_tel'),
            'stu_parent_relation': self.get_argument('stu_parent_relation'),
            'stu_parent_name_vice': self.get_argument('stu_parent_name_vice'),
            'stu_parent_tel_vice': self.get_argument('stu_parent_tel_vice'),
            'stu_parent_relation_vice': self.get_argument('stu_parent_relation_vice')
        }
        student_service.edit_stu(id_change_flag=id_change_flag, stu_info=stu_info)
        self.write_json({'success':True})
        return

class DeleteStudentHandler(BaseHandler):
    @gen.coroutine
    @tornado.web.authenticated
    def post(self, *args, **kwargs):
        stu_id = self.get_argument('stu_id')
        student_service.del_stu(stu_id=stu_id)
        self.write_json({'success': True})
        return


class DownloadStudentInfoHandler(BaseHandler):
    @gen.coroutine
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        res = yield student_service.get_stu(stu_info={})

        # Content-Type这里我写的时候是固定的了，也可以根据实际情况传值进来
        self.set_header('Content-Type', 'application/x-xls')
        self.set_header('Content-Disposition', 'attachment; filename=student_info.xls')
        thead = {
            'stu_id': '学号',
            'stu_name': '姓名',
            'stu_sex': '性别',
            'stu_cid': '学生身份证号',
            'stu_nation': '民族',
            'stu_class': '班级',
            'stu_room': '宿舍',
            'stu_tel': '学生电话',
            'province': '省',
            'city': '市',
            'zone': '区',
            'stu_adr': '家庭住址',
            'stu_parent_name': '监护人1 姓名',
            'stu_parent_relation': '监护人1 关系',
            'stu_parent_tel': '监护人1 电话',
            'stu_parent_name_vice': '监护人2 姓名',
            'stu_parent_relation_vice': '监护人2 关系',
            'stu_parent_tel_vice': '监护人2 电话'
        }
        order_res = []

        for row in res:
            row['province'] = helper_service.get_province_by_id(row['stu_adr_id'])
            row['city'] = helper_service.get_city_by_id(row['stu_adr_id'])
            row['zone'] = helper_service.get_zone_by_id(row['stu_adr_id'])
            del row['stu_adr_id']
            order_row = collections.OrderedDict()
            order_row['stu_id'] = row['stu_id']
            order_row['stu_name'] = row['stu_name']
            order_row['stu_sex'] = row['stu_sex']
            order_row['stu_cid'] = row['stu_cid']
            order_row['stu_nation'] = row['stu_nation']
            order_row['stu_class'] = row['stu_class']
            order_row['stu_room'] = row['stu_room']
            order_row['stu_tel'] = row['stu_tel']
            order_row['province'] = row['province']
            order_row['city'] = row['city']
            order_row['zone'] = row['zone']
            order_row['stu_adr'] = row['stu_adr']
            order_row['stu_parent_name'] = row['stu_parent_name']
            order_row['stu_parent_relation'] = row['stu_parent_relation']
            order_row['stu_parent_tel'] = row['stu_parent_tel']
            order_row['stu_parent_name_vice'] = row['stu_parent_name_vice']
            order_row['stu_parent_relation_vice'] = row['stu_parent_relation_vice']
            order_row['stu_parent_tel_vice'] = row['stu_parent_tel_vice']
            order_res.append(order_row)

        sio = yield helper_service.generate_excel(order_res, thead=thead)
        self.write(sio.getvalue())
        self.finish()
        return

class GetStudentHandler(BaseHandler):
    @gen.coroutine
    @tornado.web.authenticated
    def post(self, *args, **kwargs):
        info = {'stu_id': self.get_argument('stu_id_filter'),
                'stu_sex': self.get_argument('stu_sex_filter'),
                'stu_room': self.get_argument('stu_room_filter'),
                'stu_nation': self.get_argument('stu_nation_filter'),
                'stu_adr_id': ("%s" % int(self.get_argument('stu_adr_id_filter')[::-1]))[::-1],
                'stu_class': self.get_argument('stu_class_filter')
                }
        res = yield get_stu(stu_info=info)
        self.write_json({'success': True, 'res': res})
        return

class StudentSubmitHandler(BaseHandler):
    @gen.coroutine
    @tornado.web.authenticated
    def post(self, *args, **kwargs):
        stu_id = self.get_argument('stu_id')
        stu_name = self.get_argument('stu_name')
        stu_sex = self.get_argument('stu_sex')
        stu_nation = self.get_argument('stu_nation')
        stu_tel = self.get_argument('stu_tel')
        stu_cid = self.get_argument('stu_cid')
        stu_adr = self.get_argument('stu_adr')
        stu_room = self.get_argument('stu_room')
        stu_class = self.get_argument('stu_class')
        stu_parent_name = self.get_argument('stu_parent_name')
        stu_parent_relation = self.get_argument('stu_parent_relation')
        stu_parent_tel = self.get_argument('stu_parent_tel')
        stu_parent_name_vice = self.get_argument('stu_parent_name_vice')
        stu_parent_relation_vice = self.get_argument('stu_parent_relation_vice')
        stu_parent_tel_vice = self.get_argument('stu_parent_tel_vice')
        stu_adr_id = self.get_argument('stu_adr_id')

        if stu_room == 'others':
            stu_room_new = self.get_argument('stu_room_new')
            room_id = yield student_service.add_room(stu_room_new)
            stu_room = room_id[0]['id']
        if stu_class == 'others':
            stu_class_new = self.get_argument('stu_class_new')
            class_id = yield student_service.add_class(stu_class_new)
            stu_class = class_id[0]['id']

        stu_info = {
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
            "stu_parent_tel_vice": stu_parent_tel_vice,
            "stu_adr_id": stu_adr_id
        }

        res = yield student_service.add_stu(stu_info)
        self.write_json({'success': True, 'message': res})
        return