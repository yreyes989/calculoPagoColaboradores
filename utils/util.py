# from domain.models.resultadoCalculo import ResultadoCalculo
from domain.models.resultadoCalculo import ResultadoCalculo

class Utils:
    def extraerDiaDeHorario(horario):
        return horario[0:2]
    def extraerRangoDeHorario(horario):
        return horario[2:len(horario)]
    
    def imprimirResultadoCalculo(resultadoCalculo: ResultadoCalculo):
        for resultado in resultadoCalculo:
            print(f'El monto a pagar de {resultado.nombreEmpleado} es: {resultado.totalPago} USD')