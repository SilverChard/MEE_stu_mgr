# coding=utf-8
import tornado

from handlers.base import BaseHandler
from tornado import gen,web

class HolidayIndexHandler(BaseHandler):
    @gen.coroutine
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render("/holiday/index.html")