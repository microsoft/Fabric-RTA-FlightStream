from pprint import pprint
import json
import os
import sys
import time
import datetime
import traceback
import logging
import requests
#from request.auth import HTTPBasicAuth
from azure.eventhub import EventHubProducerClient, EventData


def main():
    ENDPOINT="https://opensky-network.org/api/states/all"
    #ENDPOINT="https://dog.ceo/api/breeds/list/all"

    producer = EventHubProducerClient.from_connection_string(conn_str="Endpoint=sb://eventstream-.....servicebus.windows.net/;SharedAccessKeyName=key_...;SharedAccessKey=...;EntityPath=es_...")

    event_data_batch = producer.create_batch()

    resp = requests.get(ENDPOINT, auth=('rtauser1', '...'))
    respjson=resp.json()

    for i in respjson['states']:
        event_data_batch.add(EventData(str(i)))

        #prior to hitting the max by 5k, send the current and recreate batch.
        if event_data_batch.size_in_bytes >= event_data_batch.max_size_in_bytes-5000:
            print('Sending1...')
            producer.send_batch(event_data_batch)
            event_data_batch = producer.create_batch()

    print('Sending2...')
    producer.send_batch(event_data_batch)
    producer.close()
    print('Done')

main()
