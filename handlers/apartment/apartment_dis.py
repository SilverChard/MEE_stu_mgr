# coding=utf-8
import tornado
from tornado import web, gen

from handlers.base import BaseHandler
from services import helper_service
from services.apartment import apartment_services

__author__ = 'Silver'


class ApartmentDisInputHandler(BaseHandler):
    @tornado.web.authenticated
    @gen.coroutine
    def get(self, *args, **kwargs):
        self.render('/apartment/dis_input.html')


class ApartmentSubDisIndexHandler(BaseHandler):
    @tornado.web.authenticated
    @gen.coroutine
    def post(self, *args, **kwargs):
        stu_id = self.get_argument('stu_id')
        dis_type = self.get_argument('dis_type')
        dis_class = self.get_argument('dis_class')
        dis_date = self.get_argument('dis_date')
        others = self.get_argument('others')

        dis_data = {
            "stu_id": stu_id,
            "type": dis_type,
            "dis_class": dis_class,
            "others": others,
            "dis_date": dis_date
        }

        res = yield apartment_services.insert_dis(dis_data)
        print res
        wrt = {
            'success': True,
        }
        self.write_json(wrt)


class ApartmentDisShowHandler(BaseHandler):
    @gen.coroutine
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render('/apartment/dis_show.html')


class ApartmentGetDisClassHandler(BaseHandler):
    @gen.coroutine
    @tornado.web.authenticated
    def post(self, *args, **kwargs):
        dis_type = self.get_argument('dis_type')
        res = yield apartment_services.get_dis_class_by_type(dis_type)
        self.write_json({'success': True, 'dis_class': res})


class ApartmentDisGetHandler(BaseHandler):
    @gen.coroutine
    @tornado.web.authenticated
    def post(self, *args, **kwargs):
        info = {
            "stu_sex": self.get_argument('stu_sex'),
            "stu_id": self.get_argument('stu_id'),
            "stu_room": self.get_argument('stu_room'),
            "dis_type": self.get_argument('dis_type'),
            "dis_class": self.get_argument('dis_class')
        }

        res = yield apartment_services.get_dis(info)
        wrt = {'success': True, 'dis_info': res}
        self.write_json(wrt)


class ApartmentDisUpdateHandler(BaseHandler):
    @gen.coroutine
    @tornado.web.authenticated
    def post(self, *args, **kwargs):
        if (yield helper_service.check_stu_id_exist(self.get_argument('stu_id'))):
            info = {
                "dis_id": self.get_argument('dis_id'),
                "stu_id": self.get_argument('stu_id'),
                "dis_type": self.get_argument('dis_type'),
                "dis_class": self.get_argument('dis_class'),
                "dis_date": self.get_argument('dis_date'),
                "dis_others": self.get_argument('dis_others')
            }
            apartment_services.update_dis(info)
            wrt_json = {'success': True, 'msg': '修改成功'}
        else:
            wrt_json = {'success': True, 'msg': '请认真确认学号是否正确'}
        self.write_json(wrt_json)


class ApartmentDisDelHandler(BaseHandler):
    @gen.coroutine
    @tornado.web.authenticated
    def post(self, *args, **kwargs):
        dis_id = self.get_argument('dis_id')
        apartment_services.del_dis(dis_id)
        self.write_json({'success': True})
        return
