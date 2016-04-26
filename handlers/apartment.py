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


class ApartmentDisInputHandler(BaseHandler):
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
            'success': True,
        }
        self.write_json(wrt)


class ApartmentDisShowHandler(BaseHandler):
    @gen.coroutine
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        dis_num = yield apartment_services.count_dis()
        dis_num = dis_num[0]['num']
        self.render('/apartment/dis_show.html', dis_num=dis_num)


class ApartmentGetStuRoomHandler(BaseHandler):
    @gen.coroutine
    @tornado.web.authenticated
    def post(self, *args, **kwargs):
        info = {
            "stu_sex": int(self.get_argument('stu_sex')),
            "stu_id": int(self.get_argument('stu_id')),
            "dis_type": int(self.get_argument('dis_type')),
            "dis_class": int(self.get_argument('dis_class'))
        }
        res = yield apartment_services.get_room(info)
        wrt = {'success': True, 'room_info': res}
        self.write_json(wrt)


class ApartmentDisGetHandler(BaseHandler):
    @gen.coroutine
    @tornado.web.authenticated
    def post(self, *args, **kwargs):
        page_start = int(self.get_argument('page_start'))
        info = {
            "page_offset": int(self.get_argument('page_offset')),
            "stu_sex": int(self.get_argument('stu_sex')),
            "stu_id": int(self.get_argument('stu_id')),
            "stu_room":self.get_argument('stu_room'),
            "dis_type": int(self.get_argument('dis_type')),
            "dis_class": int(self.get_argument('dis_class'))
        }
        if info['stu_room'] == "0":
            info['stu_room'] = 0
        res = yield apartment_services.get_dis(page_start, info)
        wrt = {'success': True, 'table_info': res}
        self.write_json(wrt)
