#comprehension list,set,dictionary,tuple
#list
lt1=[1,2,3,4,5,6,7,8,9,10]
print(type(lt1))

lit2=[i**2 for i in lt1 ]
print(lit2)

# dictionary comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = {num: num ** 2 for num in numbers if num %  2 ==0 }
print(result , 'dictionary comprehension')

# set comprehension
emails = [
    "A@gmail.com",
    "b@gmail.com",
    "A@gmail.com",
    "c@gmail.com",
    "b@gmail.com"
]

result = {email.lower() for email in emails}
print(result, 'set comprehension')
# map

lit1=[1,2,3,4,5,6,7,8,9,10]

result=map(lambda x: "even" if x%2==0 else "odd",lit1)
print(tuple(result))
print(tuple(result))


# adding 18 % gst
prices=[100,200,300,400,500]
result=list(map(lambda x: (x + (x*18/100)),prices))
print(result, "with GST")


# filter()
lit2=[1,2,3,4,5,6,7,8,9,10]

result=filter(lambda c: c%2==0,lit2)
print(tuple(result))
lit3=[{
    "name": "John",
    "age": 30,
    "active": True
},{
    "name": "Jane",
    "age": 25,
    "active": False
},{
    "name": "Bob",
    "age": 40,
    "active": True
}]

rslt=filter(lambda c:c["active"],lit3)
print(tuple(rslt))

# zip 
names = ["Rahul", "Aman", "Neha"]
ages = [23, 25, 22]
cities = ["Indore", "Bhopal", "Ratlam"]

result = dict(zip(names, zip(ages, cities)))
print(result)
# result = dict(zip(*records))
# print(result(names, ages, cities), "zip function")

# scenario of question 1
transactions = [
    {"user": "Alice", "amounts": [-120, -20, 50], "currency": "INR"},
    {"user": "Bob", "amounts": [-10, -5], "currency": "USD"},
    {"user": "Charlie", "amounts": [500, 300, -50], "currency": "INR"},
]

result = {user["user"]: sum(user["amounts"]) for user in transactions if user["currency"] == "INR" and sum(user["amounts"]) > 0}
print(result, "scenario of question")

# scenario of question 2
catalog = [
    ("Laptop", "Electronics", 65000, 4.5),
    ("Mouse", "Electronics", 1200, 4.8),
    ("Headphones", "Electronics", 4500, 4.5),
    ("Desk", "Furniture", 8500, 4.2),
]
catalog.sort(key=lambda item:  (-item[3],-item[2]))

print(catalog, "scenario of question 2")

new_catalog = [
    ("Narayan", 85.0,12),
    ("athrav", 90.3,10),
    ("chirag", 73.0,11),
    ("aashis", 50.0,8),
    ("rohit", 50.0,9),
]

new_catalog.sort(key=lambda item: (-item[1], -item[2]))
print(new_catalog, "scenario of question 3")

