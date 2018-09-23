
mydict = {'Name': 'Zabra', 'Age': 7}
print("Value : {}".format(mydict.get('Age')))

# If key doesn't exist, use a default. ie "Never"
print("Value : {}".format(mydict.get('Education', "Never")))


print('Value : {}'.format(mydict['Age']))

print(mydict)
