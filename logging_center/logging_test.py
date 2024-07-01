import logging

# 配置日志记录器
logging.basicConfig(filename='app.log',level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')

def example_function():
    logging.debug("This is a debug message")
    logging.info("This is an info message")
    logging.warning("This is a warning message")
    logging.error("This is an error message")
    logging.critical("This is a critical message")

example_function()
