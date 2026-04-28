#
# * =============================================================================
# * GRAPHS
# * =============================================================================
from matplotlib import pyplot as plt


def basic(
    vecx,
    vecy,
    titulo="",
    NOMEvecx="EIXO X",
    NOMEvecy="EIXO Y",
    HaveGrid=False,
    HaveBox=True,
    escala="linear",
    cor="black",
    espessura=2.5,
    fontetitulo=16,
    fonteeixos=12,
    estilo_linha="-",
    alpha_linha=0.8,
    cor_grade="#E6E6E6",
    largura_figura=7,
    altura_figura=6,
    remover_bordas=False,
    marcador=None,
    save=False,
    dpi=600,
    formato="pdf",
    nome="basicgraph",
    plot=True,
):
    """
    Gera um gráfico de linha customizado com foco em estética limpa e profissional.

    Esta função encapsula rotinas do Matplotlib para facilitar a criação de
    visualizações de dados, oferecendo controle simplificado sobre escalas,
    tipografia, estilização de eixos e salvamento automatizado em diretórios.

    Parâmetros
    ----------
    vecx : array-like
        Dados para o eixo horizontal (X).
    vecy : array-like
        Dados para o eixo vertical (Y).
    titulo : str, opcional
        O texto do título principal do gráfico.
    NOMEvecx : str, opcional
        Rótulo (label) do eixo X. O padrão é "EIXO X".
    NOMEvecy : str, opcional
        Rótulo (label) do eixo Y. O padrão é "EIXO Y".
    HaveGrid : bool, opcional
        Se True, exibe uma grade de fundo pontilhada.
    HaveBox : bool, opcional
        Se False, remove completamente a moldura do gráfico.
    escala : str, opcional
        Define o tipo de escala ("linear", "log"). O padrão é "linear".
    cor : str, opcional
        Cor da linha do gráfico (nome ou Hex). O padrão é "black".
    espessura : float, opcional
        Largura da linha plotada. O padrão é 2.5.
    fontetitulo : int, opcional
        Tamanho da fonte do título principal.
    fonteeixos : int, opcional
        Tamanho da fonte dos nomes dos eixos.
    estilo_linha : str, opcional
        Estilo da linha (ex: "-", "--", ":").
    alpha_linha : float, opcional
        Nível de transparência da linha (0 a 1).
    cor_grade : str, opcional
        Cor dos fios da grade. O padrão é um cinza claro ("#E6E6E6").
    largura_figura : int, opcional
        Largura da imagem em polegadas.
    altura_figura : int, opcional
        Altura da imagem em polegadas.
    remover_bordas : bool, opcional
        Se True, remove as bordas superior e direita para um visual moderno.
    marcador : str, opcional
        Estilo do marcador de pontos (ex: "o", "x", "s").
    save : bool, opcional
        Se True, exporta o gráfico para um arquivo local.
    dpi : int, opcional
        Resolução da imagem exportada. O padrão é 600.
    formato : str, opcional
        Extensão do arquivo de saída (ex: "png", "pdf", "svg").
    nome : str, opcional
        Nome do arquivo a ser salvo.
    plot : bool, opcional
        Se True, exibe o gráfico na tela através do plt.show().

    Notas
    -----
    A função automatiza a organização de arquivos:
    - Se `save=True`, uma pasta chamada `figures/` será criada automaticamente
      no diretório de execução, caso ainda não exista.
    - O layout utiliza `tight_layout()` para garantir que rótulos e títulos
      não sejam cortados na exportação.
    - A estética padrão prioriza o minimalismo, utilizando tons de cinza
      para spines (bordas) e grades para destacar os dados.
    """
    import matplotlib.pyplot as plt
    import os
    from matplotlib.ticker import AutoMinorLocator

    plt.rcParams.update(
        {
            "font.family": "serif",
            "mathtext.fontset": "dejavuserif",
            "axes.linewidth": 1.2,
            "xtick.direction": "in",
            "ytick.direction": "in",
            "xtick.top": True,
            "ytick.right": True,
            "xtick.labelsize": fonteeixos - 2,
            "ytick.labelsize": fonteeixos - 2,
            "legend.frameon": False,
        }
    )
    fig, ax = plt.subplots(figsize=(largura_figura, altura_figura), dpi=100)
    ax.plot(
        vecx,
        vecy,
        color=cor,
        linewidth=espessura,
        linestyle=estilo_linha,
        alpha=alpha_linha,
        marker=marcador,
        label=titulo if titulo else None,
    )
    if titulo:
        ax.set_title(titulo, fontsize=fontetitulo, pad=15, fontweight="bold")
    ax.set_xlabel(NOMEvecx, fontsize=fonteeixos, labelpad=8)
    ax.set_ylabel(NOMEvecy, fontsize=fonteeixos, labelpad=8)
    ax.set_xscale(escala)
    ax.set_yscale(escala)
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.tick_params(which="major", length=6, width=1.2)
    ax.tick_params(which="minor", length=3, width=1.0)
    if HaveGrid:
        ax.grid(True, linestyle="--", linewidth=0.5, color=cor_grade, alpha=0.7)
        ax.set_axisbelow(True)
    if not HaveBox:
        ax.set_frame_on(False)
    elif remover_bordas:
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
    else:
        for spine in ax.spines.values():
            spine.set_visible(True)
            spine.set_color("black")
    plt.tight_layout()
    if save:
        if not os.path.exists("figures"):
            os.makedirs("figures")
        caminho = f"figures/{nome}.{formato}"
        plt.savefig(caminho, dpi=dpi, bbox_inches="tight")

        plt.savefig(
            caminho, dpi=dpi, bbox_inches="tight", facecolor="white", transparent=False
        )
        print(f"Gráfico salvo com sucesso em: {caminho}")

    if plot:
        plt.show()
    else:
        plt.close(fig)

    return None


