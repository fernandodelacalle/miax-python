import logging

def config_logging():
    log_format = ('%(asctime)s %(name)s.%(funcName)s[%(process)d] '
                      '%(levelname)s %(message)s')
    handlers = list()
    handlers.append(logging.StreamHandler())
    logging.basicConfig(level=logging.INFO,
                        format=log_format,
                        handlers=handlers)
