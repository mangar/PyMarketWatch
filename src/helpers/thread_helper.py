import os
from datetime import datetime

class ThreadHelper(object):

    FILE_NAME = "thread_running.txt"

    def is_running() -> bool:
        if os.path.exists(ThreadHelper.FILE_NAME):
            # print("IS RUNNING TRUE")
            return True
        else:
            # print("IS RUNNING FALSE")
            return False


    def start_running() -> bool:
        with open(ThreadHelper.FILE_NAME, 'w') as file:
            file.write( f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n" )
        # print("START RUNNING")
        return True


    def stop_running() -> bool:
        try:
            os.remove(ThreadHelper.FILE_NAME)
        except FileNotFoundError as fe:
            print(f"STOP RUNNING .. FAIL: {fe}")
        # print("STOP RUNNING")
        return True