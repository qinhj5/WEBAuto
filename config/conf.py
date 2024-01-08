# -*- coding: utf-8 -*-
from utils import get_conf
from connection.mysql_connection import MysqlConnection


class Constants:
    _GOOGLE_CONF = get_conf(name="google")
    GOOGLE_LOGIN_URL = _GOOGLE_CONF["login_url"]


class Global:
    constants = Constants()
    db = MysqlConnection()
