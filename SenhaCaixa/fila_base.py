import abc

from constantes import TAMANHO_PADRAO_MAXIMO, TAMANHO_PADRAO_MINIMO


class FilaBase(metaclass= abc.ABCMeta):
    codigo: int = 0
    fila = []
    clientes_atendidos = []
    senha_atual: str = ""

    def reseta_fila(self) -> None:
        if self.codigo >= TAMANHO_PADRAO_MAXIMO:
            self.codigo = TAMANHO_PADRAO_MINIMO
        else:
            self.codigo += 1

    def inseri_cliente(self) -> None:
        self.fila.append(self.senha_atual)

    def gera_senhas(self):
        self.busca_posicao_fila()
        self.gera_senha_atual()
        self.inseri_cliente()

    @abc.abstractmethod
    def chama_cliente(self, caixa):
        ...

    @abc.abstractmethod
    def estatistica(self, dia, agencia, flag_detail):
        ...

    @abc.abstractmethod
    def atualiza_fila(self):
        ...
    
