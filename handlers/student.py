# coding=utf-8
import tornado
from tornado import gen

from handlers.base import BaseHandler


class StudentManagerHandler(BaseHandler):
    @gen.coroutine
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render("/student/index.html")


class AddStudentHandler(BaseHandler):
    @gen.coroutine
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render("/student/stu_add.html")


class ShowStudentHandler(BaseHandler):
    @gen.coroutine
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render("/student/stu_show.html")
