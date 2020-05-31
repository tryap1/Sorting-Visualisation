import time

def bubble_sort(data, visualise,delay):

    for i in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j],data[j+1] = data[j+1],data[j]
                visualise(data,['#F7DC6F' if x == j or x == j+1 else '#E8DAEF' for x in range(len(data)) ])
                time.sleep(delay)




