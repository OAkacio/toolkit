# **TOOLKIT**

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

Este repositório contém uma suíte modular desenvolvida em Python focada na padronização de visualizações científicas e na organização de logs de terminal. O projeto oferece um conjunto de utilitários que simplificam a geração de gráficos com qualidade de publicação e a estruturação de saídas no console, otimizando o monitoramento e a apresentação de dados oriundos de simulações numéricas complexas.

## Autoria

**Victor Moreira Acacio**

Instituto de Astronomia, Geofísica e Ciências Atmosféricas da Universidade de São Paulo (IAG-USP)

GitHub: [@OAkacio](https://github.com/OAkacio)

ORCID: [0009-0007-4484-2129](https://orcid.org/0009-0007-4484-2129)

## Instalação

Clone este repositório e instale as dependências executando os seguintes comandos no seu terminal:

```bash
git clone [https://github.com/OAkacio/toolkit.git](https://github.com/OAkacio/toolkit.git)
cd toolkit
pip install -r requirements.txt
```

## Uso

O código foi projetado para atuar como uma biblioteca utilitária em seus scripts principais. Você pode importar os módulos de gráficos e de sistema de forma independente para estilizar seus dados e o fluxo de execução.

**1. Gráficos de Linha Simples e Destacados:** Para gerar visualizações limpas e minimalistas com a função `basic`, ou destacar pontos críticos (como máximos ou mínimos) utilizando a função `basicdot`, importe o módulo de gráficos:

```python
from toolkit import graphs

graphs.basic(vecx, vecy, titulo="Evolução Temporal", save=True, nome="plot_basico")
graphs.basicdot(vecx, vecy, ponto_destaque=(x0, y0), label_ponto="Máximo Local")
```

**2. Gráficos Comparativos:** Para plotar múltiplas curvas num mesmo eixo com gestão automática de paletas de cores (via colormaps) e formatação otimizada, utilize a função `multi`:

```python
graphs.multi(lista_x, lista_y, nomes_curvas=["Modelo A", "Modelo B"], cor_estilo="random")
```

**3. Análise Estatística e Espaço de Parâmetros:** Para visualizar mapas de calor com elipses de confiança e pontos de melhor ajuste (ideal para matrizes de $\chi^2$), a função `elipse` oferece suporte nativo a formatação matemática:

```python
graphs.elipse(X, Y, Z, ponto_destaque=(best_m, best_l), niveis_elipse=[1.0, 2.0])
```

**4. Estilização de Logs de Execução:** Para separar visualmente etapas de simulação no terminal, utilize os cabeçalhos em estilo *double-line* e os indicadores de status do módulo de sistema:

```python
from toolkit import system

system.header("Início da Simulação Numérica", versao="1.0", regime="MHD")
system.status("Calculando integração de malha...")
system.space(altura=2)
```

**5. Apresentação de Dados em Terminal:** Para exibir metadados técnicos com alinhamento vertical e contraste de cores, ou desenhar tabelas estruturadas (ASCII Grid), utilize:

```python
system.param(["Densidade", 1.5, "g/cm³"], ["Velocidade", 400, "km/s"])
system.table(lista_de_dicionarios)
```

## Arquitetura Visual e Lógica de Renderização

A construção dos utilitários apoia-se na abstração de rotinas comuns de formatação. O processamento ocorre em duas frentes:

**1. Módulo `graphs.py` (Visualização Científica):** Encapsula chamadas detalhadas do *Matplotlib*, garantindo padronização estética. Todas as funções incluem recursos como:
* Layout adaptativo (`tight_layout()`) para exportação sem cortes em resoluções de até 600 DPI.
* Opção de desativação de bordas superiores e direitas (Spines) para uma estética mais limpa e moderna.
* Criação automática do diretório local `figures/` ao habilitar o salvamento em disco (`save=True`).

**2. Módulo `system.py` (Feedback de Console):** Emprega códigos de escape ANSI e caracteres Unicode para estruturação visual no terminal, operando sem dependências externas. A biblioteca gerencia dinamicamente o cálculo de comprimentos de strings para garantir que colunas, sinais de igualdade ($=$) e bordas de cabeçalho mantenham um alinhamento simétrico independente do volume de dados iterado.

## Estrutura do Projeto:

```bash
├── figures/               # Diretório (gerado automaticamente) para gráficos de saída (.png, .pdf)
├── toolkit/               # Módulo principal de ferramentas
│   ├── __pycache__/       # Arquivos compilados do Python
│   ├── graphs.py          # Utilitários de plotagem baseados no Matplotlib
│   └── system.py          # Utilitários de estilização e log de terminal (ANSI)
├── src/                   # Diretório de códigos-fonte secundários
│   └── __pycache__/       # Arquivos compilados ignorados pelo git
├── .gitignore             # Bloqueio de subdiretórios de cache e arquivos temporários
└── requirements.txt       # Arquivo de dependências
```


## Motivação

Este repositório foi consolidado para agilizar o desenvolvimento de projetos acadêmicos e científicos. Ao centralizar e automatizar rotinas visuais repetitivas, o foco é transferido da formatação manual (especialmente para a adequação de relatórios em LaTeX e documentação científica) para a física e a qualidade do código propriamente ditos, reforçando as práticas de _Open Science_.

## Referências

* HUNTER, J. D. **Matplotlib: A 2D graphics environment**. Computing in Science & Engineering, v. 9, n. 3, p. 90-95, 2007. Disponível em: https://matplotlib.org/.
* **ANSI Escape Codes**: Standard ECMA-48. Control Functions for Coded Character Sets. Disponível em: https://ecma-international.org/.