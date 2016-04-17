# coding= utf-8

import tornado
from tornado.web import MissingArgumentError
from tornado import gen
from handlers.base import BaseHandler
from services import helper_service


class GetStuInfoByIdHandler(BaseHandler):
    @tornado.web.authenticated
    @gen.coroutine
    def post(self, *args, **kwargs):
        sql_res = yield helper_service.get_stu_info_by_id(int(self.get_argument('stu_id')))
        try:
            stu_name = sql_res[0]['stu_name']
            stu_sex = sql_res[0]['stu_sex']
            wrt = {'success': True, 'stu_name': stu_name, 'stu_sex': stu_sex}
        except IndexError or MissingArgumentError:
            wrt = {'success': False, 'stu_name': '学号有误', 'stu_sex': '学号有误'}

        self.write_json(wrt)