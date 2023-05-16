from domain.models.enums.diasSemanaEnum import DiasSemanaEnum


class HorarioModel:
    diaSemana:DiasSemanaEnum = None
    horaInicio:str = ""
    horaFin:str = ""

    def __init__(self, diaSemana:DiasSemanaEnum, horaInicio:str, horaFin:str): # diaSemana:DiasSemanaEnum, horaInicio:str, horaFin:str
        self.diaSemana = diaSemana
        self.horaInicio = horaInicio
        self.horaFin = horaFin