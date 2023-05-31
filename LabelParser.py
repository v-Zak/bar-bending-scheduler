import re as regex

class LabelParser:
    """
    A class which handles parsing of strings

    """
    def __init__(self):
        pass

    def get_bar_labels(self, text):
        """
        filter and format into strings which are of expected bar format\n
        (from '8H16-02\\P4T1 4B1' to '8H16-02')\n
        H bar size only

        Parameters
        ----------
        text : list of str
            The text to parse

        Returns
        ----------
        list of str
            A list of formatted XHXX-XX bar text
    
        """
        
        #get all strings that contain HXX-
        for element in text:
            if regex.search(r'H',element):
                print (element)
