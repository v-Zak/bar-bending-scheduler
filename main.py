from DxfHandler import DxfHandler 
from LabelParser import LabelParser
from BarHandler import BarHandler
from CsvHandler import CsvHandler
from BarBendingScheduler import BarBendingScheduler

if __name__ == "__main__":

    #dxf_path = input("Enter a DXF File Path (include .dxf): ")
    dxf_path = "tests/dxf_samples/text_test_3.dxf"

    bbs = BarBendingScheduler()
    bbs.createBarQuantitiesCsv(dxf_path)





