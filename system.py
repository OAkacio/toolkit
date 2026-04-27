#
# * =============================================================================
# * SYSTEM
# * =============================================================================


def header(titulo, largura=80, **kwargs):
    """
    Gera um cabeçalho visual elegante com bordas duplas, cores e metadados.

    Esta função cria uma moldura estruturada utilizando caracteres de desenho
    de caixa Unicode (estilo double-line) e códigos de escape ANSI para criar
    uma separação visual sofisticada e profissional em terminais.

    (  "Meu título", var1=valor1, var2=valor2 ... )

    Parâmetros
    ----------
    titulo : str
        O texto principal a ser exibido no centro do cabeçalho.
    largura : int, opcional
        A largura total da moldura em caracteres. O padrão é 80.
    **kwargs : dict, opcional
        Informações adicionais para exibir abaixo do título, formatadas como
        'CHAVE: VALOR' e separadas por um marcador central (•).

    Notas
    -----
    A função utiliza uma paleta de cores fixa para garantir elegância:
    - Ouro (Gold): Para o título principal.
    - Ciano (Cyan): Para os metadados (kwargs).
    - Cinza (Gray): Para as bordas e separadores, reduzindo ruído visual.
    A moldura utiliza caracteres Unicode (╔, ═, ╗, etc.) que podem não ser
    renderizados corretamente em terminais legados sem suporte a UTF-8.
    """
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    GOLD = "\033[33m"
    GRAY = "\033[90m"
    RESET = "\033[0m"
    TL, TR = "╔", "╗"
    BL, BR = "╚", "╝"
    HL, VL = "═", "║"
    DIV_L, DIV_R = "╠", "╣"
    titulo_formatado = f" {titulo.upper()} "
    print("\n" * 2)
    print(f"{GRAY}{TL}{HL * (largura - 2)}{TR}{RESET}")
    espaco_interno = largura - 2
    print(
        f"{GRAY}{VL}{RESET}{BOLD}{GOLD}{titulo_formatado:^{espaco_interno}}{RESET}{GRAY}{VL}{RESET}"
    )
    if kwargs:
        print(f"{GRAY}{DIV_L}{HL * (largura - 2)}{DIV_R}{RESET}")
        info_str = "  •  ".join([f"{k.upper()}: {v}" for k, v in kwargs.items()])
        print(
            f"{GRAY}{VL}{RESET}{CYAN}{info_str:^{espaco_interno}}{RESET}{GRAY}{VL}{RESET}"
        )
    print(f"{GRAY}{BL}{HL * (largura - 2)}{BR}{RESET}")
    print("\n")


def status(msg):
    """
    Exibe uma mensagem de status minimalista e formatada no terminal.

    Esta função gera uma saída visual discreta para indicar o progresso ou o
    início de novas etapas no script. Ela utiliza um marcador colorido e
    espaçamento estratégico para manter a organização sem poluir o terminal.

    (  "Minha Mensagem"  )

    Parâmetros
    ----------
    msg : str
        O texto descritivo do status ou evento atual a ser exibido.

    Notas
    -----
    A saída é composta por uma quebra de linha inicial, seguida pelo caractere
    '»' (chevron duplo) estilizado em azul e negrito. O texto da mensagem é
    exibido logo após o marcador, mantendo um recuo padrão à esquerda.
    """
    BLUE = "\033[94m"
    BOLD = "\033[1m"
    RESET = "\033[0m"
    print(f"\n  {BLUE}{BOLD}»{RESET} {msg}")


