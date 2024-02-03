from googleapiclient.discovery import build
import os
import json


class Channel:
    """Класс для ютуб-канала"""
    youtube = build('youtube', 'v3', developerKey=os.getenv("API"))

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализирует id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        stats = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = stats['items'][0]['snippet']['title']
        self.channel_description = stats['items'][0]['snippet']['description']
        self.url = stats['items'][0]['snippet']['customUrl']
        self.subscriberCount = stats['items'][0]['statistics']['subscriberCount']
        self.video_count = stats['items'][0]['statistics']['videoCount']
        self.viewCount = stats['items'][0]['statistics']['viewCount']

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        youtube = build('youtube', 'v3', developerKey=os.getenv("API"))
        stats = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(stats, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        return cls.youtube

    def to_json(self, filename):
        data = (self.channel_id, self.title, self.channel_description, self.url, self.subscriberCount, self.video_count,
                self.viewCount)
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
