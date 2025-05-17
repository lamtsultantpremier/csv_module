from dataclasses import dataclass,field
from column import ColumnData
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
        pass