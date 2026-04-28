#
# * =============================================================================
# * SYSTEM
# * =============================================================================
#

import os


def header(title, width=80, **kwargs):
    """
    Gera um cabeçalho visual com bordas duplas, cores e metadados no terminal.

    Args:
        title (str): O texto principal a ser exibido no centro do cabeçalho.
        width (int, optional): A largura total da moldura em caracteres. Default é 80.
        **kwargs: Informações adicionais exibidas abaixo do título, formatadas como 'CHAVE: VALOR'.

    Returns:
        None

    Example:
        >>> sy.header("Iniciando Simulação", width=60, autor="Victor", grid="1024x1024")
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

    formatted_title = f" {title.upper()} "
    inner_space = width - 2

    print("\n" * 2)
    print(f"{GRAY}{TL}{HL * inner_space}{TR}{RESET}")
    print(
        f"{GRAY}{VL}{RESET}{BOLD}{GOLD}{formatted_title:^{inner_space}}{RESET}{GRAY}{VL}{RESET}"
    )

    if kwargs:
        print(f"{GRAY}{DIV_L}{HL * inner_space}{DIV_R}{RESET}")
        info_str = "  |  ".join([f"{k.upper()}: {v}" for k, v in kwargs.items()])
        print(
            f"{GRAY}{VL}{RESET}{CYAN}{info_str:^{inner_space}}{RESET}{GRAY}{VL}{RESET}"
        )

    print(f"{GRAY}{BL}{HL * inner_space}{BR}{RESET}")
    print("\n")


def status(message):
    """
    Exibe uma mensagem de status minimalista e formatada no terminal.

    Args:
        message (str): O texto descritivo do status ou evento atual a ser exibido.

    Returns:
        None

    Example:
        >>> sy.status("Calculando distâncias cosmológicas...")
    """
    BLUE = "\033[94m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

    print(f"\n  {BLUE}{BOLD}»{RESET} {message}")


def param(*items, indent=6):
    """
    Exibe múltiplos parâmetros com alinhamento vertical e contraste de cores.

    Args:
        *items (tuple): Sequências contendo (nome, valor, [unidade]).
        indent (int, optional): O número de espaços iniciais para o recuo no terminal. Default é 6.

    Returns:
        None

    Example:
        >>> sy.param(("Velocidade Inicial", 300, "km/s"), ("Densidade", 1e5, "cm^-3"))
    """
    if not items:
        return

    BOLD = "\033[1m"
    CYAN = "\033[36m"
    GRAY = "\033[90m"
    RESET = "\033[0m"

    processed = []
    for item in items:
        name = str(item[0])
        val = str(item[1])
        unit = str(item[2]) if len(item) > 2 else ""
        processed.append((name, val, unit))

    name_width = max(len(p[0]) for p in processed)
    val_width = max(len(p[1]) for p in processed)
    spacing = " " * indent

    for n, v, u in processed:
        name_fmt = f"{BOLD}{n.ljust(name_width)}{RESET}"
        separator = f"{GRAY}={RESET}"
        val_fmt = f"{CYAN}{v.rjust(val_width)}{RESET}"
        unit_fmt = f" {GRAY}[{u}]{RESET}" if u else ""

        print(f"{spacing}{name_fmt} {separator} {val_fmt}{unit_fmt}")


def space(height=3):
    """
    Insere um distanciamento vertical no output do terminal.

    Args:
        height (int, optional): O número de quebras de linha a serem impressas. Default é 3.

    Returns:
        None

    Example:
        >>> sy.space(height=2)
    """
    print("\n" * height)


def table(*axes, mode="column", **kwargs):
    """
    Formata e exibe dados em uma estrutura de tabela ASCII.

    Args:
        *axes (tuple): Tuplas contendo os dados.
        mode (str, optional): Define se as tuplas representam 'column' (coluna) ou 'row' (linha). Default é 'column'.
        **kwargs: Permite passar os eixos de forma nomeada.

    Returns:
        None

    Example:
        >>> sy.table(("ID", 1, 2), ("NOME", "Estrela A", "Estrela B"), mode="column")
    """
    inputs = list(axes) + list(kwargs.values())

    if not inputs:
        print("A lista está vazia.")
        return

    data = []
    if mode == "column":
        keys = [str(axis[0]) for axis in inputs]
        row_values = zip(*[axis[1:] for axis in inputs])
        for values in row_values:
            data.append(dict(zip(keys, values)))

    elif mode == "row":
        keys = [str(c) for c in inputs[0]]
        row_lines = inputs[1:]
        for values in row_lines:
            data.append(dict(zip(keys, values)))

    else:
        print(f"Tipo '{mode}' inválido. Use mode='column' ou mode='row'.")
        return

    if not data:
        print("A lista está vazia.")
        return

    columns = list(data[0].keys())
    widths = {}

    for col in columns:
        max_val_len = max([len(str(item[col])) for item in data])
        widths[col] = max(max_val_len, len(col))

    horizontal_separator = (
        "+" + "+".join(["-" * (widths[c] + 2) for c in columns]) + "+"
    )

    BOLD = "\033[1m"
    RESET = "\033[0m"
    CYAN = "\033[36m"

    print(horizontal_separator)
    header_str = "|"
    for c in columns:
        header_str += f" {BOLD}{CYAN}{c.upper().center(widths[c])}{RESET} |"
    print(header_str)
    print(horizontal_separator)

    for item in data:
        line_str = "|"
        for c in columns:
            val = str(item[c])
            if val.replace(".", "", 1).isdigit():
                line_str += f" {val.rjust(widths[c])} |"
            else:
                line_str += f" {val.ljust(widths[c])} |"
        print(line_str)

    print(horizontal_separator)


def cin(message, expected_type="string"):
    """
    Recebe e valida a entrada do usuário com um visual colorido no terminal.

    Args:
        message (str): A mensagem ou pergunta a ser exibida para o usuário.
        expected_type (str, optional): Tipo de dado ('int', 'float' ou 'string'). Default é 'string'.

    Returns:
        any: O valor inserido pelo usuário convertido para o tipo especificado.

    Example:
        >>> limite_max = sy.cin("Insira o limite superior da integração", expected_type="float")
    """
    GOLD = "\033[33m"
    CYAN = "\033[36m"
    GRAY = "\033[90m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

    question_mark = f"{GOLD}{BOLD}?{RESET}"
    error_mark = f"{RED}{BOLD}!{RESET}"
    cursor = f"{CYAN}»{RESET}"

    while True:
        prompt = (
            f"\n  {question_mark} {message} {GRAY}[{expected_type}]{RESET} {cursor} "
        )
        user_input = input(prompt)

        try:
            if expected_type.lower() == "int":
                return int(user_input)
            elif expected_type.lower() == "float":
                return float(user_input.replace(",", "."))
            elif expected_type.lower() == "string":
                return str(user_input)
            else:
                print(
                    f"\n  {error_mark} {GRAY}Erro: Formato '{expected_type}' não reconhecido. Use 'int', 'float' ou 'string'.{RESET}"
                )
                return None
        except ValueError:
            print(
                f"  {error_mark} {GRAY}Entrada inválida. Insira um valor numérico do tipo '{expected_type}'.{RESET}"
            )


def ok(messages, is_ok=True):
    """
    Exibe uma confirmação visual estilizada de sucesso ou falha no terminal.

    Args:
        messages (str ou list): Mensagem única ou lista de mensagens a serem exibidas.
        is_ok (bool, optional): Se True, exibe a tag [OK] em ciano. Se False, exibe [NOK] em vermelho. Default é True.

    Returns:
        None

    Example:
        >>> sy.ok("Matriz de densidade carregada")
        >>> sy.ok(["Arquivo corrompido", "Dados em branco"], is_ok=False)
    """
    BLUE = "\033[94m"
    BOLD = "\033[1m"
    RESET = "\033[0m"
    CYAN = "\033[36m"
    RED = "\033[31m"

    if is_ok:
        status_tag = f"{CYAN}[OK]{RESET}"
    else:
        status_tag = f"{RED}[NOK]{RESET}"

    prefix = f"            {BLUE}{BOLD}»{RESET} {status_tag}  "

    if isinstance(messages, str):
        messages = [messages]

    for item in messages:
        print(f"{prefix} {item}")


def fim():
    """
    Imprime uma mensagem visual de finalização de script no terminal.

    Args:
        None

    Returns:
        None

    Example:
        >>> sy.fim()
    """
    CYAN = "\033[36m"
    RESET = "\033[0m"
    BLUE = "\033[94m"

    print(f"\n     {BLUE}»»»»{CYAN} EXECUÇÃO FINALIZADA!{RESET}\n")


def help(filepath):
    """
    Lê e exibe um arquivo de texto no terminal utilizando uma paleta de cores minimalista (stealth).

    Args:
        filepath (str): Caminho para o arquivo de texto contendo a tabela ASCII.

    Returns:
        None

    Example:
        >>> sy.help("data/instrucoes.txt")
    """
    DARK_GRAY = "\033[90m"
    DIM = "\033[2m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

    if not os.path.exists(filepath):
        print(
            f"\n  {RED}{BOLD}!{RESET} {DARK_GRAY}Arquivo de ajuda '{filepath}' não encontrado.{RESET}"
        )
        return

    print()

    with open(filepath, "r", encoding="utf-8-sig") as file:
        for line in file:
            line = line.rstrip("\n")

            if not line:
                continue

            if line.startswith("+"):
                print(f"  {DARK_GRAY}{line}{RESET}")
            elif line.startswith("|"):
                formatted_line = line.replace("|", f"{RESET}{DARK_GRAY}|{RESET}{DIM}")
                print(f"  {DIM}{formatted_line}{RESET}")
            else:
                print(f"  {DARK_GRAY}{DIM}{line}{RESET}")

    print()
