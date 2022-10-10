test_keys =["pen", "scale", "pencil"]
test_values = [1, 2, 3]
res={}
for key in test_keys:
    for value in test_values:
        res[key] = value
        test_values.remove(value)
        break
print("dictionary : " + str(res))