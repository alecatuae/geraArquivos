#!/usr/bin/env python3
"""
Exemplos de uso do geraArquivos.py com diferentes configurações
"""

from geraArquivos import ConfiguracaoArquivos, gerar_arquivos, gerar_arquivos_aleatorios, gerar_arquivos_por_tipo

def exemplo_1_basico():
    """Exemplo básico: gerar 5 arquivos aleatórios"""
    print("=== Exemplo 1: Geração básica aleatória ===")
    gerar_arquivos_aleatorios(5)

def exemplo_2_tipos_especificos():
    """Exemplo 2: gerar apenas TXT e PDF"""
    print("\n=== Exemplo 2: Apenas TXT e PDF ===")
    gerar_arquivos_aleatorios(6, ["txt", "pdf"])

def exemplo_3_quantidade_por_tipo():
    """Exemplo 3: quantidade específica por tipo"""
    print("\n=== Exemplo 3: Quantidade específica por tipo ===")
    gerar_arquivos_por_tipo(
        quantidade_por_tipo={"txt": 2, "xlsx": 3, "jpeg": 1},
        tamanhos_mb={"txt": 0.1, "xlsx": 0.2, "jpeg": 0.5}
    )

def exemplo_4_configuracao_completa():
    """Exemplo 4: configuração completa personalizada"""
    print("\n=== Exemplo 4: Configuração completa ===")
    
    config = ConfiguracaoArquivos(
        tipos_ativados=["txt", "pdf", "docx"],
        quantidade_por_tipo={"txt": 2, "pdf": 1, "docx": 1},
        tamanho_mb={
            "txt": 0.3,    # 300KB
            "pdf": 0.8,    # 800KB
            "docx": 0.5    # 500KB
        },
        config_especifica={
            "txt": {"linhas": 15, "caracteres_por_linha": 100},
            "pdf": {"linhas": 8, "caracteres_por_linha": 100},
            "docx": {"paragrafos": 6, "caracteres_por_paragrafo": 150}
        }
    )
    
    gerar_arquivos(config)

def exemplo_5_arquivos_grandes():
    """Exemplo 5: gerar arquivos grandes"""
    print("\n=== Exemplo 5: Arquivos grandes ===")
    
    config = ConfiguracaoArquivos(
        tipos_ativados=["txt", "pdf"],
        quantidade_por_tipo={"txt": 1, "pdf": 1},
        tamanho_mb={
            "txt": 2.0,    # 2MB
            "pdf": 1.5     # 1.5MB
        }
    )
    
    gerar_arquivos(config)

def exemplo_6_apenas_um_tipo():
    """Exemplo 6: gerar apenas um tipo de arquivo"""
    print("\n=== Exemplo 6: Apenas arquivos XLSX ===")
    
    config = ConfiguracaoArquivos(
        tipos_ativados=["xlsx"],
        quantidade_por_tipo={"xlsx": 3},
        tamanho_mb={"xlsx": 0.4}
    )
    
    gerar_arquivos(config)

if __name__ == "__main__":
    print("Demonstração das funcionalidades do geraArquivos.py")
    print("=" * 60)
    
    # Executar exemplos
    exemplo_1_basico()
    exemplo_2_tipos_especificos()
    exemplo_3_quantidade_por_tipo()
    exemplo_4_configuracao_completa()
    exemplo_5_arquivos_grandes()
    exemplo_6_apenas_um_tipo()
    
    print("\n" + "=" * 60)
    print("Todos os exemplos foram executados com sucesso!")
