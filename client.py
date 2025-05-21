from dataclasses import dataclass,field
from column import ColumnData
import csv
import json
@dataclass
class ClientData:
    column:list
    dimension:tuple
    columns_data:dict=field(default_factory=dict)

    def get_csv_colum_by_name(self,name):
        try:
            dict_for_given_name={self.columns_data[name].nom:self.columns_data[name].data}
        except Exception as err:
            print(f"Erreur : {err}")
        else:
            return dict_for_given_name
    
    def get_csv_line_by_index(self,index):
        data_match_by_given_index=[]
        for values in self.columns_data.values():
           data_match_by_given_index.append(values.data[index-1])
        return data_match_by_given_index
    def get_stasts(self):
        pass

    def save_data(self,format:str):
        if format=="json":
            with open("client_data.json",mode="a") as file: 
                json.dump(self.to_dict(),file)
        elif format=="csv":
            data_colums_values=self.columns_data
            csv_header=[]
            csv_data=[]
            csv_content=[]
            for key,value in data_colums_values.items():
                csv_header.append(key)
                csv_content.append(value.data)
            csv_data=[list(client) for client in zip(*csv_content)]
            with open("client_data.csv",mode="a") as file:
                writer=csv.writer(file)
                writer.writerow(csv_header)
                writer.writerows(csv_data)

    def to_dict(self):
        return{
            "column":self.column,
            "dimension":list(self.dimension),
            "columns_data":{
                key:col.to_dict() for key,col in self.columns_data.items()
            }
        }