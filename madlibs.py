'''# concatenando strings (aka como juntar strings)

#formas de juntar strings
youtuber = "greenervolvox"
print("subscribe to" + youtuber)
print("subscribe to {}".format(youtuber))
print(f"subscribe to{youtuber}")'''

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is do {adj}! It makes me so ecited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}"

print(madlib)