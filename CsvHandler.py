import csv

class CsvHandler:
    """
    A class which handles manipulation of CSV files (read and write)

    """
    def __init__(self):
        pass

    def dict_list_to_csv(self, list_to_csv, keys = None, csv_file_path = "output.csv"):
        """
        Outputs a list of dicts to a csv file

        Parameters
        ----------
        list_to_csv : list of dicts
            The list of dictionaries to save
        keys : list of str, optional
            The keys to save
        csv_file_path : string, optional
            The path to the CSV file save location
    
        """
        if keys == None:
            keys = list_to_csv[0].keys() # get all keys if none given
            print(keys)

        with open(csv_file_path, 'w', newline='') as output_file: # output to file
            dict_writer = csv.DictWriter(output_file, fieldnames = keys)
            dict_writer.writeheader()
            for row in list_to_csv:
                    dict_writer.writerow({field: row[field] for field in keys})


    def csv_to_dict_list(self, csv_file_path):
        """
        Reads in a csv file to a list of dicts

        Parameters
        ----------
        csv_file_path : string,
            The path to the CSV file 
        
        Returns
        ----------
        data : list of dicts
            A list of dicts read in from file
    
        """

        filename = csv_file_path 
        data = []  # List to store the dictionaries

        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(dict(row))

        return data
