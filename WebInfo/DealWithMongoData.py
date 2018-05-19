import  pymongo

def update_data(docs):
    # for doc in docs:

    return None

def main():
    client = pymongo.MongoClient(host = '127.0.0.1',port = 27017)
    db = client.python
    collection = db['51JobPositionDetail']
    position_docs = collection.find()
    update_data(position_docs)


if __name__ == '__main__':
    main()