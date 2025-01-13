import os

#获取环境变量
ENV = os.environ.get('ENV')
if ENV == 'production':
    #生产环境
    from .prod import *
else:
    from .dev import *