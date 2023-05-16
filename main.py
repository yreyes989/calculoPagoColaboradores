from application.services.calculoPagoService import CalculoPagoService
from utils.util import Utils
from test.mainTest import *
def main():
    ## Ejecucion del programa
    print("----------------------------------------------------------------------")
    print("Ejecucion del programa")
    print("----------------------------------------------------------------------")
    calculoPagoService = CalculoPagoService()
    resultadoCalculo = calculoPagoService.procesarPagoEmpleado()
    Utils.imprimirResultadoCalculo(resultadoCalculo)
    
    ## Ejecucion de los test
    print("----------------------------------------------------------------------")
    print("Ejecucion de los test")
    print("----------------------------------------------------------------------")
    executeTest()

if __name__ == "__main__":
    main()