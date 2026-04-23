class Load:
    def __init__(self, dataframe, caminho_saida: str):
        self.df = dataframe
        self.caminho_saida = caminho_saida

    def executar(self):
        try:
            self.df.to_csv(self.caminho_saida, index=False)
            print("Dados salvos com sucesso!")
        except Exception as e:
            print(f"Erro ao salvar: {e}")
            raise