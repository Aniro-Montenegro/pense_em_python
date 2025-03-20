import time

class Time:
    def __init__(self):
        self.hour=None
        self.minute=None
        self.second=None

    def print_time(self,hour,minute,second):
        print('%.2d:%.2d:%.2d' % (hour, minute, second))

    def get_actual_time(self):
        tempo_atual = time.time()
        estrutura_tempo = time.localtime(tempo_atual)
        self.print_time(estrutura_tempo.tm_hour,estrutura_tempo.tm_min,estrutura_tempo.tm_sec)


time_objeto=Time()
time_objeto.get_actual_time()