#!/usr/bin/env bash
# Build the textbook PDFs (CS146S-book-*.pdf) and the weekly-notes PDFs (CS146S-notes-*.pdf) into ./dist (or $1).
# Requires: python3, weasyprint, markdown, pygments, fonttools. Fonts are downloaded to .fonts/ on first run.
set -euo pipefail
cd "$(dirname "$0")/.."
python3 scripts/fetch_fonts.py
BOOK=1 python3 scripts/build_pdf.py "${1:-dist}"
python3 scripts/build_pdf.py "${1:-dist}"
