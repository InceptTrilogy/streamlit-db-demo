from dataclasses import dataclass
from typing import Final

import streamlit as st

TITLE: Final[str] = "Streamlit DB Demo"

@dataclass(frozen=True)
class AppConfig:
    title: str

def create_app_config() -> AppConfig:
    return AppConfig(title=TITLE)

def main() -> None:
    config = create_app_config()
    st.title(config.title)
    st.write("Hello World! Database integration coming soon.")

if __name__ == "__main__":
    main()
