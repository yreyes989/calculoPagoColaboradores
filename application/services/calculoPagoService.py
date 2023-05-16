from application.dtos.horarioDto import HorarioDTO
from application.repositories.pagoRepository import PagoRepository
from domain.models.enums.diasSemanaEnum import DiasSemanaEnum
from domain.models.horarioModel import HorarioModel
from domain.models.resultadoCalculo import ResultadoCalculo
from utils.util import Utils


class CalculoPagoService:
    pagoRepository:PagoRepository = None

    def __init__(self):
        self.pagoRepository = PagoRepository

    def calcularMontoPorHorario(self, horario:HorarioModel, mostrarDetalle = False):
        totalPago = 0
        horasTrabajadas = 0
        precioPorHora = 0
        horarioDto = HorarioDTO(horario)
        if horario.diaSemana.value in DiasSemanaEnum.LABORALES.value:
            if horarioDto.getHoraInicio() >= 0 and horarioDto.getHoraFin() <= 9 and horarioDto.getMinutosInicio() >= 0 and horarioDto.getMinutosFin() <= 59:
                horasTrabajadas = (horarioDto.getHoraFin() - horarioDto.getHoraInicio())
                precioPorHora = 25
            elif horarioDto.getHoraInicio() >= 9 and horarioDto.getHoraFin() <= 18 and horarioDto.getMinutosInicio()>=0 and horarioDto.getMinutosFin() <= 59:
                horasTrabajadas = (horarioDto.getHoraFin() - horarioDto.getHoraInicio())
                precioPorHora = 15
            elif horarioDto.getHoraInicio() >= 18 and horarioDto.getHoraFin() <= 24 and horarioDto.getMinutosInicio()>=0 and horarioDto.getMinutosFin() <= 59:
                horasTrabajadas = (horarioDto.getHoraFin() - horarioDto.getHoraInicio())
                precioPorHora = 20
        elif horario.diaSemana.value in DiasSemanaEnum.NO_LABORALES.value:
            if horarioDto.getHoraInicio() >= 0 and horarioDto.getHoraFin() <= 9 and horarioDto.getMinutosInicio()>=0 and horarioDto.getMinutosFin() <= 59:
                horasTrabajadas = (horarioDto.getHoraFin() - horarioDto.getHoraInicio())
                precioPorHora = 30
            elif horarioDto.getHoraInicio() >= 9 and horarioDto.getHoraFin() <= 18 and horarioDto.getMinutosInicio()>=0 and horarioDto.getMinutosFin() <= 59:
                horasTrabajadas = (horarioDto.getHoraFin() - horarioDto.getHoraInicio())
                precioPorHora = 20
            elif horarioDto.getHoraInicio() >= 18 and horarioDto.getHoraFin() <= 24 and horarioDto.getMinutosInicio()>=0 and horarioDto.getMinutosFin() <= 59:
                horasTrabajadas = (horarioDto.getHoraFin() - horarioDto.getHoraInicio())
                precioPorHora = 25
        totalPago = horasTrabajadas * precioPorHora
        
        if mostrarDetalle:
            print(horario.diaSemana + ": " + str(horarioDto.getHoraInicio()()) + " - " + str(horarioDto.getHoraFin()))
            print("Horas Trabajadas: " + str(horasTrabajadas))
            print("Precio por Horas: " + str(precioPorHora))
            print("Total a Pagar: " + str(totalPago))
            print("--------------------------------------------------")

        return totalPago
    
    def calcularPagoEmpleado(self, datos: str, mostrarDetalle = False) -> ResultadoCalculo:
        totalPago = 0
        datosAr = datos.split('=')
        nombreEmpleado = datosAr[0]
        horarios = datosAr[1].split(',')
        resultadoCalculo: ResultadoCalculo = None
        for horario in horarios:
            dia = Utils.extraerDiaDeHorario(horario)
            rangoHorario = Utils.extraerRangoDeHorario(horario).split('-')
            horario = HorarioModel(DiasSemanaEnum(dia), rangoHorario[0], rangoHorario[1]);
            pagoPorHorario = self.calcularMontoPorHorario(horario, mostrarDetalle)
            totalPago += pagoPorHorario
        resultadoCalculo = ResultadoCalculo(nombreEmpleado, totalPago)
        return resultadoCalculo
    
    def procesarPagoEmpleado(self, mostarDetalle = False) -> list[ResultadoCalculo]:
        lineas = self.pagoRepository.obtenerInformacionPago()
        listaResultadoCalculo: list[ResultadoCalculo] = []
        for linea in lineas:
            resultadoCalculo:ResultadoCalculo = self.calcularPagoEmpleado(linea, mostarDetalle)
            listaResultadoCalculo.append(resultadoCalculo)
        return listaResultadoCalculo