###### dealing html page####################
import urllib 
from urllib import request
import requests
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
import bs4
from bs4 import BeautifulSoup
from nltk.text import Text
from nltk.tokenize import word_tokenize, sent_tokenize
##################################
##############save the url file to your system  as html file and then start scraping############################
#################################
ur = "https://timesofindia.indiatimes.com/business/india-business/indigos-10-lakh-seats-up-for-grabs-at-fares-starting-rs-999/articleshow/65652536.cms"
html = request.urlopen(ur).read().decode('utf8')
ra = BeautifulSoup(html).get_text()
to = sent_tokenize(ra)
tokens =to[14:28]
text= nltk.Text(tokens)
