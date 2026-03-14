#creating a Dictionary
students={
    "name":"   raju   ",
    "marks":[20,40,50,70]
}

#Removing WhiteSpaces and Capitalize the name 
students["name"]=students["name"].strip().capitalize()

#Creating a function for calcuting average 

def average(data):
    
    #Finding lentgh of data elements and instilazing the sum and average
    n=len(data)
    sum=0
    average=0
    #using for loop for adding elements in data to add
    
    for i in data:
        sum+=i
        
    #calculating the average and returning it
    average=sum/n 
    return average

#Calculating the averagi and storing it
percentage=average(students["marks"])

#Display the result 
print(f"Name:{students['name']}\nPercentage:{percentage}%")
