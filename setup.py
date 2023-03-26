from setuptools import setup, find_packages

setup(
    name='tomd',
    version='0.1',
    author='adabaed',
    packages=['src'],
    include_package_data=True,
    install_requires=[
        'click',
        'pdfminer.six',
        'python-docx'
    ],
    entry_points='''
        [console_scripts]
        tomd=src.main:tomd
    '''
)