with open("sophie.txt", "a") as f:
    f.write("Now the file has more content!")

# open and read the file after the appending:
with open("sophie.txt") as f:
    print(f.read())
