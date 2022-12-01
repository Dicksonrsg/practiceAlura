from fabrica_fila import FabricaFila
from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria
from estatistica_detalhada import EstatisticaDetalhada
from estatistica_resumida import EstatisticaResumida

fila = FabricaFila.pega_fila('prioritaria')
fila.atualiza_fila()
fila.atualiza_fila()
fila.atualiza_fila()
print(fila.chama_cliente(5))
print(fila.estatistica(EstatisticaResumida('20/03/2025', 1245)))