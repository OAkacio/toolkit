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
    espessura=2.0,
    fontetitulo=16,
    fonteeixos=12,
    estilo_linha="-",
    alpha_linha=0.7,
    cor_grade="#E6E6E6",
    largura_figura=10,
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
    espessura=1.5,
    fontetitulo=14,
    fonteeixos=12,
    estilo_linha="-",
    alpha_linha=1.0,
    cor_grade="#E6E6E6",
    largura_figura=8,
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
        cores = [cmap(i / n_curvas) for i in range(n_curvas)]
    elif isinstance(cor_estilo, list):
        cores = cor_estilo
    else:
        cores = [cor_estilo] * n_curvas

    for i in range(n_curvas):
        label_curva = nomes_curvas[i] if nomes_curvas else f"Curva {i+1}"
        ax.plot(
            list_vecx[i],
            list_vecy[i],
            color=cores[i % len(cores)],
            linewidth=espessura,
            linestyle=estilo_linha,
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
    X,
    Y,
    Z,
    ponto_destaque=None,
    niveis_elipse=None,
    titulo=r"Mapa de $\chi^2$",
    NOMEvecx=r"$\Omega_M$",
    NOMEvecy=r"$\Omega_\Lambda$",
    HaveGrid=True,
    HaveBox=True,
    escala="linear",
    cmap="viridis_r",
    fontetitulo=16,
    fonteeixos=12,
    cor_ponto="red",
    marcador_ponto="*",
    tamanho_ponto=100,
    estilo_elipses=["--", "-.", ":"],
    cores_elipses=["red", "green", "blue"],
    largura_figura=10,
    altura_figura=8,
    remover_bordas=False,
    mostrar_colorbar=True,
    label_colorbar=r"$\chi^2$",
    save=False,
    dpi=600,
    formato="png",
    nome="ellipse_graph",
    plot=True,
):
    """
    Gera um mapa de contornos para superfícies de erro, focado em elipses de confiança.

    Esta função é especializada na visualização de espaços de parâmetros (como mapas
    de $\chi^2$), utilizando preenchimentos degradês e sobreposição de contornos
    específicos para representar níveis de significância estatística e o ponto
    de melhor ajuste (best-fit).

    Parâmetros
    ----------
    X, Y, Z : array-like
        Matrizes de coordenadas (X, Y) e valores de superfície (Z). Geralmente
        gerados via np.meshgrid.
    ponto_destaque : tuple, opcional
        Coordenadas (x, y) do ponto de interesse (ex: mínimo global).
    niveis_elipse : list of float, opcional
        Valores de Z onde as linhas de contorno (elipses) devem ser desenhadas.
    titulo : str, opcional
        Título do gráfico. Suporta sintaxe LaTeX.
    NOMEvecx : str, opcional
        Rótulo do eixo X. O padrão utiliza notação cosmológica ($\Omega_M$).
    NOMEvecy : str, opcional
        Rótulo do eixo Y. O padrão utiliza notação cosmológica ($\Omega_\Lambda$).
    HaveGrid : bool, opcional
        Se True, exibe uma grade sutil sobre o mapa de calor.
    HaveBox : bool, opcional
        Se False, remove a moldura externa do gráfico.
    escala : str, opcional
        Define o tipo de escala dos eixos ("linear", "log").
    cmap : str, opcional
        Mapa de cores para o preenchimento. O padrão é "viridis_r" (reverso).
    fontetitulo : int, opcional
        Tamanho da fonte para o título principal.
    fonteeixos : int, opcional
        Tamanho da fonte para rótulos e legendas.
    cor_ponto : str, opcional
        Cor do marcador de destaque.
    marcador_ponto : str, opcional
        Estilo do marcador para o ponto de destaque (ex: "*", "o").
    tamanho_ponto : int, opcional
        Área do marcador de destaque.
    estilo_elipses : list of str, opcional
        Lista de estilos de linha para cada nível de contorno.
    cores_elipses : list of str, opcional
        Lista de cores para cada nível de contorno.
    largura_figura, altura_figura : int, opcional
        Dimensões da figura em polegadas.
    remover_bordas : bool, opcional
        Se True, oculta as bordas superior e direita.
    mostrar_colorbar : bool, opcional
        Se True, adiciona uma barra de cores lateral para referência de Z.
    label_colorbar : str, opcional
        Título da barra de cores, suportando LaTeX.
    save : bool, opcional
        Se True, exporta a imagem para a pasta `figures/`.
    dpi : int, opcional
        Resolução da exportação. O padrão de 600 DPI garante qualidade de publicação.
    formato : str, opcional
        Extensão do arquivo (png, pdf, svg, etc).
    nome : str, opcional
        Nome base do arquivo salvo.
    plot : bool, opcional
        Se True, exibe a figura imediatamente.

    Notas
    -----
    A função otimiza a legibilidade de dados estatísticos:
    - Uso de LaTeX: Rótulos e títulos são formatados para aceitar notação
      matemática complexa nativamente.
    - Z-Order: O ponto de destaque é renderizado acima dos contornos (`zorder=5`)
      para evitar obstruções.
    - Colorbar: O ajuste de preenchimento (`pad=0.02`) garante que a barra
      não ocupe espaço excessivo da área de plotagem.
    """
    import os
    from matplotlib import pyplot as plt

    fig, ax = plt.subplots(figsize=(largura_figura, altura_figura))
    cf = ax.contourf(X, Y, Z, levels=50, cmap=cmap, alpha=0.9)
    if niveis_elipse is not None:
        for i, nivel in enumerate(niveis_elipse):
            estilo = estilo_elipses[i % len(estilo_elipses)]
            cor = cores_elipses[i % len(cores_elipses)]
            ax.contour(
                X, Y, Z, levels=[nivel], colors=cor, linestyles=estilo, linewidths=1.5
            )
    if ponto_destaque is not None:
        ax.scatter(
            ponto_destaque[0],
            ponto_destaque[1],
            color=cor_ponto,
            marker=marcador_ponto,
            s=tamanho_ponto,
            label=f"Melhor ajuste\n({ponto_destaque[0]}, {ponto_destaque[1]})",
            zorder=5,
        )
    if mostrar_colorbar:
        cbar = fig.colorbar(cf, ax=ax, pad=0.02)
        cbar.set_label(label_colorbar, fontsize=fonteeixos)
    ax.set_title(
        titulo, fontsize=fontetitulo, pad=20, fontweight="bold", color="#333333"
    )
    ax.set_xlabel(NOMEvecx, fontsize=fonteeixos, labelpad=10)
    ax.set_ylabel(NOMEvecy, fontsize=fonteeixos, labelpad=10)
    ax.set_xscale(escala)
    ax.set_yscale(escala)
    if ponto_destaque is not None:
        ax.legend(
            frameon=True,
            facecolor="white",
            framealpha=0.7,
            edgecolor="#CCCCCC",
            fontsize=fonteeixos * 0.8,
        )
    if HaveGrid:
        ax.grid(True, linestyle="--", linewidth=0.5, color="#FFFFFF", alpha=0.3)
        ax.set_axisbelow(False)
    if not HaveBox:
        ax.set_frame_on(False)
    elif remover_bordas:
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color("#CCCCCC")
        ax.spines["bottom"].set_color("#CCCCCC")
    plt.tight_layout()
    if save:
        import os

        if not os.path.exists("figures"):
            os.makedirs("figures")
        plt.savefig(f"figures/{nome}.{formato}", dpi=dpi, bbox_inches="tight")
    if plot:
        plt.show()
    return None


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
    espessura=1.5,
    fontetitulo=14,
    fonteeixos=12,
    estilo_linha="-",
    alpha_linha=1.0,
    cor_grade="#E6E6E6",
    largura_figura=8,
    altura_figura=6,
    remover_bordas=False,
    marcador=None,
    cor_ponto="red",
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
        label=titulo if titulo else "Dados",
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
