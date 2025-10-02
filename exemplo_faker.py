#!/usr/bin/env python3
"""
Exemplos específicos para demonstrar a funcionalidade Faker no geraArquivos.py
"""

from geraArquivos import ConfiguracaoArquivos, gerar_arquivos, gerar_arquivos_por_tipo
import pandas as pd

def exemplo_xlsx_pequeno():
    """Exemplo 1: XLSX pequeno (0.1 MB)"""
    print("=== Exemplo 1: XLSX pequeno (0.1 MB) ===")
    gerar_arquivos_por_tipo(
        quantidade_por_tipo={"xlsx": 1},
        tamanhos_mb={"xlsx": 0.1}
    )

def exemplo_xlsx_medio():
    """Exemplo 2: XLSX médio (0.5 MB)"""
    print("\n=== Exemplo 2: XLSX médio (0.5 MB) ===")
    gerar_arquivos_por_tipo(
        quantidade_por_tipo={"xlsx": 1},
        tamanhos_mb={"xlsx": 0.5}
    )

def exemplo_xlsx_grande():
    """Exemplo 3: XLSX grande (1.0 MB)"""
    print("\n=== Exemplo 3: XLSX grande (1.0 MB) ===")
    gerar_arquivos_por_tipo(
        quantidade_por_tipo={"xlsx": 1},
        tamanhos_mb={"xlsx": 1.0}
    )

def exemplo_multiplos_xlsx():
    """Exemplo 4: Múltiplos XLSX com tamanhos diferentes"""
    print("\n=== Exemplo 4: Múltiplos XLSX ===")
    config = ConfiguracaoArquivos(
        tipos_ativados=["xlsx"],
        quantidade_por_tipo={"xlsx": 3},
        tamanho_mb={"xlsx": 0.2}
    )
    gerar_arquivos(config)

def exemplo_misto_com_xlsx():
    """Exemplo 5: Mistura de tipos incluindo XLSX"""
    print("\n=== Exemplo 5: Mistura de tipos ===")
    config = ConfiguracaoArquivos(
        tipos_ativados=["xlsx", "txt", "pdf"],
        quantidade_por_tipo={"xlsx": 2, "txt": 1, "pdf": 1},
        tamanho_mb={"xlsx": 0.3, "txt": 0.1, "pdf": 0.2}
    )
    gerar_arquivos(config)

def verificar_dados_gerados():
    """Verifica os dados gerados nos arquivos XLSX"""
    print("\n=== Verificando dados gerados ===")
    
    # Encontrar arquivos XLSX mais recentes
    import os
    import glob
    
    arquivos_xlsx = glob.glob("arquivos_teste/*.xlsx")
    if arquivos_xlsx:
        # Pegar o arquivo mais recente
        arquivo_mais_recente = max(arquivos_xlsx, key=os.path.getctime)
        
        print(f"Analisando: {arquivo_mais_recente}")
        df = pd.read_excel(arquivo_mais_recente)
        
        print(f"Total de linhas: {len(df)}")
        print(f"Total de colunas: {len(df.columns)}")
        print(f"Colunas: {list(df.columns)}")
        
        print("\nPrimeiras 2 linhas:")
        print(df.head(2).to_string())
        
        print(f"\nTamanho do arquivo: {os.path.getsize(arquivo_mais_recente) / (1024*1024):.2f} MB")

if __name__ == "__main__":
    print("Demonstração da funcionalidade Faker para XLSX")
    print("=" * 60)
    
    # Executar exemplos
    exemplo_xlsx_pequeno()
    exemplo_xlsx_medio()
    exemplo_xlsx_grande()
    exemplo_multiplos_xlsx()
    exemplo_misto_com_xlsx()
    
    # Verificar dados gerados
    verificar_dados_gerados()
    
    print("\n" + "=" * 60)
    print("Todos os exemplos foram executados com sucesso!")
    print("Os arquivos XLSX agora contêm dados realistas em português brasileiro!")
