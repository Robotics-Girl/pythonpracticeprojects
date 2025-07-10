class Bank: 
    def __init__(self): 
        self.accounts = {}
    def create_account(self, username): 
        if username not in self.accounts: 
            self.accounts[username] = {
                "balance" : 0, "history" : []
            } 
        else: 
            print("Already exists")
    def 