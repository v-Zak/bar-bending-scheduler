import ezdxf
import sys
from Logger import Logger

class DxfHandler:
    """
    A class which handles manipulation of DXF files (read and write)

    """
    def __init__(self, logger : Logger):
        self.logger = logger

    def get_all_mtext(self, dxf_file_path):
        """
        Get all the mtext entities within a dxf file

        Parameters
        ----------
        dxf_file_path : string
            The path to the DXF file

        Returns
        ----------
        exdxf.query.EntityQuery
            A group of all mtext components found in modelspace
    
        """
        # open the file
        try:
            doc = ezdxf.readfile(dxf_file_path)
        except IOError as err:
            self.logger.inputLog(f"Not a DXF file or a generic I/O error:")
            self.logger.inputLog(dxf_file_path)
            raise(err)
        except ezdxf.DXFStructureError as err:
            self.logger.inputLog(f"Invalid or corrupted DXF file:")
            self.logger.inputLog(dxf_file_path)
            raise(err)
        
        # get all text in modelspace
        model_space = doc.modelspace()
        mtext = model_space.query("MTEXT")

        return mtext

    def get_all_mtext_text(self, dxf_file_path):
        """
        Get all the text attributes of any mtext entities within a dxf file
        (all text including formatting returned)

        Parameters
        ----------
        dxf_file_path : string
            The path to the DXF file

        Returns
        ----------
        list of str
            A list of all the text found in modelspace
    
        """
        mtext = self.get_all_mtext(dxf_file_path)

        text_contents = list(map(self.get_text_att, mtext))
        
        return text_contents

    def get_text_att(self, mtext):
        """
        Get the text attribute of a mtext entity

        Parameters
        ----------
        mtext : ezdxf.entities.mtext.MText
            The mtext entity

        Returns
        ----------
        string
            The mtext text contents
    
        """
        return mtext.text