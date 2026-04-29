#
# * =============================================================================
# * GRAPHS
# * =============================================================================
#

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (
    AutoMinorLocator,
    LogFormatterMathtext,
    LogLocator,
    MaxNLocator,
)
from matplotlib.colors import LogNorm


def basic(
    x_data,
    y_data,
    title="",
    x_label="EIXO X",
    y_label="EIXO Y",
    show_grid=False,
    show_box=True,
    axis_scale="linear",
    color="black",
    linewidth=2.5,
    title_fontsize=16,
    axis_fontsize=12,
    linestyle="-",
    alpha=0.8,
    grid_color="#E6E6E6",
    fig_width=7,
    fig_height=6,
    remove_borders=False,
    marker=None,
    save_fig=False,
    dpi=600,
    file_format="pdf",
    filename="basicgraph",
    show_plot=True,
):
    """
    Gera um gráfico 2D simples de uma única curva.

    Args:
        x_data (array-like): Dados do eixo X.
        y_data (array-like): Dados do eixo Y.
        title (str, optional): Título principal do gráfico. Default é "".
        x_label (str, optional): Rótulo do eixo X. Default é "EIXO X".
        y_label (str, optional): Rótulo do eixo Y. Default é "EIXO Y".
        show_grid (bool, optional): Ativa a grade no fundo do gráfico. Default é False.
        show_box (bool, optional): Mantém a caixa ao redor do gráfico. Default é True.
        axis_scale (str, optional): Escala dos eixos ('linear', 'log'). Default é "linear".
        color (str, optional): Cor da linha. Default é "black".
        linewidth (float, optional): Espessura da linha. Default é 2.5.
        title_fontsize (int, optional): Tamanho da fonte do título. Default é 16.
        axis_fontsize (int, optional): Tamanho da fonte dos eixos. Default é 12.
        linestyle (str, optional): Estilo da linha (ex: '-', '--', ':'). Default é "-".
        alpha (float, optional): Opacidade da linha (0.0 a 1.0). Default é 0.8.
        grid_color (str, optional): Cor da grade. Default é "#E6E6E6".
        fig_width (float, optional): Largura da figura em polegadas. Default é 7.
        fig_height (float, optional): Altura da figura em polegadas. Default é 6.
        remove_borders (bool, optional): Remove as bordas superior e direita se show_box=True. Default é False.
        marker (str, optional): Marcador dos pontos (ex: 'o', '*', 's'). Default é None.
        save_fig (bool, optional): Se True, salva a figura no diretório 'figures/'. Default é False.
        dpi (int, optional): Resolução da imagem salva. Default é 600.
        file_format (str, optional): Formato do arquivo salvo ('pdf', 'png', 'svg'). Default é "pdf".
        filename (str, optional): Nome do arquivo a ser salvo. Default é "basicgraph".
        show_plot (bool, optional): Exibe o gráfico na tela. Default é True.

    Returns:
        None

    Example:
        >>> import numpy as np
        >>> x = np.linspace(0, 10, 100)
        >>> y = np.sin(x)
        >>> gp.basic(x, y, title="Função Seno", x_label="Tempo (s)", y_label="Amplitude")
    """
    plt.rcParams.update(
        {
            "font.family": "serif",
            "mathtext.fontset": "dejavuserif",
            "axes.linewidth": 1.2,
            "xtick.direction": "in",
            "ytick.direction": "in",
            "xtick.top": True,
            "ytick.right": True,
            "xtick.labelsize": axis_fontsize - 2,
            "ytick.labelsize": axis_fontsize - 2,
            "legend.frameon": False,
        }
    )

    fig, ax = plt.subplots(figsize=(fig_width, fig_height), dpi=100)
    ax.plot(
        x_data,
        y_data,
        color=color,
        linewidth=linewidth,
        linestyle=linestyle,
        alpha=alpha,
        marker=marker,
        label=title if title else None,
    )

    if title:
        ax.set_title(title, fontsize=title_fontsize, pad=15, fontweight="bold")

    ax.set_xlabel(x_label, fontsize=axis_fontsize, labelpad=8)
    ax.set_ylabel(y_label, fontsize=axis_fontsize, labelpad=8)
    ax.set_xscale(axis_scale)
    ax.set_yscale(axis_scale)
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.tick_params(which="major", length=6, width=1.2)
    ax.tick_params(which="minor", length=3, width=1.0)

    if show_grid:
        ax.grid(True, linestyle="--", linewidth=0.5, color=grid_color, alpha=0.7)
        ax.set_axisbelow(True)

    if not show_box:
        ax.set_frame_on(False)
    elif remove_borders:
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
    else:
        for spine in ax.spines.values():
            spine.set_visible(True)
            spine.set_color("black")

    plt.tight_layout()

    if save_fig:
        if not os.path.exists("figures"):
            os.makedirs("figures")
        filepath = f"figures/{filename}.{file_format}"
        plt.savefig(filepath, dpi=dpi, bbox_inches="tight", facecolor="white")

    if show_plot:
        plt.show()
    else:
        plt.close(fig)

    return None


