# coding=utf-8
import tornado
from tornado import web

from handlers.base import BaseHandler

__author__ = 'Silver'


class IndexHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render('index.html')

    @tornado.web.authenticated
    def post(self, *args, **kwargs):
        self.render('index.html')


