#!/usr/bin/env python3
"""
Exemplos específicos para demonstrar a funcionalidade Lorem Ipsum no geraArquivos.py
"""

from geraArquivos import ConfiguracaoArquivos, gerar_arquivos, gerar_arquivos_por_tipo

def exemplo_txt_pequeno():
    """Exemplo 1: TXT pequeno (0.1 MB) com Lorem Ipsum"""
    print("=== Exemplo 1: TXT pequeno (0.1 MB) com Lorem Ipsum ===")
    gerar_arquivos_por_tipo(
        quantidade_por_tipo={"txt": 1},
        tamanhos_mb={"txt": 0.1}
    )

def exemplo_txt_grande():
    """Exemplo 2: TXT grande (0.5 MB) com Lorem Ipsum"""
    print("\n=== Exemplo 2: TXT grande (0.5 MB) com Lorem Ipsum ===")
    gerar_arquivos_por_tipo(
        quantidade_por_tipo={"txt": 1},
        tamanhos_mb={"txt": 0.5}
    )

def exemplo_pdf_medio():
    """Exemplo 3: PDF médio (0.3 MB) com Lorem Ipsum"""
    print("\n=== Exemplo 3: PDF médio (0.3 MB) com Lorem Ipsum ===")
    gerar_arquivos_por_tipo(
        quantidade_por_tipo={"pdf": 1},
        tamanhos_mb={"pdf": 0.3}
    )

def exemplo_docx_grande():
    """Exemplo 4: DOCX grande (0.8 MB) com Lorem Ipsum"""
    print("\n=== Exemplo 4: DOCX grande (0.8 MB) com Lorem Ipsum ===")
    gerar_arquivos_por_tipo(
        quantidade_por_tipo={"docx": 1},
        tamanhos_mb={"docx": 0.8}
    )

def exemplo_misto_lorem():
    """Exemplo 5: Mistura de tipos com Lorem Ipsum"""
    print("\n=== Exemplo 5: Mistura de tipos com Lorem Ipsum ===")
    config = ConfiguracaoArquivos(
        tipos_ativados=["txt", "pdf", "docx"],
        quantidade_por_tipo={"txt": 1, "pdf": 1, "docx": 1},
        tamanho_mb={"txt": 0.2, "pdf": 0.4, "docx": 0.6}
    )
    gerar_arquivos(config)

def exemplo_configuracao_personalizada():
    """Exemplo 6: Configuração personalizada com Lorem Ipsum"""
    print("\n=== Exemplo 6: Configuração personalizada ===")
    config = ConfiguracaoArquivos(
        tipos_ativados=["txt", "pdf"],
        quantidade_por_tipo={"txt": 2, "pdf": 1},
        tamanho_mb={"txt": 0.15, "pdf": 0.25},
        config_especifica={
            "txt": {"linhas": 20, "caracteres_por_linha": 100},
            "pdf": {"linhas": 15, "caracteres_por_linha": 90}
        }
    )
    gerar_arquivos(config)

def verificar_conteudo_lorem():
    """Verifica o conteúdo Lorem Ipsum nos arquivos gerados"""
    print("\n=== Verificando conteúdo Lorem Ipsum ===")
    
    import os
    import glob
    
    # Verificar arquivo TXT mais recente
    arquivos_txt = glob.glob("arquivos_teste/*.txt")
    if arquivos_txt:
        arquivo_mais_recente = max(arquivos_txt, key=os.path.getctime)
        print(f"Arquivo TXT: {arquivo_mais_recente}")
        print(f"Tamanho: {os.path.getsize(arquivo_mais_recente) / (1024*1024):.2f} MB")
        
        with open(arquivo_mais_recente, 'r', encoding='utf-8') as f:
            conteudo = f.read()
            print(f"Caracteres: {len(conteudo)}")
            print(f"Parágrafos: {conteudo.count('Parágrafo')}")
            print("Primeiras 3 linhas:")
            print('\n'.join(conteudo.split('\n')[:3]))
    
    # Verificar arquivo PDF mais recente
    arquivos_pdf = glob.glob("arquivos_teste/*.pdf")
    if arquivos_pdf:
        arquivo_mais_recente = max(arquivos_pdf, key=os.path.getctime)
        print(f"\nArquivo PDF: {arquivo_mais_recente}")
        print(f"Tamanho: {os.path.getsize(arquivo_mais_recente) / (1024*1024):.2f} MB")
    
    # Verificar arquivo DOCX mais recente
    arquivos_docx = glob.glob("arquivos_teste/*.docx")
    if arquivos_docx:
        arquivo_mais_recente = max(arquivos_docx, key=os.path.getctime)
        print(f"\nArquivo DOCX: {arquivo_mais_recente}")
        print(f"Tamanho: {os.path.getsize(arquivo_mais_recente) / (1024*1024):.2f} MB")

if __name__ == "__main__":
    print("Demonstração da funcionalidade Lorem Ipsum")
    print("=" * 60)
    
    # Executar exemplos
    exemplo_txt_pequeno()
    exemplo_txt_grande()
    exemplo_pdf_medio()
    exemplo_docx_grande()
    exemplo_misto_lorem()
    exemplo_configuracao_personalizada()
    
    # Verificar conteúdo gerado
    verificar_conteudo_lorem()
    
    print("\n" + "=" * 60)
    print("Todos os exemplos foram executados com sucesso!")
    print("Os arquivos TXT, PDF e DOCX agora contêm texto Lorem Ipsum!")
