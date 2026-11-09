#!/bin/zsh
set -e
PROJECT_ROOT="${0:A:h}"
cd "$PROJECT_ROOT/Lab10-DataScience"
exec "$PROJECT_ROOT/.venv/bin/python" -m streamlit run app.py
