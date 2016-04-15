import base64
import uuid
import os

settings = {
    'template_path': os.path.join(os.path.dirname(__file__), "templates"),
    'static_path': os.path.join(os.path.dirname(__file__), "static"),
    'ports': 8888,
    'debug': True,
    'login_url': '/login',
    'cookie_secret': 'g+BZ3nY5T8qO5RheV0++u+sJ8M7F20FWnU61VipoyNA=',
    'xsrf_cookies': False,
}

mysql_db_host = '192.168.1.7'
mysql_db_port = 3306
mysql_db_user = 'root'
mysql_db_pass = 'silver'
mysql_db_database = 'mee_stu_mgr'
