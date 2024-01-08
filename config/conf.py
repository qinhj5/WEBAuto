# -*- coding: utf-8 -*-
from utils import get_conf, MysqlConnection


class Constants:
    _GOOGLE_CONF = get_conf(name="google")
    GOOGLE_LOGIN_URL = _GOOGLE_CONF["login_url"]


class Global:
    constants = Constants()
    db = MysqlConnection()
