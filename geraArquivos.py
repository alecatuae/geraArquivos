import os
import random
import string
from io import BytesIO
from PIL import Image, ImageDraw
from reportlab.pdfgen import canvas
from docx import Document
import pandas as pd
from dataclasses import dataclass
from typing import Dict, List, Optional
from faker import Faker
from lorem_text import lorem

# Pasta onde salvar os arquivos
OUTPUT_DIR = "arquivos_teste"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Instância global do Faker para gerar dados realistas
fake = Faker('pt_BR')  # Português brasileiro

@dataclass
class ConfiguracaoArquivos:
    """Configuração para geração de arquivos"""
    # Tipos de arquivo ativados
    tipos_ativados: List[str] = None
    
    # Quantidade de arquivos por tipo (None = aleatório)
    quantidade_por_tipo: Dict[str, int] = None
    
    # Tamanho alvo em MB para cada tipo
    tamanho_mb: Dict[str, float] = None
    
    # Configurações específicas por tipo
    config_especifica: Dict[str, Dict] = None
    
    def __post_init__(self):
        if self.tipos_ativados is None:
            self.tipos_ativados = ["jpeg", "pdf", "docx", "xlsx", "txt"]
        
        if self.quantidade_por_tipo is None:
            self.quantidade_por_tipo = {}
        
        if self.tamanho_mb is None:
            self.tamanho_mb = {
                "jpeg": 0.5,    # 500KB
                "pdf": 1.0,     # 1MB
                "docx": 0.8,    # 800KB
                "xlsx": 0.3,    # 300KB
                "txt": 0.1      # 100KB
            }
        
        if self.config_especifica is None:
            self.config_especifica = {
                "jpeg": {"linhas_texto": 50, "resolucao": (800, 600)},
                "pdf": {"linhas": 5, "caracteres_por_linha": 80},
                "docx": {"paragrafos": 5, "caracteres_por_paragrafo": 120},
                "xlsx": {"linhas": 20, "colunas": 15},  # 15 colunas com dados realistas
                "txt": {"linhas": 10, "caracteres_por_linha": 80}
            }

# Função para gerar texto aleatório
def texto_aleatorio(tamanho=100):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=tamanho))

# Funções auxiliares para gerar dados realistas com Faker
def gerar_dados_realistas_xlsx(num_linhas):
    """Gera dados realistas para planilha XLSX usando Faker"""
    dados = {
        "ID": [fake.random_int(min=1000, max=9999) for _ in range(num_linhas)],
        "Nome": [fake.name() for _ in range(num_linhas)],
        "Email": [fake.email() for _ in range(num_linhas)],
        "Telefone": [fake.phone_number() for _ in range(num_linhas)],
        "Endereço": [fake.address().replace('\n', ', ') for _ in range(num_linhas)],
        "Cidade": [fake.city() for _ in range(num_linhas)],
        "Estado": [fake.state() for _ in range(num_linhas)],
        "CEP": [fake.postcode() for _ in range(num_linhas)],
        "Data_Nascimento": [fake.date_of_birth(minimum_age=18, maximum_age=80).strftime('%d/%m/%Y') for _ in range(num_linhas)],
        "Profissão": [fake.job() for _ in range(num_linhas)],
        "Empresa": [fake.company() for _ in range(num_linhas)],
        "Salário": [fake.random_int(min=1500, max=15000) for _ in range(num_linhas)],
        "Data_Contrato": [fake.date_between(start_date='-5y', end_date='today').strftime('%d/%m/%Y') for _ in range(num_linhas)],
        "Status": [fake.random_element(elements=('Ativo', 'Inativo', 'Férias', 'Licença')) for _ in range(num_linhas)],
        "Observações": [fake.text(max_nb_chars=100) for _ in range(num_linhas)]
    }
    return dados

