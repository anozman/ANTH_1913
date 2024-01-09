#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 14:53:31 2021

@author: anozman

This Program reads in the data from the OU Covid Dashboard and puts this data into a pandas dataframe
From this dataframe, numerous graphs and figures are then produced

This will be fun
"""
#Data structures and arithmatic functions
import pandas as pd
import numpy as np

#Graphing utilities 
import plotly.express as px
import plotly.graph_objects as plot
import plotly.io as pio
from plotly.subplots import make_subplots
#pio.renderers.default = 'svg'
pio.renderers.default = 'browser'

#Website scrapping
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
#import mechanicalsoup

import sys,os

'''This function was amde to scrap the OU Covid Dashboard data
   This function is incomplete'''
def scrapDashboard():
    url = "https://www.ou.edu/together/dashboard"
    #This is the website found that is just the data itself, contained within the dashboard
    url = "https://app.powerbi.com/view?r=eyJrIjoiYzY4MGZmMDEtMTc0Zi00YWM2LWFiNDItYmRjMDgwM2U5NmI3IiwidCI6IjljN2RlMDlkLTkwMzQtNDRjMS1iNDYyLWM0NjRmZWNlMjA0YSIsImMiOjN9&pageName=ReportSection53258f705abe18640c22"
    #fileName = "Covid_data.csv"
    
    #urllib.request.urlretrieve(url, filename=(fileName))
    
   # css_soup = BeautifulSoup('<p class="body"></p>')
    #css_soup.p['class']
    # ["body"]
    
    #page = urlopen(url)
    #html = page.read().decode("utf-8")
    #soup = BeautifulSoup(html, "html.parser")
    
    #Creates the mechanical soup object
    #browser = mechanicalsoup.StatefulBrowser()
    #page = browser.get(url)
    #opens the url in the object
    #browser.open(url)
    #print(browser.page())
    #finds and selects the form
    #browser.select_form()
    
    
    #print(soup.get_text()) 
    
def scrapWebsite(website):
    url = website
    

'''Uses Plotly subplots in order to create the secondary axis'''
"""This function creates the graphs for each season with the desired input
    dataframe: Dataframe containing the data of the covid statistics
    name_season: "#Season" "#Year" Ex: "Fall 2020" """
def make_graphs(dataframe, name_season):
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(plot.Bar(x = dataframe['Week dates']['Week dates'], y = dataframe['Weekly Results']['Positives'], name = "Confirmed Positive"), secondary_y = False)
    fig.add_trace(plot.Bar(x = dataframe["Week dates"]['Week dates'], y = dataframe['Weekly Results']['Tests'], name = "Total Tests"), secondary_y = False)
    fig.update_layout(barmode = 'group')
    fig.add_trace(plot.Line(x = dataframe['Week dates']['Week dates'], y = dataframe['Weekly Results']['%Positive'], name = "%Positive"), secondary_y = True)
    fig.update_layout(title = name_season + "OU Covid Statistics", xaxis_title = "Week dates")
    fig.update_yaxes(title_text = "Test numbers", secondary_y = False)
    fig.update_yaxes(title_text = "%Positive", range = list([0,100]), secondary_y = True)
    fig.show()
    #print(str(os.path.dirname(os.getcwd()) + "/ANTH_1913/" + name_season.split(" ")[0] + "_" + name_season.split(" ")[1] + ".html"))
    fig.write_html(str(os.path.dirname(os.getcwd()) + "/ANTH_1913/" + name_season.split(" ")[0] + "_" + name_season.split(" ")[1] + ".html"))
    
    
'''MAIN METHOD'''
if __name__ == "__main__":
    #scrapDashboard()
    
    #Reads in the data from the excep spread sheet
    fall_dataframe = pd.read_excel("Covid_dashboard_data_transfer.xlsx" , sheet_name = "Fall 2020", header = [0,1])
    spring_dataframe = pd.read_excel("Covid_dashboard_data_transfer.xlsx" , sheet_name = "Spring 2021", header = [0,1])
    fall_2021_dataframe = pd.read_excel("Covid_dashboard_data_transfer.xlsx" , sheet_name = "Fall 2021", header = [0,1])
    
    #Using the previous method
    make_graphs(fall_dataframe, "Fall 2020")
    make_graphs(spring_dataframe, "Spring 2021")
    make_graphs(fall_2021_dataframe, "Fall 2021")
    
