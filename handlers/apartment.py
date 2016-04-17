# coding=utf-8
import tornado
from tornado import web

from handlers.base import BaseHandler

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
    def post(self, *args, **kwargs):
        stu_id = self.get_argument('stu_id')
        dis_type = self.get_argument('dis_type')
        dis_2 = self.get_argument('dis_2')
        others = self.get_argument('others')

        if dis_type == 'dis_item':
            dis_type = "1"
        elif dis_type == 'dis_behavior':
            dis_type = "2"

        dis_data={
            "stu_id" : stu_id,
            "type" : dis_type,
            "dis_class": dis_2,
            "others":others
        }



