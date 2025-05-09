class ConversorBasico:
    def __init__(self):
        self._valor_origen = None
        self._unidad_origen = None
        self._unidad_destino = None
        self._valor_convertido = None

    def _conversion_generica(self, valor, factor_conversion):
        return valor * factor_conversion

    def _mostrar_resultados(self):
        print(f"{self._valor_origen} {self._unidad_origen} son {self._valor_convertido} {self._unidad_destino}")

class ConversorDistancia(ConversorBasico):
    def metros_a_centimetros(self, metros):
        self._valor_origen = metros
        self._unidad_origen = "metros"
        self._unidad_destino = "centimetros"
        self._valor_convertido = self._conversion_generica(metros, 100)
        self._mostrar_resultados()

    def centimetros_a_kilometros(self, centimetros):
        self._valor_origen = centimetros
        self._unidad_origen = "centimetros"
        self._unidad_destino = "kilometros"
        self._valor_convertido = self._conversion_generica(centimetros, 0.00001)
        self._mostrar_resultados()