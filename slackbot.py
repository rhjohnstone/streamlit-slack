from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

class SlackBot:
    def __init__(self, token: str, channel_id: str) -> None:
        self.client = WebClient(token=token)
        self.channel_id = channel_id
    
    def send_message(self, message: str):
        try:
            return self.client.chat_postMessage(
                channel=self.channel_id,
                text=message,
            )

        except SlackApiError as e:
            print(f"Error: {e}")
