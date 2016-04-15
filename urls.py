# coding=utf-8
from handlers.apartment import ApartmentIndexHandler, ApartmentInputHandler
from handlers.index import IndexHandler
from handlers.user_auth import LoginHandler, LogoutHanlder

url_patterns = [

    # 公寓类
    (r'/apartment', ApartmentIndexHandler),
    (r'/apartment/input', ApartmentInputHandler),

    (r'/', IndexHandler),

    (r'/login', LoginHandler),
    (r'/logout', LogoutHanlder)
]
