from pathlib import Path
from abc import ABC, abstractmethod, abstractproperty

ROOT_PATH = Path(__file__).parent

class File(ABC):
    
    def receber_nome_arquivo(funcao):
        def envelope(**kwargs):
            NOME_PADRAO = "nome_arquivo"
            nome_arquivo = input("Digite o nome do arquivo: ")
            kwargs.fromkeys([NOME_PADRAO], nome_arquivo)
            while not(kwargs.get(NOME_PADRAO)):
                print("Ops, parece que você não informou o nome do arquivo!")
                nome_arquivo = input("Campos vazios são infalidos\n Digite o nome do arquivo, nomamente: ")
    
            resultado = funcao(**kwargs)
            return resultado
        
        return envelope

    @receber_nome_arquivo
    @abstractmethod
    def criar_file(**kwargs):
        CHAVES = [chave for chave in kwargs.keys()]
        ARQUIVO = kwargs.get(CHAVES[0], "erro")
        print(ARQUIVO)
        with open(ROOT_PATH / ARQUIVO, "w") as file:
            return f"Arquivo criado com sucesso:\r{file.name}"
            
    
    @abstractmethod
    def mostrar_conteudo(self,arquivo):
        with open(ROOT_PATH / arquivo,  "r") as file:
            for reading in file.readlines():
                print(reading)

#-------------------------------------------------

class JavaScript(File):
    INSTENCAO_JS = ".js"

    @classmethod
    def criar_file(cls, **arquivo):
        print(arquivo.get("nome_arquivo"))
        arquivo_js_formatado = arquivo.get("nome_arquivo") + cls.INSTENCAO_JS
        print(arquivo_js_formatado)
        return super().criar_file(arquivo_js=arquivo_js_formatado)
    
    def mostrar_conteudo(self, **arquivo):
        return super().mostrar_conteudo(arquivo)

#-------------------------------------------------

class Html(File):
    INSTENCAO_HTML = ".html"
    
    @classmethod
    def criar_file(cls, **arquivo):
        print(arquivo.get("nome_arquivo"))
        arquivo_html_formatado = arquivo.get("nome_arquivo") + cls.INSTENCAO_HTML
        print(arquivo_html_formatado)
        return super().criar_file(arquivo_html=arquivo_html_formatado)
    
    def mostrar_conteudo(self, **arquivo):
        return super().mostrar_conteudo(arquivo)
    

instancia = Html()
instancia.criar_file(nome_arquivo="primeiro_teste")