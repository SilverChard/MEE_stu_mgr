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
        self.render('/apartment/input.html')