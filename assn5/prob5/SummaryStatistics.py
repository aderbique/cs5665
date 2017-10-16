import os, sys
from statistics import *

def SS(v):
    sv = sorted(v)
    lv = len(sv)
    Min,Max = min_max(sv)
    dict = {"Count":lv,"Sum":sum(sv),"Min":Min,"Max":Max,"Median":median(sv,lv),"Mode":mode(v),"Mean":mean(sv,lv),"Q1":quantile(sv,0.25,lv),"Q3":quantile(sv,0.75,lv),"Variance":variance(sv,lv),"StdDev":standard_deviation(sv,lv),"Range":data_range(sv),"IQR":interquartile_range(sv,lv)}
    return(dict)
