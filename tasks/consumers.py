import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import Task


class TaskConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = 'task_room'
        self.room_group_name = 'task_group'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        task = text_data_json['task']

        if task.get('action') == 'create':
            Task.objects.create(
                title=task['title'],
                description=task.get('description', ''),
                completed=task.get('completed', False),
                user=self.scope['user']
            )

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'send_notification',
                'notification': json.dumps({
                    'action': task.get('action'),
                    'task': {
                        'id': task.get('id'),
                        'title': task['title'],
                        'description': task.get('description', ''),
                        'completed': task.get('completed', False),
                    }
                })
            }
        )

    def send_notification(self, event):
        notification = event['notification']
        self.send(text_data=notification)
