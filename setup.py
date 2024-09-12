from setuptools import setup, find_packages

setup(
    name='PatternPalette',
    version='0.1',
    description='A Python package for generating various patterns.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Aditya Srivastav',
    author_email='adityathestar2006@gmail.com',
    packages=find_packages(),
    install_requires=[],
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
)
