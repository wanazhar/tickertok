# api/terminal_features.py
@router.post("/bloomberg-composite")
async def bloomberg_composite(symbols: List[str]):
    bb = BloombergBridge()
    bb.subscribe(symbols, ["LAST_PRICE", "VOLUME"])
    return {"status": "subscribed"}

@router.websocket("/eikon-data")
async def eikon_stream(websocket: WebSocket):
    await websocket.accept()
    eikon = RefinitivStream()
    while True:
        data = eikon.get_update()
        await websocket.send_json(data)