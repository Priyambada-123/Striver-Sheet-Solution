# class Solution:
#    def inversionCount(self, arr, n):
#        temp_arr=[0]*n
#         return (self.mergesort(temp_arr,arr,0,n-1))
#     def mergesort(temp_arr,arr,low,high):
#         res=0
#         if low<high:
#             mid=(low+high)//2
#             res+=self.mergesort(temp_arr,arr,low,mid)
#             res+=self.mergesort(temp_arr,arr,mid+1,high)
#             res+=self.merge(temp_arr,arr,low,mid,high)
#         return res
            
#     def merge(self,temp_arr,arr,low,mid,high):
#        i=low
#        j=mid+1
#        k=low
#        count=0
#        while(i<=mid and j<=high):
#            if(arr[i]<=arr[j]):
#                # no inversion
#                temp_arr[k]=arr[i]
#                k+=1
#                i+=1
#            else:
#                temp_arr[k]=arr[j]
#                count+=(mid-i+1)
#                k+=1
#                j+=1
#        while(i<=mid):
#            temp_arr[k]=arr[i]
#            k+=1
#            i+=1
#        while(j<=high):
#            temp_arr[k]=arr[j]
#            k+=1
#            j+=1
#        for i in range(low,high+1):
#            arr[i]=temp_arr[i]
#        return(count)