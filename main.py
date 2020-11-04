#idea concived by Henry
__author__ = "Gordan"
from endings import * #importing custom ending module
from time import sleep
sh = sleep(0.5)
#creating a class instance
end = endings()
print("Presenting...", sh)
print("initialising...")
print("Adventure of The Lemom")

name = input("What is the name of our hero?: ")
if name == "grolong" or name == "Grolong":
    print("The venial sin has been committed.")
    print("The eternal covenant broken.")
    print("Be gone traitor.")
    end.groending()
print("so be it.")
print("Our story begins in the wilderness")