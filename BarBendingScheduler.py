from DxfHandler import DxfHandler 
from LabelParser import LabelParser
from BarHandler import BarHandler
from CsvHandler import CsvHandler
from Logger import Logger

class BarBendingScheduler:
    """
    A class which handles the creation of a BBS (CSV) based on a given DXF file

    """
    def __init__(self, logger : Logger):
        self.logger = logger
    
    def createBarQuantitiesCsv(self, dxf_path, csv_path = None):
        """
        creates a BBS in CSV format based on a given DXF file\n
        if {dxf_path} is within csv_path its replaces with the DXF full path

        Parameters
        ----------
        dxf_path : string
            The path to the DXF to read
        csv_path : string
            The path to save the CSV (default is '{dxf_path}-BBS-output.csv')
    
        """
        try:
            if csv_path == None:            
                csv_path = dxf_path[0:-4] + '-BBS-output.csv'
            else:
                csv_path = csv_path.replace("{dxf_path}", dxf_path[0:-4])
            
            
            self.logger.inputLog('Reading...')
            dxf_handler = DxfHandler(self.logger)   
            all_text = dxf_handler.get_all_mtext_text(dxf_path) # get text

            if len(all_text) == 0:
                raise("No MTEXT variables found in model space")

            self.logger.inputLog('Parsing...')
            label_parser = LabelParser()
            bars = label_parser.get_bars(all_text) # get bars as dicts

            if len(bars) == 0:
                raise("No Bars found in model space MTEXT")

            self.logger.inputLog('Creating Bars...')
            bar_handler = BarHandler()
            bars_unique = bar_handler.get_bar_set(bars) # get unique set of bar marks
            bars_summed = bar_handler.sum_quantities(bars_unique) # get the bbs formatted set

            self.logger.inputLog('Exporting...')
            csv_handler = CsvHandler(self.logger)
            csv_handler.dict_list_to_csv(   list_to_csv = bars_summed, 
                                            keys = [   'bar_mark', 'type', 
                                                    'size', 'number_of_members',
                                                    'number_of_bars_in_each'
                                                ],
                                            csv_file_path = csv_path)

            self.logger.inputLog('Done...')
            self.logger.inputLog(f'File saved to: {csv_path}')
        except Exception as err:
            self.logger.inputLog(str(err))
