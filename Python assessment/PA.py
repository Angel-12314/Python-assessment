import wikipedia

def searchquery():
        
    print("Please enter query to search in wikipedia : ")
              
def takecommand():
    
    try:
        query=input()
        print("query = ",query)
    
    except Exception as e:
        print(e)
        print("please enter that again")
        query="nothing"
    return query
    
if __name__=='__main__':
     searchquery()
  
     while True:

            query = takecommand().lower()
 

            if "wikipedia" in query:
           
                print("searching in wikipedia")
                query=query.replace("search in wikipedia","")
                results=wikipedia.summary(query,sentences=2)
                print("According to wikipedia, ")
                print(results)