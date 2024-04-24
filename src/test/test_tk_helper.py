from helpers import TkHelper

def test_get_label_name__ok():
    current_str = '2024-04-23 12:00:00'
    assert current_str.replace(" ", "") == TkHelper.get_label_name(current_str)

    current_str = 'HORA AGORA 2024-04-23 12:00:00'
    assert current_str.lower().replace(" ", "") == TkHelper.get_label_name(current_str)