def multi(
    list_vecx,
    list_vecy,
    nomes_curvas=None,
    titulo="",
    NOMEvecx="EIXO X",
    NOMEvecy="EIXO Y",
    HaveGrid=False,
    HaveBox=True,
    escala="linear",
    cor_estilo="random",
    espessura=2,
    fontetitulo=14,
    fonteeixos=12,
    estilo_linha="cycle",
    alpha_linha=1.0,
    cor_grade="#E6E6E6",
    largura_figura=7,
    altura_figura=6,
    remover_bordas=False,
    marcador=None,
    mostrar_legenda=True,
    titulo_legenda=None,
    box_legenda=False,
    save=False,
    dpi=600,
    formato="pdf",
    nome="multigraph",
    plot=True,
):
    """
    Gera um gráfico comparativo de múltiplas curvas com gestão avançada de cores e legendas.

    Esta função permite a visualização simultânea de diversos conjuntos de dados,
    oferecendo automação na escolha de paletas cromáticas (via colormaps) e
    ajustes finos de layout para garantir clareza em plotagens complexas.

    Parâmetros
    ----------
    list_vecx : list of array-like
        Lista contendo os arrays de dados para o eixo X de cada curva.
    list_vecy : list of array-like
        Lista contendo os arrays de dados para o eixo Y de cada curva.
    nomes_curvas : list of str, opcional
        Lista de etiquetas para a legenda. Se None, utiliza "Curva 1, 2...".
    titulo : str, opcional
        Título principal posicionado no topo do gráfico.
    NOMEvecx : str, opcional
        Nome do eixo horizontal. O padrão é "EIXO X".
    NOMEvecy : str, opcional
        Nome do eixo vertical. O padrão é "EIXO Y".
    HaveGrid : bool, opcional
        Se True, ativa a grade de referência em segundo plano.
    HaveBox : bool, opcional
        Se False, remove a moldura externa do gráfico.
    escala : str, opcional
        Define a escala dos eixos ("linear" ou "log").
    cor_estilo : str ou list, opcional
        Define o esquema de cores: "random" (tab10), "preto", ou lista de cores.
    espessura : float, opcional
        Espessura da linha de todas as curvas plotadas.
    fontetitulo : int, opcional
        Tamanho da fonte do título principal.
    fonteeixos : int, opcional
        Tamanho da fonte dos rótulos dos eixos e legendas.
    estilo_linha : str, opcional
        Padrão da linha (ex: "-", "--", "-.").
    alpha_linha : float, opcional
        Opacidade das linhas (0 a 1).
    cor_grade : str, opcional
        Cor hexadecimal da grade de fundo.
    largura_figura : int, opcional
        Dimensão horizontal da figura em polegadas.
    altura_figura : int, opcional
        Dimensão vertical da figura em polegadas.
    remover_bordas : bool, opcional
        Se True, suaviza o gráfico removendo as bordas superior e direita.
    marcador : str, opcional
        Símbolo opcional para marcar os pontos dos dados.
    mostrar_legenda : bool, opcional
        Se True, exibe a caixa de identificação das curvas.
    titulo_legenda : str, opcional
        Título descritivo para a caixa de legenda.
    box_legenda : bool, opcional
        Se True, desenha uma borda ao redor da legenda.
    save : bool, opcional
        Se True, exporta a imagem para o diretório local.
    dpi : int, opcional
        Densidade de pixels por polegada para a exportação.
    formato : str, opcional
        Formato do arquivo de saída (ex: "png", "pdf").
    nome : str, opcional
        Nome do arquivo salvo.
    plot : bool, opcional
        Se True, renderiza o gráfico no terminal/notebook.

    Notas
    -----
    A função implementa verificações de integridade e lógica de cores:
    - Validação: O número de sublistas em `list_vecx` e `list_vecy` deve ser idêntico.
    - Gestão de Cores: O modo "random" utiliza o mapa de cores 'tab10' do Matplotlib
      para garantir contraste visual máximo entre curvas próximas.
    - Exportação: Assim como na versão básica, arquivos são organizados na pasta
      `figures/` com recorte automático de espaços brancos (`bbox_inches='tight'`).
    """
    import matplotlib.pyplot as plt
    import os
    from matplotlib.ticker import AutoMinorLocator

    plt.rcParams.update(
        {
            "font.family": "serif",
            "mathtext.fontset": "dejavuserif",
            "axes.linewidth": 1.2,
            "xtick.direction": "in",
            "ytick.direction": "in",
            "xtick.top": True,
            "ytick.right": True,
            "xtick.labelsize": fonteeixos - 2,
            "ytick.labelsize": fonteeixos - 2,
        }
    )

    if len(list_vecx) != len(list_vecy):
        raise ValueError(
            "O número de listas em X deve ser igual ao número de listas em Y."
        )

    fig, ax = plt.subplots(figsize=(largura_figura, altura_figura), dpi=100)
    n_curvas = len(list_vecx)

    if cor_estilo == "preto":
        cores = ["black"] * n_curvas
    elif cor_estilo == "random":
        cmap = plt.get_cmap("tab10")
        cores = [cmap(i % 10) for i in range(n_curvas)]
    elif isinstance(cor_estilo, list):
        cores = cor_estilo
    else:
        cores = [cor_estilo] * n_curvas

    if estilo_linha == "cycle":
        lista_estilos = ["-", ":", "--", "-."]
    elif isinstance(estilo_linha, list):
        lista_estilos = estilo_linha
    else:
        lista_estilos = [estilo_linha]

    for i in range(n_curvas):
        label_curva = nomes_curvas[i] if nomes_curvas else f"Curva {i+1}"
        ax.plot(
            list_vecx[i],
            list_vecy[i],
            color=cores[i % len(cores)],
            linewidth=espessura,
            linestyle=lista_estilos[i % len(lista_estilos)],
            alpha=alpha_linha,
            marker=marcador,
            label=label_curva,
        )

    if titulo:
        ax.set_title(titulo, fontsize=fontetitulo, pad=15, fontweight="bold")

    ax.set_xlabel(NOMEvecx, fontsize=fonteeixos, labelpad=8)
    ax.set_ylabel(NOMEvecy, fontsize=fonteeixos, labelpad=8)
    ax.set_xscale(escala)
    ax.set_yscale(escala)

    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.tick_params(which="major", length=6, width=1.2)
    ax.tick_params(which="minor", length=3, width=1.0)

    if mostrar_legenda:
        ax.legend(
            title=titulo_legenda,
            frameon=box_legenda,
            fontsize=fonteeixos * 0.9,
            title_fontsize=fonteeixos,
            loc="best",
            edgecolor="black" if box_legenda else None,
        )

    if HaveGrid:
        ax.grid(True, linestyle="--", linewidth=0.5, color=cor_grade, alpha=0.7)
        ax.set_axisbelow(True)

    if not HaveBox:
        ax.set_frame_on(False)
    elif remover_bordas:
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
    else:
        for spine in ax.spines.values():
            spine.set_visible(True)
            spine.set_color("black")

    plt.tight_layout()

    if save:
        if not os.path.exists("figures"):
            os.makedirs("figures")
        caminho = f"figures/{nome}.{formato}"
        plt.savefig(caminho, dpi=dpi, bbox_inches="tight", facecolor="white")

    if plot:
        plt.show()
    else:
        plt.close(fig)

    return None


