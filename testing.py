import json
import time
import sys

def type_writer(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

with open('data/people_data.json', 'r') as file:
    data = json.load(file)

    interval = 0.2
    for person in data:
        type_writer(f"Name: {person['name']}")
        type_writer(f"Age: {person['age']}")
        type_writer(f"Email: {person['email']}")

        type_writer(f"City: {person['address']['city']}")
        type_writer(f"Country: {person['address']['country']}")

        print(f"Hobby: ")
        for hobby in person['hobbies']:
            type_writer({hobby})  

        print()
        time.sleep(interval)