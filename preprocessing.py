from client import ClientData
def process_data(client_data:ClientData)->ClientData:
    pass

def convert_month_to_number(client_data)->ClientData:
    months=["January","February","March","April","May","June","July","August","September","October","November","December"]
    month_with_three_letters={}
    for i in range(len(months)):
        month_with_three_letter=months[i][0:3].lower()
        month_with_three_letters[month_with_three_letter]=i+1
    months_come_to_column_data=list(client_data.columns_data["month"].data)
    month_converted_to_numeric=[month_with_three_letters[m] for m in months_come_to_column_data]
    client_data.columns_data["month"].data=month_converted_to_numeric
    return client_data

def convert_pdays_to_minus_one(client_data:ClientData)->ClientData:
    tuple_to_change_number=client_data.columns_data["pdays"].data
    for i in range(len(tuple_to_change_number)):
        if type(tuple_to_change_number)!=list:
            tuple_to_change_number=list(tuple_to_change_number)
            if tuple_to_change_number[i]==999:
                tuple_to_change_number[i]=-1
    client_data.columns_data["pdays"].data=tuple(tuple_to_change_number)
    return client_data

    
def convert_column_data_data_item_to_int(client_data:ClientData,column_name):
    try:
        tuple_to_convert=client_data.columns_data[column_name].data
        if type(tuple_to_convert)!=list:
            tuple_to_convert=list(tuple_to_convert)
            tuple_to_convert=map(int,tuple_to_convert)
            client_data.columns_data[column_name].data=tuple(tuple_to_convert)
            client_data.columns_data[column_name].data_type=int
        return client_data
    except KeyError as k:
        print(f"Erreur : {k=} {k.args}")
