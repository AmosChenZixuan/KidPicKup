import json
from channels.generic.websocket import WebsocketConsumer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

HARDCODE_GROUP_NAME = 'test'

class Consumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = HARDCODE_GROUP_NAME

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'message',
                'message':'hi, ' + self.channel_name
            }
        )

    def message(self, event):
        self.send(text_data=json.dumps({
            'type':'message',
            'message':event['message'],
        }))


    def add_student(self, event):
        self.send(text_data=json.dumps({
            'type':'add_student',
            'data':event['data'],
        }))

    def remove_student(self, event):
        self.send(text_data=json.dumps({
            'type':'remove_student',
            'data':event['data'],
        }))
   

    # def receive(self, text_data):
    #     text_data_json = json.loads(text_data)
    #     message = text_data_json['message']

    #     print(self.channel_name, message)


def notify_student_added(wl):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        HARDCODE_GROUP_NAME,
        {
            'type': 'add_student', 
            'data': {
                'student_id':wl.student_id.id,
                'student_name': str(wl.student_id),
                'student_class':wl.student_id.classes,
                'car_id': str(wl.vehicle_id),
            }
        }
    )

def notify_student_removed(student):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        HARDCODE_GROUP_NAME,
        {
            'type': 'remove_student', 
            'data': {
                'student_id':student.id,
                'student_class':student.classes
            }
        }
    )