def elipse(
    X,  # Matriz de coordenadas X (geralmente de um meshgrid)
    Y,  # Matriz de coordenadas Y (geralmente de um meshgrid)
    Z,  # Matriz de valores Z (superfície de chi-quadrado ou probabilidade)
    pontos_linha_x=None,  # Array de coordenadas X para a linha extra
    pontos_linha_y=None,  # Array de coordenadas Y para a linha extra
    legenda_linha="Linha extra",  # Texto da legenda para a linha extra
    espessura_linha=1.0,  # Espessura da linha extra
    estilo_linha=":",  # Estilo da linha extra (nativamente: pontilhada)
    cor_linha="black",  # Cor da linha extra (nativamente: preta)
    ponto_destaque=None,  # Tupla (x, y) para marcar o melhor ajuste (best-fit)
    niveis_elipse=None,  # Lista de floats com os valores de Z para desenhar as elipses
    nomes_sigmas=None,  # Lista de strings para nomear cada nível (ex: ['68%', '95%'])
    mostrar_sigma=True,  # Booleano: define se o nome do nível aparece escrito sobre a elipse
    titulo=None,  # Título do gráfico (None para nativamente sem título)
    NOMEvecx="EIXO X",  # Rótulo do eixo X
    NOMEvecy="EIXO Y",  # Rótulo do eixo Y
    HaveGrid=True,  # Booleano: ativa ou desativa a grade
    HaveBox=True,  # Booleano: mantém ou remove a moldura (box)
    frame_legenda=True,  # Booleano: ativa ou desativa a caixa em volta da legenda
    framealpha=0.5,  # Transparencia da caixa em volta da legenda
    tamanho_fonte_legenda=11, # Tamanho da fonte específica para a caixa de legenda
    form="neither",  # Formato da colorbar ('max', 'min', 'both' ou 'neither')
    escala="linear",  # Escala dos eixos X e Y ('linear' ou 'log')
    escala_z="linear",  # Escala do mapa de calor Z ('linear' ou 'log')
    num_ticks_colorbar=None, # Número máximo de valores mostrados na barra de cores (ex: 5)
    cmap="viridis_r",  # Mapa de cores do fundo
    fontetitulo=16,  # Tamanho da fonte do título
    fonteeixos=14,  # Tamanho da fonte dos eixos e legendas
    ponto_nome="Destaque",  # Texto da legenda para o destaque
    cor_ponto="red",  # Cor do marcador de melhor ajuste
    marcador_ponto="*",  # Estilo do marcador de melhor ajuste
    tamanho_ponto=150,  # Tamanho do marcador de melhor ajuste
    estilo_elipses=[
        "-",
        ":",
        ":",
    ],  # Estilo das linhas (nativamente: contínua na primeira, pontilhada nas outras)
    cores_elipses=["red", "green", "blue"],  # Cores de cada nível de elipse
    largura_figura=8,  # Largura da imagem em polegadas
    altura_figura=6,  # Altura da imagem em polegadas
    remover_bordas=False,  # Se True, remove as linhas superior e direita da moldura
    mostrar_colorbar=True,  # Booleano: exibe ou oculta a barra de cores lateral
    label_colorbar=r"$\chi^2$",  # Título da barra de cores
    niveis_mapa_calor=200,  # Quantidade de níveis no contourf para garantir continuidade
    save=False,  # Booleano: salva o arquivo se True
    dpi=600,  # Resolução de saída para publicação
    formato="pdf",  # Formato de salvamento (pdf é ideal para meio acadêmico)
    nome="ellipse_graph",  # Nome do arquivo de saída
    plot=True,  # Booleano: exibe o gráfico na tela
):
    import os
    import numpy as np
    from matplotlib import pyplot as plt
    from matplotlib.colors import LogNorm
    from matplotlib.ticker import LogFormatterMathtext, LogLocator, MaxNLocator

    plt.rcParams.update(
        {
            "text.usetex": False,
            "font.family": "serif",
            "font.serif": ["Computer Modern Roman", "DejaVu Serif"],
            "mathtext.fontset": "cm",
            "xtick.direction": "in",
            "ytick.direction": "in",
            "xtick.top": True,
            "ytick.right": True,
            "axes.linewidth": 1.2,
        }
    )

    fig, ax = plt.subplots(figsize=(largura_figura, altura_figura))

    # Configuração da escala Z (linear ou logarítmica)
    if escala_z == "log":
        Z_min_positivo = np.min(Z[Z > 0]) if np.any(Z > 0) else 1e-10
        norm = LogNorm(vmin=Z_min_positivo, vmax=np.max(Z))
        levels_cf = np.geomspace(Z_min_positivo, np.max(Z), niveis_mapa_calor)
    else:
        norm = None
        levels_cf = niveis_mapa_calor

    cf = ax.contourf(
        X, Y, Z, 
        levels=levels_cf, 
        cmap=cmap, 
        norm=norm, 
        extend=form,
        antialiased=False
    )
    
    for c in cf.collections:
        c.set_edgecolor("face")
        c.set_linewidth(1e-9)

    if niveis_elipse is not None:
        if nomes_sigmas is None:
            nomes_sigmas = [rf"{i+1}$\sigma$" for i in range(len(niveis_elipse))]

        for i, nivel in enumerate(niveis_elipse):
            estilo = estilo_elipses[i % len(estilo_elipses)]
            cor = cores_elipses[i % len(cores_elipses)]
            nome_sigma = nomes_sigmas[i % len(nomes_sigmas)]

            contorno = ax.contour(
                X, Y, Z, levels=[nivel], colors=[cor], linestyles=estilo, linewidths=1.8
            )

            if mostrar_sigma:
                fmt = {nivel: nome_sigma}
                textos_labels = ax.clabel(
                    contorno,
                    inline=True,
                    fontsize=fonteeixos * 0.9,
                    fmt=fmt,
                    colors=[cor],
                )
                for texto in textos_labels:
                    texto.set_fontweight("bold")

    if pontos_linha_x is not None and pontos_linha_y is not None:
        ax.plot(
            pontos_linha_x,
            pontos_linha_y,
            color=cor_linha,
            linestyle=estilo_linha,
            linewidth=espessura_linha,
            label=legenda_linha,
            zorder=4,
        )

    if ponto_destaque is not None:
        ax.scatter(
            ponto_destaque[0],
            ponto_destaque[1],
            color=cor_ponto,
            marker=marcador_ponto,
            s=tamanho_ponto,
            label=f"{ponto_nome}\n({ponto_destaque[0]:.3f}, {ponto_destaque[1]:.3f})",
            zorder=5,
        )

    if mostrar_colorbar:
        cbar = fig.colorbar(cf, ax=ax, pad=0.02)
        cbar.set_label(label_colorbar, fontsize=fonteeixos)
        cbar.ax.tick_params(labelsize=fonteeixos * 0.8)
        cbar.outline.set_linewidth(1.2)
        
        # Controle dos limites e labels da colorbar
        if escala_z == "log":
            cbar.ax.yaxis.set_major_formatter(LogFormatterMathtext())
            if num_ticks_colorbar is not None:
                cbar.ax.yaxis.set_major_locator(LogLocator(base=10.0, numticks=num_ticks_colorbar))
            else:
                cbar.ax.yaxis.set_minor_locator(LogLocator(base=10.0, subs=np.arange(2, 10) * 0.1))
        else:
            if num_ticks_colorbar is not None:
                cbar.ax.yaxis.set_major_locator(MaxNLocator(num_ticks_colorbar))

    if titulo:
        ax.set_title(titulo, fontsize=fontetitulo, pad=15)

    ax.set_xlabel(NOMEvecx, fontsize=fonteeixos, labelpad=10)
    ax.set_ylabel(NOMEvecy, fontsize=fonteeixos, labelpad=10)
    ax.set_xscale(escala)
    ax.set_yscale(escala)

    ax.minorticks_on()
    ax.tick_params(which="minor", direction="in", top=True, right=True)

    if ponto_destaque is not None or (pontos_linha_x is not None and pontos_linha_y is not None):
        ax.legend(
            frameon=frame_legenda,
            facecolor="white",
            framealpha=framealpha,
            edgecolor="#333333",
            fontsize=tamanho_fonte_legenda,  # Passando o novo controle de fonte aqui
            loc="best",
        )

    if HaveGrid:
        ax.grid(True, linestyle=":", linewidth=0.5, color="black", alpha=0.15)
        ax.set_axisbelow(False)

    if not HaveBox:
        ax.set_frame_on(False)
    elif remover_bordas:
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

    # TRAVANDO OS LIMITES DO EIXO PARA REMOVER BORDAS BRANCAS
    ax.set_xlim(np.min(X), np.max(X))
    ax.set_ylim(np.min(Y), np.max(Y))

    plt.tight_layout()

    if save:
        if not os.path.exists("figures"):
            os.makedirs("figures")
        plt.savefig(f"figures/{nome}.{formato}", dpi=dpi, bbox_inches="tight")

    if plot:
        plt.show()

    return fig, ax


