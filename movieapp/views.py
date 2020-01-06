from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen,Request

HOME_URL='https://www.cinemablend.com'
BASE_URL='https://www.cinemablend.com/reviews'

# Create your views here.
def testing(request):
    req=Request(BASE_URL,headers={'User-Agent': 'Mozilla/5.0'})
    uClient=urlopen(req)
    html_page=uClient.read()
    uClient.close()
    soup=BeautifulSoup(html_page,'html.parser')
    all_movies_list=soup.select('div[class^=story_item]')
    #print(all_movies_list)
    final_reviews=[]

    for review in all_movies_list:
        movie_link=review.a['href']
        movie_review_link=HOME_URL+movie_link
        imges=review.find('img')
        movie_image=imges.get('data-src')
        content_clss=review.find('div',{'class':'content'})
        movie_title=''
        if content_clss!=None:
         movie_title = content_clss.div.a.text
         #print(movie_title)

        author_class = review.find('div', {'class': 'author'})
        movie_rating=''
        movie_releasedate=''
        if author_class!=None:
            if author_class.div!=None:
             movie_rating=author_class.div.img['title']
             movie_star_symbol=author_class.find('img').get('data-src')
             movie_rating_in_star=HOME_URL+movie_star_symbol
            story_published=author_class.find('span',{'class':'story_published'})
            if story_published!=None:
                movie_releasedate=story_published.text
        # print(movie_review_link)
        # print(movie_image)
        # print(movie_title)
        # print(movie_rating)
        # print(movie_releasedate)
        if movie_title!='' and movie_releasedate!='':
         final_reviews.append((movie_title,movie_rating,movie_releasedate,movie_image,movie_review_link,movie_rating_in_star))

    stuff_for_frontend={
        'final_reviews':final_reviews
    }
    return render(request,'base.html',stuff_for_frontend)