import time
#implementing quicksort

def setup(data, start,end, visualise,delay):
    #setting up array to be partitioned
    #such that everything to the left of the border is smaller than the pivot
    pivot = data[end]
    border = start
    visualise(data,color_array(len(data), start, end,border, border))
    time.sleep(delay)



    #checking through array between the border and the pivod
    for i in range(start,end):
        if data[i]< pivot:
            data[border],data[i] = data[i],data[border]
            border += 1
        visualise(data, color_array(len(data), start, end - 1, border, i))
        time.sleep(delay)

    #swap value of border with pivot
    data[end],data[border] = data[border], data[end]
    visualise(data, color_array(len(data), start, end - 1, border, end, True))
    time.sleep(delay)
    return border #to partition the remaining sub arrays via recursion



def quick_sort(data, start,end,visualise,delay):
    if start < end:
        border = setup(data, start,end,visualise,delay)
        #sort left
        quick_sort(data,start,border-1,visualise,delay)
        #sort right, do not include border
        quick_sort(data,border+1,end,visualise,delay)



def color_array(data_length,start,end,border,pointer,swapping = False):
    color = []

    for i in range(data_length):
        if i >= start and i <= end:
            color.append('#AED6F1')
        else:
            color.append('#E8DAEF')
        if i == border:
            color.append("#C0392B")

        elif i == end:
            color.append("#34495E")

        elif i == pointer:
            color.append('#D35400')

        if swapping:
            if i == border or i == pointer:
                color.append('#2ECC71')

    return color

