"""_summary_
python 3.8.10
"""

from MyLogger import Logger
from MyLogger import LoggerFromConfig
from sum import sum
from subtract import subtract

def fun1():
    log1.info("Hi!")

def fun2():
    log2.info("Hi!")

if __name__ == '__main__':
    log1 = Logger(__name__).logger
    log2 = LoggerFromConfig.logger
    fun1()
    fun2()
    log1.info(sum(2, 3))
    log2.debug(subtract(5, 4))
