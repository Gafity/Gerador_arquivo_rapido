from pathlib import Path
from abc import ABC, abstractmethod, abstractproperty

ROOT_PATH = Path(__file__).parent

class File(ABC):
    
    def receber_nome_arquivo(funcao):
        def envelope(**kwargs):
            print(kwargs)
            nome_arquivo = input("Digite o nome do arquivo: ")
            
            while not(nome_arquivo):
                print("Ops, parece que você não informou o nome do arquivo!")
                arquivo_arquivo = input("Campos vazios são infalidos\n Digite o nome do arquivo, nomamente: ")
            
            INSTENCAO = kwargs.get("instencao", "instencao não encontrada")
            ARQUIVO_FORMATADO = nome_arquivo + INSTENCAO
            resultado = funcao(arquivo=ARQUIVO_FORMATADO)
            return resultado
        
        return envelope

    @receber_nome_arquivo
    @abstractmethod
    def criar_file(**kwargs):
        CHAVES = [chave for chave in kwargs.keys()]
        ARQUIVO = kwargs.get(CHAVES[0], "erro")
        print(ARQUIVO)
        with open(ROOT_PATH / ARQUIVO, "w") as file:
            pass
        return 
            
    
    @abstractmethod
    def mostrar_conteudo(self,arquivo):
        with open(ROOT_PATH / arquivo,  "r") as file:
            for reading in file.readlines():
                print(reading)

#-------------------------------------------------

class JavaScript(File):
    INSTENCAO_JS = ".js"

    @classmethod
    def criar_file(cls):
        return super().criar_file(instencao = cls.INSTENCAO_JS)
    
    def mostrar_conteudo(self, **arquivo):
        return super().mostrar_conteudo(arquivo)

#-------------------------------------------------

class Html(File):
    INSTENCAO_HTML = ".html"
    
    @classmethod
    def criar_file(cls):
        return super().criar_file(instencao = cls.INSTENCAO_HTML)
    
    def mostrar_conteudo(self, **arquivo):
        return super().mostrar_conteudo(arquivo)
    

instancia = Html()
instancia.criar_file()