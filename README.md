# 🚀 GeraArquivos - Gerador de Arquivos de Teste

Sistema simples para gerar arquivos de teste em diferentes formatos (JPEG, PNG, PDF, DOCX, XLSX, TXT) com conteúdo realista.

## 🎯 O que faz?

Cria automaticamente arquivos de teste com:
- **Imagens**: JPEG e PNG com wordclouds coloridos
- **Documentos**: PDF e DOCX com texto Lorem Ipsum
- **Planilhas**: XLSX com dados de funcionários
- **Texto**: TXT com conteúdo estruturado

## 📚 Documentação

| Arquivo | Propósito | Para quem |
|---------|-----------|-----------|
| **[setup.md](setup.md)** | 🛠️ Instalação completa do Python e dependências | Iniciantes |
| **[howto.md](howto.md)** | 📖 Guia de uso prático com exemplos | Todos os usuários |
| **[GERADOR_INFINITO.md](GERADOR_INFINITO.md)** | 🔄 Gerador em loop infinito para testes de storage | Testes avançados |

## 🚀 Início Rápido

### 1. Instalação
Siga o guia completo em **[setup.md](setup.md)** para instalar Python e dependências.

### 2. Uso Básico
```bash
# Ativar ambiente
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Gerar 10 arquivos
python -c "from geraArquivos import gerar; gerar(10)"
```

### 3. Exemplos Práticos
Veja **[howto.md](howto.md)** para exemplos detalhados e comandos prontos para usar.

## 🎯 Funcionalidades Principais

### 📁 Tipos de Arquivo Suportados
- **JPEG/PNG**: Imagens com wordclouds coloridos
- **PDF**: Documentos com texto Lorem Ipsum
- **DOCX**: Documentos Word estruturados
- **XLSX**: Planilhas com dados de funcionários
- **TXT**: Arquivos de texto simples

### 🎨 Templates Pré-definidos
- **`equilibrado`**: Distribuição balanceada (padrão)
- **`foco_imagens`**: 60% imagens (JPEG/PNG)
- **`foco_documentos`**: 70% documentos (PDF/DOCX)
- **`foco_dados`**: 50% planilhas (XLSX)
- **`minimal`**: Apenas TXT e PDF

### 🔧 Configuração
- **config.json**: Todas as configurações centralizadas
- **Nomes únicos**: SHA-1 para evitar conflitos
- **Tamanhos personalizáveis**: Controle de MB por tipo
- **Diretórios customizáveis**: Escolha onde salvar

### 🔄 Gerador Infinito (Avançado)
- **Loop infinito**: Para testes de storage contínuos
- **Monitoramento**: Estatísticas em tempo real
- **Teste de deduplicação**: Validar eficiência de storage
- **Simulação de carga**: Popular storage com dados realistas

## 📁 Estrutura do Projeto

```
geraArquivos/
├── geraArquivos.py          # Módulo principal
├── config.json              # Configurações
├── requirements.txt         # Dependências
├── setup.md                # Guia de instalação
├── howto.md                # Guia de uso
├── GERADOR_INFINITO.md      # Gerador em loop infinito
├── gerador_infinito.sh      # Script de loop infinito
├── teste_gerador.sh         # Script de teste
├── README.md               # Este arquivo
├── ativar_ambiente.sh        # Script Linux/Mac
├── ativar_ambiente.bat     # Script Windows
└── venv/                   # Ambiente virtual
```

## 🚀 Exemplos Rápidos

### Uso Mais Simples
```bash
# Gerar 20 arquivos
python -c "from geraArquivos import gerar; gerar(20)"
```

### Com Template Específico
```bash
# Focar em imagens
python -c "from geraArquivos import gerar; gerar(30, 'foco_imagens', 'imagens')"
```

### Com Diretório Personalizado
```bash
# Salvar em pasta específica
python -c "from geraArquivos import gerar; gerar(50, 'equilibrado', 'meus_arquivos')"
```

### Gerador Infinito (Avançado)
```bash
# Teste inicial (3 iterações)
./teste_gerador.sh

# Execução infinita para testes de storage
./gerador_infinito.sh
```

## 📚 Próximos Passos

1. **📖 [setup.md](setup.md)** - Instalação completa
2. **📖 [howto.md](howto.md)** - Exemplos práticos e comandos
3. **🧪 Teste básico** - Comece com `gerar(5)`
4. **🎯 Explore templates** - Teste diferentes distribuições
5. **🔄 [GERADOR_INFINITO.md](GERADOR_INFINITO.md)** - Para testes de storage avançados

---

**🎉 Pronto para gerar arquivos de teste!**