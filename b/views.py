from django.shortcuts import render,redirect 
import requests 
import os
from .models import product_models , comments ,category_saver, ratings , User_model , business_model
from a import settings 
#from .models import table names 
import random 
from datetime import date,timedelta
from django.http import JsonResponse , HttpResponse
import json 
import pandas as pd 
import numpy as np
import schedule

import pandas as pd 
import numpy as np

r = request.POST

def searcher(query_string):
    def category_finder(query_string):
        query_string = query_string.split()
        processed_array = []
        for i in query_string:
            j = i.lower()
            processed_array.append(j)
        
        return processed_array 
    
    def lcl(word):#letter_count_list
    # Initialize a list of 26 zeros, one for each letter of the alphabet
        counts = [0] * 26

    # Iterate over each letter in the word
        for letter in word:
        # Convert the letter to lowercase and calculate its index in the alphabet (0-indexed)
            index = ord(letter.lower()) - ord('a')
        # Increment the count for that letter
            if 0 <= index < 26:
                counts[index] += 1

        return counts
    def sma(list1, list2):
    # Convert lists to NumPy arrays
    
        arr1 = np.array(list1)
        arr2 = np.array(list2)
    
    # Calculate the squared difference between corresponding elements
        squared_diff = (arr1 - arr2) ** 2
    
    # Calculate the mean of the squared differences
        mse = np.mean(squared_diff)
    
        return mse
    def jethalal(word):
        worded = lcl(word)
        smas = []
        list_content = [('momo', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), ('chowmein', [0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]), ('pizza', [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]), ('coke', [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), ('fanta', [2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]), ('thing', [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0])]
        for i in list_content:
            sma_cal = sma(worded , i[1])
            smas.append((sma_cal , i[0]))
        sorted_list = sorted(smas, key=lambda x: x[0], reverse=False)    
        most_milne = sorted_list[0]
        if most_milne[1][3:] == word[3:]:
            return most_milne 
        else:
            return_list = [1 , "none"]
            return return_list
    def baga(words):
        most_milne_token = []
        vector_to_find = []
        for i in words:
            one_word_removed = i[:-1]
            two_word_removed = i[:-2]
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            most_milne_one = []
            for word in alphabet:
            
                word3 = i + word 
            
                smas_calc = jethalal(word3)
                most_milne_one.append(smas_calc)
            sorted_one = sorted(most_milne_one , key = lambda x:x[0] , reverse = False)
            most_mil = sorted_one[0]
            actual_thing = jethalal(i)
            owr_milne = jethalal(one_word_removed)
            twr_milne = jethalal(two_word_removed)
            appended = [most_mil , actual_thing , owr_milne , twr_milne]
            sorted_two = sorted(appended , key = lambda x:x[0] , reverse = False)
            if sorted_two[0][0]<0.04:
                most_milne_token.append((sorted_two[0][1] , i))
            sorted_two = []    
        print(most_milne_token)
        return most_milne_token 
    
    words = category_finder(query_string)   
    listed = baga(words)  
    categories = []
    category = category_saver.objects.all()
    for i in category:
        categories.append((str(i.category) , i.subcategory))
    #categories = [(("Junk food") , ["momo" , "chowmein" , "pizza"])]
    sorted_cat = []
    for i in listed:
        searching_word = i[0]
        for cat , mouse in categories:
            for j in mouse:
                if str(j)== str(searching_word):
                    sorted_cat.append(cat)
                    break
        #print(f"the word is {searching_word} ,actual word is {i[1]} and sorted is {sorted_cat[0]}")
        #the word is momo , actual word is chowmei and sorted is Junk Food.
    return sorted_cat 
        
#searcher(query_string)

def thousands_to_k(value):
    try:
        value = int(value)
        if value >= 1000:
            return str(round(value / 1000, 1)) + 'k'
        else:
            return str(value)
    except (ValueError, TypeError):
        return value  
def homepage(request):
    return render(request, "homepage.html")
def form_func(request):
    return render(request , "form.html")
def search_results(query_string):
    sorted_cat = searcher(query_string)

def auto_update():
        now = datetime.now()
        hour = now.hour
        if hour == 0:
            for model in business_model.objects.all():
                model.monthly_views += model.today_views
                model.today_views = 0
                model.save()
schedule.every().hour.do(auto_update)
def signup(request):
    username = r.get("username_signup")
    password = r.get("password_signup")
    email = r.get("email")
    gender = r.get("gender_signup")
        