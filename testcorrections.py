# -*- coding: utf-8 -*-
"""
Created on Sunday Feb 11 2024

@author: 19177: Belle Nahoom
"""


#PART 2
proteins = [
    "PF13411.1", "PF12727.1", "PF01381.2", "PF00205.2",
    "PF10875.1", "PF05766.1", "PF00860.2", "PF10766.1",
    "PF11812.1"
    ]

def count_unique_proteins(protein_list):
    '''

    Parameters
    ----------
    proteins : List of strings representing different protein familes
                    first part of string PF = protein family
                    number after the period is the proteins revision number

    Returns : number of unique family names in the list

    '''
    #Instead of writing out long loop can just do one line
    #fits the parameters of the question now
    return len({protein_list.split('.')[0] for protein in protein_list})

def count_proteins(protein_list):
    '''

    Parameters
    ----------
    proteins : List
        strings representing different protein familes.

    Returns
    -------
    dict:
        keys:are the unique family numbers
        values: count/number of times the family number occurs in the list.

    '''
    #define dictionary as {} instead of 0
    protein_count = {}
    #loop to count protein in proteins. add 1 if unique
    for protein in protein_list:
        unique_protein =  protein.split('.')[0] #split by . to get family name
        if unique_protein in protein_count:
            protein_count[unique_protein] += 1
        else:
            protein_count[unique_protein] = 1
    return protein_count #should return unique name: count, as dict

def merge_protein_counts(dict1, dict2):
    '''

    Parameters
    ----------
    dict1 : dictionary of proteins and their value counts.
    dict2 : dictionary of proteins and their value counts.
        Function takes two dictionaries and combines their common protein names
        and adds their value counts.

    Returns
    -------
    single_dict : combination of dict1 and dict 2

    '''
    single_dict = {} #didn't define new dictionary in original test
    #To check if keys are in both dictionary need to use sets
    #Union set checks to find out if keys are unique or shared
    both_keys = set(dict1.keys() | dict2.keys())

    for key in both_keys:
        count_dict1 = dict1.get(key, 0) #the 0 helps avoid TypeErrors
        count_dict2 = dict2.get(key, 0)
        single_dict[key] = (count_dict1, count_dict2) #create single key
    return single_dict

#PART 3

dates_list = {"Febuary 6, 1992" , "Febuary 18, 1992" , "Febuary 27, 1992",
              "September 6, 1994" , "December 1, 1993"}

def dates_to_iso8601(list1):
    months_converted = {
        "January": "01", "Febuary": "02", "March": "03", "April": "04",
        "May": "05", "June": "06", "July": "07", "August": "08",
        "September": "09", "October": "10", "November": "11", "December": "12"
    } #need to write out conversion so we can turn month names into numerical
    #values

    reformatted_dates = [] #define new list which will be our returned value

    for date in list1:
        new_dates = date.split(" ")
        year = new_dates[2]
        month = months_converted[new_dates[0]] #using month_conversion
        day = new_dates[1]
        day = day.strip(",") #day is currently "6," we need to remove the ,

        if len(day) != 2: #ensure that date always has length of 2
            day = "0" + day

        reformatted_dates.append(year + "-" + month + "-" + day)
    return reformatted_dates


dates_list = {"Febuary 6, 1992", "Febuary 18, 1992", "Febuary 27, 1992",
              "September 6, 1994", "December 1, 1993"}

month_conversion = {
    "January": "01", "Febuary": "02", "March": "03", "April": "04",
    "May": "05", "June": "06", "July": "07", "August": "08",
    "September": "09", "October": "10", "November": "11", "December": "12"
}

def sort_dates(list1):
    dates_sorted = []
    new_dates = dates_to_iso8601(list1)#use other function as helper function
    sorted_formatted_dates = sorted(new_dates) #sort before appending
    dates_sorted.append((sorted_formatted_dates, list1)) #original and sorted
    final_sorted_original = [original for _, original in dates_sorted]
    #compares the original and the sorted so that we can return original setup 
    #of list
    return final_sorted_original
