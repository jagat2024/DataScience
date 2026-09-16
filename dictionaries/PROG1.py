# pythpn scrpit to merge two dictionaries
dict1={"A":100,"B":200,"C":300}
dict2={"D":400,"E":500}
merged_dict=dict1|dict2
print(merged_dict)
# sum of all values in dictionary
sum=0
for i in merged_dict:
    sum+=merged_dict[i]
print("the sum of values of the dictionary is ",sum)
# couint the freq of each elemnt in a list
l1=[1,2,3,1,4,2,100,2,4,2,5,6,7,8,9,4,6,345,5,34,5,6,7]
dict={}
for i in l1:
    if(i in dict.keys()):
        dict[i]+=1;
    else:
        dict[i]=1;
print(dict)
# combine values of 2 dict common 
d1={10:100,20:200,30:300}
d2={10:100,20:200,30:300}
d3={}
for i in d1.keys():
    for j in d2.keys():
        if(i==j):
            d3[i]=d1[i]+d2[j]
print(d3)