# Funções auxiliares para gerar textos longos com Lorem Ipsum
def gerar_texto_lorem_ipsum(tamanho_mb_alvo, tipo_arquivo="txt"):
    """
    Gera texto Lorem Ipsum baseado no tamanho alvo em MB
    
    Args:
        tamanho_mb_alvo: Tamanho alvo em MB
        tipo_arquivo: Tipo do arquivo (txt, pdf, docx)
    
    Returns:
        Lista de strings com o texto gerado
    """
    # Calcular quantidade de caracteres necessários baseado no tamanho
    # Assumindo ~1 caractere = 1 byte para texto simples
    caracteres_necessarios = int(tamanho_mb_alvo * 1024 * 1024)
    
    # Ajustar baseado no tipo de arquivo
    if tipo_arquivo == "pdf":
        # PDF tem overhead de formatação, reduzir em 30%
        caracteres_necessarios = int(caracteres_necessarios * 0.7)
    elif tipo_arquivo == "docx":
        # DOCX tem overhead de XML, reduzir em 50%
        caracteres_necessarios = int(caracteres_necessarios * 0.5)
    
    # Garantir mínimo de caracteres
    caracteres_necessarios = max(caracteres_necessarios, 1000)
    
    textos = []
    caracteres_gerados = 0
    
    while caracteres_gerados < caracteres_necessarios:
        # Gerar parágrafo com tamanho variável
        tamanho_paragrafo = random.randint(50, 200)  # palavras por parágrafo
        paragrafo = lorem.paragraph()
        
        # Se o parágrafo for muito pequeno, gerar mais texto
        while len(paragrafo) < 100:
            paragrafo += " " + lorem.sentence()
        
        textos.append(paragrafo)
        caracteres_gerados += len(paragrafo)
        
        # Adicionar quebra de linha
        if tipo_arquivo == "txt":
            caracteres_gerados += 1  # \n
    
    return textos

