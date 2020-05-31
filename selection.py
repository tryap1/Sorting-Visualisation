##SELECTION SORT
import time

def select_sort(data, visualise, delay):

    for i in range(len(data)):

        for j in range(i+1,len(data)):
            if data[i] > data[j]:
                data[i],data[j] = data[j],data[i]
                visualise(data,color_array(len(data),i,j))

                time.sleep(delay)

def color_array(data_length,i,j):
    color = []

    for x in range(data_length):
        if x == i:
            color.append('#F1948A')

        elif x == j:
            color.append('#F7DC6F')

        else:
            color.append('#E8DAEF')

    return color


