from setuptools import setup

readme = open("./README.md", "r")

setup(
    name='consolebox',
    packages=['consolebox'],
    version='0.1',
    license='LGPL v3',
    description='A library for creating frames in the console',
    author='JordyM01',
    author_email='montoyamjavier@gmail.com',
    url='https://github.com/JordyM01/consolebox', # Usa la URL del repositorio de GitHub
    download_url='https://github.com/JordyM01/consolebox/archive/v0.1.tar.gz', # Te lo explico a continuación
    keywords='test example develop', # Palabras que definan tu paquete
    classifiers=['Programming Language :: Python',  # Clasificadores de compatibilidad con versiones de Python para tu paquete
                 'Programming Language :: Python :: 3.3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7'],
)