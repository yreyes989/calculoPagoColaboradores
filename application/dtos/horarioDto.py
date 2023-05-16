from domain.models.horarioModel import HorarioModel

class HorarioDTO:
    horario:HorarioModel = None
    
    def __init__(self, horario:HorarioModel):
        self.horario = horario

    def getHoraInicio(self) -> int:
        return int(self.horario.horaInicio[0:2])
    def getHoraFin(self) -> int:
        return int(self.horario.horaFin[0:2])
    
    def getMinutosInicio(self) -> int:
        return int(self.horario.horaInicio[3:4])
    def getMinutosFin(self) -> int:
        return int(self.horario.horaFin[3:4])