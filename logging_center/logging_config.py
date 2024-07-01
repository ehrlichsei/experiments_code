# logging_config.py

import logging

# 设置全局日志级别为 DEBUG
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')
