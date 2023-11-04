import requests
from bs4 import BeautifulSoup
import pandas as pd

URL='https://g1.globo.com/busca/?q='
busca=input('Qual o tema da pesquisa:')
lista_noticias=[]

pesquisa=requests.get(URL+busca)
site=BeautifulSoup(pesquisa.text,'html.parser')

noticias=site.findAll('li',attrs={'class':'widget widget--card widget--info'})
#print(noticias.prettify())

for noticia in noticias:
    titulo=noticia.find('div',attrs={'class':'widget--info__title product-color'})
    link_noticias=noticia.find('a',attrs={'class':'widget--info__media widget--info__media--video'})
    subtTitulo=noticia.find('p',attrs={'class':'widget--info__description'})

    #print('Título da notícia:',titulo.text.strip())
    #print('Descrição:', subtTitulo.text.strip())

    if(link_noticias):
        #print('Link da notícia:', link_noticias['href'])
        lista_noticias.append([titulo.text,subtTitulo.text,link_noticias['href']])
    else:
        lista_noticias.append([titulo.text, subtTitulo.text,''])

    #print('\n\n')

lista=pd.DataFrame(lista_noticias,columns=['Título da notícia','Descrição','Link'])
lista.to_excel('NoticiaPesquisa.xlsx',index=False)