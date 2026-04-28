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
        info_str = "  |  ".join([f"{k.upper()}: {v}" for k, v in kwargs.items()])
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


def table(*eixos, tipo="coluna", **kwargs):
    """
    Formata e exibe dados em uma estrutura de tabela ASCII.

    Esta função foi aprimorada para receber tuplas de forma intuitiva,
    convertendo-as internamente para a estrutura original de renderização.

    Exemplos de Uso:
    1. Por Colunas (Padrão):
       table(("ID", 1, 2), ("NOME", "Ana", "João"))
       table(tipo="coluna", eixo1=("ID", 1, 2), eixo2=("NOME", "Ana", "João"))

    2. Por Linhas (A 1ª tupla define os cabeçalhos das colunas):
       table(("ID", "NOME"), ("1", "Ana"), ("2", "João"), tipo="linha")

    Parâmetros
    ----------
    *eixos : tuple
        As tuplas contendo os dados.
    tipo : str, opcional
        Define se as tuplas representam 'coluna' ou 'linha'. Padrão é 'coluna'.
    **kwargs : dict
        Permite passar os eixos de forma nomeada (ex: eixo1=(...)).
    """
    # --- NOVA MECÂNICA DE RECEBIMENTO DE DADOS ---
    # Unificando as entradas passadas sem nome (*eixos) e com nome (**kwargs)
    entradas = list(eixos) + list(kwargs.values())

    if not entradas:
        print("A lista está vazia.")
        return

    dados = []
    if tipo == "coluna":
        # O índice [0] de cada tupla é o cabeçalho. O restante [1:] são os valores.
        chaves = [str(eixo[0]) for eixo in entradas]
        valores_por_linha = zip(*[eixo[1:] for eixo in entradas])
        
        for valores in valores_por_linha:
            dados.append(dict(zip(chaves, valores)))

    elif tipo == "linha":
        # A primeira tupla assume o papel de cabeçalhos das colunas. As seguintes são os valores.
        chaves = [str(c) for c in entradas[0]]
        linhas_dados = entradas[1:]
        
        for valores in linhas_dados:
            dados.append(dict(zip(chaves, valores)))
    else:
        print(f"Tipo '{tipo}' inválido. Use tipo='coluna' ou tipo='linha'.")
        return
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


def cin(msg, formato="string"):
    """
    Recebe e valida a entrada do usuário com um visual colorido no terminal.

    Esta função exibe um prompt personalizado, sinalizando uma requisição de
    dados. Ela também garante a robustez do script capturando erros de
    tipagem caso o usuário insira um formato incorreto, repetindo a
    pergunta de forma suave e estilizada até obter um valor válido.

    (  "Qual é a sua idade?", "int"  )

    Parâmetros
    ----------
    msg : str
        A mensagem ou pergunta a ser exibida para o usuário.
    formato : str, opcional
        O tipo de dado esperado da entrada. Os valores aceitos são:
        'int', 'float' ou 'string'. O padrão é 'string'.

    Retornos
    --------
    any
        O valor inserido pelo usuário, devidamente convertido para o tipo
        especificado no parâmetro `formato`.

    Notas
    -----
    A interface utiliza a seguinte paleta de cores:
    - Ouro (Gold): Marcador de interrogação ('?'), indicando uma ação requerida.
    - Cinza (Gray): Indicador discreto do tipo esperado, ex: [int].
    - Ciano (Cyan): Cursor de entrada ('»').
    - Vermelho (Red): Mensagem de erro caso a conversão de tipo falhe.
    """
    GOLD = "\033[33m"
    CYAN = "\033[36m"
    GRAY = "\033[90m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

    # Marcadores estéticos
    marcador_pergunta = f"{GOLD}{BOLD}?{RESET}"
    marcador_erro = f"{RED}{BOLD}!{RESET}"
    cursor = f"{CYAN}»{RESET}"

    while True:
        # Montagem do prompt estilizado (ex:  ? Qual o valor? [float] » )
        prompt = f"\n  {marcador_pergunta} {msg} {GRAY}[{formato}]{RESET} {cursor} "
        
        entrada = input(prompt)
        
        try:
            if formato.lower() == 'int':
                return int(entrada)
            elif formato.lower() == 'float':
                # Replace da vírgula por ponto para evitar erros de digitação comuns no Brasil
                return float(entrada.replace(',', '.'))
            elif formato.lower() == 'string':
                return str(entrada)
            else:
                # Caso o desenvolvedor passe um formato não mapeado
                print(f"\n  {marcador_erro} {GRAY}Erro no código: Formato '{formato}' não reconhecido. Use 'int', 'float' ou 'string'.{RESET}")
                return None
                
        except ValueError:
            # Retorno de erro elegante para o usuário, sem quebrar o script principal
            print(f"  {marcador_erro} {GRAY}Entrada inválida. Por favor, insira um valor numérico do tipo '{formato}'.{RESET}")

