from __future__ import print_function
import argparse
import sys
from googleapiclient import sample_tools


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



frame=0

argparser = argparse.ArgumentParser(add_help=False)
argparser.add_argument('property_uri', type=str,default="unizone.edu.vn",
                       help=('Site or app URI to query data for (including '
                             'trailing slash).'))
argparser.add_argument('start_date', type=str,default="2020-09-01",
                       help=('Start date of the requested date range in '
                             'YYYY-MM format.'))
argparser.add_argument('end_date', type=str,default="2020-09-30",
                       help=('End date of the requested date range in '
                             'YYYY-MM format.'))




  

def getData(ngaybatdau,ngayketthuc,url):
    #sys.print(sys.argv)
    
  service, flags = sample_tools.init(
      ['search_analytics_api_sample.py','unizone.edu.vn','2020-09-01','2020-09-30'], 'webmasters', 'v3', __doc__, __file__, parents=[argparser],
      scope='https://www.googleapis.com/auth/webmasters.readonly')

 
  request = {
      'startDate': ngaybatdau,
      'endDate': ngayketthuc,
      'dimensions': ['date']
  }
  request2 = {
      'startDate': ngaybatdau,
      'endDate': ngayketthuc,
      
  }
  response = execute_request(service, url, request)
  response2 = execute_request(service, url, request2)
  print_table(response,'Available dates',frame)
  print_table2(response,'Available dates')
  



def execute_request(service, property_uri, request):
  """Executes a searchAnalytics.query request.
  Args:
    service: The webmasters service to use when executing the query.
    property_uri: The site or app URI to request data for.
    request: The request to be executed.
  Returns:
    An array of response rows.
  """
  return service.searchanalytics().query(
      siteUrl=property_uri, body=request).execute()

def print_table2(response,title):
  """Prints out a response table.
  Each row contains key(s), clicks, impressions, CTR, and average position.
  Args:
    response: The server response to be printed as a table.
    title: The title of the table.
  """
  print('\n --' + title + ':')
  
  if 'rows' not in response:
    print('Empty response')
    return

  rows = response['rows']
  row_format = '{:<20}' + '{:>20}' * 4
  print(row_format.format('Keys', 'Clicks', 'Impressions', 'CTR', 'Position'))
  
  i=0;
  key=[]
  click=[]
  impression=[]
  ctr=[]
  position=[]
  for row in rows:
    keys = ''
    # Keys are returned only if one or more dimensions are requested.
    if 'keys' in row:
      keys = u','.join(row['keys']).encode('utf-8').decode()
      key.append(keys)
      click.append(row['clicks'])
      impression.append(row['impressions'])
      ctr.append(row['ctr'])
      position.append(row['position'])
  label=['Clicks','Impression','CTR*1000','Position*100']
  value=[row['clicks'],row['impressions'],row['ctr']*1000,row['position']*100]
  plt.bar(label,value)
  plt.title('Biểu đồ cột')
  plt.show()


def print_table(response,title,frame):
  """Prints out a response table.
  Each row contains key(s), clicks, impressions, CTR, and average position.
  Args:
    response: The server response to be printed as a table.
    title: The title of the table.
  """
  print('\n --' + title + ':')
  
  if 'rows' not in response:
    print('Empty response')
    return

  rows = response['rows']
  row_format = '{:<20}' + '{:>20}' * 4
  print(row_format.format('Keys', 'Clicks', 'Impressions', 'CTR', 'Position'))
  
  i=0;
  key=[]
  click=[]
  impression=[]
  ctr=[]
  position=[]
  for row in rows:
    keys = ''
    # Keys are returned only if one or more dimensions are requested.
    if 'keys' in row:
      keys = u','.join(row['keys']).encode('utf-8').decode()
      line='Date: '+str(keys)+' '+'Clicks: '+ str(row['clicks'])+' '+'Impressions: '+str(row['impressions'])+' '+'CTR: '+str(row['ctr'])+' '+'Position: '+str(row['position'])
      '''lb=tk.Label(frame2,text=line)
      lb.grid(row=i,column=1)'''
      key.append(keys)
      click.append(row['clicks'])
      impression.append(row['impressions'])
      ctr.append(row['ctr']*1000)
      position.append(row['position']*1000)
      i+=1
    print(row_format.format(
        keys, row['clicks'], row['impressions'], row['ctr'], row['position']))
  
  plt.plot(key,click,label='Clicks',color='red',marker='.',markersize=10,markeredgecolor='red')
  plt.plot(key,impression,label='Impressions',color='blue',marker='.',markersize=10,markeredgecolor='blue')
  plt.plot(key,ctr,label='CTR*1000',color='green',marker='.',markersize=10,markeredgecolor='green')
  plt.plot(key,position,label='Position*1000',color='yellow',marker='.',markersize=10,markeredgecolor='yellow')
  plt.title('Biểu đồ đường')
  plt.xlabel('Ngày')
  plt.ylabel('Số lượt') 
  plt.legend() 
  plt.show()

getData('2020-09-01','2020-09-30','unizone.edu.vn')
    
