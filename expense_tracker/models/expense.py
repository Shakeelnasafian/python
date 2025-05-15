class Expense:
    def __init__(self, name:str, amount: float, date: str, category: str, description: str = ""):
        self.name = name
        self.amount = amount
        self.date = date
        self.category = category
        self.description = description

    def to_dict(self):
        return {
            "name": self.name,
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "description": self.description,
        }