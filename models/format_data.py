import datetime


def format_result(time, hour):
    """
    Funcion que lee la hora y el tiempo de la dosis y la da con el formato hh:mm
    """
    n = int(time/60)
    time += -n*60
    time = datetime.time(hour+n, time)
    return time


def text_warming(time, text):
    """
    Verifica si se cumple la dosis o si no existe riesgo
    """
    if int(str(time)[0:2]) >= 21:
        time = text
    return time


def date_format(date):
    year = (date)[0:4]
    month = (date)[5:7]
    day = (date)[8:10]
    date = day+"/"+month+"/"+year
    return date


def mm_dd_format(date):
    month = (date)[5:7]
    day = (date)[8:10]
    return month+"-"+day


def hour_format(hour_request):
    hour = int(hour_request[0:2])
    minute = int(hour_request[3:5])
    return hour, minute


class labels_formats:
    """
    Realiza el cambio de numero con el nombre correspondiente a
    cada valor
    """

    def __init__(self):
        self.phototypes = ["I", "II", "III", "IV", "V", "VI"]
        self.cloud_names = ["Despejado", "Medio nublado", "Nublado"]

    def obatin_phototype(self, number):
        """
        Obtiene el nombre del fototipo dependiendo del valor ingresado
        """
        self.phototype = self.phototypes[number]

    def obtain_cloud(self, number):
        """
        Obtiene el nombre de la condidcion del cielo dependiendo del valor ingresado
        """
        self.cloud = self.cloud_names[number]
