import keep_alive
from replit import db
import time
import os
os.system("pip install scratch2py && pip install --force-reinstall websocket-client")
from scratch2py import Scratch2Py
#temp websites
print(db.keys())
password = os.environ['password']
projectID = "616759917"
s2py = Scratch2Py("xMysticalLegend", password)
cloudproject = s2py.scratchConnect(projectID)
project = s2py.project(projectID)
print("Connection to user and project complete. Starting loop.")
keep_alive.keep_alive()
while True:
  websites = ""
  
  for i in range(len(db.keys())):
    websites = websites + list(db.keys())[i] + ", "
  try:
    cloudproject.setCloudVar('websitesC', s2py.decode(websites))
    print("websites set.")
  except:
    print("Websites not set. Continuing.")
  
    

  
  comments = project.getComments()
  comments = comments[0]
  comments = comments["content"]
  print(comments)
  if "WEBSITE(" in comments:
    print("Website requested")
    comments = comments.replace("WEBSITE(", "")
    comments = comments.replace(")", "")
    comments = comments.split(",")
    if comments[0] not in db.keys():
      print("Website created")
      db[comments[0]] = comments[1]
  
  try:
    search = s2py.decode(cloudproject.readCloudVar('search'))
  except:
    continue
  if search == "0":
    continue
  else:
    if search in db.keys():
      cloudproject.setCloudVar('result', s2py.encode(str(db[search])))
      cloudproject.setCloudVar('resultStatus', "0")
      
    else:
      cloudproject.setCloudVar('resultStatus', "2")
      continue
  
  
      
                               
    
  