from setuptools import setup, find_packages 
setup( 
    name="streamlimit", 
    version="0.1", 
    packages=find_packages(), 
    install_requires=[ 
        "streamlit", 
        "numpy", 
        "pandas", 
        "matplotlib", 
    ], 
) 
