import csv
from client import ClientData
from column import ColumnData
def load_csv_data(csv_file:str)->list[list]:

    """Return the list of list where 
    input
    csv_file: represente the csv_file

    output

    index[0] : represente the list of column name
    other[index] : represente the list of values or the line of csv file

    """
    
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
        # for key,value in data_list_to_return:
        #      keys=key
        #      values=value
        #      client_data=ClientData(keys)

    return data_list_to_return
