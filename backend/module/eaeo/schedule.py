import time
from datetime import datetime
from module.eaeo import constant as mcs
from module.eaeo import common as mcm
from module.eaeo import logging as lgg

def instagram_sync_scheduler():
    while 1:
        lgg._logging("====> task started", 1, 1)
        time.sleep(mcs.instagram_sync_period)
        now = datetime.now()
        weekday = now.weekday()
        hour = now.hour
        # 0 o'clock on Saturday
        if weekday != 5 or hour != 0:
            continue

        lgg._logging("====> start syncing", 1, 1)
        res = mcm.scheduled_sync_instagram_accounts()
        lgg._logging("====> syncing ended", 1, 1)
        if res == 1:
            lgg._logging("====> success to sync all", 1, 1)
        else:
            lgg._logging("====> fail to sync one of handles", 1, 1)