#!/usr/bin/env python3
"""
Arquivo de configuração para o geraArquivos.py
Permite personalizar facilmente os parâmetros de geração
"""

from geraArquivos import ConfiguracaoArquivos

# =============================================================================
# CONFIGURAÇÕES PRINCIPAIS
# =============================================================================

# Configuração padrão para execução rápida
CONFIGURACAO_PADRAO = ConfiguracaoArquivos(
    tipos_ativados=["txt", "pdf", "docx", "xlsx", "jpeg"],
    quantidade_por_tipo={},  # Vazio = aleatório
    tamanho_mb={
        "txt": 0.1,    # 100KB
        "pdf": 0.3,    # 300KB
        "docx": 0.2,   # 200KB
        "xlsx": 0.1,   # 100KB
        "jpeg": 0.5    # 500KB
    }
)

# Configuração para arquivos pequenos (testes rápidos)
CONFIGURACAO_PEQUENA = ConfiguracaoArquivos(
    tipos_ativados=["txt", "pdf"],
    quantidade_por_tipo={"txt": 2, "pdf": 1},
    tamanho_mb={"txt": 0.05, "pdf": 0.1}
)

# Configuração para arquivos médios (testes normais)
CONFIGURACAO_MEDIA = ConfiguracaoArquivos(
    tipos_ativados=["txt", "pdf", "docx", "xlsx"],
    quantidade_por_tipo={"txt": 3, "pdf": 2, "docx": 2, "xlsx": 2},
    tamanho_mb={"txt": 0.2, "pdf": 0.4, "docx": 0.3, "xlsx": 0.2}
)

# Configuração para arquivos grandes (testes de performance)
CONFIGURACAO_GRANDE = ConfiguracaoArquivos(
    tipos_ativados=["txt", "pdf", "docx", "xlsx"],
    quantidade_por_tipo={"txt": 2, "pdf": 1, "docx": 1, "xlsx": 1},
    tamanho_mb={"txt": 1.0, "pdf": 2.0, "docx": 1.5, "xlsx": 0.5}
)

# Configuração apenas para dados realistas (XLSX)
CONFIGURACAO_DADOS_REALISTAS = ConfiguracaoArquivos(
    tipos_ativados=["xlsx"],
    quantidade_por_tipo={"xlsx": 5},
    tamanho_mb={"xlsx": 0.3}
)

# Configuração apenas para texto Lorem Ipsum
CONFIGURACAO_LOREM_IPSUM = ConfiguracaoArquivos(
    tipos_ativados=["txt", "pdf", "docx"],
    quantidade_por_tipo={"txt": 2, "pdf": 1, "docx": 1},
    tamanho_mb={"txt": 0.5, "pdf": 0.8, "docx": 0.6}
)

# =============================================================================
# CONFIGURAÇÕES ESPECÍFICAS POR TIPO
# =============================================================================

# Configurações específicas para TXT
CONFIG_TXT = {
    "linhas": 20,
    "caracteres_por_linha": 80
}

# Configurações específicas para PDF
CONFIG_PDF = {
    "linhas": 15,
    "caracteres_por_linha": 80
}

# Configurações específicas para DOCX
CONFIG_DOCX = {
    "paragrafos": 8,
    "caracteres_por_paragrafo": 150
}

# Configurações específicas para XLSX
CONFIG_XLSX = {
    "linhas": 50,
    "colunas": 15
}

# Configurações específicas para JPEG
CONFIG_JPEG = {
    "linhas_texto": 50,
    "resolucao": (800, 600)
}

# =============================================================================
# CONFIGURAÇÕES DE EXECUÇÃO
# =============================================================================

# Quantidade de arquivos para geração aleatória
QTD_ARQUIVOS_ALEATORIOS = 10

# Pasta de saída
PASTA_SAIDA = "arquivos_teste"

# Mostrar estatísticas após geração
MOSTRAR_ESTATISTICAS = True

# Limpar arquivos antigos antes de gerar novos
LIMPAR_ANTES = False

# =============================================================================
# FUNÇÕES DE CONVENIÊNCIA
# =============================================================================

def obter_configuracao(nome="padrao"):
    """
    Retorna uma configuração pré-definida
    
    Args:
        nome: Nome da configuração ('padrao', 'pequena', 'media', 'grande', 
              'dados_realistas', 'lorem_ipsum')
    
    Returns:
        ConfiguracaoArquivos
    """
    configuracoes = {
        "padrao": CONFIGURACAO_PADRAO,
        "pequena": CONFIGURACAO_PEQUENA,
        "media": CONFIGURACAO_MEDIA,
        "grande": CONFIGURACAO_GRANDE,
        "dados_realistas": CONFIGURACAO_DADOS_REALISTAS,
        "lorem_ipsum": CONFIGURACAO_LOREM_IPSUM
    }
    
    return configuracoes.get(nome, CONFIGURACAO_PADRAO)

def criar_configuracao_personalizada(tipos, quantidades, tamanhos):
    """
    Cria uma configuração personalizada
    
    Args:
        tipos: Lista de tipos de arquivo
        quantidades: Dicionário com quantidade por tipo
        tamanhos: Dicionário com tamanho em MB por tipo
    
    Returns:
        ConfiguracaoArquivos
    """
    return ConfiguracaoArquivos(
        tipos_ativados=tipos,
        quantidade_por_tipo=quantidades,
        tamanho_mb=tamanhos
    )

# =============================================================================
# EXEMPLOS DE USO
# =============================================================================

if __name__ == "__main__":
    print("🔧 CONFIGURAÇÕES DISPONÍVEIS:")
    print("=" * 50)
    
    configuracoes = [
        ("padrao", "Configuração padrão - todos os tipos"),
        ("pequena", "Arquivos pequenos - testes rápidos"),
        ("media", "Arquivos médios - testes normais"),
        ("grande", "Arquivos grandes - testes de performance"),
        ("dados_realistas", "Apenas XLSX com dados realistas"),
        ("lorem_ipsum", "Apenas texto Lorem Ipsum")
    ]
    
    for nome, descricao in configuracoes:
        config = obter_configuracao(nome)
        print(f"📋 {nome.upper()}: {descricao}")
        print(f"   Tipos: {config.tipos_ativados}")
        print(f"   Tamanhos: {config.tamanho_mb}")
        print()
    
    print("💡 Para usar uma configuração:")
    print("   from configuracao import obter_configuracao")
    print("   config = obter_configuracao('media')")
    print("   from geraArquivos import gerar_arquivos")
    print("   gerar_arquivos(config)")
