from datetime import datetime
import random
import json
import asyncio
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData

class simulation:
    def __init__(self, shopping_centre_id):
        self.weight = random.randint(30, 100) # this is the weight of the person in kilograms
        self.time_on_sensor = random.random() * 3 # max time that someone stays on this sensor
        self.power_output = random.randint(5, 8) # between 5-8 watts
        self.tile_id = random.randint(1, 5000) # between 1 and 5000
        self.lat = 0
        self.long = 0
        self.time_generated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.shopping_centre_id = shopping_centre_id
 
    async def generate_event(self):
        diction = {
            'Weight': self.weight,
            'TimeOnSensor': self.time_on_sensor,
            'PowerOutput': self.power_output,
            'TileId': self.tile_id,
            'Lat': self.lat,
            'Long': self.long,
            'TimeGenerated': self.time_generated,
            'ShoppingCentreId': self.shopping_centre_id
        }
        producer = EventHubProducerClient.from_connection_string(conn_str="Endpoint=sb://piezotiles.servicebus.windows.net/;SharedAccessKeyName=tilesender;SharedAccessKey=agoiv73QWyI+wKVlRBbRedBfv3ofmR96NJrLczM2iBI=;EntityPath=tiles", eventhub_name="tiles")
        async with producer:
             event_data_batch = await producer.create_batch()
             # Add events to the batch.
             event_data_batch.add(EventData(json.dumps(diction)))
             await producer.send_batch(event_data_batch)
             print('Message sent on the event hub ...')