import json
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
import pandas as pd
import ast,joblib
import requests as rs
from .forms import SignUpForm
from django.contrib import messages

from dotenv import load_dotenv
import os

load_dotenv()
# Create your views here.

df = pd.read_csv('static/dataset/final_data.csv')
model = joblib.load('static/model/model.pkl')

API_KEY = os.getenv('API_KEY')
API_URL = os.getenv('API_URL')



def autocomplete(request):
    data = list(df['title'])
    return HttpResponse(json.dumps(data),content_type='application/json')

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'You have successfully loged in')
            return redirect('home')
        else:
            messages.success(request, f"Failed to login with the Username: {username} and Password: {password}")
            return redirect('home')
    return render(request,'content.html')

def logout_user(request):
    logout(request)
    messages.success(request,'You have successfully logout')
    return redirect("home")

def signup_user(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request,username=username,password=password)
            login(request,user)
            messages.success(request,f'Successfully Created the user {username}')
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request,'signup.html',{'form':form})

def recommend(request):
    if request.method == 'POST':
        movie_name = request.POST['movie_name']
        return redirect(recommend_movies,movie_name=movie_name)
    else:
        return render(request,'base.html')
   
def recommend_movies(request,movie_name='Avatar'):
    try:
        movies_data,movie_info=get_movies_info(movie_name)
        name=movie_info[0]
        status=movie_info[1]
        lang=movie_info[2]
        director=movie_info[3]
        cast=movie_info[4]
        overview=movie_info[5]
        img=movie_info[6]
        genres = movie_info[7]
        
    except Exception as e:
        return render(request,'content.html',{'fail_display':'block','fail_name':movie_name })

    return render(request,'content.html',{"display":'block',"movie_data":movies_data,
        "name":name,"status":status,"lang":lang,"director":director,"cast":cast,"overview":overview,"img":img,"genres":genres})   
    
def get_movies_info(movie):
    movie_poster=[]
    movie_names=[]
    movie_index = df[df['title'] == movie].index[0]
    movie_list = sorted(enumerate(model[movie_index]),reverse=True,key=lambda x: x[1])[1:9]
    for i in movie_list:
        movieid = df.iloc[i[0]].movie_id
        movienames= df.iloc[i[0]].title
        movie_names.append(movienames)
        movie_poster.append(poster(movieid))

    return zip(movie_names,movie_poster),main_movie_info(movie_index)

def main_movie_info(movie):
    movie_id = df.iloc[movie].movie_id
    response=rs.get('{}{}?api_key={}'.format(API_URL,movie_id,API_KEY))
    data=response.json()
    img_path = "https://image.tmdb.org/t/p/w500/"+data['poster_path']
    movie_name = df.iloc[movie].title
    movie_cast = ", ".join(ast.literal_eval(df.iloc[movie].cast))
    movie_director = ", ".join(ast.literal_eval(df.iloc[movie].crew))
    movie_genres = ", ".join(ast.literal_eval(df.iloc[movie].genres))
    movie_lang = df.iloc[movie].original_language
    movie_status = df.iloc[movie].status
    movie_overview = df.iloc[movie].overview
    
    return [movie_name,movie_status,movie_lang,movie_director,movie_cast,movie_overview,img_path,movie_genres]
    
def poster(movie):
    response=rs.get('{}{}?api_key={}'.format(API_URL,movie,API_KEY))
    data=response.json()
    if data['poster_path']!=None:
        return "https://image.tmdb.org/t/p/w500/"+data['poster_path']
    return None

