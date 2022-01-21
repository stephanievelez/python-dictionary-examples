statData ="data/ex4.csv" #relative data used for our calculation. Separated by day and precipitation

#comment here
def getProcessedList(items_in_file):#shows rows of dates and precipitation as float separated by , and ending with \n
    list_precipitation =[None] * len(items_in_file) #this is a list where "none" holds a spot for each variable that the list contains in items_in file
    counter=0 #this helps in reiterating through the loop and placing the precipitation numbers in the following rows
    for item in items_in_file: #loop that iterates through the rows in items_in_file and places precipitation numbers (as floats) in list_precipitation to take place of "none"
        row = item.split(",") #separating date and value in each iteration
        precipitation = float(row[1])#the 2nd row is the one we are interested in since the 1st is the title of each column
        list_precipitation[counter]=precipitation 
        counter +=1 
    return list_precipitation


def processFile(items, N): #function that takes in items from statData and calculates the moving average according to N
    processed_list = getProcessedList(items) #calls the function to get the list of precipitation ready to calculate
    total_items = len(processed_list) #k which is the length of the processed_list 
    last_item_index = total_items - N #this will read up to total in list - N
    total_mov_avgs = last_item_index  + 1
    moving_averages = [None] * total_mov_avgs # holds a spot for a the lengthh of total_mov_avgs
    pos = 0
    for index in range(total_mov_avgs):
        items_to_calculate = processed_list[index:index+N] #takes the precipitation numbers from processed_list from index to index+N
        total_sum = sum(items_to_calculate) #adds all the values in items_to_calculate for the caculation
        avg = total_sum / N
        moving_averages[pos] = avg
        pos +=1
    return moving_averages #list of the calculated averages moving + N
    
    

def getNAvg(file, N):
      with open(file, "r") as weather_data: #this opens the extracted data (ex4.csv) and names it as weather_data
        data = weather_data.readlines()[1:] #this reads each line starting at the 2nd line (to ommit titles) and saves it as data date and precipitation 
        return processFile(data, N)
        



print(getNAvg(statData, 3))
