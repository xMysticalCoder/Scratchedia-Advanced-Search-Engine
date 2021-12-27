import keep_alive
from replit import db
import time
import os
os.system("pip install scratch2py && pip install --force-reinstall websocket-client")
from scratch2py import Scratch2Py
# above are neccassary imports 
#temp websites start
#template for temp website: db["temp website name"] = "temp website data"
#temp websites end
print(db.keys())

password = os.environ['password']
projectID = "616759917"
s2py = Scratch2Py("xMysticalLegend", password)
cloudproject = s2py.scratchConnect(projectID)
project = s2py.project(projectID)
print("Connection to user and project complete. Starting loop.")
#above connects to my account and connects to the project
# about that, we will use the scratchedia account to change the cloud variables and stuff in the final version, for safety. 
while True:
  websites = ""
  
  for i in range(len(db.keys())):
    websites = websites + list(db.keys())[i] + ", "
  
  try:
    websitesC = s2py.decode(websites)
    cloudproject.setCloudVar('websitesC', websitesC)
    print("websites set.")
  except:
    print("Websites not set. Continuing.")
  #above was me trying to make it so that the user can see all the websites it has. (does not work because of the encoder of s2py)
  
    

  
  comments = project.getComments()
  comments = comments[0]
  comments = comments["content"]
  print(comments)
  #above gets the newest comment
  if "WEBSITE(" in comments:
    print("Website requested")
    comments = comments.replace("WEBSITE(", "")
    comments = comments.replace(")", "")
    comments = comments.split(",", 1)
    if comments[0] not in db.keys():
      print("Website created")
      db[comments[0]] = comments[1]
  #above sees if the comment fits the format for website creation. if yes, it makes the website
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
#above is the actual search engine. 
  
  
      
                               
    
  