def multi(
    x_list,
    y_list,
    curve_names=None,
    title="",
    x_label="EIXO X",
    y_label="EIXO Y",
    show_grid=False,
    show_box=True,
    axis_scale="linear",
    color_style="random",
    linewidth=2,
    title_fontsize=14,
    axis_fontsize=12,
    linestyle="cycle",
    alpha=1.0,
    grid_color="#E6E6E6",
    fig_width=7,
    fig_height=6,
    remove_borders=False,
    marker=None,
    show_legend=True,
    legend_title=None,
    legend_box=False,
    save_fig=False,
    dpi=600,
    file_format="pdf",
    filename="multigraph",
    show_plot=True,
):
    """
    Gera um gráfico 2D contendo múltiplas curvas sobrepostas.

    Args:
        x_list (list de arrays): Lista contendo os arrays do eixo X para cada curva.
        y_list (list de arrays): Lista contendo os arrays do eixo Y para cada curva.
        curve_names (list de str, optional): Nomes de cada curva para a legenda. Default é None.
        title (str, optional): Título principal do gráfico. Default é "".
        x_label (str, optional): Rótulo do eixo X. Default é "EIXO X".
        y_label (str, optional): Rótulo do eixo Y. Default é "EIXO Y".
        show_grid (bool, optional): Ativa a grade no fundo. Default é False.
        show_box (bool, optional): Mantém a caixa ao redor do gráfico. Default é True.
        axis_scale (str, optional): Escala dos eixos. Default é "linear".
        color_style (str ou list, optional): 'random', 'preto', ou lista de cores customizada. Default é "random".
        linewidth (float, optional): Espessura das linhas. Default é 2.
        title_fontsize (int, optional): Tamanho da fonte do título. Default é 14.
        axis_fontsize (int, optional): Tamanho da fonte dos eixos. Default é 12.
        linestyle (str ou list, optional): 'cycle' para alternar automaticamente, ou lista customizada. Default é "cycle".
        alpha (float, optional): Opacidade das linhas. Default é 1.0.
        grid_color (str, optional): Cor da grade. Default é "#E6E6E6".
        fig_width (float, optional): Largura da figura em polegadas. Default é 7.
        fig_height (float, optional): Altura da figura em polegadas. Default é 6.
        remove_borders (bool, optional): Remove as bordas superior e direita. Default é False.
        marker (str, optional): Marcador dos pontos. Default é None.
        show_legend (bool, optional): Exibe a legenda. Default é True.
        legend_title (str, optional): Título da caixa de legenda. Default é None.
        legend_box (bool, optional): Adiciona moldura ao redor da legenda. Default é False.
        save_fig (bool, optional): Salva a figura no disco. Default é False.
        dpi (int, optional): Resolução de salvamento. Default é 600.
        file_format (str, optional): Formato do arquivo. Default é "pdf".
        filename (str, optional): Nome do arquivo. Default é "multigraph".
        show_plot (bool, optional): Exibe o gráfico na tela. Default é True.

    Returns:
        None

    Example:
        >>> import numpy as np
        >>> x1, y1 = np.linspace(0, 5, 50), np.linspace(0, 5, 50)**2
        >>> x2, y2 = np.linspace(0, 5, 50), np.linspace(0, 5, 50)**3
        >>> gp.multi([x1, x2], [y1, y2], curve_names=["Quadrática", "Cúbica"], x_label="x", y_label="f(x)")
    """
    plt.rcParams.update(
        {
            "font.family": "serif",
            "mathtext.fontset": "dejavuserif",
            "axes.linewidth": 1.2,
            "xtick.direction": "in",
            "ytick.direction": "in",
            "xtick.top": True,
            "ytick.right": True,
            "xtick.labelsize": axis_fontsize - 2,
            "ytick.labelsize": axis_fontsize - 2,
        }
    )

    if len(x_list) != len(y_list):
        raise ValueError(
            "O número de listas em X deve ser igual ao número de listas em Y."
        )

    fig, ax = plt.subplots(figsize=(fig_width, fig_height), dpi=100)
    num_curves = len(x_list)

    if color_style == "preto":
        colors = ["black"] * num_curves
    elif color_style == "random":
        cmap = plt.get_cmap("tab10")
        colors = [cmap(i % 10) for i in range(num_curves)]
    elif isinstance(color_style, list):
        colors = color_style
    else:
        colors = [color_style] * num_curves

    if linestyle == "cycle":
        styles_list = ["-", ":", "--", "-."]
    elif isinstance(linestyle, list):
        styles_list = linestyle
    else:
        styles_list = [linestyle]

    for i in range(num_curves):
        curve_label = curve_names[i] if curve_names else f"Curva {i+1}"
        ax.plot(
            x_list[i],
            y_list[i],
            color=colors[i % len(colors)],
            linewidth=linewidth,
            linestyle=styles_list[i % len(styles_list)],
            alpha=alpha,
            marker=marker,
            label=curve_label,
        )

    if title:
        ax.set_title(title, fontsize=title_fontsize, pad=15, fontweight="bold")

    ax.set_xlabel(x_label, fontsize=axis_fontsize, labelpad=8)
    ax.set_ylabel(y_label, fontsize=axis_fontsize, labelpad=8)
    ax.set_xscale(axis_scale)
    ax.set_yscale(axis_scale)

    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.tick_params(which="major", length=6, width=1.2)
    ax.tick_params(which="minor", length=3, width=1.0)

    if show_legend:
        ax.legend(
            title=legend_title,
            frameon=legend_box,
            fontsize=axis_fontsize * 0.9,
            title_fontsize=axis_fontsize,
            loc="best",
            edgecolor="black" if legend_box else None,
        )

    if show_grid:
        ax.grid(True, linestyle="--", linewidth=0.5, color=grid_color, alpha=0.7)
        ax.set_axisbelow(True)

    if not show_box:
        ax.set_frame_on(False)
    elif remove_borders:
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
    else:
        for spine in ax.spines.values():
            spine.set_visible(True)
            spine.set_color("black")

    plt.tight_layout()

    if save_fig:
        if not os.path.exists("figures"):
            os.makedirs("figures")
        filepath = f"figures/{filename}.{file_format}"
        plt.savefig(filepath, dpi=dpi, bbox_inches="tight", facecolor="white")

    if show_plot:
        plt.show()
    else:
        plt.close(fig)

    return None


