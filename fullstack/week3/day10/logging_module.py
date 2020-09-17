# import logging   #18-06
# logging.debug("hello world")
# logging.info("苍井空")
# logging.warning("波多野结衣")
# logging.error("小泽玛利亚")
# logging.critical("最喜欢吉泽明步")
#CRITICAL > ERROR > WARNING > INFO > DEBUG  默认是warning及以上输出

#设置输出级别和格式
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
#                     datefmt="%a,%d %b %Y %H:%M:%S",    #lineno  表示行号
#                     #filename="test.py",   #表示输出方式 默认输出到控制台，这指定输出到的文档
#                     filemode="w")     #表示读写方式有可以写成"a"
# logging.debug("hello world")
# logging.info("苍井空")
# logging.warning("波多野结衣")
# logging.error("小泽玛利亚")
# logging.critical("最喜欢吉泽明步")

#既输出到控制台又能输出到文件
import logging
#logger 是模块级别的函数
logger = logging.getLogger()

#设置输出级别
logger.setLevel(logging.DEBUG)

#创建一个handler,用于输出日志文件
fh = logging.FileHandler("test.py")
#创建一个handler，用于输出到控制台
ch = logging.StreamHandler()

formatter=logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)

logger.debug("hello world")
logger.info("苍井空")
logger.warning("波多野结衣")
logger.error("小泽玛利亚")
logger.critical("最喜欢吉泽明步")

