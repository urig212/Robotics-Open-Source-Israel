from operator import le
from re import X
import re
from flask import render_template,request,redirect
from app import app
from fileinput import filename
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('opensourceapi-ff95b70856c1.json', scope)

gc = gspread.authorize(credentials)

ws_community = gc.open('Community').sheet1
ws_mechanics = gc.open('Mechanics').sheet1
ws_electronics = gc.open('Electronics').sheet1
ws_yezor = gc.open('Yezor').sheet1
ws_cad = gc.open('Cad').sheet1
ws_code = gc.open('Code').sheet1
ws_other = gc.open('Other').sheet1


df_community = pd.DataFrame(ws_community.get_all_records())
df_mechanics = pd.DataFrame(ws_mechanics.get_all_records())
df_electronics = pd.DataFrame(ws_electronics.get_all_records())
df_yezor = pd.DataFrame(ws_yezor.get_all_records())
df_cad = pd.DataFrame(ws_cad.get_all_records())
df_code = pd.DataFrame(ws_code.get_all_records())
df_other = pd.DataFrame(ws_other.get_all_records())
df_explore = pd.concat([df_community,df_mechanics,df_electronics,df_yezor,df_cad,df_code,df_other])
df_search = df_explore.copy()

data_community = df_community.values.tolist()
data_mechanics = df_mechanics.values.tolist()
data_electronics = df_electronics.values.tolist()
data_yezor = df_yezor.values.tolist()
data_cad = df_cad.values.tolist()
data_code = df_code.values.tolist()
data_other = df_other.values.tolist()
data_explore = df_explore.values.tolist()
data_search = data_explore.copy()


@app.route('/')
@app.route('/home', methods=["GET","POST"])
def index():
    df_search = df_explore.copy()
    data_search = df_search.values.tolist()
    df_search.reset_index(inplace=True,drop=True)
    index_list = []
    if request.method == "POST":
        df_search = df_explore.copy()
        data_search = df_search.values.tolist()
        df_search.reset_index(inplace=True,drop=True)
        index_list = []
        req = request.form
        search_result = req["search_res"]
        for i in range(0,df_explore.shape[0]):
            df_head = data_search[i][0] + data_search[i][1]+ data_search[i][3]+ str(data_search[i][6])
            if df_head.count(search_result)==0:
                index_list.append(i)
        df_search.drop(index_list,inplace=True)
        data_search=df_search.values.tolist()
        user = {'username': 'Miguel'}
        return render_template('explore.html', title='Home', user=user, len=df_search.shape[0], data=data_search)
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)

@app.route('/')
@app.route('/community', methods=["GET","POST"])
def community():
    df_search = df_explore.copy()
    data_search = df_search.values.tolist()
    df_search.reset_index(inplace=True,drop=True)
    index_list = []
    if request.method == "POST":
        df_search = df_explore.copy()
        data_search = df_search.values.tolist()
        df_search.reset_index(inplace=True,drop=True)
        index_list = []
        req = request.form
        search_result = req["search_res"]
        for i in range(0,df_explore.shape[0]):
            df_head = data_search[i][0] + data_search[i][1]+ data_search[i][3]+ str(data_search[i][6])
            if df_head.count(search_result)==0:
                index_list.append(i)
        df_search.drop(index_list,inplace=True)
        data_search=df_search.values.tolist()
        user = {'username': 'Miguel'}
        return render_template('explore.html', title='Home', user=user, len=df_search.shape[0], data=data_search)

    user = {'username': 'Miguel'}
    return render_template('community.html', title='Home', user=user, len=df_community.shape[0], data=data_community)
   
@app.route('/') 
@app.route('/code', methods=["GET","POST"])
def code():
    df_search = df_explore.copy()
    data_search = df_search.values.tolist()
    df_search.reset_index(inplace=True,drop=True)
    index_list = []
    if request.method == "POST":
        df_search = df_explore.copy()
        data_search = df_search.values.tolist()
        df_search.reset_index(inplace=True,drop=True)
        index_list = []
        req = request.form
        search_result = req["search_res"]
        for i in range(0,df_explore.shape[0]):
            df_head = data_search[i][0] + data_search[i][1]+ data_search[i][3]+ str(data_search[i][6])
            if df_head.count(search_result)==0:
                index_list.append(i)
        df_search.drop(index_list,inplace=True)
        data_search=df_search.values.tolist()
        user = {'username': 'Miguel'}
        return render_template('explore.html', title='Home', user=user, len=df_search.shape[0], data=data_search)

    user = {'username': 'Miguel'}
    return render_template('code.html', title='Home', user=user, len=df_code.shape[0], data=data_code)

@app.route('/')
@app.route('/electronics', methods=["GET","POST"])
def electronics():
    df_search = df_explore.copy()
    data_search = df_search.values.tolist()
    df_search.reset_index(inplace=True,drop=True)
    index_list = []
    if request.method == "POST":
        df_search = df_explore.copy()
        data_search = df_search.values.tolist()
        df_search.reset_index(inplace=True,drop=True)
        index_list = []
        req = request.form
        search_result = req["search_res"]
        for i in range(0,df_explore.shape[0]):
            df_head = data_search[i][0] + data_search[i][1]+ data_search[i][3]+ str(data_search[i][6])
            if df_head.count(search_result)==0:
                index_list.append(i)
        df_search.drop(index_list,inplace=True)
        data_search=df_search.values.tolist()
        user = {'username': 'Miguel'}
        return render_template('explore.html', title='Home', user=user, len=df_search.shape[0], data=data_search)

    user = {'username': 'Miguel'}
    return render_template('electronics.html', title='Home', user=user, len=df_electronics.shape[0], data=data_electronics)

