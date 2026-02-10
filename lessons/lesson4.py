class Test:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
test_obj = Test("321456")
my_int = 123

print(test_obj)
print(my_int)


class MyInt:

    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)
    def __add__(self, other):
        print(self.value)
        print(other.value)
        return self.value + other.value
    def __call__(self, *args, **kwargs):
        self.view_count += 1
        print(self.view_count)

my_int1 = MyInt(12)
my_int2 = MyInt(10)
my_int3 = my_int1 + my_int2
print(my_int3)
print(my_int1())
print(my_int1())