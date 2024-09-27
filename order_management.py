# nodes 
class OrderNode:
    def __init__(self, order):
        self.order = order 
        self.next = None  

# Queue 
class OrderQueue:
    def __init__(self):
        self.front = None  
        self.rear = None  

    # Add order
    def add_order(self, order):
        new_order = OrderNode(order)
        if self.rear is None:  
            self.front = self.rear = new_order
            return
        self.rear.next = new_order  
        self.rear = new_order

    # Remove order
    def remove_order(self):
        if self.front is None:
            print("No orders aviailable.")
            return None
        removed_order = self.front.order
        self.front = self.front.next

        if self.front is None:  
            self.rear = None
        return removed_order

    # Display Orders
    def display_orders(self):
        if self.front is None:
            print("Queue is Empty.")
            return
        current = self.front
        while current:
            print(f"Order: {current.order}")
            current = current.next

# Testing 
if __name__ == "__main__":
    kitchen_queue = OrderQueue()

    # Adding new orders
    kitchen_queue.add_order("Taco")
    kitchen_queue.add_order("Nacho")
    kitchen_queue.add_order("Burrito")
    
    # Displaying the current orders
    print("Orders in queue:")
    kitchen_queue.display_orders()

    # Removing orders
    print("\nRemoving first order...")
    print(f"Removeded: {kitchen_queue.remove_order()}")
    
    print("\nOrders After Removing:")
    kitchen_queue.display_orders()

