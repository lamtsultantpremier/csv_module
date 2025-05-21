import csv
from client import ClientData
from column import ColumnData
from preprocessing import *
def load_csv_data(csv_file:str)->ClientData:

    """Retourne la liste de tous les clients,toutes les colonnes ainsi que la dimension des données contenues dans le fichier csv"""
    
    with open(csv_file,newline='') as csvfile:
        spamread=csv.reader(csvfile)
        csv_data=[]
        for row in spamread:
            csv_data.append(row) 
        column_names=csv_data.pop(0)
        column_values=csv_data
        dimension=(len(column_values),len(column_names))
        transpose_data=list(zip(*column_values))
        column_name_to_values=dict(list(zip(column_names,(transpose_data))))
        client_data=ClientData(column_names,dimension)
        for key,value in column_name_to_values.items():
             client_data.columns_data[key]=ColumnData(key,value,type(value[0]))
        # client_data=convert_pdays_to_minus_one(client_data)
        # client_data=convert_column_data_data_item_to_int(client_data,"age")
        # client_data=convert_column_data_data_item_to_int(client_data,"day")
        # client_data=convert_column_data_data_item_to_int(client_data,"pdays")
        # client_data=convert_column_data_data_item_to_int(client_data,"balance")
        # client_data=convert_column_data_data_item_to_int(client_data,"duration")
        # client_data=convert_column_data_data_item_to_int(client_data,"campaign")
        # client_data=convert_column_data_data_item_to_int(client_data,"previous")
    return client_data

def convert_to_int(value:tuple)->tuple:

    data_list_to_return=[]
    for value in value:
        data_list=[]
        for item in value:
                try:
                     data_list.append(int(value))
                except (ValueError,TypeError):
                    data_list.append(value)
        data_list_to_return.append(tuple(data_list))
    return data_list_to_return


     
