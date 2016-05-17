import tornado
from tornado import gen,web

from handlers.base import BaseHandler


class ApartmentIndexHandler(BaseHandler):
    @tornado.web.authenticated
    @gen.coroutine
    def get(self, *args, **kwargs):
        self.render('/apartment/index.html')
