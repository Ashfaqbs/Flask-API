import logging

class Config:
    PORT = 3031
    LOGGING_LEVEL = logging.INFO
    LOG_FILE = 'logs/app.log'

    @staticmethod
    def init_app(app):
        logging.basicConfig(filename=Config.LOG_FILE, level=Config.LOGGING_LEVEL)
