from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='vinicultura',
    version='1.0.0',
    packages=find_packages(),
    description='Este pacote trata informações sobre vinicultura',
    author='Márcio',
    author_email='marciohenrique79@gmail.com',
    install_requires=[
        'fastapi==0.115.12',
        'beautifulsoup4==4.13.4',
        'bs4==.0.2',
        'requests==2.32.3'
    ],
    url='https://github.com/marcioxxxx/vinicultura',  
    license='MIT',  
    long_description=long_description,
    long_description_content_type='text/markdown' 
)