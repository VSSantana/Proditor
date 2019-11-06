"""
    Módulo responsável pelo gerenciamento da recursos.
    Trata a alocação e liberação dos recursos de E/S para os processos.
"""


class Recurso:
    """
        Classe responsável por recursos disponíveis.
    """

    def __init__(self):
        """
            Construtor da classe de Recurso
        """
        self.scanner = [None]
        self.codigo_impressora = [None]
        self.modem = [None]
        self.codigo_disco = [None, None]

    def verificar_disponibilidade_recurso(self, processo):
        """
            Metodo responsável por verificar a disponibilidade de um recurso 
            se tiver disponibilidade aloca o recurso para processo solitado e retorna True.
            caso não seja possível retorna False 
        """
        recurso = True
        if (processo.scanner == 1) and (self.scanner[0] is not None):
            recurso = False
        if (processo.codigo_impressora == 1) and (self.codigo_impressora[0] is not None):
            recurso = False
        if (processo.modem == 1) and (self.modem[0] is not None):
            recurso = False
        if (processo.codigo_disco == 1) and (self.codigo_disco[0] is not None):
            recurso = False
        if (processo.codigo_disco == 2) and (self.codigo_disco[1] is not None):
            recurso = False
        if recurso:
            if(processo.scanner == 1):
                self.scanner[0] = True
            if(processo.codigo_impressora == 1):
                self.codigo_impressora[0] = True
            if(processo.modem == 1):
                self.modem[0] = True
            if(processo.codigo_disco == 1):
                self.codigo_disco[0] = True
            if(processo.codigo_disco == 2):
                self.codigo_disco[1] = True
        return recurso

    def liberar_recursos(self):
        """
            Metodo responsável por liberar os recursos, logo após o termino de execução do quantum
            libera todos os recursos independente do processo pois os processos de tempo_real
            nao podem acessar recursos e os de usuario duram um quantum definido.
        """
        self.scanner = [None]
        self.codigo_impressora = [None]
        self.modem = [None]
        self.codigo_disco = [None, None]
