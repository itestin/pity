# 基础配置类
import os


class Config(object):
    ROOT = os.path.dirname(os.path.abspath(__file__))
    LOG_NAME = os.path.join(ROOT, 'logs', 'pity.log')
    JSON_AS_ASCII = False  # Flask jsonify编码问题

    # MySQL连接信息
    MYSQL_HOST = "127.0.0.1"
    MYSQL_PORT = 3306
    MYSQL_USER = "root"
    MYSQL_PWD = "wuranxu@33"
    DBNAME = "pity"

    # sqlalchemy
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{}:{}@{}:{}/{}'.format(
                                    MYSQL_USER, MYSQL_PWD, MYSQL_HOST, MYSQL_PORT, DBNAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = False