# *args **kwargs are used to pass a variable number of arguments to a function.




def sun(*numbers):
    total =0
    for num in numbers :
        total += num
    return total
print(sun(1,2,3,4,5)) # Output: 15

def student_info(**kwargs):
    for key , value in kwargs.items():
        print(f"{key}: {value}")

student_info(name="John", age=25, grade="A")

# def change_num(*nums):
#     nums[2] = 10
#     return nums

# print(change_num(1, 2, 3, 4, 5)) # Output: (1, 2, 10, 4, 5)

def change_value(**kwargs):
    kwargs['name'] = "yash"
    return kwargs
print(change_value(name="John", age=25, grade="A")) # Output: {'name': 'yash', 'age': 25, 'grade': 'A'}

def all(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

all(1, 2, 3, name="John", age=25, sex="Male") # Output: Positional arguments: (1, 2, 3) Keyword arguments: {'name': 'John', 'age': 25, 'sex': 'Male'}

def with_nomal_args(normal_arg, *args, **kwargs):
    print("Normal argument:", normal_arg)
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

with_nomal_args("Hello", 1, 2, 3, name="John", age=25, sex="Male") # Output: Normal argument: Hello Positional arguments: (1, 2, 3) Keyword arguments: {'name': 'John', 'age': 25, 'sex': 'Male'}

def dispatch_event(event_type, *tag, time=30 ,**metadata):
    print(f"Event Type: {event_type}")
    dup = tag[0].upper()
    print(f"Tag: {dup}")
    if time is 60:
        print ("error message: time is 60")
    metadata['time'] = time
    for t in tag:
        metadata['tag'] = t
    print(f"metadata Info: {metadata}")

dispatch_event("click", "button", "submit", time=45, user="John", location="homepage") 

def Create_counter(start=0, step=1):
    count = start
    def counter():
        nonlocal count
        count += step
        return count
    return counter

sounter = Create_counter(1, 2)
print(sounter()) # Output: 3

change=10
def change_value():
     number=20
     def inner():
            nonlocal number
            global change
            change = 5
            number = 10
            return number + change
     return inner() + 5

result = change_value()
print(result)  # Output: 20