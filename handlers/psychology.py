# coding=utf-8
import tornado
from tornado import gen,  web

from handlers.base import BaseHandler


class PsyIndexHandler(BaseHandler):
    @gen.coroutine
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render("/psychology/index.html")
