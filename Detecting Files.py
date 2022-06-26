import os

userinput = input("Type location: ")

path = userinput

#"C:\\Users\\Your name of the device\\Desktop\\"

if os.path.exists(path):
    print("Location of the file:", path)
    print("Location found")
    
    

else: 
    print("****Not found!****")
         