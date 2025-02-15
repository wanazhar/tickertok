# api/trading.py
class FIXEngine:
    def __init__(self):
        self.fix = quickfix.Initiator(
            quickfix.SessionSettings("fix.cfg"),
            quickfix.FileStoreFactory("fix_store"),
            quickfix.ScreenLogFactory()
        )
        self.fix.start()

@router.post("/place-order")
async def fix_order(order: FIXOrder):
    fix_msg = quickfix.Message()
    fix_msg.setField(quickfix.ClOrdID(order.clordid))
    fix_msg.setField(quickfix.Symbol(order.symbol))
    fix_msg.setField(quickfix.Side(order.side))
    fix_msg.setField(quickfix.OrderQty(order.quantity))
    fix_msg.setField(quickfix.Price(order.price))
    quickfix.Session.sendToTarget(fix_msg)