def param(*items, indent=6):
    """
    Exibe múltiplos parâmetros com alinhamento vertical e contraste de cores.

    Esta função processa uma coleção de parâmetros e formata a saída para que
    os nomes, os separadores de igualdade e as unidades físicas fiquem
    perfeitamente alinhados, facilitando a leitura de dados técnicos e
    relatórios científicos no terminal.

    (  ("Meu valor é", valor1, "unidade1") , ("Meu valor é", valor2, "unidade2")... )

    Parâmetros
    ----------
    *items : list ou tuple
        Um número variável de sequências. Cada item deve conter:
        - nome (str): O identificador do parâmetro.
        - valor (any): O valor numérico ou textual associado.
        - unidade (str, opcional): A unidade física de medida.
    indent : int, opcional
        O número de espaços iniciais para o recuo do bloco no terminal.
        O padrão é 6.

    Notas
    -----
    A função utiliza uma paleta de cores técnica para otimizar a leitura:
    - Negrito (Bold): Destaca os nomes das variáveis à esquerda.
    - Ciano (Cyan): Realça os valores numéricos (dados centrais).
    - Cinza (Gray): Suaviza os elementos estruturais (= e colchetes).
    O cálculo de largura é feito antes da inserção dos códigos ANSI,
    garantindo que o alinhamento não seja quebrado por caracteres invisíveis.
    """
    if not items:
        return

    BOLD = "\033[1m"
    CYAN = "\033[36m"
    GRAY = "\033[90m"
    RESET = "\033[0m"

    processados = []
    for item in items:
        nome = str(item[0])
        val = str(item[1])
        unidade = str(item[2]) if len(item) > 2 else ""
        processados.append((nome, val, unidade))

    largura_n = max(len(p[0]) for p in processados)
    largura_v = max(len(p[1]) for p in processados)

    espacamento = " " * indent

    for n, v, u in processados:
        nome_fmt = f"{BOLD}{n.ljust(largura_n)}{RESET}"
        separador = f"{GRAY}={RESET}"
        valor_fmt = f"{CYAN}{v.rjust(largura_v)}{RESET}"
        unidade_fmt = f" {GRAY}[{u}]{RESET}" if u else ""

        print(f"{espacamento}{nome_fmt} {separador} {valor_fmt}{unidade_fmt}")


def space(altura=3):
    """
    Insere um distanciamento vertical no output do terminal.

    Esta função gera um respiro visual no console através da impressão de
    quebras de linha, permitindo separar seções de execução e evitar que a
    saída de dados fique visualmente congestionada.

    Parâmetros
    ----------
    altura : int, opcional
        O número de quebras de linha a serem impressas.
        O padrão é 3.

    Notas
    -----
    A função foca exclusivamente no deslocamento vertical do cursor, sem
    adicionar caracteres, marcadores ou qualquer poluição visual, sendo
    ideal para manter a sobriedade em logs e relatórios de terminal.
    """
    print("\n" * altura)


def table(dados):
    """
    Formata e exibe uma lista de dicionários em uma estrutura de tabela ASCII.

    Esta função transforma dados estruturados em uma representação visual
    organizada, calculando dinamicamente a largura das colunas para garantir
    o alinhamento perfeito de cabeçalhos e valores no terminal.

    (    [{"COLUNA 1": "val1", "COLUNA 2": "val2"}, {"COLUNA 1": "val3", "COLUNA 2": "val4"}] )

    Parâmetros
    ----------
    dados : list of dict
        Uma lista contendo dicionários, onde as chaves representam os nomes
        das colunas e os valores representam o conteúdo de cada linha.

    Notas
    -----
    A função aplica uma lógica de alinhamento inteligente para otimizar a
    escaneabilidade:
    - Cabeçalhos: Centralizados e destacados em negrito e ciano.
    - Números: Alinhados à direita (facilitando a leitura de casas decimais).
    - Textos: Alinhados à esquerda.
    A moldura utiliza um estilo clássico de grade (ASCII Grid) que delimita
    claramente a separação entre metadados e o corpo dos dados.
    """
    if not dados:
        print("A lista está vazia.")
        return
    colunas = list(dados[0].keys())
    larguras = {}
    for coluna in colunas:
        max_valor = max([len(str(item[coluna])) for item in dados])
        larguras[coluna] = max(max_valor, len(coluna))
    separador_horizontal = (
        "+" + "+".join(["-" * (larguras[c] + 2) for c in colunas]) + "+"
    )
    BOLD = "\033[1m"
    RESET = "\033[0m"
    CYAN = "\033[36m"
    print(separador_horizontal)
    header_str = "|"
    for c in colunas:
        header_str += f" {BOLD}{CYAN}{c.upper().center(larguras[c])}{RESET} |"
    print(header_str)
    print(separador_horizontal)
    for item in dados:
        linha = "|"
        for c in colunas:
            valor = str(item[c])
            if valor.replace(".", "", 1).isdigit():
                linha += f" {valor.rjust(larguras[c])} |"
            else:
                linha += f" {valor.ljust(larguras[c])} |"
        print(linha)
    print(separador_horizontal)
