from tornado import gen
import database


@gen.coroutine
def check_user(user, pwd):
    cur = yield database.pool.execute(
        "SELECT admin_pwd=md5(sha(%s)) AS check_flag, admin_name  , admin_id AS id FROM admin WHERE admin_id=%s;",
        (pwd, user))
    rs = database.cur_to_dict(cur)
    raise gen.Return(rs)


