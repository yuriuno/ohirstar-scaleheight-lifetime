from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here,'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ohirstar-scaleheight-lifetime',
    packages=['ohirstar-scaleheight-lifetime'], 
    version='1.0.0', 
    license='MIT', 
    install_requires=['numpy','scipy'], 
    author='yuriuno', 
    author_email='k8688309@kadai.jp',
    url='https://github.com/yuriuno/ohirstar-scaleheight-lifetime',
    description='Estimate a distribution and lifetime of star in the Galaxy.',
    long_description=long_description, 
    long_description_content_type='text/markdown',
    keywords='scaleheight scale-height lifetime OH/IR star',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
    )
