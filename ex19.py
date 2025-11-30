
def function_1_param(Param):
    print(f"Param: {Param}")


y = "Test_string"
function_1_param(y)

def cheese_and_crackers(cheese, crackers):
    print(f"We have this unexpected number of snacks!!")
    print(f"We have this number of cheese : {cheese}")
    print(f"We have this number of crackers : {crackers}")
    pass

print("We can pass numbers directly")

cheese_and_crackers(10, 20)

#We can even do math inside
cheese_and_crackers(1+1, 2-1)

cheese_count = 4
crackers_count = 22


#And we can combine the two methods - variables and integers
cheese_and_crackers(1 + cheese_count, 2 + crackers_count)