def basicdot(
    vecx,
    vecy,
    ponto_destaque=None,
    titulo="",
    NOMEvecx="EIXO X",
    NOMEvecy="EIXO Y",
    HaveGrid=False,
    HaveBox=True,
    escala="linear",
    cor="black",
    espessura=2.0,
    fontetitulo=16,
    fonteeixos=12,
    estilo_linha="-",
    alpha_linha=0.7,
    cor_grade="#E6E6E6",
    largura_figura=7,
    altura_figura=6,
    remover_bordas=False,
    marcador=None,
    cor_ponto="red",
    label_curva="Dados",
    marcador_ponto="*",
    tamanho_ponto=150,
    label_ponto="Destaque",
    save=False,
    dpi=600,
    formato="pdf",
    nome="basicdot_graph",
    plot=True,
):
    """
    Gera um gráfico de linha com a capacidade de enfatizar um ponto específico.

    Esta função combina a simplicidade de um gráfico linear clássico com ferramentas
    de anotação visual, permitindo destacar coordenadas críticas (como máximos,
    mínimos ou valores observados) através de marcadores customizados e legendas automáticas.

    Parâmetros
    ----------
    vecx : array-like
        Dados para o eixo horizontal (X).
    vecy : array-like
        Dados para o eixo vertical (Y).
    ponto_destaque : tuple, opcional
        Coordenadas (x, y) de um ponto a ser realçado com um marcador especial.
    titulo : str, opcional
        Título principal do gráfico. Se fornecido, aparece na legenda por padrão.
    NOMEvecx : str, opcional
        Rótulo do eixo X. O padrão é "EIXO X".
    NOMEvecy : str, opcional
        Rótulo do eixo Y. O padrão é "EIXO Y".
    HaveGrid : bool, opcional
        Se True, desenha uma grade pontilhada para facilitar a leitura.
    HaveBox : bool, opcional
        Se False, remove toda a moldura externa do gráfico.
    escala : str, opcional
        Define o regime de escala ("linear" ou "log").
    cor : str, opcional
        Cor da linha principal do gráfico.
    espessura : float, opcional
        Largura da linha principal.
    fontetitulo, fonteeixos : int, opcional
        Tamanhos das fontes para o título e rótulos, respectivamente.
    estilo_linha : str, opcional
        Tipo de traçado da linha (ex: "-", "--").
    alpha_linha : float, opcional
        Transparência da linha (0.0 a 1.0).
    cor_grade : str, opcional
        Cor hexadecimal da grade.
    largura_figura, altura_figura : int, opcional
        Dimensões da figura em polegadas.
    remover_bordas : bool, opcional
        Se True, remove as linhas superior e direita da moldura para um visual moderno.
    marcador : str, opcional
        Marcador para os pontos da linha principal.
    cor_ponto : str, opcional
        Cor do marcador de destaque. O padrão é "red".
    marcador_ponto : str, opcional
        Símbolo do marcador de destaque (ex: "*", "o", "v").
    tamanho_ponto : int, opcional
        Escala visual (tamanho) do marcador de destaque.
    label_ponto : str, opcional
        Texto descritivo que aparecerá na legenda para o ponto de destaque.
    save : bool, opcional
        Se True, salva o gráfico no diretório 'figures/'.
    dpi : int, opcional
        Qualidade da imagem salva (Dots Per Inch).
    formato : str, opcional
        Formato de arquivo para salvamento (ex: "png", "svg").
    nome : str, opcional
        Nome do arquivo a ser gerado.
    plot : bool, opcional
        Se True, renderiza a imagem na tela.

    Notas
    -----
    A função gerencia a hierarquia visual de forma inteligente:
    - Z-Order: O ponto de destaque é renderizado acima da linha (`zorder=5`) para
      garantir visibilidade absoluta.
    - Legendas: A legenda é ativada automaticamente sempre que um título ou um
      ponto de destaque for definido, utilizando um layout sem moldura (`frameon=False`).
    - Organização: Se a opção de salvamento estiver ativa, o script verifica e cria
      o diretório `figures/` automaticamente para evitar erros de execução.
    """
    import os
    from matplotlib import pyplot as plt
    from matplotlib.ticker import AutoMinorLocator

    plt.rcParams.update(
        {
            "font.family": "serif",
            "mathtext.fontset": "dejavuserif",
            "axes.linewidth": 1.2,
            "xtick.direction": "in",
            "ytick.direction": "in",
            "xtick.top": True,
            "ytick.right": True,
            "xtick.labelsize": fonteeixos - 2,
            "ytick.labelsize": fonteeixos - 2,
        }
    )

    fig, ax = plt.subplots(figsize=(largura_figura, altura_figura), dpi=100)

    ax.plot(
        vecx,
        vecy,
        color=cor,
        linewidth=espessura,
        linestyle=estilo_linha,
        alpha=alpha_linha,
        marker=marcador,
        label=label_curva if label_curva else "Dados",
    )

    if ponto_destaque is not None:
        ax.scatter(
            ponto_destaque[0],
            ponto_destaque[1],
            color=cor_ponto,
            marker=marcador_ponto,
            s=tamanho_ponto,
            label=label_ponto,
            zorder=5,
        )

    if titulo:
        ax.set_title(titulo, fontsize=fontetitulo, pad=15, fontweight="bold")

    ax.set_xlabel(NOMEvecx, fontsize=fonteeixos, labelpad=8)
    ax.set_ylabel(NOMEvecy, fontsize=fonteeixos, labelpad=8)
    ax.set_xscale(escala)
    ax.set_yscale(escala)

    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.tick_params(which="major", length=6, width=1.2)
    ax.tick_params(which="minor", length=3, width=1.0)

    if titulo or ponto_destaque:
        ax.legend(frameon=False, fontsize=fonteeixos * 0.9)

    if HaveGrid:
        ax.grid(True, linestyle="--", linewidth=0.5, color=cor_grade, alpha=0.7)
        ax.set_axisbelow(True)

    if not HaveBox:
        ax.set_frame_on(False)
    elif remover_bordas:
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
    else:
        for spine in ax.spines.values():
            spine.set_visible(True)
            spine.set_color("black")

    plt.tight_layout()

    if save:
        if not os.path.exists("figures"):
            os.makedirs("figures")
        caminho = f"figures/{nome}.{formato}"
        plt.savefig(caminho, dpi=dpi, bbox_inches="tight", facecolor="white")

    if plot:
        plt.show()
    else:
        plt.close(fig)

    return None
