

class BarHandler:
    """
    A class which handles the creation of Bar Dicts

    """
    def __init__(self):
        pass
    
    def get_bar_set(self, bars):
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