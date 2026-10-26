#!/usr/bin/env bash
# Build the textbook PDFs (CS146S-book-*.pdf) and the weekly-notes PDFs (CS146S-notes-*.pdf) into ./dist (or $1).
# Requires: python3, weasyprint, markdown, Noto Sans SC (or another CJK font).
set -euo pipefail
cd "$(dirname "$0")/.."
BOOK=1 python3 scripts/build_pdf.py "${1:-dist}"
python3 scripts/build_pdf.py "${1:-dist}"
