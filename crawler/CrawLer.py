import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pytesseract
import plotly.express as px
import duckduckgo_search
import cv2
from flair.models import SequenceTagger
from flair.data import Sentence
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from duckduckgo_search import ddg_images
import re
import PIL
from fastdownload import download_url
from time import sleep

############################

def ViewImage(image_path,figure_size=None): 
    """
    Display and return an image from the given file path.

    Parameters:
        image_path (str): The path to the image file.
        figure_size (tuple, optional): The size of the figure for displaying the image. Defaults to None.

    Returns:
        numpy.ndarray: The image as a NumPy array.

    Raises:
        FileNotFoundError: If the image file does not exist."""
    
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    plt.figure(figsize=figure_size)
    plt.imshow(image)
    return image
    

def perform_search(query):
    """Execute search for the inputted query"""
    search_results = []
    url = f"https://duckduckgo.com/html/?q={query}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.select('.result__url')
    for result in results:
        search_results.append(result.text)
    return search_results


def select_search(Tag1,Tag2=None):
    """
    Select and combine terms based on the provided tags.

    Parameters:
        Tag1 (str): The first tag to filter the DataFrame.
        Tag2 (str, optional): The second tag to filter the DataFrame. Defaults to None.

    Returns:
        pandas.Series: The combined terms from the filtered DataFrame.

    Raises:
        KeyError: If the provided tags are not present in the DataFrame.
    """
    # TAG1
    tag1 = df[df['Tag'] == Tag1]
    tag1.reset_index(inplace=True)
    tag1 = tag1.drop(['index','Tag'],axis=1)
    # TAG2
    tag2 = df[df['Tag'] == Tag2]
    tag2 = tag2.reset_index()
    tag2 = tag2.drop(['index','Tag'],axis=1)
    
    if Tag2 is not None:
        TERMS = pd.Series([(i +' '+j) for i in tag1.values for j in tag2.values])
    else:
        TERMS = pd.Series([i for i in tag1.values])
    return TERMS

def filter_linkedin_urls(strings):
    """Filter string for linkedin urls"""
    pattern = r"(?:http[s]?://)?(?:www\.)?linkedin\.com/(?:in|company)/[\w-]+"
    filtered_urls = [string.strip() for string in strings if re.search(pattern, string)]
    return filtered_urls

def search_images(term, max_images):
    """Search images """
    print(f'searching for {term}')
    return (ddg_images(keywords=term,max_results=max_images))