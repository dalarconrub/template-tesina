#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para reproducir la estructura completa de carpetas de la tesina,
incluyendo todos los archivos .txt y .gitkeep.
Uso: python crear_estructura_tesina.py [ruta_destino]
      Si no se indica ruta, se crea la carpeta 'Tesina' en el directorio actual.
"""

import os
import sys
from pathlib import Path


def crear_tesina(base: Path) -> None:
    """Crea la estructura de carpetas y archivos de la tesina bajo `base`."""
    base = Path(base)

    # 01_Borradores_y_textos_propios
    (base / "01_Borradores_y_textos_propios").mkdir(parents=True, exist_ok=True)
    (base / "01_Borradores_y_textos_propios" / "Capítulo1_Introducción.txt").write_text(
        "[Plantilla para Capítulo 1 - Introducción]\n"
        "Guarda este archivo como .docx cuando trabajes en Word, o edita aquí.\n",
        encoding="utf-8",
    )
    (base / "01_Borradores_y_textos_propios" / "Capítulo2_Metodología.txt").write_text(
        "[Plantilla para Capítulo 2 - Metodología]\n"
        "Guarda este archivo como .docx cuando trabajes en Word, o edita aquí.\n",
        encoding="utf-8",
    )
    (base / "01_Borradores_y_textos_propios" / "Notas_reuniones.txt").write_text(
        "Notas de reuniones con tutor/a\n"
        "-------------------------------\n"
        "Formato sugerido: Año_Mes_Día - Tema o resumen\n",
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
        "  Año_Mes_Día_Entrega_Tesina_vN.docx\n\n"
        "Ejemplos:\n"
        "  2025_03_15_Entrega_Tesina_v1.docx\n"
        "  2025_04_20_Entrega_Tesina_v2_correcciones.docx\n",
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
