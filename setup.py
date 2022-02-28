from setuptools import find_packages, setup

setup(
    name='nexus_statscalc',
    packages=find_packages(include=['nexus_statscalc']),
    version='0.1.0',
    description='Generates queries for statsdata',
    install_requires=['pandas','cs20-easygui==0.9.5', 'easygui-qt==0.9.3', 'openpyxl==3.0.9', 'PyQt5', 'pyperclip'],
    setup_requires = [],
    tests_require = [],
    author='Nexus Integra',
    license='UNLICENSED: private Nexus Integra',
)