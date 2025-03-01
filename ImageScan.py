import json
import requests
from Settings import fetch_setting

# params = {
#     'url': '',
#     'models': 'offensive',
#     'api_user': '308358527',
#     'api_secret': 'T9crUizWPEcKL6BPHFLu'
# }
# r = requests.get('https://api.sightengine.com/1.0/check.json', params=params)

# output = json.loads(r.text)

# print(output)
class MemberScanner:
    def __init__(self, member):
        self.member = member
        self.guild = member.guild

    async def scanImage(self):
        if not hasattr(self.member.avatar, 'url'): return None
        params = {
            'url': str(self.member.avatar.url),
            'models': 'offensive',
            'api_user': '308358527',
            'api_secret': 'T9crUizWPEcKL6BPHFLu'
        }
        r = requests.get('https://api.sightengine.com/1.0/check.json', params=params)
        output = json.loads(r.text)
        self.output = output
        return output

    async def hasBadPfp(self):
        output = await self.scanImage()
        if output != None and output['offensive']['prob'] > 0.5 and len([box["label"] for box in self.output["offensive"]["boxes"] if box["prob"] > 0.5 and box["label"] != 'middlefinger']) > 0:
            return True
        return False
        
    def getReasons(self):
        return ", ".join([box["label"] for box in self.output["offensive"]["boxes"] if box["prob"] > 0.5])

    async def scanMember(self):
        if await self.hasBadPfp():
            await self.takeAction()

    async def takeAction(self):
        channel_id = fetch_setting(self.guild.id, 'log_channel')
        if channel_id is None: return
        channel = self.guild.get_channel(channel_id)
        await channel.send(f"<@811369189658591233>, <@811376322584641606>, <@811441753194233856>: New user {self.member.mention} has a profile picture containing `{self.getReasons()}`")
        # <@811369189658591233>, <@811376322584641606>, <@811441753194233856> Mod role pings