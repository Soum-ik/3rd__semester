# genaret a evenNumber
def evenNumber(num):
    for i in range (1, num+1):
        if(i % 2 == 0):
            yield i    
result = evenNumber(100);
for n in result:
        print(n)
totalValue = result;
# print(totalValue)
if totalValue == object:
    print('procces working')
else:
    print('not working')


# genaret a oddNumber
# def evenNumber(num):
#     for i in range (1, num+1):
#         if(i % 2 != 0):
#             yield i    
# result = evenNumber(100);
# for n in result:
#         print(n)
# print(result);

