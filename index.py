from pymongo import MongoClient
import random
import datetime

import pandas as pd
import matplotlib.pyplot as plt

try:
    mongo_client = MongoClient('mongodb://localhost:27017/')
    print("MongoDB connected successfully.")
except:
    print("Could not connect to MongoDB")

db = mongo_client.rayndex
collection = db.index

def run():
    # Item 1: Generate and insert 1.000.000 of documents in the collection
    #         and calculate the time spend in this operation.
    values_to_insert = []

    # Generate datas to insert
    for i in range(1000000):
        values_to_insert.append({"var1": random.randint(0, 100),
                            "var2": random.randint(0, 100)})


    # Clearing file to save time spent inserting
    open('files/insert-before-index.txt', 'w').close()

    start = datetime.datetime.today()

    # Inserting values in collection
    collection.insert_many(values_to_insert)

    end = datetime.datetime.today()

    # Calculating time spend in insertion
    duration = end - start

    with open('files/insert-before-index.txt', 'a') as file:
        file.write(str(duration.total_seconds()) + "\n")
        file.close

    # Item 2: Find for values to var1 between 1 and 10 
    #         and calculate the time spend in this operation.

    # Clearing file to save time spent in find
    open('files/find-before-index.txt', 'w').close()

    start = datetime.datetime.today()

    # Finding values for var1 between 1 and 10 in collection
    values = collection.find({'var1': {'$gt': 0, '$lt': 10}})

    end = datetime.datetime.today()

    # Calculating time spend in insertion
    duration = end - start

    with open('files/find-before-index.txt', 'a') as file:
        file.write(str(duration.total_seconds()) + "\n")
        file.close

    # Item 3: Create an index for var1 and repeat the previous query 
    #         and calculate the time spend in this operation.

    # Creating the index for var1
    resp = collection.create_index([("var1", 1)])

    # Clearing file to save time spent in find
    open('files/find-after-index.txt', 'w').close()

    start = datetime.datetime.today()

    # Finding values for var1 between 1 and 10 in collection
    values = collection.find({'var1': {'$gt': 0, '$lt': 10}})

    end = datetime.datetime.today()

    # Calculating time spend in insertion
    duration = end - start

    with open('files/find-after-index.txt', 'a') as file:
        file.write(str(duration.total_seconds()) + "\n")
        file.close

    # Item 4: Repeat the previous query returning only the value of var1 
    #         (remove _id and var2 using projection) and calculate the time 
    #         spend in this operation.

    # Clearing file to save time spent in find
    open('files/find-proj-after-index.txt', 'w').close()

    start = datetime.datetime.today()

    # Finding values for var1 between 1 and 10 in collection
    values = collection.find({'var1': {'$gt': 0, '$lt': 10}}, {'var1': 1, '_id': 0})

    end = datetime.datetime.today()

    # Calculating time spend in insertion
    duration = end - start

    with open('files/find-proj-after-index.txt', 'a') as file:
        file.write(str(duration.total_seconds()) + "\n")
        file.close

    # Item 5: Generate and insert more 1.000.000 of documents in the collection
    #         and calculate the time spend in this operation.

    values_to_insert_after_index = []

    # Generate datas to insert
    for i in range(1000000):
        values_to_insert_after_index.append({"var1": random.randint(0, 100),
                            "var2": random.randint(0, 100)})

    # Clearing file to save time spent inserting
    open('files/insert-after-index.txt', 'w').close()

    start = datetime.datetime.today()

    # Inserting values in collection
    collection.insert_many(values_to_insert_after_index)

    end = datetime.datetime.today()

    # Calculating time spend in insertion
    duration = end - start

    with open('files/insert-after-index.txt', 'a') as file:
        file.write(str(duration.total_seconds()) + "\n")
        file.close

if __name__ == "__main__":
    run()

    # Time spend for insert and find before create index
    time_insert_before_index = pd.read_csv('files/insert-before-index.txt', sep="\n", header=None)
    time_find_before_index = pd.read_csv('files/find-before-index.txt', sep="\n", header=None)

    # Time spend for insert and find after create index
    time_insert_after_index = pd.read_csv('files/insert-after-index.txt', sep="\n", header=None)
    time_find_after_index = pd.read_csv('files/find-after-index.txt', sep="\n", header=None)
    time_find_proj_after_index = pd.read_csv('files/find-proj-after-index.txt', sep="\n", header=None)
    
    times_insert = []
    times_insert.append(time_insert_before_index[0][0])
    times_insert.append(time_insert_after_index[0][0])

    keys_insert = ["Before index", "After index"]
    
    plt.suptitle('Time spent inserting before and after index creation (in seconds).')
    plt.bar(keys_insert, times_insert)
    plt.savefig('images/time_insert.jpg')

    times_find = []
    times_find.append(time_find_before_index[0][0])
    times_find.append(time_find_after_index[0][0])
    times_find.append(time_find_proj_after_index[0][0])

    keys_find = ["Before index", "After index", "After index and \n with projection"]

    plt.suptitle('Time spent finding values for var1 between 1 and 10 before and \n after index creation (in seconds).')
    plt.bar(keys_find, times_find)
    plt.savefig('images/time_find.jpg')