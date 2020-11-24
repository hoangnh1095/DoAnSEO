from __future__ import print_function
import argparse
import sys
from googleapiclient import sample_tools

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Declare command-line flags.
argparser = argparse.ArgumentParser(add_help=False)
argparser.add_argument('property_uri', type=str,default="unizone.edu.vn",
                       help=('Site or app URI to query data for (including '
                             'trailing slash).'))
argparser.add_argument('start_date', type=str,default="2020-09-01",
                       help=('Start date of the requested date range in '
                             'YYYY-MM-DD format.'))
argparser.add_argument('end_date', type=str,default="2020-09-30",
                       help=('End date of the requested date range in '
                             'YYYY-MM-DD format.'))

#Variables
HEIGHT=500
WIDTH=600



#function
def popup_showinfo():
    showinfo("Loading", "Đang tải dữ liệu về...")
def main(argv):
  #sys.print(sys.argv)
  service, flags = sample_tools.init(
      ['search_analytics_api_sample.py','unizone.edu.vn','2020-09-01','2020-09-30'], 'webmasters', 'v3', __doc__, __file__, parents=[argparser],
      scope='https://www.googleapis.com/auth/webmasters.readonly')

  # First run a query to learn which dates we have data for. You should always
  # check which days in a date range have data before running your main query.
  # This query shows data for the entire range, grouped and sorted by day,
  # descending; any days without data will be missing from the results.
  request = {
      'startDate': flags.start_date,
      'endDate': flags.end_date,
      'dimensions': ['date']
  }
  response = execute_request(service, flags.property_uri, request)
  print_table(response, 'Available dates')
  

  # Get totals for the date range.
  request = {
      'startDate': flags.start_date,
      'endDate': flags.end_date
  }
  response = execute_request(service, flags.property_uri, request)
  print_table(response, 'Totals')
  



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



def print_table(response, title):
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
  for row in rows:
    keys = ''
    # Keys are returned only if one or more dimensions are requested.
    if 'keys' in row:
      keys = u','.join(row['keys']).encode('utf-8').decode()
      line='Date: '+str(keys)+' '+'Clicks: '+ str(row['clicks'])+' '+'Impressions: '+str(row['impressions'])+' '+'CTR: '+str(row['ctr'])+' '+'Position: '+str(row['position'])
      lb=tk.Label(frame2,text=line)
      lb.grid(row=i,column=1)
      i+=1
    print(row_format.format(
        keys, row['clicks'], row['impressions'], row['ctr'], row['position']))
        
    
    
        

#set up
window = tk.Tk()
window.title("Phần mềm phân tích trang web")
window.geometry("+300+100")


canvas=tk.Canvas(window,height=HEIGHT,width=WIDTH,bg="white")
canvas.pack()

#lable frame
frame=tk.Frame(window,bg="white")
frame.place(relx=0.2,rely=0.05,relwidth=0.8,relheight=0.1)

lable=tk.Label(frame,text="Nhấn bắt đầu để tiến hành phân tích trang web unizone.edu.vn !!!", bg="white",font=("Times New Roman",12))

lable.grid(row=0,column=1)

button=tk.Button(frame,text="Bắt đầu",bg="blue",command=lambda: main(sys.argv))
button.grid(row=1,column=1)

#content frame

frame2=tk.Frame(window,bg="#99FFFF")
frame2.place(relx=0.1,rely=0.2,relwidth=0.82,relheight=0.7)

label2={}
window.mainloop()