def elipse(
    x_data,
    y_data,
    z_data,
    extra_line_x=None,
    extra_line_y=None,
    extra_line_label="Linha extra",
    extra_line_width=1.0,
    extra_line_style=":",
    extra_line_color="black",
    highlight_point=None,
    ellipse_levels=None,
    sigma_names=None,
    show_sigma=True,
    title=None,
    x_label="EIXO X",
    y_label="EIXO Y",
    show_grid=True,
    show_box=True,
    legend_frame=True,
    legend_alpha=0.5,
    legend_fontsize=11,
    colorbar_format="neither",
    axis_scale="linear",
    z_scale="linear",
    colorbar_ticks=None,
    cmap="viridis_r",
    title_fontsize=16,
    axis_fontsize=14,
    highlight_label="Destaque",
    highlight_color="red",
    highlight_marker="*",
    highlight_size=150,
    ellipse_styles=["-", ":", ":"],
    ellipse_colors=["red", "green", "blue"],
    fig_width=8,
    fig_height=6,
    remove_borders=False,
    show_colorbar=True,
    colorbar_label=r"$\chi^2$",
    heatmap_levels=200,
    save_fig=False,
    dpi=600,
    file_format="pdf",
    filename="ellipse_graph",
    show_plot=True,
):
    """
    Gera um mapa de contorno (heat map) frequentemente usado para visualização de chi-quadrado e intervalos de confiança.

    Args:
        x_data (array-like): Matriz de coordenadas X (geralmente gerada por meshgrid).
        y_data (array-like): Matriz de coordenadas Y (geralmente gerada por meshgrid).
        z_data (array-like): Matriz de valores Z correspondentes a X e Y.
        extra_line_x (array-like, optional): Coordenadas X para uma linha adicional sobreposta. Default é None.
        extra_line_y (array-like, optional): Coordenadas Y para uma linha adicional sobreposta. Default é None.
        extra_line_label (str, optional): Rótulo da linha extra. Default é "Linha extra".
        extra_line_width (float, optional): Espessura da linha extra. Default é 1.0.
        extra_line_style (str, optional): Estilo da linha extra. Default é ":".
        extra_line_color (str, optional): Cor da linha extra. Default é "black".
        highlight_point (tuple, optional): Tupla (x, y) marcando o melhor ajuste (best-fit). Default é None.
        ellipse_levels (list, optional): Valores exatos de Z onde os contornos (elipses) serão desenhados. Default é None.
        sigma_names (list, optional): Lista de strings nomeando os níveis (ex: ['68%', '95%']). Default é None.
        show_sigma (bool, optional): Escreve o nome do nível sobre a linha da elipse. Default é True.
        title (str, optional): Título do gráfico. Default é None.
        x_label (str, optional): Rótulo do eixo X. Default é "EIXO X".
        y_label (str, optional): Rótulo do eixo Y. Default é "EIXO Y".
        show_grid (bool, optional): Ativa a grade do gráfico. Default é True.
        show_box (bool, optional): Mantém a moldura do gráfico. Default é True.
        legend_frame (bool, optional): Ativa a caixa ao redor da legenda. Default é True.
        legend_alpha (float, optional): Transparência do fundo da legenda. Default é 0.5.
        legend_fontsize (int, optional): Tamanho da fonte da legenda. Default é 11.
        colorbar_format (str, optional): Formato de extensão da colorbar ('max', 'min', 'both', 'neither'). Default é "neither".
        axis_scale (str, optional): Escala para os eixos X e Y. Default é "linear".
        z_scale (str, optional): Escala de cor do eixo Z ('linear' ou 'log'). Default é "linear".
        colorbar_ticks (int, optional): Limite de marcações na barra de cores. Default é None.
        cmap (str, optional): Colormap para a superfície de preenchimento. Default é "viridis_r".
        title_fontsize (int, optional): Tamanho da fonte do título. Default é 16.
        axis_fontsize (int, optional): Tamanho da fonte dos eixos. Default é 14.
        highlight_label (str, optional): Nome para o ponto de destaque na legenda. Default é "Destaque".
        highlight_color (str, optional): Cor do marcador de destaque. Default é "red".
        highlight_marker (str, optional): Símbolo do marcador de destaque. Default é "*".
        highlight_size (int, optional): Tamanho do marcador de destaque. Default é 150.
        ellipse_styles (list, optional): Estilos das elipses traçadas. Default é ["-", ":", ":"].
        ellipse_colors (list, optional): Cores das elipses traçadas. Default é ["red", "green", "blue"].
        fig_width (float, optional): Largura da figura. Default é 8.
        fig_height (float, optional): Altura da figura. Default é 6.
        remove_borders (bool, optional): Remove as bordas direitas e superiores. Default é False.
        show_colorbar (bool, optional): Exibe a barra lateral de cores. Default é True.
        colorbar_label (str, optional): Rótulo da barra de cores. Default é r"$\chi^2$".
        heatmap_levels (int, optional): Níveis gerados no contourf para gradiente suave. Default é 200.
        save_fig (bool, optional): Salva o gráfico em arquivo. Default é False.
        dpi (int, optional): Resolução do arquivo salvo. Default é 600.
        file_format (str, optional): Formato do arquivo salvo. Default é "pdf".
        filename (str, optional): Nome do arquivo a ser salvo. Default é "ellipse_graph".
        show_plot (bool, optional): Exibe o gráfico na tela. Default é True.

    Returns:
        tuple: (fig, ax) contendo os objetos de figura e eixo da Matplotlib.

    Example:
        >>> import numpy as np
        >>> X, Y = np.meshgrid(np.linspace(-3, 3, 100), np.linspace(-3, 3, 100))
        >>> Z = X**2 + Y**2
        >>> gp.elipse(X, Y, Z, ellipse_levels=[2.30, 6.18], highlight_point=(0,0), cmap="magma")
    """
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

    fig, ax = plt.subplots(figsize=(fig_width, fig_height))

    if z_scale == "log":
        Z_min_positive = np.min(z_data[z_data > 0]) if np.any(z_data > 0) else 1e-10
        norm = LogNorm(vmin=Z_min_positive, vmax=np.max(z_data))
        levels_cf = np.geomspace(Z_min_positive, np.max(z_data), heatmap_levels)
    else:
        norm = None
        levels_cf = heatmap_levels

    cf = ax.contourf(
        x_data,
        y_data,
        z_data,
        levels=levels_cf,
        cmap=cmap,
        norm=norm,
        extend=colorbar_format,
        antialiased=True,
        rasterized=True,
    )

    if ellipse_levels is not None:
        if sigma_names is None:
            sigma_names = [rf"{i+1}$\sigma$" for i in range(len(ellipse_levels))]

        for i, level in enumerate(ellipse_levels):
            style = ellipse_styles[i % len(ellipse_styles)]
            color = ellipse_colors[i % len(ellipse_colors)]
            sigma_name = sigma_names[i % len(sigma_names)]

            contour = ax.contour(
                x_data,
                y_data,
                z_data,
                levels=[level],
                colors=[color],
                linestyles=style,
                linewidths=1.8,
            )

            if show_sigma:
                fmt = {level: sigma_name}
                labels_text = ax.clabel(
                    contour,
                    inline=True,
                    fontsize=axis_fontsize * 0.9,
                    fmt=fmt,
                    colors=[color],
                )
                for text in labels_text:
                    text.set_fontweight("bold")

    if extra_line_x is not None and extra_line_y is not None:
        ax.plot(
            extra_line_x,
            extra_line_y,
            color=extra_line_color,
            linestyle=extra_line_style,
            linewidth=extra_line_width,
            label=extra_line_label,
            zorder=4,
        )

    if highlight_point is not None:
        ax.scatter(
            highlight_point[0],
            highlight_point[1],
            color=highlight_color,
            marker=highlight_marker,
            s=highlight_size,
            label=f"{highlight_label}\n({highlight_point[0]:.3f}, {highlight_point[1]:.3f})",
            zorder=5,
        )

    if show_colorbar:
        cbar = fig.colorbar(cf, ax=ax, pad=0.02)
        cbar.set_label(colorbar_label, fontsize=axis_fontsize)
        cbar.ax.tick_params(labelsize=axis_fontsize * 0.8)
        cbar.outline.set_linewidth(1.2)

        if z_scale == "log":
            cbar.ax.yaxis.set_major_formatter(LogFormatterMathtext())
            if colorbar_ticks is not None:
                cbar.ax.yaxis.set_major_locator(
                    LogLocator(base=10.0, numticks=colorbar_ticks)
                )
            else:
                cbar.ax.yaxis.set_minor_locator(
                    LogLocator(base=10.0, subs=np.arange(2, 10) * 0.1)
                )
        else:
            if colorbar_ticks is not None:
                cbar.ax.yaxis.set_major_locator(MaxNLocator(colorbar_ticks))

    if title:
        ax.set_title(title, fontsize=title_fontsize, pad=15)

    ax.set_xlabel(x_label, fontsize=axis_fontsize, labelpad=10)
    ax.set_ylabel(y_label, fontsize=axis_fontsize, labelpad=10)
    ax.set_xscale(axis_scale)
    ax.set_yscale(axis_scale)

    ax.minorticks_on()
    ax.tick_params(which="minor", direction="in", top=True, right=True)

    if highlight_point is not None or (
        extra_line_x is not None and extra_line_y is not None
    ):
        ax.legend(
            frameon=legend_frame,
            facecolor="white",
            framealpha=legend_alpha,
            edgecolor="#333333",
            fontsize=legend_fontsize,
            loc="best",
        )

    if show_grid:
        ax.grid(True, linestyle=":", linewidth=0.5, color="black", alpha=0.15)
        ax.set_axisbelow(False)

    if not show_box:
        ax.set_frame_on(False)
    elif remove_borders:
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

    ax.set_xlim(np.min(x_data), np.max(x_data))
    ax.set_ylim(np.min(y_data), np.max(y_data))

    plt.tight_layout()

    if save_fig:
        if not os.path.exists("figures"):
            os.makedirs("figures")
        filepath = f"figures/{filename}.{file_format}"
        plt.savefig(filepath, dpi=dpi, bbox_inches="tight")

    if show_plot:
        plt.show()

    return fig, ax


