import sys
from streamlit.web import cli as stcli

sys.argv = ["streamlit", "run", "book-analyzer.py"]
sys.exit(stcli.main())
