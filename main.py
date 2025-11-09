"""Inter-Sight Main Entry Point"""

import sys
import subprocess

if __name__ == "__main__":
    # Run Streamlit app
    subprocess.run([
        sys.executable, "-m", "streamlit", "run",
        "ui/streamlit_app.py"
    ])
