import logging.handlers
# 创建日志器对象


class generate_log():
    logger = None
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }#日志级别关系映射
    @classmethod
    def log(cls,files):
        if cls.logger is None:
            cls.logger = logging.getLogger('杨楷亮')
            #设置日志级别
            cls.logger.setLevel(logging.INFO)
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
            fm = logging.Formatter(fmt)
            tf = logging.handlers.TimedRotatingFileHandler(
                filename = files,
                when = 'H',
                backupCount = 10,
                encoding = 'utf-8'
            )
            tf.setFormatter(fm)
            # 给“处理器”设置级别
            tf.setLevel(cls.level_relations)
            cls.logger.addHandler(tf)
            #日志输出到控制台的写法
            ch = logging.StreamHandler()
            ch.setLevel(cls.level_relations)
            ch.setFormatter(fm)

            conslon = cls.logger.addHandler(ch)
            cls.logger.removeHandler(conslon)

        return cls.logger


if __name__ == '__main__':
    pass
    logger = generate_log().log(r'F:\ES\Data\report.log')
    logger.info('调试信息')
    logger.info('消息级别的调试信息')


