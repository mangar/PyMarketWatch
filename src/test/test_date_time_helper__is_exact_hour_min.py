from datetime import datetime
from helpers import DateTimeHelper

def test_is_exact_hour_min():
    current_str = '2024-04-23 12:00:00'
    current = datetime.strptime(current_str, '%Y-%m-%d %H:%M:%S')
    assert DateTimeHelper.is_exact_hour_min("12:00", current)

