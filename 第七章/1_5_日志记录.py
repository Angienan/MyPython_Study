"""通过官方发logging 模块来输出日志"""
import logging
logging.basicConfig(
    #INFO日志级别 : DEBUG,INFO,WARNING,ERROR,FATAL
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)