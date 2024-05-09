from setuptools import setup, find_packages

setup(
    name='Tamilnumbers',
    version='1.0.0',
    packages=find_packages(),
    author='Velkadamban',
    author_email='velkadamban@gmail.com',
    description='A package for converting Hindu-Arabic numerals to Tamil numerals.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/velkadamban/Tamil-numbers-converter/',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
)