import requests
from bs4 import BeautifulSoup
import pandas as pd

#Fazer a busca por noticias igual ao do mercado livre

lista_noticias=[]

URL="https://g1.globo.com"
pagina=requests.get(URL)
conteudo=pagina.content

#print(pagina.content)
#print(type(pagina.content)) Tipo bytes o conteúdo da página

site=BeautifulSoup(conteudo,'html.parser')

#print(type(site)) Tipo BeautifulSoup o conteúdo da página
#print(site.prettify())

noticias=site.find_all('div',attrs={'class':'feed-post-body'})

for noticia in noticias:

    titulo = noticia.find('a', attrs={'class': 'feed-post-link gui-color-primary gui-color-hover'})
    #print(titulo.text)
    #print("Link:",titulo['href'])

    subtitulo = noticia.find('div', attrs={'class': 'feed-post-body-resumo'})
    if(subtitulo):
        #print(subtitulo.text)
        lista_noticias.append([titulo.text,subtitulo.text,titulo['href']])
    else:
        lista_noticias.append([titulo.text,'',titulo['href']])
        #print()


news=pd.DataFrame(lista_noticias,columns=['Título','Subtítulo','Link'])
news.to_excel('noticias.xlsx',index=False)

#print(news)

#print(noticia.prettify())