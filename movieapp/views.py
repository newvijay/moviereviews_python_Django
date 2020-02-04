import re
from urllib.parse import quote_plus

import bs4
from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen,Request

HOME_URL='https://www.cinemablend.com'
BASE_URL='https://www.cinemablend.com/reviews'
CONSTRUCTED_URL='https://www.cinemablend.com/reviews/?page={}'
RATING_URL='https://www.cinemablend.com/static/images/stars/{}.yellow.svg'

# Create your views here.
def testing(request):
    id=request.POST.get('action')
    if id:
        final_url = CONSTRUCTED_URL.format(quote_plus('2'))
    else:
        final_url=CONSTRUCTED_URL.format(quote_plus('1'))
    req=Request(final_url,headers={'User-Agent': 'Mozilla/5.0'})
    uClient=urlopen(req)
    html_page=uClient.read()
    uClient.close()
    soup=BeautifulSoup(html_page,'html.parser')
    #all_movies_list=soup.select("a[class='story-related-story']")
    all_movies_list=soup.find_all('a',{'class':'story-related-story'})

    #print(all_movies_list)
    final_reviews=[]

    for review in all_movies_list:
        movie_review_link=review['href']
        content_clss=review.find('div',{'class':'story-related-content'})
        movie_title=''
        movie_rating=''
        movie_releasedate=''
        movie_summary=''
        movie_image=''
        movie_star_url=''
        if content_clss!=None:
         movie_im = content_clss.find('span', {'class': 'story-cover-image'})
         if movie_im != None:
                img=movie_im.find('img')
                movie_image = str(img.get('srcset')).split(' ')[0]
                #print(movie_image)

         movie_tit = content_clss.find('span',{'class':'story-related-title'})
         if movie_tit!=None:
             movie_title=movie_tit.text
         story_published = content_clss.find('span', {'class': 'story-related-release-date'})
         if story_published != None:
            movie_releasedate = story_published.text
         movie_sum = content_clss.find('span', {'class': 'story-related-summary'})
         if movie_sum != None:
            movie_summary = movie_sum.text
         movie_rat = content_clss.find('span', {'class': 'story-related-score'})
         if movie_rat != None:
             mv_rat=str(movie_rat)
             m=re.search('score-(.+?)',mv_rat)
             if m:
                 score=m.group(1)
                 movie_star_url=RATING_URL.format(score)
                 movie_rating=int(score)/2;

        if movie_title!='' and movie_releasedate!='':
         final_reviews.append((movie_title,movie_rating,movie_releasedate,movie_image,movie_review_link,movie_summary,movie_star_url))
    nextpageurl=BASE_URL+'/?page=2'

    stuff_for_frontend={
        'nextpageurl': nextpageurl,
        'final_reviews':final_reviews
    }
    return render(request,'base.html',stuff_for_frontend)

def nextpage(request):
    nextpageurl=BASE_URL+'/?page=2'
    nextpagecontext={
        'nextpageurl':nextpageurl
    }
    return render(request,'movieapp/nextpageurl.html',nextpagecontext)
