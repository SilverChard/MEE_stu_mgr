# coding=utf-8
import tornado
from tornado import gen

from handlers.base import BaseHandler
from services.student import student_service


class StudentManagerHandler(BaseHandler):
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
            "stu_parent_tel_vice": stu_parent_tel_vice
        }

        res = yield student_service.add_stu(stu_info)
        self.write_json({'success': True, 'message': res})

