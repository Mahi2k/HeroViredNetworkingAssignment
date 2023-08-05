import urllib.request
import time

finalListOfWebsiteStatus = {}
    
def scanWebsite(websiteList):
   #Run the loop to keep monitoring
    if(len(websiteList) < 1):
        return

    time_delay = 2
    while True:
        for i in range(len(websiteList)):
            # Hit the website through url lib and requesting the website
            status = urllib.request.urlopen(websiteList[i]).getcode()
            #If it returns 200, the website is GOOD else BAD
            if status != 200:
                #Call email function
                addToWebsiteList(websiteList[i], "GOOD")
            else:
                addToWebsiteList(websiteList[i], "BAD")    
            
        time.sleep(time_delay)
        printTheStatus()
        
            
def addToWebsiteList(name, status):
    # Function for creating a list of websites
    finalListOfWebsiteStatus.update({name:status})
    
def printTheStatus():
    # Function to print table format
    print("{:<30} {:<10}".format(' ',' '))
    print("{:<30} {:<10}".format('Website','Status'))
    for name, status in finalListOfWebsiteStatus.items():
        print("{:<30} {:<10}".format(name, status))


def websiteScanner():
    scanWebsite(["http://awesomevicky.com", "http://dev.awesomevicky.com", "http://qa.awesomevicky.com"])
    

websiteScanner()