def ok(lista, one=False):
    if one:
        BLUE = "\033[94m"
        BOLD = "\033[1m"
        RESET = "\033[0m"
        CYAN = "\033[36m"
        print(f"             {BLUE}{BOLD}»{RESET} {f"{CYAN}[OK]{RESET}   {lista}"}")
        return
    for item in lista:
        BLUE = "\033[94m"
        BOLD = "\033[1m"
        RESET = "\033[0m"
        CYAN = "\033[36m"
        print(f"             {BLUE}{BOLD}»{RESET} {f"{CYAN}[OK]{RESET}   {item}"}")

def fim():
    CYAN = "\033[36m"
    RESET = "\033[0m"
    BLUE = "\033[94m"
    print(f"\n     {BLUE}»»»»{CYAN} EXECUÇÃO FINALIZADA!{RESET}\n")


def help(arquivo):
    """
    Exibe um arquivo de texto formatado como tabela em um estilo visual suave.

    Esta função lê um arquivo .txt contendo uma tabela ASCII (nos mesmos moldes
    gerados pela função `table`) e a renderiza no terminal com uma paleta de
    cores mais escura, apagada e minimalista. Ideal para menus de ajuda ou
    tabelas de referência que não devem ofuscar a interface principal.

    (  "ajuda.txt"  )

    Parâmetros
    ----------
    arquivo : str
        O caminho para o arquivo de texto contendo a tabela ASCII.

    Notas
    -----
    A interface utiliza uma paleta "stealth" (discreta):
    - Cinza Escuro (Dark Gray): Para as bordas e separadores da tabela (+, -, |).
    - Opaco/Escurecido (Dim): Para o conteúdo em texto, tornando a leitura
      confortável e reduzindo o contraste na tela.
    """
    import os

    DARK_GRAY = "\033[90m"
    DIM = "\033[2m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

    # Verificação elegante de erro caso o arquivo txt não exista
    if not os.path.exists(arquivo):
        print(f"\n  {RED}{BOLD}!{RESET} {DARK_GRAY}Arquivo de ajuda '{arquivo}' não encontrado.{RESET}")
        return

    print() # Respiro inicial
    
    with open(arquivo, 'r', encoding='utf-8-sig') as f:
        for linha in f:
            # Removemos apenas a quebra de linha do final, preservando espaços internos
            linha = linha.rstrip('\n')
            
            if not linha:
                continue
                
            # Renderização sutil
            if linha.startswith('+'):
                # Separadores horizontais (+---+---+) ficam inteiramente em cinza escuro
                print(f"  {DARK_GRAY}{linha}{RESET}")
                
            elif linha.startswith('|'):
                # Nas linhas de dados, substituímos a barra vertical (|) para que 
                # a barra fique cinza e o texto interno aplique o filtro 'DIM' (opaco)
                linha_formatada = linha.replace('|', f"{RESET}{DARK_GRAY}|{RESET}{DIM}")
                print(f"  {DIM}{linha_formatada}{RESET}")
                
            else:
                # Qualquer outra linha fora da estrutura da tabela fica esmaecida
                print(f"  {DARK_GRAY}{DIM}{linha}{RESET}")
                
    print() # Respiro final