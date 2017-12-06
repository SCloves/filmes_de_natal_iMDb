# usr/bin/python -tt
import sys
from os import path
import numpy as np
from PIL import Image
from wordcloud import WordCloud
import nltk

# get path to script's directory
currdir = path.dirname('/home/cloves/Documentos/cognitivo_ai/webinar/scraping_filmes_natal/')
STOPWORDS = nltk.corpus.stopwords.words('english')

def create_wordcloud(text, nome_img):
    # create numpy araay for wordcloud mask image
    mask = np.array(Image.open(path.join(currdir, "cloud.png")))

    # create set of stopwords
    stopwords = set(STOPWORDS)

    # create wordcloud object
    wc = WordCloud(background_color="white", 
                   max_words=200, 
                   mask=mask, 
                   stopwords=stopwords)
    
    wc.generate(text)

    # save wordcloud
    wc.to_file(path.join(currdir, nome_img + ".png"))


if __name__ == "__main__":
    # pegar arquivo
    text = open(sys.argv[1], 'r')
    palavras = text.readlines()
    text.close()
    texto = ''
    for comentario in palavras:
        texto += comentario
    # generate wordcloud
    create_wordcloud(texto, sys.argv[2])
