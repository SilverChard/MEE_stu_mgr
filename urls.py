# coding=utf-8
from handlers.apartment.apartment_dis import ApartmentDisInputHandler, ApartmentSubDisIndexHandler, \
    ApartmentDisShowHandler, ApartmentDisGetHandler, ApartmentGetDisClassHandler, ApartmentDisUpdateHandler, \
    ApartmentDisDelHandler
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
    (r'/apartment', ApartmentIndexHandler),  # 公寓类 index页面
    # 公寓违纪类
    (r'/apartment/dis_input', ApartmentDisInputHandler),  # 录入违纪页面
    (r'/apartment/sub_dis', ApartmentSubDisIndexHandler),  # 提交url ajax
    (r'/apartment/dis_show', ApartmentDisShowHandler),  # 违纪展示页面
    (r'/apartment/get_dis', ApartmentDisGetHandler),  # 获取违纪url ajax
    (r'/apartment/get_dis_class', ApartmentGetDisClassHandler),  # 根据'type'获取'dis_class'与'dis_class_id'对应键值对 ajax
    (r'/apartment/dis_update', ApartmentDisUpdateHandler),  # 更新违纪信息 ajax
    (r'/apartment/dis_del', ApartmentDisDelHandler),  # 删除指定违纪记录 ajax
    # 公寓卫生类
    (r'/apartment/sanitation_add', ApartmentSanitationAddHandler),  # 添加卫生情况页面
    (r'/apartment/sanitation_show', ApartmentSanitationShowHandler),  # 展示卫生情况页面

    # 课堂管理类
    (r'/class', ClassIndexHandler),  # 课堂类 index页面

    # 心理测评类
    (r'/psy', PsyIndexHandler),  # 心理类 index页面

    # 节假日管理类 注意 部分节假日是不需要验证用户信息的
    (r'/holiday', HolidayIndexHandler),  # 节假日类 index页面

    # 学生类
    (r'/stu_mgr', StudentIndexHandler),  # 学生类 index页面
    (r'/stu_mgr/stu_add', AddStudentHandler),  # 添加学生信息页面
    (r'/stu_mgr/stu_show', ShowStudentHandler),  # 展示学生信息页面
    (r'/stu_mgr/stu_submit', StudentSubmitHandler),  # 学生信息提交url ajax
    (r'/stu_mgr/get_stu', GetStudentHandler),  # 获取学生信息url ajax
    (r'/stu_mgr/download_stu_info', DownloadStudentInfoHandler),  # 学生信息下载(excel)页面
    (r'/stu_mgr/stu_edit', EditStudentInfoHandler),  # 修改学生信息url ajax
    (r'/stu_mgr/stu_del', DeleteStudentHandler),  # 删除学生信息url ajax

    # 公共类
    (r'/', IndexHandler),
    (r'/getStuInfoById', GetStuInfoByIdHandler),  # 通过id获取学生信息url ajax
    (r'/getStuRoom', GetRoomHandler),  # 获取宿舍信息url ajax
    (r'/getStuClass', GetClassHandler),  # 获取班级信息url ajax

    # 权限类
    (r'/login', LoginHandler),  # 登录页面
    (r'/logout', LogoutHanlder)  # 退出url ajax
]
