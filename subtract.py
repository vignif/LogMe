from MyLogger import LoggerFromConfig

log = LoggerFromConfig.logger

def subtract(a, b):
    log.info(f'Subtracting {a} from {b}')
    return a - b