class TargetModel:
    # Set attributes for Target
    IPAddress : str
    hostName : str
    SSHKey : str

    # Initialize empty list
    def __init__(self):
        self.targetList = []

    # Function to get target list data
    def getTargetList(self):
        return self.targetList
    
    def getCountTargetList(self):
        return len(self.getTargetList())
    
    # Function to set target list data
    def setTargetList(self, newData):
        self.targetList = newData