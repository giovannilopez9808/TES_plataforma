from .format_data import *
from flask import request
import pandas as pd
import datetime


class Data_TES:
    """
    Busca la informacion de las dosis en los archivos y los prepara con el formato
    """

    def __init__(self, request):
        self.request = request
        self.get_initial_data()

    def get_initial_data(self):
        self.treatment = self.request.form["treatment"]
        self.date = self.request.form["date"]
        self.index = self.request.form["hour"]
        self.hour, self.minute = hour_format(self.index)
        self.skin = int(self.request.form["skin"])

    def get_final_data(self):
        self.get_initial_data()
        self.n_cloud = int(self.request.form["cloud"])
        self.header = mm_dd_format(self.date)
        self.date = date_format(self.date)
        self.search_data()
        self.labels.obtain_cloud(self.n_cloud)

    def search_data(self):
        """
        Recolenta la información dependiendo de los datos obtenidos de la request de la página
        """
        self.labels = labels_formats()
        self.labels.obatin_phototype(self.skin)
        name_dosis = "Data/dosis_{}_{}.csv".format(self.treatment,
                                                   self.n_cloud)
        name_phototype = "Data/Max_{}_{}.csv".format(self.labels.phototype,
                                                     self.n_cloud)
        # Se suma 2 a la dosis para tener un rango efectivo
        self.time_dosis = int(pd.read_csv(name_dosis,
                                          index_col=0)
                              [self.header][self.index]+2+self.minute)
        self.time_max = int(pd.read_csv(name_phototype,
                                        index_col=0)
                            [self.header][self.index]+2+self.minute)
        # Da formato a el tiempo maximo y de dosis
        self.time_max = format_result(self.time_max,
                                      self.hour)
        self.time_dosis = format_result(self.time_dosis,
                                        self.hour)
        self.time_dosis = text_warming(self.time_dosis,
                                       "No se completará la dosis")
        self.time_max = text_warming(self.time_max,
                                     "Sin riesgo")
