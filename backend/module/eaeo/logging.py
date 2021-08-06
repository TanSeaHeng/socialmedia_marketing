from django.conf import settings
import os
import sys
from datetime import datetime
from sty import fg, bg, ef, rs

def _logging(msg= None, type = 0, level = 0):
    if type == 0:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        msg = bg.red
        msg += str(exc_obj) + ", File: " + str(exc_tb.tb_frame.f_code.co_filename) + ", Line: " + str(exc_tb.tb_lineno)
        msg += bg.rs
        msg += "\n"
    else:
        if level == 0:
            title = 'ERROR'
        else:
            title = 'INFO'
        msg = "EAEO [" + str(datetime.now()) + "] [" + title + "] " + msg + "\n"

    log_file = os.path.join(settings.BASE_DIR, 'eaeo.log')
    f = open(log_file, 'a')
    f.write(msg)
    f.close()
    return 1