

class BarHandler:
    """
    A class which handles the creation of Bar Dicts

    """
    def __init__(self):
        pass

    def get_bar_set(self, bars):
        """
        return a unique set of bars with the quantities stored as a list

        Parameters
        ----------
        bars : list of bar dicts
            The bars list containing duplicate bar marks

        Returns
        ----------
        bar_set 
            A list of unique bars with their updated quantities
    
        """
        bar_set = []
        for bar in bars:  
            added = False      
            for unique_bar in bar_set:
                if bar['bar_mark'] == unique_bar['bar_mark'] and bar['size'] == unique_bar['size']: # bar already in set
                        unique_bar['quantity'].append(bar['quantity']) # add quantity to quantity list
                        added = True
            if not added:
                formatted_bar = { 
                'bar_mark': bar['bar_mark'],
                'type': bar['type'],
                'size': bar['size'],
                'quantity': [bar['quantity']], # list of quantities
                }
                bar_set.append(formatted_bar)    
        return bar_set
    

    def sum_quantities(bar_set):
        """
        Sum up each bars' quantities list into No. of Mbars, No. of bars in each\n
        i.e [8,8] = 2, 8 or [8,16] = 1, 24

        Parameters
        ----------
        bars : list of unique bars
            The bars list containing quantity list

        Returns
        ----------
        bar_set_formatted
            A list of unique bars with 'number_of_members' and 'number_of_bars_in_each', rather than a list of 'quantities'

        """

        raise NotImplementedError("This function is not implemented yet")