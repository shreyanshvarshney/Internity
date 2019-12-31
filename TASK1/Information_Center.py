import re  
  
def extract(text):    

    email = re.findall(r'\S+@\S+', text)
    name = re.findall(r'[a-zA-Z]{2,}\s[a-zA-Z]{2,}',text)
    number = re.findall(r'[6-9]\d{9}$',text)
    date = re.findall(r'\d{4}-\d{2}-\d{2}', text)

    #This is just for testing it in Terminal
    print(email) 
    print(name)
    print(number)
    print(date)

    file1 = open("email.txt",'w')
    file2 = open("name.txt",'w')
    file3 = open("number.txt",'w')
    file4 = open("date.txt",'w')

    file1.write(email[0])
    file2.write(name[0])
    file3.write(number[0])
    file4.write(date[0])

    file1.close()
    file2.close()
    file3.close()
    file4.close()
        
#Sample input you can use for testing
text = 'adcde.abc@gmail.com, 1999-10-02,Shreyansh Varshney,9898776655'        
extract(text)
