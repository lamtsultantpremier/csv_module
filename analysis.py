from client import ClientData
from preprocessing import *
def sorted_client_by_age(clientdata:ClientData)->list[ClientData]:
    all_clients_informations=[]
    list_clients=[]
    for value in clientdata.columns_data.values():
        list_clients.append(list(value.data))
    all_clients_informations=list(zip(*list_clients))
    all_clients_informations_soted_by_age=sorted(all_clients_informations,key=lambda x:x[0])
    return all_clients_informations_soted_by_age

def most_common_job(client_data:ClientData)->dict:
    dict_of_job_occurence={}
    list_of_client_jobs=list(client_data.columns_data["job"].data)
    dict_of_job_occurence={job:list_of_client_jobs.count(job) for job in list_of_client_jobs}
    dict_of_job_occurence=dict(sorted(dict_of_job_occurence.items(),key=lambda x:x[1],reverse=True))
    return dict_of_job_occurence

def filter_by_max_or_min_age(client_data:ClientData,min_age:int=0,max_age:int=100)->list[tuple]:
    client_data=convert_column_data_data_item_to_int(client_data,"age")
    all_clients_informations=[]
    list_clients=[]
    for value in client_data.columns_data.values():
        list_clients.append(list(value.data))
    all_clients_informations=list(zip(*list_clients))
    all_clients_informations_filter_by_age=[client for client in all_clients_informations if min_age<=client[0]<=max_age]
    return all_clients_informations_filter_by_age

def calculate_subscription_rate(client_data:ClientData)->dict:
    list_of_all_subscription_or_not=client_data.columns_data["y"].data
    dict_of_subscriptions={subscription:list_of_all_subscription_or_not.count(subscription) for subscription in list_of_all_subscription_or_not}
    return dict_of_subscriptions
    



