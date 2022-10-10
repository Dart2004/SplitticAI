from setuptools import setup
import pypandoc

setup(
    name='Splittic',
    url='https://github.com/Dart2004/Splittic-AI',
    author='Daniel Klimmer',
    author_email='danielklimmer2000@protonmail.com',
    packages=['splitticai'],
    install_requires=['requests', 'bs4'],
    version='1.0',
    license='MIT',
    description='The Most Advanced AI Ever',
    long_description=pypandoc.convert('README.md', 'rst')
)
