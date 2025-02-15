# api/neural_orders.py
class NeuralOrderRouter:
    def __init__(self):
        self.gnn = GraphNeuralNetwork()
        self.order_graph = nx.DiGraph()
    
    def add_order(self, order):
        self.order_graph.add_node(order.id, **order.dict())
        self.gnn.update_embeddings(self.order_graph)
    
    def optimal_route(self, order):
        return self.gnn.predict_path(
            self.order_graph, 
            source=order.id,
            target_type=order.asset_class
        )