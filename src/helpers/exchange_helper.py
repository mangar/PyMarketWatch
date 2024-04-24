import asyncio
from datetime import datetime, time
from helpers import DateTimeHelper
from .sound_helper import SoundHelper

class ExchangeHelper(object):

    STATUS = {
        "open": "green",
        "close": "gray",
        "preopen": "yellow",
        "preclose": "yellow",
    }


    def status(open, close, current = None) -> str:
        """
        open = current > open and current <= close
        preopen = current < open and 10 minutes before open        
        preclosed = current > open and current <= close and 10 min before close
        closed = current < open and current > close
        return: preopen|open|preclosed|closed|not_defined
        """
        status = "not_defined"
        current = datetime.now() if current == None else current

        try:
            _time = time( int(open.split(':')[0]), int(open.split(':')[1]), 0)
            open_d = datetime.combine(current.date(), _time)

            _time = time( int(close.split(':')[0]), int(close.split(':')[1]), 0)
            close_d = datetime.combine(current.date(), _time)


            diff_open_sec = open_d - current          
            diff_open_sec = diff_open_sec.total_seconds()

            if current >= open_d and current <= close_d:

                diff_close_sec = close_d - current
                diff_close_sec = diff_close_sec.total_seconds()

                if (diff_close_sec / 60) <= 10:
                    return "preclose"

                return "open"

            if current < open_d and (diff_open_sec / 60) <= 10:
                return "preopen"

            if (current < open_d and (diff_open_sec / 60) > 10) or \
                (current >= close_d):

                return "close"


        except Exception as e:
            print(f"Erro: {e}")

        return status


    def status_color(status = "open") -> str:
        return ExchangeHelper.STATUS.get(status)
        



