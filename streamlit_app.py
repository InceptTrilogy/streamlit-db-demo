import sys
from pathlib import Path

# Add the src directory to Python path
src_path = Path(__file__).parent / "src"
sys.path.append(str(src_path))

# Import and run the main app
from streamlit_db_demo.app import main

if __name__ == "__main__":
    main()
