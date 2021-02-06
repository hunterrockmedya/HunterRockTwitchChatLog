import logging, os
import logging.config

class Log():
    def __init__(self, main_file):
        here = os.path.abspath(os.path.dirname(main_file))
        this_file = os.path.basename(main_file)
        
        max_name_size = 4
        for fname in os.listdir(here):
            if fname.endswith(".py") and fname != this_file:
                if max_name_size + 3 < len(fname):
                    max_name_size = len(fname) - 3

        if "PYTHON_LOGGING_CONFIG" in os.environ:
            logging.config.fileConfig(os.environ.get("PYTHON_LOGGING_CONFIG"), defaults={"logfilename": this_file.replace(".py", ".log")})
        else:
            logging.basicConfig(level=logging.INFO, format=f'[%(asctime)s] [%(name)-{max_name_size}s] [%(levelname)-8s] - %(message)s')