from datetime import datetime
from helpers import ExchangeHelper

def test_status_open():
    current_str = '2024-04-23 12:00:00'
    current = datetime.strptime(current_str, '%Y-%m-%d %H:%M:%S')
    assert "open" == ExchangeHelper.status("11:00", "17:00", current)    

def test_status_preopen():
    current_str = '2024-04-23 10:55:00'
    current = datetime.strptime(current_str, '%Y-%m-%d %H:%M:%S')
    assert "preopen" == ExchangeHelper.status("11:00", "17:00", current)


def test_status_close_before_open():
    current_str = '2024-04-23 10:00:00'
    current = datetime.strptime(current_str, '%Y-%m-%d %H:%M:%S')
    assert "close" == ExchangeHelper.status("11:00", "17:00", current)    

def test_status_close_after_close():
    current_str = '2024-04-23 17:01:00'
    current = datetime.strptime(current_str, '%Y-%m-%d %H:%M:%S')
    assert "close" == ExchangeHelper.status("11:00", "17:00", current)    

def test_status_preclose():
    current_str = '2024-04-23 16:30:00'
    current = datetime.strptime(current_str, '%Y-%m-%d %H:%M:%S')
    assert "preclose" == ExchangeHelper.status("11:00", "17:00", current)    
