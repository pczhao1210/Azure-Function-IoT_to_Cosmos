import logging
import datetime,json
import pymongo
import azure.functions as func

def main(event: func.EventHubEvent):
    payload = event.get_body()
    payload_json = json.loads(payload)
    for i in payload_json:
        #logging.info(i)
        payload_final = i
    logging.info(datetime.datetime.now())
    logging.info("Payload is: %s", payload_final)
    #logging.info(type(payload_final))


    # write to cosmos 
    uri = "MongoDB Uri + &retrywrites=false"
    client = pymongo.MongoClient(uri)
    db = client.{database_name}
    collection = db.{collection_name}
    collection.insert_one(payload_final)
    logging.info("Succefully Write: %s", payload_final)


