# Download NLTK resources
import nltk
nltk.download('stopwords')
nltk.download('wordnet')

# Dowload gensim models
import gensim.downloader as api
glove_wiki_100 = api.load("glove-wiki-gigaword-100")  
# optional (900MB): 
# fasttext_wiki_news_300 = api.load("fasttext-wiki-news-subwords-300")