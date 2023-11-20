def setup_logger():
    
    logger = logging.getLogger('bs_server')
    logger.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
    
    file_handler = TimedRotatingFileHandler('/var/log/bs_server/bs_server.log', when='midnight', interval=1, backupCount=7)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger
