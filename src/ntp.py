import ntplib
from time import ctime

def get_ntp_time(ntp_server):
    try:
        client = ntplib.NTPClient()
        response = client.request(ntp_server, version=3)
        ntp_time = ctime(response.tx_time)
        return ntp_time
    except Exception as e:
        return f"Failed to get NTP time: {e}"

# Usando o servidor NTP brasileiro
print(get_ntp_time('pool.ntp.br'))