from application.services.calculoPagoService import CalculoPagoService
import unittest


class PruebaCalculoPago(unittest.TestCase):
    
        def testCalculoPagoEvaluarCantidadEmpleado(self):
            calculoPagoService = CalculoPagoService()
            resultado = calculoPagoService.procesarPagoEmpleado()
            self.assertEqual(len(resultado), 6)

        def testCalculoPagoEvaluarPagoRENE(self):
            calculoPagoService = CalculoPagoService()
            resultado = calculoPagoService.procesarPagoEmpleado()
            self.assertEqual(resultado[0].totalPago, 215)
        
        def testCalculoPagoEvaluarPagoASTRID(self):
            calculoPagoService = CalculoPagoService()
            resultado = calculoPagoService.procesarPagoEmpleado()
            self.assertEqual(resultado[1].totalPago, 85)

        def testCalculoPagoEvaluarPagoYUNIOR(self):
            calculoPagoService = CalculoPagoService()
            resultado = calculoPagoService.procesarPagoEmpleado()
            self.assertEqual(resultado[2].totalPago, 275)

def executeTest():
    unittest.main()