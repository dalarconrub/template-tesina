#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para reproducir la estructura completa de carpetas de la tesina,
incluyendo archivos .txt, .tex (LaTeX) y .gitkeep.
Soporta documentación en Word (.docx) y LaTeX (.tex → .pdf).
Uso: python crear_estructura_tesina.py [ruta_destino]
      Si no se indica ruta, se crea la carpeta 'Tesina' en el directorio actual.
"""

import os
import sys
from pathlib import Path


def crear_tesina(base: Path) -> None:
    """Crea la estructura de carpetas y archivos de la tesina bajo `base`."""
    base = Path(base)

    # 01_Borradores_y_textos_propios (Word + LaTeX)
    borr = base / "01_Borradores_y_textos_propios"
    borr.mkdir(parents=True, exist_ok=True)
    (borr / "Capítulo1_Introducción.txt").write_text(
        "[Plantilla para Capítulo 1 - Introducción]\n"
        "Puedes trabajar en Word (guarda como .docx) o en LaTeX (usa capitulo1_introduccion.tex y main.tex).\n",
        encoding="utf-8",
    )
    (borr / "Capítulo2_Metodología.txt").write_text(
        "[Plantilla para Capítulo 2 - Metodología]\n"
        "Puedes trabajar en Word (guarda como .docx) o en LaTeX (usa capitulo2_metodologia.tex y main.tex).\n",
        encoding="utf-8",
    )
    (borr / "Notas_reuniones.txt").write_text(
        "Notas de reuniones con tutor/a\n"
        "-------------------------------\n"
        "Formato sugerido: Año_Mes_Día - Tema o resumen\n",
        encoding="utf-8",
    )
    # LaTeX: documento principal y capítulos
    (borr / "main.tex").write_text(
        "% Documento principal de la tesina (LaTeX)\n"
        "% Compilar con: pdflatex main && pdflatex main (o latexmk -pdf main)\n\n"
        "\\documentclass[12pt,a4paper]{report}\n"
        "\\usepackage[utf8]{inputenc}\n"
        "\\usepackage[T1]{fontenc}\n"
        "\\usepackage[spanish]{babel}\n"
        "\\usepackage{graphicx}\n"
        "\\usepackage{hyperref}\n\n"
        "\\title{Título de la tesina}\n"
        "\\author{Autor}\n"
        "\\date{\\today}\n\n"
        "\\begin{document}\n"
        "\\maketitle\n"
        "\\tableofcontents\n\n"
        "\\input{capitulo1_introduccion}\n"
        "\\input{capitulo2_metodologia}\n\n"
        "% Añade más capítulos según necesites:\n"
        "% \\input{capitulo3_resultados}\n"
        "% \\input{capitulo4_discusion}\n\n"
        "% \\bibliographystyle{plain}\n"
        "% \\bibliography{../02_Referencias_bibliograficas/Referencias/mibiblio}\n\n"
        "\\end{document}\n",
        encoding="utf-8",
    )
    (borr / "capitulo1_introduccion.tex").write_text(
        "% Capítulo 1 — Introducción\n\n"
        "\\chapter{Introducción}\\label{cap:introduccion}\n\n"
        "Escribe aquí la introducción de tu tesina.\n\n"
        "Puedes usar referencias cruzadas (\\verb|\\ref{cap:introduccion}|) y citas "
        "(incluye un archivo \\texttt{.bib} en Referencias y usa \\verb|\\cite{}|).\n",
        encoding="utf-8",
    )
    (borr / "capitulo2_metodologia.tex").write_text(
        "% Capítulo 2 — Metodología\n\n"
        "\\chapter{Metodología}\\label{cap:metodologia}\n\n"
        "Escribe aquí la sección de metodología: diseño del estudio, fuentes de datos, "
        "métodos de análisis, etc.\n",
        encoding="utf-8",
    )

    # 02_Referencias_bibliográficas
    ref = base / "02_Referencias_bibliográficas"
    ref.mkdir(parents=True, exist_ok=True)
    (ref / "LEEME.txt").write_text(
        "Nombra los PDFs con el formato: Autor_Año_Título.pdf\n\n"
        "Ejemplos:\n"
        "  Libros/     → Garcia_2020_Introduccion_estadistica.pdf\n"
        "  Artículos/  → Lopez_2019_Metodos_cualitativos.pdf\n"
        "  Tesis/      → Perez_2018_Tesis_maestria.pdf\n\n"
        "Usa Zotero, Mendeley o EndNote para gestionar citas y exportar la bibliografía.\n",
        encoding="utf-8",
    )
    for sub in ["Libros", "Artículos", "Tesis"]:
        (ref / sub).mkdir(parents=True, exist_ok=True)
        (ref / sub / ".gitkeep").write_text("", encoding="utf-8")
    (ref / "Referencias").mkdir(parents=True, exist_ok=True)
    (ref / "Referencias" / "README.txt").write_text(
        "Referencias — Gestor bibliográfico (Zotero, EndNote, Mendeley)\n\n"
        "Aquí: bibliografías exportadas (BibTeX, RIS), copias de la base de datos o enlaces al gestor, "
        "y listas de referencias para insertar en el documento.\n\n"
        "Los PDFs van en las carpetas de este mismo nivel: Libros/, Artículos/, Tesis/. "
        "Nombra los archivos: Autor_Año_Título.pdf\n",
        encoding="utf-8",
    )

    # 03_Datos
    datos = base / "03_Datos"
    for sub in ["Datos_originales", "Datos_procesados", "Analisis", "Resultados"]:
        (datos / sub).mkdir(parents=True, exist_ok=True)
        (datos / sub / ".gitkeep").write_text("", encoding="utf-8")
    (datos / "Analisis" / "LEEME.txt").write_text(
        "Scripts de análisis y resultados.\n"
        "Guarda aquí scripts (R, Python, Stata, etc.) y los resultados generados.\n",
        encoding="utf-8",
    )

    # 04_Material_adicional
    mat = base / "04_Material_adicional"
    for sub in ["Imágenes", "Presentaciones", "Correspondencia_con_tutores"]:
        (mat / sub).mkdir(parents=True, exist_ok=True)
        (mat / sub / ".gitkeep").write_text("", encoding="utf-8")

    # 05_Versiones_entregadas
    (base / "05_Versiones_entregadas").mkdir(parents=True, exist_ok=True)
    (base / "05_Versiones_entregadas" / "LEEME.txt").write_text(
        "Guarda aquí cada versión entregada con el formato:\n"
        "  Año_Mes_Día_Entrega_Tesina_vN\n\n"
        "Formatos admitidos:\n"
        "  • Word:  .docx  (ej. 2025_03_15_Entrega_Tesina_v1.docx)\n"
        "  • LaTeX: .pdf   (ej. 2025_04_20_Entrega_Tesina_v2_correcciones.pdf)\n",
        encoding="utf-8",
    )

    print(f"Estructura de tesina creada en: {base.absolute()}")


def main() -> None:
    if len(sys.argv) > 1:
        destino = Path(sys.argv[1])
    else:
        destino = Path.cwd() / "Tesina"
    crear_tesina(destino)


if __name__ == "__main__":
    main()
