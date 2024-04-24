from datetime import datetime
from helpers import ThreadHelper

def test_is_running__OK():
    current_str = '2024-04-23 12:00:00'
    current = datetime.strptime(current_str, '%Y-%m-%d %H:%M:%S')
    assert "open" == ExchangeHelper.status("11:00", "17:00", current)    

