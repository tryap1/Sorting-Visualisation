import time

def merge_sort(data, visualise, delay):
    split_algo(data, 0, len(data)-1, visualise, delay)

def split_algo(data, left,right,visualise,delay):
    #base case
    if left < right:
        #split data in 2 halves
        mid = (left+right)//2
        #split data in left half
        split_algo(data, left,mid,visualise,delay)
        #split data in right half
        split_algo(data, mid+1,right, visualise, delay)
        #merge data
        merge_algo(data,left,mid,right,visualise,delay)

def merge_algo(data,left,mid,right,visualise,delay):
    visualise(data,color_array(len(data),left,mid,right))
    time.sleep(delay)
    #assigning array values on each respective half
    left_half = data[left:mid+1] #from left to mid
    right_half = data[mid+1:right+1] #from mid+1 to right

    #initialise index for each array
    leftindex = 0
    rightindex = 0

    for i in range(left, right+1):
        #check if there is anything to sort
        if leftindex < len(left_half) and rightindex < len(right_half):
            #sort!
            if left_half[leftindex]<= right_half[rightindex]:
                data[i] = left_half[leftindex]
                leftindex = leftindex+1

            else: #right half greater than left
                data[i] = right_half[rightindex]
                rightindex = rightindex+1

        #if right side is sorted, but left side is not complete
        elif leftindex < len(left_half):
            data[i] = left_half[leftindex]
            leftindex = leftindex+1

        #else, left if sorted but right is not complete
        else:
            data[i] = right_half[rightindex]
            rightindex = rightindex+1
    #visualise(data, ['green' if x >=left or x <= right else 'white' for x in range(len(data))] )
    #time.sleep(delay)


def color_array(data_length,left,mid,right):
    color = []

    for i in range(data_length):
        if i >= left and i <= right:
            if i <= mid:
                color.append("#F7DC6F")

            else:
                color.append("#F1948A")

        else:
            color.append('#E8DAEF')

    return color





