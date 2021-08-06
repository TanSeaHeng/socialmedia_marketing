from django.core.management.base import BaseCommand
from module.eaeo import schedule as sch
from module.eaeo import constant as mcs
from module.eaeo import common as mcm
import threading
from module.eaeo import logging as lgg

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass
    def handle(self, *args, **options):
        #initial sync
        lgg._logging("Initial auto-sync started", 1, 1)
        mcm.manual_sync_instagram_accounts()

        if mcs.auto_sync:
            lgg._logging("Scheduler started", 1, 1)
            th = threading.Thread(target=sch.instagram_sync_scheduler())
            th.start()

