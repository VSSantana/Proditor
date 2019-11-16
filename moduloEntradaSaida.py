"""
    Módulo responsável pelos métodos de leitura e exibição de dados.
"""

import moduloProcessos as Proc


class LeitorArquivo:

    """
        Classe dos métodos de leitura dos dados.
    """

    def __init__(self):
        pass
        
    def leitura_arquivo_processos(self, arquivo_processo):

        """
            Cria a lista de processos a partir do arquivo processo e retorna a lista criada.
        """
        pid = 0
        lista_processos = []
        with open(arquivo_processo, "r") as arquivo_processo:
            for linha in arquivo_processo:
                lista_processos.append(Proc.Processo([int(dado) for dado in linha.split(',')]))

        """
            Faz a designação do id de cada processo com base na ordem disposta no arquivo de entrada.
        """

        for processo in lista_processos:
            processo.pid = pid
            pid += 1
        return lista_processos
    
    def leitura_arquivo_file(self, arquivo_file):

        """
            Cria a lista de arquivos e de instruções a partir do arquivo file e retorna as duas listas criadas.
        """

        lista_arquivos = []
        with open(arquivo_file, "r") as arquivo_file:
            arquivo = arquivo_file.read().splitlines()
            
        lista_arquivos.append(int(arquivo[0]))
        i = int(arquivo[1])
        
        for linha in range(2, i + 2):
            lista_arquivos.append(arquivo[linha])
        lista_instrucoes = []
        for linha in range(i + 2, len(arquivo)):
            lista_instrucoes.append(arquivo[linha])
        return [lista_arquivos, lista_instrucoes]


class Impressao:

    """
        Classe dos métodos de impressão de dados.
    """

    def __init__(self):

        # Construtor da classe Impressao.

        self.log_operacao = []

    def imprimir_mapa_disco(self, mapa_disco):

        """
            Método para imprimir o mapa do disco.
        """

        print("\n")
        print(mapa_disco)

    def imprimir_dispatcher(self, processo):

        """
            Método para imprimir a mensagem do dispatcher do processo referenciado.
        """

        print('\ndispatcher =>')
        print('\tPID:\t\t {}'.format(processo.pid))
        print('\toffset:\t\t {}'.format(processo.posicao_bloco_disco))
        print('\tblocks:\t\t {}'.format(processo.bloco_memoria))
        print('\tpriority:\t {}'.format(processo.prioridade))
        print('\ttime:\t\t {}'.format(processo.tempo_processador))
        print('\tprinters:\t {}'.format(bool(processo.codigo_impressora)))
        print('\tscanners:\t {}'.format(bool(processo.scanner)))
        print('\tmodems:\t\t {}'.format(bool(processo.modem)))
        print('\tdrives:\t\t {}'.format(bool(processo.codigo_disco)))

    def imprimir_log(self):

        """
            Método para imprime o log das operações executadas.
        """

        for log in self.log_operacao:
            print(log)
