from datetime import datetime
from helpers import DateTimeHelper

def test_is_pre_hour_min__OK():
    current_str = '2024-04-23 11:30:00'
    current = datetime.strptime(current_str, '%Y-%m-%d %H:%M:%S')
    assert DateTimeHelper.is_pre_hour_min("12:00", current)

def test_is_pre_hour_min__NOK_before():
    current_str = '2024-04-23 11:29:00'
    current = datetime.strptime(current_str, '%Y-%m-%d %H:%M:%S')
    assert not DateTimeHelper.is_pre_hour_min("12:00", current)

def test_is_pre_hour_min__NOK_after():
    current_str = '2024-04-23 11:30:01'
    current = datetime.strptime(current_str, '%Y-%m-%d %H:%M:%S')
    assert not DateTimeHelper.is_pre_hour_min("12:00", current)