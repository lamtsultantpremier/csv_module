from dataclasses import dataclass

@dataclass
class ColumnData:
    nom:str
    data:list
    data_type:None

    def unique(self)->tuple:
        data_unique=list(tuple(self.data))
        return data_unique
    
    def value_counts(self):
        dict_for_occurence_values={}
        for value in self.data:
            dict_for_occurence_values[value]=self.data.count(value)
            return dict_for_occurence_values
