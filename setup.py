from setuptools import setup, find_packages

setup(
    name="streamlit_db_demo",
    version="0.1.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "streamlit>=1.30.0",
        "pytest>=7.4.0",
        "pyright>=1.1.0",
        "setuptools>=65.0.0",
    ],
    python_requires=">=3.8",
)