def gerar_texto_lorem_por_linhas(num_linhas, caracteres_por_linha=80):
    """
    Gera texto Lorem Ipsum com número específico de linhas
    
    Args:
        num_linhas: Número de linhas a gerar
        caracteres_por_linha: Caracteres por linha
    
    Returns:
        Lista de strings com as linhas geradas
    """
    linhas = []
    
    for i in range(num_linhas):
        # Gerar linha com tamanho variável
        tamanho_linha = random.randint(caracteres_por_linha // 2, caracteres_por_linha)
        
        # Gerar texto até atingir o tamanho desejado
        linha = ""
        while len(linha) < tamanho_linha:
            palavra = lorem.word()
            if len(linha) + len(palavra) + 1 <= tamanho_linha:
                linha += palavra + " " if linha else palavra
            else:
                break
        
        # Adicionar número da linha se for TXT
        if caracteres_por_linha <= 100:  # Assumindo que é TXT
            linha = f"Linha {i+1}: {linha.strip()}"
        
        linhas.append(linha.strip())
    
    return linhas

# Funções auxiliares para controle de tamanho
def calcular_tamanho_arquivo(caminho_arquivo):
    """Calcula o tamanho do arquivo em MB"""
    return os.path.getsize(caminho_arquivo) / (1024 * 1024)

def ajustar_conteudo_para_tamanho(tipo_arquivo, tamanho_mb_alvo, config):
    """Ajusta o conteúdo baseado no tamanho alvo"""
    if tipo_arquivo == "txt":
        # Para TXT: usar Lorem Ipsum baseado no tamanho
        return tamanho_mb_alvo
    
    elif tipo_arquivo == "pdf":
        # Para PDF: usar Lorem Ipsum baseado no tamanho
        return tamanho_mb_alvo
    
    elif tipo_arquivo == "docx":
        # Para DOCX: usar Lorem Ipsum baseado no tamanho
        return tamanho_mb_alvo
    
    elif tipo_arquivo == "xlsx":
        # Para XLSX: estimativa baseada em linhas
        # Considerando ~15 colunas com dados realistas, cada linha ≈ 0.5KB
        # Então 1MB ≈ 2000 linhas
        linhas_necessarias = int(tamanho_mb_alvo * 2000)
        return max(linhas_necessarias, 10)  # Mínimo de 10 linhas
    
    elif tipo_arquivo == "jpeg":
        # Para JPEG: ajustar resolução baseada no tamanho
        if tamanho_mb_alvo <= 0.1:
            return (400, 300)
        elif tamanho_mb_alvo <= 0.5:
            return (800, 600)
        elif tamanho_mb_alvo <= 1.0:
            return (1200, 900)
        else:
            return (1600, 1200)
    
    return config

# Gerar JPEG
def gerar_jpeg(nome, config, tamanho_mb_alvo=None):
    resolucao = config["resolucao"]
    if tamanho_mb_alvo:
        resolucao = ajustar_conteudo_para_tamanho("jpeg", tamanho_mb_alvo, config)
    
    img = Image.new("RGB", resolucao, color=(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    draw = ImageDraw.Draw(img)
    draw.text((10, 10), texto_aleatorio(config["linhas_texto"]), fill=(255,255,255))
    img.save(nome, "JPEG")

# Gerar PDF
def gerar_pdf(nome, config, tamanho_mb_alvo=None):
    if tamanho_mb_alvo:
        # Usar Lorem Ipsum baseado no tamanho
        textos = gerar_texto_lorem_ipsum(tamanho_mb_alvo, "pdf")
    else:
        # Usar configuração padrão
        linhas = config["linhas"]
        textos = gerar_texto_lorem_por_linhas(linhas, config["caracteres_por_linha"])
    
    c = canvas.Canvas(nome)
    y_pos = 800
    
    for texto in textos:
        # Quebrar texto em linhas se necessário
        palavras = texto.split()
        linha_atual = ""
        
        for palavra in palavras:
            if len(linha_atual + " " + palavra) <= 80:  # Limite de caracteres por linha
                linha_atual += " " + palavra if linha_atual else palavra
            else:
                if linha_atual:
                    c.drawString(100, y_pos, linha_atual)
                    y_pos -= 20
                    if y_pos < 50:  # Nova página se necessário
                        c.showPage()
                        y_pos = 800
                linha_atual = palavra
        
        # Desenhar última linha
        if linha_atual:
            c.drawString(100, y_pos, linha_atual)
            y_pos -= 20
            if y_pos < 50:
                c.showPage()
                y_pos = 800
    
    c.save()

# Gerar DOCX
def gerar_docx(nome, config, tamanho_mb_alvo=None):
    if tamanho_mb_alvo:
        # Usar Lorem Ipsum baseado no tamanho
        textos = gerar_texto_lorem_ipsum(tamanho_mb_alvo, "docx")
    else:
        # Usar configuração padrão
        paragrafos = config["paragrafos"]
        textos = []
        for i in range(paragrafos):
            # Gerar parágrafo Lorem Ipsum
            paragrafo = lorem.paragraph()
            while len(paragrafo) < config["caracteres_por_paragrafo"]:
                paragrafo += " " + lorem.sentence()
            textos.append(paragrafo)
    
    doc = Document()
    
    # Adicionar título
    doc.add_heading('Documento Lorem Ipsum', 0)
    
    # Adicionar parágrafos
    for texto in textos:
        doc.add_paragraph(texto)
    
    # Adicionar informações do documento
    doc.add_heading('Informações do Documento', level=1)
    doc.add_paragraph(f'Data de geração: {fake.date_time_this_year().strftime("%d/%m/%Y %H:%M")}')
    doc.add_paragraph(f'ID do documento: {fake.uuid4()}')
    doc.add_paragraph(f'Tamanho alvo: {tamanho_mb_alvo:.2f} MB' if tamanho_mb_alvo else 'Tamanho padrão')
    
    doc.save(nome)

# Gerar XLSX
def gerar_xlsx(nome, config, tamanho_mb_alvo=None):
    linhas = config["linhas"]
    if tamanho_mb_alvo:
        linhas = ajustar_conteudo_para_tamanho("xlsx", tamanho_mb_alvo, config)
    
    # Gerar dados realistas usando Faker
    dados = gerar_dados_realistas_xlsx(linhas)
    df = pd.DataFrame(dados)
    
    # Salvar com formatação melhorada
    with pd.ExcelWriter(nome, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Dados', index=False)
        
        # Ajustar largura das colunas automaticamente
        worksheet = writer.sheets['Dados']
        for column in worksheet.columns:
            max_length = 0
            column_letter = column[0].column_letter
            for cell in column:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(str(cell.value))
                except:
                    pass
            adjusted_width = min(max_length + 2, 50)  # Máximo de 50 caracteres
            worksheet.column_dimensions[column_letter].width = adjusted_width

# Gerar TXT
def gerar_txt(nome, config, tamanho_mb_alvo=None):
    if tamanho_mb_alvo:
        # Usar Lorem Ipsum baseado no tamanho
        textos = gerar_texto_lorem_ipsum(tamanho_mb_alvo, "txt")
    else:
        # Usar configuração padrão
        linhas = config["linhas"]
        textos = gerar_texto_lorem_por_linhas(linhas, config["caracteres_por_linha"])
    
    with open(nome, 'w', encoding='utf-8') as arquivo:
        # Escrever cabeçalho
        arquivo.write("=" * 80 + "\n")
        arquivo.write("DOCUMENTO LOREM IPSUM\n")
        arquivo.write("=" * 80 + "\n\n")
        
        # Escrever conteúdo Lorem Ipsum
        for i, texto in enumerate(textos, 1):
            arquivo.write(f"Parágrafo {i}:\n")
            arquivo.write(texto + "\n\n")
        
        # Escrever rodapé
        arquivo.write("=" * 80 + "\n")
        arquivo.write("INFORMAÇÕES DO DOCUMENTO\n")
        arquivo.write("=" * 80 + "\n")
        arquivo.write(f"Data de geração: {fake.date_time_this_year().strftime('%d/%m/%Y %H:%M')}\n")
        arquivo.write(f"ID do arquivo: {fake.uuid4()}\n")
        arquivo.write(f"Tamanho alvo: {tamanho_mb_alvo:.2f} MB\n" if tamanho_mb_alvo else "Tamanho padrão\n")
        arquivo.write(f"Total de parágrafos: {len(textos)}\n")
        arquivo.write("=" * 80 + "\n")

# Função principal
def gerar_arquivos(config: ConfiguracaoArquivos = None, qtd_total=None):
    """
    Gera arquivos baseado na configuração fornecida
    
    Args:
        config: ConfiguracaoArquivos com parâmetros de geração
        qtd_total: Quantidade total de arquivos (ignora quantidade_por_tipo se especificado)
    """
    if config is None:
        config = ConfiguracaoArquivos()
    
    # Determinar quantos arquivos gerar de cada tipo
    arquivos_para_gerar = {}
    
    if qtd_total is not None:
        # Modo aleatório: distribuir qtd_total entre tipos ativados
        for i in range(qtd_total):
            tipo = random.choice(config.tipos_ativados)
            arquivos_para_gerar[tipo] = arquivos_para_gerar.get(tipo, 0) + 1
    else:
        # Modo controlado: usar quantidade_por_tipo
        for tipo in config.tipos_ativados:
            if tipo in config.quantidade_por_tipo:
                arquivos_para_gerar[tipo] = config.quantidade_por_tipo[tipo]
            else:
                # Se não especificado, gerar 1 arquivo do tipo
                arquivos_para_gerar[tipo] = 1
    
    # Gerar os arquivos
    contador_global = 1
    for tipo, quantidade in arquivos_para_gerar.items():
        for i in range(quantidade):
            nome = os.path.join(OUTPUT_DIR, f"arquivo_{contador_global}.{tipo}")
            tamanho_alvo = config.tamanho_mb.get(tipo, 0.5)
            config_tipo = config.config_especifica.get(tipo, {})
            
            try:
                if tipo == "jpeg":
                    gerar_jpeg(nome, config_tipo, tamanho_alvo)
                elif tipo == "pdf":
                    gerar_pdf(nome, config_tipo, tamanho_alvo)
                elif tipo == "docx":
                    gerar_docx(nome, config_tipo, tamanho_alvo)
                elif tipo == "xlsx":
                    gerar_xlsx(nome, config_tipo, tamanho_alvo)
                elif tipo == "txt":
                    gerar_txt(nome, config_tipo, tamanho_alvo)
                
                tamanho_real = calcular_tamanho_arquivo(nome)
                print(f"[OK] Gerado: {nome} ({tamanho_real:.2f} MB)")
                contador_global += 1
                
            except Exception as e:
                print(f"[ERRO] Falha ao gerar {nome}: {e}")

# Funções de conveniência para configurações comuns
def gerar_arquivos_aleatorios(qtd=20, tipos_ativados=None):
    """Gera arquivos aleatoriamente"""
    config = ConfiguracaoArquivos()
    if tipos_ativados:
        config.tipos_ativados = tipos_ativados
    gerar_arquivos(config, qtd)

def gerar_arquivos_por_tipo(quantidade_por_tipo, tamanhos_mb=None):
    """Gera arquivos com quantidade específica por tipo"""
    config = ConfiguracaoArquivos()
    config.quantidade_por_tipo = quantidade_por_tipo
    if tamanhos_mb:
        config.tamanho_mb.update(tamanhos_mb)
    gerar_arquivos(config)

if __name__ == "__main__":
    # Exemplo de uso com configuração personalizada
    print("=== Gerando arquivos com configuração personalizada ===")
    
    # Configuração 1: Apenas TXT e PDF, tamanhos específicos
    config1 = ConfiguracaoArquivos(
        tipos_ativados=["txt", "pdf"],
        quantidade_por_tipo={"txt": 3, "pdf": 2},
        tamanho_mb={"txt": 0.2, "pdf": 0.5}
    )
    gerar_arquivos(config1)
    
    print("\n=== Gerando arquivos aleatoriamente ===")
    # Configuração 2: Modo aleatório
    gerar_arquivos_aleatorios(10, ["jpeg", "xlsx", "txt"])
