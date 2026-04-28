#
# * =============================================================================
# * SYSTEM
# * =============================================================================


def savetable(nome, matriz, vertical=True, header=None, sep="\t"):
    import os
    folder = "data"
    if not os.path.exists(folder):
        os.makedirs(folder)

    caminho = os.path.join(folder, f"{nome}.txt")
    
    # --- CORREÇÃO AQUI ---
    # Se for uma lista 1D (ex: uma única coluna de strings ou números), 
    # envolvemos ela em outra lista para forçar o formato de matriz 2D.
    if matriz and not isinstance(matriz[0], (list, tuple)):
        matriz = [matriz]

    # Agora o zip() funcionará corretamente sem fatiar as strings
    dados_para_salvar = zip(*matriz) if vertical else matriz

    with open(caminho, "w", encoding="utf-8") as f:
        if header:
            linhas_header = header.split("\n") if isinstance(header, str) else header
            for linha_h in linhas_header:
                f.write(f"# {linha_h}\n")

        for linha in dados_para_salvar:
            # Transformamos tudo para string e unimos com o separador
            string_linha = sep.join(map(str, linha))
            f.write(string_linha + "\n")


def loadtable(nome, vertical=True, sep="\t"):
    import os

    caminho = os.path.join(f"{nome}")
    if not os.path.exists(caminho):
        return None
        
    matriz_lida = []
    with open(caminho, "r", encoding="utf-8-sig") as f:
        for linha in f:
            linha = linha.strip()
            # Ignora linhas vazias ou comentários
            if not linha or linha.startswith("#"):
                continue
                
            valores = []
            for x in linha.split(sep):
                item = x.strip()
                try:
                    # Tenta converter para float
                    valores.append(float(item))
                except ValueError:
                    # Se falhar (for um texto), adiciona como string
                    valores.append(item)
                    
            matriz_lida.append(valores)
            
    # Transpõe a matriz caso a leitura seja vertical
    if vertical:
        matriz_lida = [list(item) for item in zip(*matriz_lida)]
        
    return matriz_lida


def identificadora(caminho):
    import os

    if not os.path.exists(caminho):
        return None
    candidatos = ["\t", ",", ";", " "]
    with open(caminho, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if not linha or linha.startswith("#"):
                continue
            contagem = {sep: linha.count(sep) for sep in candidatos}
            melhor_sep = max(contagem, key=contagem.get)
            return melhor_sep if contagem[melhor_sep] > 0 else "\t"
    return "\t"


def ler_cabecalho(nome):
    import os

    caminho = os.path.join("data", f"{nome}.txt")
    if not os.path.exists(caminho):
        return None
    header = []
    with open(caminho, "r", encoding="utf-8-sig") as f:
        for linha in f:
            if linha.startswith("#"):
                header.append(linha.replace("#", "").strip())
            else:
                break
    return header


def versionador(nome):
    import os

    folder = "data"
    caminho = os.path.join(folder, f"{nome}.txt")
    if not os.path.exists(caminho):
        return nome

    contador = 1
    while os.path.exists(os.path.join(folder, f"{nome}_{contador}.txt")):
        contador += 1
    return f"{nome}_{contador}"
