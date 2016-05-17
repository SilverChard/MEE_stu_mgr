import tornado
from tornado import gen, web

from handlers.base import BaseHandler


class ApartmentSanitationAddHandler(BaseHandler):
    @gen.coroutine
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render('/apartment/sanitation_add.html')


class ApartmentSanitationShowHandler(BaseHandler):
    @gen.coroutine
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render('/apartment/sanitation_show.html')
