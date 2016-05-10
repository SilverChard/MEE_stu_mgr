import tornado
from tornado import gen

from handlers.base import BaseHandler


class ClassIndexHandler(BaseHandler):
    @gen.coroutine
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render("/stu_class/index.html")