# api/p2p_data_layer.py
class DistributedTickerPlant:
    def __init__(self):
        self.nodes = []
        self.ledger = BlockchainLedger()
    
    def add_data_node(self, node_url):
        self.nodes.append(node_url)
    
    def get_market_data(self, symbol):
        responses = asyncio.gather(*[self.query_node(n, symbol) for n in self.nodes])
        return self.consensus_algorithm(responses)

    async def query_node(self, node_url, symbol):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{node_url}/ticker/{symbol}") as resp:
                return await resp.json()