"""
    Classe responsavel por gerenciar os arquivos em disco.
    Trata as operações create e delete sobre os arquivos.
"""


class Arquivo:
    
    """
        Classe responsável por carregamento de dados dos arquivos.
    """

    def __init__(self, nome_arquivo=0, posicao_bloco=0, tamanho=0, criador=None):
        """
            Construtor da classe de Arquivo
        """
        self.nome_arquivo = nome_arquivo
        self.posicao_bloco = posicao_bloco
        self.tamanho = tamanho
        self.criador = criador

    def __str__(self):
        """
            Método responsável por retornar uma string mensagem
        """
        return ("| {} ".format(self.nome_arquivo))


class GerenciadorArquivos:
    
    """
        Classe responsável por manipulação de arquivos criar e deletar.
    """
    
    def __init__(self, lista_arquivos):
        """
            Construtor da classe de GerenciadorArquivos
        """
        self.lista_blocos_disco = []
        self.tamanho_blocos_disco = int(lista_arquivos[0])
        
        for _ in range(0, self.tamanho_blocos_disco):
            self.lista_blocos_disco.append(Arquivo())
        lista_arquivos.pop(0)
        
        for arquivo in lista_arquivos:
            linha = arquivo.split(',')
            for i in range(0, len(self.lista_blocos_disco)):
                posicao_inicial = int(linha[1])
                posicao_final = posicao_inicial + int(linha[2]) - 1
                if ((i >= posicao_inicial)and (i <= posicao_final)):
                    self.lista_blocos_disco[i].posicao_bloco = posicao_inicial
                    self.lista_blocos_disco[i].nome_arquivo = linha[0]
                    self.lista_blocos_disco[i].tamanho = posicao_final - posicao_inicial + 1
    
    def __str__(self):
        """
            Método responsável por retornar uma string mensagem
        """
        string = "MAPA DOS BLOCOS DO DISCO:\n\t"
        for bloco in self.lista_blocos_disco:
            string += str(bloco)
        string += "|"
        return string

    def executar_operacao(self, processo, sequencia_geral,):
        """
            Metodo responsável por executar_operacao as intrucoes do processo com base na 
            execucao atual e posicao do lista de instrucoes.
            Retorna uma string mensagem de sucesso/falha da operação executada.
        """
        mensagem = ""
        dispobilidade = 0
      
        operacao = processo.lista_instrucoes[sequencia_geral][1]
        nome_arquivo = processo.lista_instrucoes[sequencia_geral][2]
        
        if operacao == 0:  # Criar arquivo
            tamanho_arquivo = processo.lista_instrucoes[sequencia_geral][3]
            numero_operacao_processo_atual = processo.lista_instrucoes[sequencia_geral][4]

            for i in range(0, self.tamanho_blocos_disco):
                
                if(self.lista_blocos_disco[i].nome_arquivo == 0):
                    dispobilidade += 1
                  
                    if dispobilidade == tamanho_arquivo:
                        posicao = i - tamanho_arquivo + 1
                        arquivo = Arquivo(nome_arquivo, posicao, tamanho_arquivo, processo.pid)
                        self.lista_blocos_disco[posicao:i + 1] = dispobilidade * [arquivo]
                        
                        mensagem = "P{} instruction {}".format(processo.pid, numero_operacao_processo_atual)
                        mensagem += " - Sucesso!\n"
                        mensagem += "O processo {} criou o arquivo {} ".format(processo.pid, nome_arquivo)
                        mensagem += "(do bloco {} a {}).\n".format(posicao, posicao + tamanho_arquivo - 1)
                        break
                else: 
                    dispobilidade = 0
                    mensagem = "P{} instruction {}".format(processo.pid, numero_operacao_processo_atual)
                    mensagem += " - Falha!\n"
                    mensagem += "O processo {} ".format(processo.pid)
                    mensagem += "não pode criar o arquivo {} por falta de espaço.\n".format(nome_arquivo)
            
            return mensagem
        
        elif operacao == 1:  # Deletar arquivo
            numero_operacao_processo_atual = processo.lista_instrucoes[sequencia_geral][3]
            for i in range(0, self.tamanho_blocos_disco):
                if(self.lista_blocos_disco[i].nome_arquivo == nome_arquivo):
                   
                    #
                    if((processo.pid == self.lista_blocos_disco[i].criador) or processo.prioridade == 0):
                        tamanho_arquivo = self.lista_blocos_disco[i].tamanho
                        self.lista_blocos_disco[i:i + tamanho_arquivo] = tamanho_arquivo * [Arquivo()]
                      
                        mensagem = "P{} instruction {}".format(processo.pid, numero_operacao_processo_atual)
                        mensagem += " - Sucesso!\n"
                        mensagem += "O processo {} deletou o arquivo {}.\n".format(processo.pid, nome_arquivo)
                        break
                    else:
                        mensagem = "P{} instruction {}".format(processo.pid, numero_operacao_processo_atual)
                        mensagem += " - Falha!\n"
                        mensagem += "O processo {} não pode deletar o arquivo {} porque não existe esse arquivo.\n".format(processo.pid, nome_arquivo)
                else:
                    mensagem = "P{} instruction {}".format(processo.pid, numero_operacao_processo_atual)
                    mensagem += " - Falha!\n"
                    mensagem += "O processo {}: não pode deletar o arquivo {} porque não existe esse arquivo.\n".format(processo.pid, nome_arquivo)
            return mensagem
        else:
            return "Operacao nao existente"

