# import os

# f = open("file/demo.txt", "r")
# data = f.read(5)
# print(data)
# readLine = f.readline()
# print(readLine)
# f.close()


# fw = open("file/demo.txt", "a")
# fw.write("\n i want to learn Python language.")
# fw.close()

# f = open("file/sample.txt", "w")
# f.close()

# os.remove("file/sample.txt")


# file = open("file/demo.txt", "a")

# file.write("\n i wan to learn Javascript")

# file.close()


# with open("file/demo.txt", "r") as f:
#     data = f.read()
#     new_data = data.replace("python", "Js")
#     print(new_data)
# with open("file/demo.txt", "w") as f:
#     f.write(new_data)

with open("file/demo.txt", "r") as f:
    data = f.read()
    if "Js" in data:
        print("found")
    else:
        print("not found")
