a=[1,0,2,42,1,0,-1,49,453,90]
n=len(a)
s=sorted(a,key=lambda x:-x)
print(s)
# for i in range(n):
#     for j in range(i+1,n):
#         if a[i]<a[j]:
#             a[i],a[j]=a[j],a[i]
#             print(a)
# print(a)