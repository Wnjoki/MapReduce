from functools import reduce
from itertools import groupby
from operator import itemgetter

def mapper(line):
   data=line.split(",")

   date=data[0].strip()
   url = data[1].strip()

   year= date[0:4]
   month= date[5:7]
   if year =='2014':
     return (month,url,1)


def reducer(in1,in2):
    return(in1[0],in1[1],in1[2]+in2[2])

def  reduce(out1,out2):
     if out1[2]>=out2[2]:
        return out1
     else:
        return out2
     
def print_list(stage_name=None,list=[]):
   print("-----\n\n%s\n\n-----".format(stage_name))
   for i in list :
       print(i)
       print("-----\n\nList of %s \n\n-----".format(stage_name))

data=[
    "2014-04-01 13:45:42 http://example.com/products.html 77.140.91.33 89"
    "2014-10-01 14:39:48 http://example.com/index.html 113.107.99.122 13"
    "2014-06-23 21:27:50 http://example.com/about.html 50.98.73.129 73"
    "2014-01-15 21:27:09 http://example.com/services.html 149.59.51.52 59"
    "2014-05-13 11:43:42 http://example.com/about.html 61.91.88.85 46"
    "2014-02-17 03:17:37 http://example.com/contact.html 68.78.59.117 98"
]

map_phase=map(mapper,data)
print_list("MAP",list(map_phase))
print(list(map_phase))
sort_shuffle=groupby(sorted(map_phase),keys=itemgetter(0))
print_list("SORT AND SHUFFLE",list(sort_shuffle))
reducer1_out= [reduce(reducer,values) for k,v in sort_shuffle for key,values in groupby(sorted(v),key=itemgetter(1))]
print_list("SUM  REDUCER",reducer1_out)
reducer2_out=[reduce(reducer,values) for key,values in groupby(sorted(reducer1_out),key=itemgetter(0)) ]
print_list("MAX REDUCER",reducer2_out)