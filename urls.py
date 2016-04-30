# coding=utf-8
from handlers.apartment import ApartmentIndexHandler, ApartmentDisInputHandler, ApartmentSubDisIndexHandler, \
    ApartmentDisShowHandler, ApartmentDisGetHandler, ApartmentGetStuRoomHandler
from handlers.helper import GetStuInfoByIdHandler, GetRoomHandler, GetClassHandler
from handlers.index import IndexHandler
from handlers.student import StudentManagerHandler, AddStudentHandler, ShowStudentHandler
from handlers.user_auth import LoginHandler, LogoutHanlder

url_patterns = [

    # 公寓类
    (r'/apartment', ApartmentIndexHandler),
    (r'/apartment/dis_input', ApartmentDisInputHandler),
    (r'/apartment/sub_dis', ApartmentSubDisIndexHandler),
    (r'/apartment/dis_show', ApartmentDisShowHandler),
    (r'/apartment/get_dis', ApartmentDisGetHandler),
    (r'/apartment/get_stu_room', ApartmentGetStuRoomHandler),

    # 学生类
    (r'/stu_mgr', StudentManagerHandler),
    (r'/stu_mgr/stu_add', AddStudentHandler),
    (r'/stu_mgr/stu_show', ShowStudentHandler),

    # 公共类
    (r'/', IndexHandler),
    (r'/getStuInfoById', GetStuInfoByIdHandler),
    (r'/getStuRoom', GetRoomHandler),
    (r'/getStuClass', GetClassHandler),
    # 权限类
    (r'/login', LoginHandler),
    (r'/logout', LogoutHanlder)
]
