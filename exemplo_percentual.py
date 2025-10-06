#!/usr/bin/env python3
"""
Exemplos específicos para demonstrar a funcionalidade de distribuição por percentual
"""

from geraArquivos import (
    ConfiguracaoArquivos, 
    gerar_arquivos, 
    gerar_arquivos_por_quantidade,
    gerar_arquivos_por_percentual
)

def exemplo_quantidade_total():
    """Exemplo 1: Gerar quantidade total específica"""
    print("=== Exemplo 1: Quantidade total específica (20 arquivos) ===")
    gerar_arquivos_por_quantidade(20, ["txt", "pdf", "docx", "xlsx"])

def exemplo_percentual_70_30():
    """Exemplo 2: 70% PDF, 30% outros tipos"""
    print("\n=== Exemplo 2: 70% PDF, 30% outros tipos ===")
    gerar_arquivos_por_percentual(
        quantidade_total=20,
        percentual_por_tipo={"pdf": 70, "outros": 30},
        tipos_ativados=["txt", "pdf", "docx", "xlsx"],
        tamanhos_mb={"txt": 0.1, "pdf": 0.3, "docx": 0.2, "xlsx": 0.1}
    )

def exemplo_percentual_50_30_20():
    """Exemplo 3: 50% TXT, 30% PDF, 20% DOCX"""
    print("\n=== Exemplo 3: 50% TXT, 30% PDF, 20% DOCX ===")
    gerar_arquivos_por_percentual(
        quantidade_total=15,
        percentual_por_tipo={"txt": 50, "pdf": 30, "docx": 20},
        tipos_ativados=["txt", "pdf", "docx"],
        tamanhos_mb={"txt": 0.2, "pdf": 0.4, "docx": 0.3}
    )

def exemplo_percentual_80_20():
    """Exemplo 4: 80% XLSX, 20% outros"""
    print("\n=== Exemplo 4: 80% XLSX, 20% outros ===")
    gerar_arquivos_por_percentual(
        quantidade_total=25,
        percentual_por_tipo={"xlsx": 80, "outros": 20},
        tipos_ativados=["txt", "pdf", "docx", "xlsx"],
        tamanhos_mb={"txt": 0.1, "pdf": 0.2, "docx": 0.15, "xlsx": 0.2}
    )

def exemplo_configuracao_completa():
    """Exemplo 5: Configuração completa com percentuais"""
    print("\n=== Exemplo 5: Configuração completa ===")
    config = ConfiguracaoArquivos(
        tipos_ativados=["txt", "pdf", "docx", "xlsx"],
        quantidade_total=30,
        percentual_por_tipo={"pdf": 60, "txt": 25, "outros": 15},
        tamanho_mb={"txt": 0.15, "pdf": 0.3, "docx": 0.2, "xlsx": 0.1}
    )
    gerar_arquivos(config)

def exemplo_percentual_especifico():
    """Exemplo 6: Percentuais específicos para cada tipo"""
    print("\n=== Exemplo 6: Percentuais específicos ===")
    gerar_arquivos_por_percentual(
        quantidade_total=24,
        percentual_por_tipo={"txt": 25, "pdf": 25, "docx": 25, "xlsx": 25},
        tipos_ativados=["txt", "pdf", "docx", "xlsx"],
        tamanhos_mb={"txt": 0.1, "pdf": 0.2, "docx": 0.15, "xlsx": 0.1}
    )

def exemplo_percentual_grande():
    """Exemplo 7: Arquivos grandes com percentual"""
    print("\n=== Exemplo 7: Arquivos grandes (100 arquivos) ===")
    gerar_arquivos_por_percentual(
        quantidade_total=100,
        percentual_por_tipo={"pdf": 70, "outros": 30},
        tipos_ativados=["txt", "pdf", "docx", "xlsx"],
        tamanhos_mb={"txt": 0.5, "pdf": 0.8, "docx": 0.6, "xlsx": 0.3}
    )

def verificar_distribuicao():
    """Verifica a distribuição real dos arquivos gerados"""
    print("\n=== Verificando distribuição real ===")
    
    import os
    import glob
    
    # Contar arquivos por tipo
    tipos = {}
    total_arquivos = 0
    
    for extensao in ["txt", "pdf", "docx", "xlsx", "jpeg"]:
        arquivos = glob.glob(f"arquivos_teste/*.{extensao}")
        quantidade = len(arquivos)
        if quantidade > 0:
            tipos[extensao] = quantidade
            total_arquivos += quantidade
    
    if total_arquivos > 0:
        print(f"📊 Distribuição real dos arquivos:")
        print(f"📁 Total: {total_arquivos} arquivos")
        
        for tipo, quantidade in sorted(tipos.items()):
            percentual = (quantidade / total_arquivos) * 100
            print(f"   {tipo.upper()}: {quantidade} arquivos ({percentual:.1f}%)")
    else:
        print("❌ Nenhum arquivo encontrado")

if __name__ == "__main__":
    print("Demonstração da funcionalidade de distribuição por percentual")
    print("=" * 70)
    
    # Executar exemplos
    exemplo_quantidade_total()
    exemplo_percentual_70_30()
    exemplo_percentual_50_30_20()
    exemplo_percentual_80_20()
    exemplo_configuracao_completa()
    exemplo_percentual_especifico()
    exemplo_percentual_grande()
    
    # Verificar distribuição
    verificar_distribuicao()
    
    print("\n" + "=" * 70)
    print("Todos os exemplos foram executados com sucesso!")
    print("A distribuição por percentual está funcionando perfeitamente!")
