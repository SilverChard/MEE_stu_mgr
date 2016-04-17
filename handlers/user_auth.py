# coding=utf-8
from tornado import gen
from tornado.web import MissingArgumentError

from handlers.base import BaseHandler
from services import login_service

__author__ = 'Silver'


class LoginHandler(BaseHandler):
    @gen.coroutine
    def get(self, *args, **kwargs):
        if self.current_user is not None:
            self.redirect("/")
            return
        try:
            self.get_argument('next')
            flag = 1
        except MissingArgumentError:
            flag = 0
        self.render('login.html', flag=flag)

    @gen.coroutine
    def post(self, *args, **kwargs):
        if self.current_user is not None:
            self.redirect("/")
            return

        try:
            user = self.get_argument('user')
            pwd = self.get_argument('pwd')
            res = yield login_service.check_user(user, pwd)
            if res[0]['check_flag'] == 1:
                self.set_secure_cookie('userName', res[0]['admin_name'])
                data_json = {
                    'success': True,
                    'userName': res[0]['admin_name']
                }
            else:
                data_json = {
                    'success': False,
                }
            self.write_json(data_json)
        except MissingArgumentError:
            pass


class LogoutHanlder(BaseHandler):
    @gen.coroutine
    def get(self, *args, **kwargs):
        self.clear_cookie('userName')
        self.redirect('/')
