#Complete the mean function to make it return the mean of a list of numbers

data1=[49., 66, 24, 98, 37, 64, 98, 27, 56, 93, 68, 78, 22, 25, 11]

def mean(data):
    total = 0
    mean = None
    #Insert your code here
    for data_set in data:
        total = total + data_set
        mean = total/len(data)
    return mean

print(mean(data1))