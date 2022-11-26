#dictionary in python
# {}is used for this dictinoary,inside this after assigning the  value with"" and end with :. and to cahnge the value we have to use []bracket
student={"name":"maryam tahir","age":"18","gender":"female" }
print(student)
student["name"]="warda"
print(student)
#to know the key we have to use .keys() and for values .values()
print(student.keys())
print(student.values())
#if we have get  dictionary key and values in pairs we have to use.items()
print(student.items())
#if we want to check that specific key is present in dictionary we use if "any key"in variable: 
if "name" in student:
    print("yes this key exist in dictionary")