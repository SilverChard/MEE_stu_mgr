# coding=utf-8
from handlers.apartment.apartment_dis import ApartmentDisInputHandler, ApartmentSubDisIndexHandler, \
    ApartmentDisShowHandler, ApartmentDisGetHandler, ApartmentGetStuRoomHandler
from handlers.apartment.apartment import ApartmentIndexHandler
from handlers.apartment.apartment_sanitation import ApartmentSanitationAddHandler, ApartmentSanitationShowHandler
from handlers.helper import GetStuInfoByIdHandler, GetRoomHandler, GetClassHandler
from handlers.holiday import HolidayIndexHandler
from handlers.index import IndexHandler
from handlers.psychology import PsyIndexHandler
from handlers.stu_class import ClassIndexHandler
from handlers.student import StudentIndexHandler, AddStudentHandler, ShowStudentHandler, StudentSubmitHandler, \
    GetStudentHandler, DownloadStudentInfoHandler, EditStudentInfoHandler, DeleteStudentHandler
from handlers.user_auth import LoginHandler, LogoutHanlder

url_patterns = [

    # 公寓类
    (r'/apartment', ApartmentIndexHandler),
    # 公寓违纪类
    (r'/apartment/dis_input', ApartmentDisInputHandler),
    (r'/apartment/sub_dis', ApartmentSubDisIndexHandler),
    (r'/apartment/dis_show', ApartmentDisShowHandler),
    (r'/apartment/get_dis', ApartmentDisGetHandler),
    (r'/apartment/get_stu_room', ApartmentGetStuRoomHandler),
    # 公寓卫生类
    (r'/apartment/sanitation_add', ApartmentSanitationAddHandler),
    (r'/apartment/sanitation_show', ApartmentSanitationShowHandler),

    # 课堂管理类
    (r'/class', ClassIndexHandler),

    # 心理测评类
    (r'/psy', PsyIndexHandler),

    # 节假日管理类 注意 部分节假日是不需要验证用户信息的
    (r'/holiday', HolidayIndexHandler),

    # 学生类
    (r'/stu_mgr', StudentIndexHandler),
    (r'/stu_mgr/stu_add', AddStudentHandler),
    (r'/stu_mgr/stu_show', ShowStudentHandler),
    (r'/stu_mgr/stu_submit', StudentSubmitHandler),
    (r'/stu_mgr/get_stu', GetStudentHandler),
    (r'/stu_mgr/download_stu_info', DownloadStudentInfoHandler),
    (r'/stu_mgr/stu_edit', EditStudentInfoHandler),
    (r'/stu_mgr/stu_del', DeleteStudentHandler),

    # 公共类
    (r'/', IndexHandler),
    (r'/getStuInfoById', GetStuInfoByIdHandler),
    (r'/getStuRoom', GetRoomHandler),
    (r'/getStuClass', GetClassHandler),

    # 权限类
    (r'/login', LoginHandler),
    (r'/logout', LogoutHanlder)
]
