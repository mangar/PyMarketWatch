from datetime import datetime, time, timedelta


class DateTimeHelper(object):

    def full_date_today() -> str:       
        data_formatada = datetime.today().strftime('%A, %d de %B de %Y')
        return data_formatada


    def diff_now(time2):
        """
        diferenca em minutos da data e hora atual com 'time2'
        """
        _times = time2.split(':')
        _time = time( int(_times[0]), int(_times[1]), 0)

        abertura = datetime.combine(datetime.now().date(), _time)
        # print(abertura)

        return DateTimeHelper.diff(datetime.now(), abertura)


    def diff(data1, data2):
        diferenca = data2 - data1
        return diferenca.total_seconds()

    def format_diff(total_segundos):
        minutos, segundos = divmod(total_segundos, 60)
        tempo_formatado = f"{int(minutos):02}:{int(segundos):02}"  
        return tempo_formatado 


    def format_diff_now(time2):

        _times = time2.split(':')
        _time = time( int(_times[0]), int(_times[1]), 0)

        abertura = datetime.combine(datetime.now().date(), _time)
        abertura_sec = DateTimeHelper.diff(datetime.now(), abertura)

        minutos, segundos = divmod(abertura_sec, 60)
        tempo_formatado = f"{int(minutos):02}:{int(segundos):02}"  
        return tempo_formatado 


    def is_exact_hour_min(hour_min = "10:00", current = None) -> bool:
        """ 
        """
        current = datetime.now() if current == None else current

        h = int(hour_min.split(":")[0])
        m = int(hour_min.split(":")[1])
        s = 0

        return current.hour == h and current.minute == m and current.second == s


    def is_pre_hour_min(hour_min = "10:00", current = None, previous_min=10) -> bool:
        """ 
        """
        current = datetime.now() if current == None else current
        abertura = datetime.combine(current, time( int(hour_min.split(":")[0]), int(hour_min.split(":")[1]), 0))
        abertura = abertura - timedelta(minutes=previous_min)

        h = abertura.hour
        m = abertura.minute
        s = 0

        return current.hour == h and current.minute == m and current.second == s