@app.route('/')
@app.route('/mechanics', methods=["GET","POST"])
def mechanics():
    df_search = df_explore.copy()
    data_search = df_search.values.tolist()
    df_search.reset_index(inplace=True,drop=True)
    index_list = []
    if request.method == "POST":
        df_search = df_explore.copy()
        data_search = df_search.values.tolist()
        df_search.reset_index(inplace=True,drop=True)
        index_list = []
        req = request.form
        search_result = req["search_res"]
        for i in range(0,df_explore.shape[0]):
            df_head = data_search[i][0] + data_search[i][1]+ data_search[i][3]+ str(data_search[i][6])
            if df_head.count(search_result)==0:
                index_list.append(i)
        df_search.drop(index_list,inplace=True)
        data_search=df_search.values.tolist()
        user = {'username': 'Miguel'}
        return render_template('explore.html', title='Home', user=user, len=df_search.shape[0], data=data_search)

    user = {'username': 'Miguel'}
    return render_template('mechanics.html', title='Home', user=user, len=df_mechanics.shape[0], data=data_mechanics)

@app.route('/')
@app.route('/yezor', methods=["GET","POST"])
def yezor():
    df_search = df_explore.copy()
    data_search = df_search.values.tolist()
    df_search.reset_index(inplace=True,drop=True)
    index_list = []
    if request.method == "POST":
        df_search = df_explore.copy()
        data_search = df_search.values.tolist()
        df_search.reset_index(inplace=True,drop=True)
        index_list = []
        req = request.form
        search_result = req["search_res"]
        for i in range(0,df_explore.shape[0]):
            df_head = data_search[i][0] + data_search[i][1]+ data_search[i][3]+ str(data_search[i][6])
            if df_head.count(search_result)==0:
                index_list.append(i)
        df_search.drop(index_list,inplace=True)
        data_search=df_search.values.tolist()
        user = {'username': 'Miguel'}
        return render_template('explore.html', title='Home', user=user, len=df_search.shape[0], data=data_search)

    user = {'username': 'Miguel'}
    return render_template('yezor.html', title='Home', user=user, len=df_yezor.shape[0], data=data_yezor)

@app.route('/')
@app.route('/cad', methods=["GET","POST"])
def cad():
    df_search = df_explore.copy()
    data_search = df_search.values.tolist()
    df_search.reset_index(inplace=True,drop=True)
    index_list = []
    if request.method == "POST":
        df_search = df_explore.copy()
        data_search = df_search.values.tolist()
        df_search.reset_index(inplace=True,drop=True)
        index_list = []
        req = request.form
        search_result = req["search_res"]
        for i in range(0,df_explore.shape[0]):
            df_head = data_search[i][0] + data_search[i][1]+ data_search[i][3]+ str(data_search[i][6])
            if df_head.count(search_result)==0:
                index_list.append(i)
        df_search.drop(index_list,inplace=True)
        data_search=df_search.values.tolist()
        user = {'username': 'Miguel'}
        return render_template('explore.html', title='Home', user=user, len=df_search.shape[0], data=data_search)

    user = {'username': 'Miguel'}
    return render_template('cad.html', title='Home', user=user, len=df_cad.shape[0], data=data_cad)

@app.route('/')
@app.route('/other', methods=["GET","POST"])
def other():
    df_search = df_explore.copy()
    data_search = df_search.values.tolist()
    df_search.reset_index(inplace=True,drop=True)
    index_list = []
    if request.method == "POST":
        df_search = df_explore.copy()
        data_search = df_search.values.tolist()
        df_search.reset_index(inplace=True,drop=True)
        index_list = []
        req = request.form
        search_result = req["search_res"]
        for i in range(0,df_explore.shape[0]):
            df_head = data_search[i][0] + data_search[i][1]+ data_search[i][3]+ str(data_search[i][6])
            if df_head.count(search_result)==0:
                index_list.append(i)
        df_search.drop(index_list,inplace=True)
        data_search=df_search.values.tolist()
        user = {'username': 'Miguel'}
        return render_template('explore.html', title='Home', user=user, len=df_search.shape[0], data=data_search)

    user = {'username': 'Miguel'}
    return render_template('other.html', title='Home', user=user, len=df_other.shape[0], data=data_other)

@app.route('/')
@app.route('/explore', methods=["GET","POST"])
def explore():
    df_search = df_explore.copy()
    data_search = df_search.values.tolist()
    df_search.reset_index(inplace=True,drop=True)
    index_list = []
    if request.method == "POST":
        df_search = df_explore.copy()
        data_search = df_search.values.tolist()
        df_search.reset_index(inplace=True,drop=True)
        index_list = []
        req = request.form
        search_result = req["search_res"]
        for i in range(0,df_explore.shape[0]):
            df_head = data_search[i][0] + data_search[i][1]+ data_search[i][3]+ str(data_search[i][6])
            if df_head.count(search_result)==0:
                index_list.append(i)
        df_search.drop(index_list,inplace=True)
        data_search=df_search.values.tolist()
        user = {'username': 'Miguel'}
        return render_template('explore.html', title='Home', user=user, len=df_search.shape[0], data=data_search)
    user = {'username': 'Miguel'}
    return render_template('explore.html', title='Home', user=user, len=df_explore.shape[0], data=data_explore)