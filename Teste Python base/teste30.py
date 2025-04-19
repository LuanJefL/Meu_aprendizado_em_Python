def eggs(someParameter):
    someParameter.append('Hello')
    print(someParameter)
spam = [1, 2, 3]
eggs(spam)  
print(spam)
spam.append("Irineu")
eggs(spam)
print(spam)
