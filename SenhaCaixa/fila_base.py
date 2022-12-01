import abc

from typing import List

from constantes import TAMANHO_PADRAO_MAXIMO, TAMANHO_PADRAO_MINIMO


class FilaBase(metaclass= abc.ABCMeta):
    codigo: int = 0
    fila: List[str] = []
    clientes_atendidos: List[str] = []
    senha_atual: str = ""

    def reseta_fila(self) -> None:
        if self.codigo >= TAMANHO_PADRAO_MAXIMO:
            self.codigo = TAMANHO_PADRAO_MINIMO
        else:
            self.codigo += 1

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.inseri_cliente()

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
    def gera_senha_atual(self):
        ...
    
