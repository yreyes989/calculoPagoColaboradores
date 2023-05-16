from application.dtos.horarioDto import HorarioDTO


class DetallePagoEmpleadoDTO:
    nombreEmpleado = ""
    horario = [HorarioDTO]
    def __init__(self, nombreEmpleado, horario):
        self.nombreEmpleado = nombreEmpleado
        self.horario = horario
