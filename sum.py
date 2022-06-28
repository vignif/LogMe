from MyLogger import Logger

log = Logger(__name__).logger

def sum(a, b):
    log.info(f'Sum of {a} and {b}')
    return a + b