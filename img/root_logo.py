from pathlib import Path

def pegar_logo():
    ROOT_LOGO = Path(__file__).parent
    for logo in ROOT_LOGO.iterdir():
        return str(logo)
    


