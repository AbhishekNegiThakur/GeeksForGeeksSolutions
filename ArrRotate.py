import  array



def shift(arr,z):
    temp=arr[0]
    for i in range(z-1):
          arr[i]=arr[i+1]
    arr[z-1]=temp

def ArrayRotate(arr,d,z):
    for i in range(d):
      shift(arr,z)

def printArray(arr, size):
    for i in range(size):
        print(arr[i],end=" ")

arr=array.array('i',[1,2,3,4,5,6,7])
d=7
z=len(arr)
ArrayRotate(arr,d,z)
print(arr,z)