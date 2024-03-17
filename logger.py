from datetime import datetime
import os

class TheLogger:

    def __init__(self, name_with_extention, destination_folder):
        self.filename = name_with_extention
        self.destination_folder = destination_folder
       

    def write_on_log_and_console(self, message):   
        timestamp = datetime.now().strftime("%Y-%m-%d || %H:%M:%S")
        try:
            with open(self.destination_folder+self.filename, 'a') as file:
                file.write(timestamp+' - '+message+'\n')
                print(timestamp+' - '+message+'\n')
        except FileNotFoundError or FileExistsError:
            with open(self.destination_folder+self.filename,'w') as file:
                file.write(timestamp+' - '+message+'\n')
                print(timestamp+' - '+message+'\n')
        except IOError:
            print(f"{timestamp} - Error: Unable to write to file: {self.filename}" + 
                   " folder: {self.destination_folder}")
        
    