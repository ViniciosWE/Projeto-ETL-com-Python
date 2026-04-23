import os
from src.extract import Extract
from src.transform import Transform
from src.load import Load


def main():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    caminho_entrada = os.path.join(BASE_DIR, "data", "entrada.csv")
    caminho_saida = os.path.join(BASE_DIR, "data", "saida.csv")

    extractor = Extract(caminho_entrada)
    dados = extractor.executar()

    transformer = Transform(dados)
    dados_transformados = transformer.executar()

    loader = Load(dados_transformados, caminho_saida)
    loader.executar()


if __name__ == "__main__":
    main()