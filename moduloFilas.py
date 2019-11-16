"""
    Módulo responsável pelo gerenciamento das filas.
    Mantém as interfaces e funções que operam sobre os processos.
"""


class Fila:

    def __init__(self):

        self.lista_processo_usuario_pronto = None
        self.lista_entrada_saida = None
        self.lista_processo_0 = []
        self.lista_processo_1 = []
        self.lista_processo_2 = []
        self.lista_processo_3 = []
        self.lista_processo_usuario_execucao = []
        self.lista_processo_sistema_execucao = []
        self.lista_processo_pronto = []
    
    def inicializar_fila(self):
        self.lista_processo_0 = []
        self.lista_processo_1 = []
        self.lista_processo_2 = []
        self.lista_processo_3 = []
        self.lista_processo_usuario_execucao = []
        self.lista_processo_sistema_execucao = []
             
    def ordenar_filas_prioridade(self, tempo_execucao):

        """
            Método responsável por ordenar os processos processos 
            na fila de prioridade, em ordem crescente de menor para maior.     
        """

        for processo in self.lista_processo_pronto:          
              
            if processo.tempo_inicializacao <= tempo_execucao:
                
                if processo.prioridade == 0:
                    self.lista_processo_0.append(processo)
                    
                if processo.prioridade == 1:
                    self.lista_processo_1.append(processo)
                     
                if processo.prioridade == 2:
                    self.lista_processo_2.append(processo)
                    
                if processo.prioridade == 3:
                    self.lista_processo_3.append(processo)

    def alterar_fila_prioridade_usuario(self, tempo_execucao):
        """
            EVITAR STARVATION
            Método responsável por alterar a prioridade dos processos  
            que estiverem mais de 10 unidades de tempo esperando 
            sem nunca terem sidos executados na fila de prioridade.
        """       
        for processo in self.lista_processo_2:
          
            if((processo.execucao == 0) and (processo.tempo_inicializacao + 9 < tempo_execucao) and
                    (not processo.lista_prioridade)):
                processo.lista_prioridade = True
                self.lista_processo_1.append(processo)
            elif((processo.execucao == 0) and (processo.tempo_inicializacao + 19 < tempo_execucao) and
                 processo.lista_prioridade):
                self.lista_processo_1.append(processo)
       
        for processo in self.lista_processo_3:
            if((processo.execucao == 0) and (processo.tempo_inicializacao + 9 < tempo_execucao) and
                    (not processo.lista_prioridade)):
                processo.lista_prioridade = True 
                self.lista_processo_2.append(processo)

    def adicionar_processo_fila_prioridade_usuario(self):
        """
            Método responsável por adicionar um processo que não terminou sua execução 
            no final na fila processo após a execucao.
        """
        for processo in self.lista_processo_usuario_execucao:
            if processo.execucao >= processo.tempo_processador:
                self.lista_entrada_saida.append(processo)
            else:
                if processo.prioridade == 1:
                    self.lista_processo_1.append(processo)
                    self.lista_processo_usuario_pronto.append(processo)
                  
                if processo.prioridade == 2:
                    self.lista_processo_2.append(processo)
                    self.lista_processo_usuario_pronto.append(processo)
                   
                if processo.prioridade == 3:
                    self.lista_processo_3.append(processo)
                    self.lista_processo_usuario_pronto.append(processo)    
