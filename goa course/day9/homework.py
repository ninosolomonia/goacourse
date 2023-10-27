# 1 way to print Hello world.
message = ["Hello, world!"]
for i in message:
    print(i)

# 2 way to print Hello world.
message = "Hello,"
message1 = "world!"
print(message + " " + message1)

# 3 way to print Hello world.
world = ["Hello, world!"]
msg = "".join(world)
print(msg)

# 4 way to print Hello world.
hello = "Hello, world!"
time = int(input("Enter the current time: "))
a = 6 
b = 18
if time >=a and time <=b:
    print(hello)
else:
    print("Good Bye, world!!!")