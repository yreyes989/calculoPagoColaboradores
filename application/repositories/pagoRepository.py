from application.dtos.detallePagoEmpleadoDto import DetallePagoEmpleadoDTO


class PagoRepository:
    def obtenerInformacionPago() -> list[str]:
        lines = [""]
        with open('./infrastructure/persistence/datos_empleados.txt', 'r') as archivo:
            lines = archivo.readlines()
        return lines