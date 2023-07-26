from setuptools import setup, find_packages

setup(
    name='crawler',
    version='0.1',
    packages=find_packages(),
    install_requires=[flair,duckduckgo_search,pandas,numpy,matplotlib,pytesseract,cv2,requests,bs4,re,PIL,fastdownload,time],
    author='Harsh Jadhav',
    author_email='jadhavharshvardhan6301@gmail.com',
    description='A python package using OCR, NLP for goal of extracting and mining information through web searches
*In development*',
    url='https://github.com/Harshj6301/Crawler',
)