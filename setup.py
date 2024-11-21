from setuptools import setup, find_packages

setup(
    name="streamlit_db_demo",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "streamlit>=1.30.0",
        "pytest>=7.4.0",
        "pyright>=1.1.0"
    ],
    python_requires=">=3.8",
)
