import matplotlib as mp
import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import filedialog

def decide_which_countries():
    global df
    #import_file_path = filedialog.askopenfilename()
    #xl = pd.ExcelFile(import_file_path)
    xl = pd.ExcelFile("./data/UN_MigFlow_Totals.xlsx")
    df = xl.parse('Totals')
    data = df.to_numpy()
    
    list_of_countries = []
    #list_of_criteria = []
    #both = []
    
    #remove countries with lower data counts
    #i.e. if they don't have any data up to 1985
    for datum in data:
        #test: print(datum),
        for x in range(10):
            #if there's in integer in the first 9 columns
            #keeping in mind the first four are the names of the countries, etc
            #then add that country to the list we'll keep
            if( (isinstance(datum[x], int) or isinstance(datum[x], float))
                and not np.isnan(datum[x])):
                # test: print(datum[x])
                if (datum[0] == "United Kingdom of Great Britain and Northern Ireland"):
                    list_of_countries.append("United Kingdom")
                elif(datum[0] == 'CntName' or datum[2] == 'Emigrants'):
                    continue
                else:
                    list_of_countries.append(datum[0])
                #list_of_criteria.append(datum[1])
                #print("Country: ", datum[0], " Criteria: ", datum[1])

                # no need to check the next four if applicable
                continue

    #kill duplicates:
    list_of_countries = list(set(list_of_countries))

    #sorted(both, key=lambda country: country[0])
    try:
        list_of_countries.remove('CntName')
    except ValueError:
        print('List of Countries gathered.')
    
    #print(list_of_countries)

    return list_of_countries

def make_migrant_table():
    countries  = decide_which_countries()

    criteria = ['Residence', 'Citizenship', 'Place of birth']

    data_by_country = []

    for country in countries:

        #print("Country: ", country, "|", end = " ")
        
        excelPath = "./data/" + country + ".xlsx"
        xl = pd.ExcelFile(excelPath)

        tabnames = xl.sheet_names
        parsename = ""
        #print(tabnames)
        #want residence, then citizenship, then pob
        for tabname in tabnames:
            if(tabname == country + " by " + criteria[0]):
                parsename = country + " by " + criteria[0]
            elif(tabname == country + " by " + criteria[1]):
                parsename = country + " by " + criteria[1]
            elif(tabname == country + " by " + criteria[2]):
                parsename = country + " by " + criteria[2]

        #we need the Australia, Germany, US, (etc) by Residence tab:
        #but the tab is different for each thing        
        df = None
        try:
            if(country is 'United States of America'):
                df = xl.parse("USA by " + criteria[2])
            if(country == 'United Kingdom'):
                df = xl.parse("United Kingdom by " + criteria[0])
            else:
                df = xl.parse(parsename)
        except:
            df = xl.parse("USA by " + criteria[2]) #USA fails sometimes because python string checking sucks

        data = df.to_numpy()
            
        data = country_data(countries,data)

        cnt = [country,data]

        #We want a table like this:
        #[ [Country1, [ [countr2, [data...]], [countr3, [data...]], ... ], ... ]
        data_by_country.append(cnt)

    return data_by_country

#Given string country's name and nparr data
#pick out the important bits
def country_data(countries,data):
    new_data = []
    for datum in data: #data is list of rows
        if(datum[0] == 'Immigrants' and datum[2] in countries):
            row = [datum[2],datum[9:43]] #dub check 42 or 43 (DONE)
            #print(row)
            new_data.append(row)
    return new_data
