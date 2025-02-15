# terminal_killer/data/bloodfeed.py
class HemoglobinStream:
    def __init__(self):
        self.veins = {}
        self.arteries = defaultdict(list)
    
    def puncture_exchange(self, exchange):
        self.veins[exchange] = HemorrhageAPIConnection(exchange)
    
    def start_bleeding(self):
        for exchange in self.veins.values():
            exchange.start_hemorrhaging()
    
    def transfuse(self, data_type):
        return [a.pump() for a in self.arteries[data_type]]

class HemorrhageAPIConnection:
    def start_hemorrhaging(self):
        self.socket = websockets.connect('wss://terminal-killer.xyz/vampire-feed')
        asyncio.create_task(self._exsanguinate())
    
    async def _exsanguinate(self):
        async with self.socket as ws:
            while True:
                data = await ws.recv()
                self._process_blood_packet(data)
    
    def _process_blood_packet(self, data):
        packet = json.loads(data)
        if packet['type'] == 'KILL_SWITCH':
            self.trigger_apocalypse(packet)