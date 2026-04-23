import pandas as pd


class Extract:
    def __init__(self, caminho_arquivo: str):
        self.caminho_arquivo = caminho_arquivo

    def executar(self) -> pd.DataFrame:
        try:
            df = pd.read_csv(self.caminho_arquivo)
            print("Dados extraídos com sucesso!")
            return df
        except Exception as e:
            print(f"Erro na extração: {e}")
            raise