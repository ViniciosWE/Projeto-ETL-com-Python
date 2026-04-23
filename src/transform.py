class Transform:
    def __init__(self, dataframe):
        self.df = dataframe

    def _gerar_mensagem(self, row):
        if row["score"] >= 800:
            return f"{row['nome']}, você tem acesso a benefícios exclusivos!"

        elif row["score"] < 650:
            return f"{row['nome']}, confira dicas para melhorar seu score!"

        else:
            return f"{row['nome']}, temos uma nova oferta para você!"

    def _classificar_cliente(self, score):
        if score >= 800:
            return "VIP"
        elif score < 650:
            return "Risco"
        else:
            return "Comum"

    def executar(self):
        self.df["mensagem"] = self.df.apply(self._gerar_mensagem, axis=1)
        self.df["categoria"] = self.df["score"].apply(self._classificar_cliente)

        print("Dados transformados com sucesso!")
        return self.df