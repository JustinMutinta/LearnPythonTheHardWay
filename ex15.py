#imports the module to allow you to enter the file names when running the script in terminal
from sys import argv

#script(name of the script) and the file name will get their variables from terminal
script, filename = argv

#txt will open the file
txt = open(filename)

#First one is going to say whats about to happen, second one will read off from the file
print(f"Here's your file {filename}:")
print(txt.read())

#Now the user will enter the file name manually
print("Type the filename again:")
file_again = input("> ")

#Outputs the file name again after opening it.
txt_again = open(file_again)

print(txt_again.read())