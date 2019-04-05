import array


def binary(arr,n,num):
    z=int(n/2)
    if(arr[z]==num):
        print('Number is found at the index :',z)
        return
    elif(num<arr[z]):
        binary(arr,n-z,num)
    elif(num>arr[z]):
        binary(arr,n+z,num)

arr=array.array('i',[5,6,7,8,9])
n=len(arr)
binary(arr,n,6)