# coding=utf-8
import tornado
from tornado import web
from tornado.web import gen
from handlers.base import BaseHandler
from services.apartment import apartment_services

__author__ = 'Silver'


class ApartmentIndexHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render('/apartment/index.html')


class ApartmentInputHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render('/apartment/dis_input.html')


class ApartmentSubDisIndexHandler(BaseHandler):
    @tornado.web.authenticated
    @gen.coroutine
    def post(self, *args, **kwargs):
        stu_id = self.get_argument('stu_id')
        dis_type = self.get_argument('dis_type')
        dis_2 = self.get_argument('dis_2')
        dis_date = self.get_argument('dis_date')
        others = self.get_argument('others')

        if dis_type == 'dis_item':
            dis_type = "1"
        elif dis_type == 'dis_behavior':
            dis_type = "2"

        dis_data = {
            "stu_id": stu_id,
            "type": dis_type,
            "dis_class": dis_2,
            "others": others,
            "dis_date": dis_date
        }

        res = yield apartment_services.insert_dis(dis_data)
        print res
        wrt = {
            'success':True,
        }
        self.write_json()
