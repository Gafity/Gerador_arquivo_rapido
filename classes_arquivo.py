from pathlib import Path
from abc import ABC, abstractmethod, abstractproperty

ROOT_PATH = Path(__file__).parent

class Pasta(Path):
    @staticmethod
    def listar_arquivos():
        for arquivo in ROOT_PATH.iterdir():
            if arquivo.is_dir():
                continue
            elif arquivo.is_file():
                list_arquivo = list(str(arquivo))
                caminho = "".join(list_arquivo)
                diretorios_isolados = caminho.split("\\")
                total_diretorios = caminho.count("\\")
                print(diretorios_isolados[total_diretorios])
    
    @staticmethod
    def listar_diretorios():
        for arquivo in ROOT_PATH.iterdir():
            if arquivo.is_dir():
                list_arquivo = list(str(arquivo))
                caminho = "".join(list_arquivo)
                diretorios_isolados = caminho.split("\\")
                try:
                    diretorios_isolados.remove(".git")
                except ValueError:
                    [print(diretorios) for diretorios in diretorios_isolados]
                
                [print(diretorios) for diretorios in diretorios_isolados]
            elif arquivo.is_file():
                continue

    @staticmethod
    def criar_diretorios():
        try:
            nome_pasta = input("Digite o nome da pasta: ")
            caminho_nova_pasta = ROOT_PATH / nome_pasta
            caminho_nova_pasta.mkdir(parents=True, exist_ok=False)
        except FileExistsError as erro:
            tentativa = 1
            acerto = 0
            incremento_pasta_numero = 1
            while tentativa > acerto:
                try:
                    caminho_nova_pasta = ROOT_PATH.joinpath(f"{nome_pasta+" "+str(incremento_pasta_numero)}") 
                    acerto += 1
                    caminho_nova_pasta.mkdir(parents=True, exist_ok=False)
                except FileExistsError:
                    incremento_pasta_numero += 1
                    print(f"Esse é o valor do incremento {incremento_pasta_numero}")
                    tentativa += 1
                    continue
        
    @staticmethod
    def criar_estrutura_web():
        try:
            estrutura_diretorios = ["css", "img", "js"]
            for pasta in estrutura_diretorios:
                caminho_pasta = ROOT_PATH / pasta
                caminho_pasta.mkdir(parents=True, exist_ok=False)
                if pasta != "img":
                    if pasta == "js":
                        with open(caminho_pasta / f"script.{pasta}", "w"):
                            pass
                    else:
                        with open(caminho_pasta/ f"styles.{pasta}", "w"):
                            pass

        except FileExistsError:
            print("estrutura de diretorios já criado ou contém alguma pasta da estrutura já existe")
        
        #adicionar os tratamentos de erro para os arquivos.

            
            
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

    @abstractmethod
    def criar_arquivos(**kwargs):
        loop = True
        INSTENCAO = kwargs.get("instencao")
        while loop:
            vetor_nomes = input('Digite o nome dos arquivos (seperado por ","): ')
            vetor_nomes = vetor_nomes.lstrip()
            vetor_nomes = vetor_nomes.split(",")
            incremento = 0
            with open(ROOT_PATH.joinpath([nomes+INSTENCAO for nomes in vetor_nomes][incremento]) , "w") as file:
                print(f"Arquivo criado com sucesso! {vetor_nomes[incremento]}")
                incremento += incremento
            
            opcao = input("Deseja criar mais arquivos? S/n").upper()
            opcao == "N" if not loop else print("Programa finalizado com sucesso!")

#-------------------------------------------------

class JavaScript(File):
    INSTENCAO_JS = ".js"

    @classmethod
    def criar_file(cls):
        return super().criar_file(instencao = cls.INSTENCAO_JS)
    
    def mostrar_conteudo(self, **arquivo):
        return super().mostrar_conteudo(arquivo)

    @classmethod
    def criar_arquivos(cls):
        return super().criar_arquivos(instencao = cls.INSTENCAO_JS)
#-------------------------------------------------

class Html(File):
    INSTENCAO_HTML = ".html"
    
    @classmethod
    def criar_file(cls):
        return super().criar_file(instencao = cls.INSTENCAO_HTML)
    
    def mostrar_conteudo(self, **arquivo):
        return super().mostrar_conteudo(arquivo)
    
    @classmethod
    def criar_arquivos(cls):
        return super().criar_arquivos(instencao = cls.INSTENCAO_HTML)

Pasta.criar_estrutura_web()
