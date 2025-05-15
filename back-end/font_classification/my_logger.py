import logging

def set_logger(name, log_save_path):
    mylogger = logging.getLogger(name)
    mylogger.setLevel(level=logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

    file_handler = logging.FileHandler(log_save_path)
    file_handler.setLevel(level=logging.INFO)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)

    mylogger.addHandler(file_handler)
    mylogger.addHandler(stream_handler)

    return mylogger