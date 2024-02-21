import uuid # Class for creating custom ID strings

class Transaction():
    def __init__(self, title: str, description: str, amount: float, date: str, id=None) -> None:        
        self.title = title
        self.description = description
        self.amount = amount
        self.date = date

        # If the user has not passed an ID, generate one
        self.__id = id if id else self.__generate_id()
    
    def __generate_id(self):
        '''
            Generates a new ID

            return 
                str 
        '''
        return str(uuid.uuid4())
    
    @property
    def id(self):
        return self.__id
    
    def __str__(self) -> str:
        output = f"ID: \t\t\t{self.id}\n"
        output += f"Title: \t\t\t{self.title}\n"
        output += f"Description: \t\t{self.description}\n"
        output += f"Amount: \t\t{self.amount}\n"
        output += f"Date: \t\t\t{self.date}"

        return output
    
    def get_dict(self):
        return {
            "id": self.__id,
            "title": self.title,
            "description": self.description,
            "amount": self.amount,
            "date": self.date
        }

    
