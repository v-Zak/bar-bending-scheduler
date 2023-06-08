class Logger:
    """
    A class which handles the logging of text information

    """
    def __init__(self):
        self.log = []
    def inputLog(self, input_string : str):
        """
        Stores input string in log

        Parameters
        ----------
        input_string : str
            A string to log
    
        """
        self.log.append(input_string)
    
    def emptyLog(self):
        """
        Empties the log
    
        """
        self.log = []

    def getAll(self) -> list:
        """
        Outputs the stored log as a list of str

        Returns
        ----------
        log : list of str
            A list of log inputs
    
        """
        return self.log.copy()
    
    def getAllAsString(self, newLine = '\n') -> str:
        """
        Outputs the stored log as a str with newLine char inbetween 

        Parameters
        ----------
        newline : str, default = '\\n'
            The newLine Character to use

        Returns
        ----------
        log : str
            A concat of all logs
    
        """
        concat = ''
        for log in self.log:
            concat += log + newLine
        return concat
    
    def getLast(self) -> str:
        """
        Outputs the last log as a str

        Returns
        ----------
        log : str
           last log
    
        """
        return self.log[-1].copy()

    def printLast(self):
        """
        Prints the last Log
    
        """
        print(self.log[-1])

    def printAll(self):
        """
        Prints the whole log
    
        """
        for entry in self.log:
            print(entry)