def basicstyle(
    x_data,
    y_data,
    highlight_point=None,
    title="",
    x_label="EIXO X",
    y_label="EIXO Y",
    show_grid=False,
    show_box=True,
    axis_scale="linear",
    color="black",
    linewidth=2.0,
    title_fontsize=16,
    axis_fontsize=12,
    linestyle="-",
    alpha=0.7,
    grid_color="#E6E6E6",
    fig_width=7,
    fig_height=6,
    remove_borders=False,
    marker=None,
    highlight_color="red",
    curve_label="Dados",
    highlight_marker="*",
    highlight_size=150,
    highlight_label="Destaque",
    save_fig=False,
    dpi=600,
    file_format="pdf",
    filename="basicdot_graph",
    show_plot=True,
):
    """
    Gera um gráfico 2D focado em exibir uma curva em conjunto com a evidenciação de um ponto específico.

    Args:
        x_data (array-like): Dados do eixo X.
        y_data (array-like): Dados do eixo Y.
        highlight_point (tuple, optional): Coordenadas (x, y) do ponto que receberá destaque. Default é None.
        title (str, optional): Título do gráfico. Default é "".
        x_label (str, optional): Rótulo do eixo X. Default é "EIXO X".
        y_label (str, optional): Rótulo do eixo Y. Default é "EIXO Y".
        show_grid (bool, optional): Ativa a grade do gráfico. Default é False.
        show_box (bool, optional): Mantém a caixa ao redor do gráfico. Default é True.
        axis_scale (str, optional): Escala para os eixos. Default é "linear".
        color (str, optional): Cor da curva de dados. Default é "black".
        linewidth (float, optional): Espessura da curva. Default é 2.0.
        title_fontsize (int, optional): Tamanho da fonte do título. Default é 16.
        axis_fontsize (int, optional): Tamanho da fonte dos eixos. Default é 12.
        linestyle (str, optional): Estilo da linha. Default é "-".
        alpha (float, optional): Opacidade da linha. Default é 0.7.
        grid_color (str, optional): Cor da grade. Default é "#E6E6E6".
        fig_width (float, optional): Largura da figura. Default é 7.
        fig_height (float, optional): Altura da figura. Default é 6.
        remove_borders (bool, optional): Remove bordas superior e direita. Default é False.
        marker (str, optional): Marcador de pontos na curva regular. Default é None.
        highlight_color (str, optional): Cor do marcador de destaque. Default é "red".
        curve_label (str, optional): Nome da curva na legenda. Default é "Dados".
        highlight_marker (str, optional): Símbolo do marcador de destaque. Default é "*".
        highlight_size (int, optional): Tamanho do marcador de destaque. Default é 150.
        highlight_label (str, optional): Nome do marcador de destaque na legenda. Default é "Destaque".
        save_fig (bool, optional): Salva a figura em arquivo. Default é False.
        dpi (int, optional): Resolução de salvamento. Default é 600.
        file_format (str, optional): Formato do arquivo gerado. Default é "pdf".
        filename (str, optional): Nome do arquivo. Default é "basicdot_graph".
        show_plot (bool, optional): Exibe o gráfico em tela. Default é True.

    Returns:
        None

    Example:
        >>> import numpy as np
        >>> x = np.linspace(0, 10, 50)
        >>> y = np.exp(-x)
        >>> gp.basicdot(x, y, highlight_point=(0, 1), highlight_label="Ponto de Injeção")
    """
    plt.rcParams.update(
        {
            "font.family": "serif",
            "mathtext.fontset": "dejavuserif",
            "axes.linewidth": 1.2,
            "xtick.direction": "in",
            "ytick.direction": "in",
            "xtick.top": True,
            "ytick.right": True,
            "xtick.labelsize": axis_fontsize - 2,
            "ytick.labelsize": axis_fontsize - 2,
        }
    )

    fig, ax = plt.subplots(figsize=(fig_width, fig_height), dpi=100)

    ax.plot(
        x_data,
        y_data,
        color=color,
        linewidth=linewidth,
        linestyle=linestyle,
        alpha=alpha,
        marker=marker,
        label=curve_label if curve_label else "Dados",
    )

    if highlight_point is not None:
        ax.scatter(
            highlight_point[0],
            highlight_point[1],
            color=highlight_color,
            marker=highlight_marker,
            s=highlight_size,
            label=highlight_label,
            zorder=5,
        )

    if title:
        ax.set_title(title, fontsize=title_fontsize, pad=15, fontweight="bold")

    ax.set_xlabel(x_label, fontsize=axis_fontsize, labelpad=8)
    ax.set_ylabel(y_label, fontsize=axis_fontsize, labelpad=8)
    ax.set_xscale(axis_scale)
    ax.set_yscale(axis_scale)

    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.tick_params(which="major", length=6, width=1.2)
    ax.tick_params(which="minor", length=3, width=1.0)

    if title or highlight_point:
        ax.legend(frameon=False, fontsize=axis_fontsize * 0.9)

    if show_grid:
        ax.grid(True, linestyle="--", linewidth=0.5, color=grid_color, alpha=0.7)
        ax.set_axisbelow(True)

    if not show_box:
        ax.set_frame_on(False)
    elif remove_borders:
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
    else:
        for spine in ax.spines.values():
            spine.set_visible(True)
            spine.set_color("black")

    plt.tight_layout()

    if save_fig:
        if not os.path.exists("figures"):
            os.makedirs("figures")
        filepath = f"figures/{filename}.{file_format}"
        plt.savefig(filepath, dpi=dpi, bbox_inches="tight", facecolor="white")

    if show_plot:
        plt.show()
    else:
        plt.close(fig)

    return None
