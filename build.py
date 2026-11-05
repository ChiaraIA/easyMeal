#!/usr/bin/env python3
"""Genera index.html (versione standalone) da src/easymeal.html.

src/easymeal.html è scritto nel formato degli Artifact di claude.ai
(solo il contenuto della pagina: <title>, <style>, markup e <script>),
quindi qui lo avvolgiamo nello scheletro HTML completo per poterlo aprire
direttamente nel browser o pubblicarlo su GitHub Pages.

Uso:  python3 build.py
"""
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "src" / "easymeal.html"
OUT = ROOT / "index.html"

SKELETON = """<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="color-scheme" content="light dark">
<style>body{{margin:0}}[hidden]{{display:none!important}}img{{max-width:100%}}</style>
</head>
<body>
<!-- File generato da build.py: modifica src/easymeal.html, non questo file. -->
{body}
</body>
</html>
"""


def main() -> None:
    body = SRC.read_text(encoding="utf-8").strip()
    OUT.write_text(SKELETON.format(body=body), encoding="utf-8")
    print(f"✓ {OUT.relative_to(ROOT)} generato ({OUT.stat().st_size / 1024:.1f} KB)")


if __name__ == "__main__":
    main()
