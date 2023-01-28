# intro print statement to introduce the project to the reader
print("Are you ready for the most entertaining/confusing MadLib you have ever seen? Start entering inputs to see what happens...")

# input statements asking the reader certain questions which will be stored in the assigned variables
name = input("Enter a name: ")
verb1 = input("Enter a verb ending with -ing: ")
number = input("Enter a number: ")
furniture = input("Enter a piece of furniture: ")
food = input("Enter a food: ")
verb2 = input("Enter a verb ending with -ed: ")
store = input("Enter a store name: ")
adjective = input("Enter an adjective: ")
transition = input("Enter a transition word: ")
disease = input("Enter a disease: ")

# final print statement to take all the stored information and display it in the story respectively
print("Hello", name + ", one day I was", verb1 + " a", number + " mile marathon. After the marathon, I sat down on my", furniture + " and ate a full bowl of", food + ". I", verb2 + " to the local", store + " and bought a", adjective + " slurpee.", transition + ", I got", disease + " and was rushed to the hospital. I woke up from a", number + " year coma and decided to retake this computer science course and make this MadLib for you!")
