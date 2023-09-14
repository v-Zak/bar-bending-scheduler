import re as regex

class LabelParser:
    """
    A class which handles parsing of strings

    """
    def __init__(self):
        pass

    def get_bars(self, text : list) -> list:
        """
        get all bars as dicts (bar_mark, type, size and quantity)\n
        H bar size only

        Parameters
        ----------
        text : list of str
            The text to parse

        Returns
        ----------
        list of dict
            A list of bars
    
        """
        #get all strings that contain xxxH-xx-xx
        bar_text = self.filter_strings_with_pattern(text, r'\d+H\d+-\d+')
        bars = []
        for string in bar_text:
            # Split the string at the hyphen
            parts = string.split('-')
            bar_mark = parts[1]  # Extract the bar mark
            size = parts[0].split('H')[1]  # Extract the size
            quantity = parts[0].split('H')[0]  # Extract the quantity
            
            # Create a dictionary for the parsed values
            parsed_dict = {
                'bar_mark': bar_mark,
                'type': 'H',
                'size': int(size),
                'quantity': int(quantity)
            }
            bars.append(parsed_dict)
        return bars
        

    def filter_strings_with_pattern(self, string_list : str, pattern : str) -> list:
        """
        filter strings using regex pattern given\n

        Parameters
        ----------
        string_list : list of str
            The text to parse
        pattern : list of str
            The regex pattern to filter with

        Returns
        ----------
        list of str
            A list of filtered strings that exactly match the pattern
    
        """

        filtered_list = []
        for string in string_list:
            match = regex.search(pattern, string)
            if match:
                filtered_list.append(match.group())
        return filtered_list

    