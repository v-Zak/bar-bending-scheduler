from DxfHandler import DxfHandler 
from LabelParser import LabelParser
from BarHandler import BarHandler

if __name__ == "__main__":
    dxf_handler = DxfHandler()   
    all_text = dxf_handler.get_all_mtext_text("tests/dxf_samples/text_test_3.dxf") # get text
    
    label_parser = LabelParser()
    bars = label_parser.get_bars(all_text) # get bars as dicts

    bar_handler = BarHandler()
    bars_unique = bar_handler.get_bar_set(bars) # get unique set of bar marks
    bars_summed = bar_handler.sum_quantities(bars_unique) # get the bbs formatted set
    print(bars_unique) # need to make deep copy in sum function so this doesn't change 
    print(bars_summed)



