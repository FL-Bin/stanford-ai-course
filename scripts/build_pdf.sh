#!/usr/bin/env bash
# Build both PDF books into ./dist (or $1). Requires: python3, weasyprint, markdown, fonts-noto-cjk.
set -euo pipefail
cd "$(dirname "$0")/.."
python3 scripts/build_pdf.py "${1:-dist}"
