from dataclasses import dataclass
import statistics
@dataclass
class ColumnData:
    nom:str
    data:list
    data_type:None

    def unique(self)->set:
        self.data=set(self.data)
        return self.data
    
    def value_counts(self):
        dict_for_occurence_values={value:self.data.count(value) for value in self.data}
        return dict_for_occurence_values
    def get_column_state(self):
        if self.data_type==int:
            moyenne=statistics.mean(self.data)
            count=len(self.data)
            somme=sum(self.data)
            median=statistics.median(self.data)
            mode=statistics.mode(self.data)
            minimum=min(self.data)
            maximum=max(self.data)
            etendu=maximum-minimum
            variance=statistics.variance(self.data)
            return {

                "moyenne":moyenne,
                "taille":count,
                "somme":somme,
                "median":median,
                "mode":mode,
                "minimum":minimum,
                "maximum":maximum,
                "etendu":etendu,
                "variance":variance
            }
        elif self.data_type==str:
           count=len(self.data)
           mode=statistics.mode(self.data)
           unique_value=[value for value in self.data if self.data.count(value)==1]
           frequence={value:self.data.count(value) for value in self.data}
           return{
               "taille":count,
               "mode":mode,
               "frequence":frequence,
               "unique-value":unique_value
           }
        
    def to_dict(self):
        return{
            "nom":self.nom,
            "data":list(self.data),
            "type":self.data_type.__name__
        }
