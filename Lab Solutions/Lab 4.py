"""
a) Create a text file and manually add some data to the file

"""
try :
    sample = open("Sample.txt","a")
except FileNotFoundError as e :
    print(f" Error : {e}")
except FileExistsError as e :
    print(f" Error : {e}")
else :
    print("here")
    value = "Hello World"
    sample.write(value)
finally :
    sample.close()


# file = open('Sample.txt', 'w')
# try :
#     file.read()
# except IOError as e : 
#     print(f"Error : {e}")
# except Exception as e:
#     print(f"Exception : {e}")
# finally :
#     file.close()



