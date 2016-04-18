# coding=utf-8
from handlers.apartment import ApartmentIndexHandler, ApartmentInputHandler, ApartmentSubDisIndexHandler
from handlers.helper import GetStuInfoByIdHandler
from handlers.index import IndexHandler
from handlers.user_auth import LoginHandler, LogoutHanlder

url_patterns = [

    # 公寓类
    (r'/apartment', ApartmentIndexHandler),
    (r'/apartment/dis_input', ApartmentInputHandler),
    (r'/apartment/sub_dis' , ApartmentSubDisIndexHandler),

    (r'/', IndexHandler),
    (r'/getStuInfoById', GetStuInfoByIdHandler),

    (r'/login', LoginHandler),
    (r'/logout', LogoutHanlder)
]
