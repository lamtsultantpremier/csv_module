from loader import load_csv_data
from preprocessing import *
from analysis import *
import json

print("Bienvenue sur l'application de Manipulation de fichier CSV")
print("Choisissez une option")

client_data=None
choice_for_continue="o"
while choice_for_continue=="o" or choice_for_continue=="O":
        print("1- Charger le le fichier contenant les données du csv sous forme data")
        print("2- Effectuer des pretraitement sur les données")
        print("3- pretraitrement sur les données")
        print("4- Fonction d'analyse")
        choice=int(input("Fais un choix : "))
        if choice==1:
            client_data=load_csv_data("bank.csv")
            print(client_data)
            print("Voulez vous effectuer une autre action o/n")
            choice_for_operation=input("o/n")
            if choice_for_operation=="o":
                continue
            else:
                break
        if choice==2:
            client_data=load_csv_data("bank.csv")
            print("1 Obtenir une colonne colonne du csv à partir de son nom")
            print("2 Obtenir une ligne du csv à partir de son index")
            print("3 Otenir des statistique sur une colonne donnée")
            print("4 Sauvegarder les données dans un fichier")
            print("5- Obtenir les valeurs unique de chaque colonne")
            print("6- Obtenir le nombre de d'occurence de chaque valeurs dans une colonne")
            choice=int(input('Entere le numero e votre opération : '))
        try:    
            if choice==1:
                print("Entrer le nom de la colonne que vous souhaitiez obtenir")
                print(f"La Liste de toutes les colonnes {client_data.column}")
 
                column_choice_name=input("Nom de la colonne: ")
                dict_for_given_data=client_data.get_csv_colum_by_name(column_choice_name)
                print(dict_for_given_data)

            if choice==2:
                print(f"Dimension des données : (ligne,colonne) => {client_data.dimension}")
                index_choice=int(input("Numero de la ligne : "))
                data_match_by_given_index=client_data.get_csv_line_by_index(index_choice)
                print(f"Information du client : {data_match_by_given_index}")
        
            if choice==3:
                print("3 Otenir des statistique sur une colonne donnée")
                client_data=convert_column_data_data_item_to_int(client_data,"age")
                client_data=convert_column_data_data_item_to_int(client_data,"balance")
                client_data=convert_column_data_data_item_to_int(client_data,"day")
                client_data=convert_column_data_data_item_to_int(client_data,"duration")
                client_data=convert_column_data_data_item_to_int(client_data,"previous")
                client_data=convert_column_data_data_item_to_int(client_data,"pdays")
                client_data=convert_column_data_data_item_to_int(client_data,"campaign")
                for key in client_data.columns_data.keys():
                    print({key:(client_data.columns_data[key].get_column_state())})
            if choice==4:
                print("Sauvegarde de la class ClienData dans un fichier client_informations.json")
                print("4 Sauvegarder les données dans un fichier")

                client_data=convert_column_data_data_item_to_int(client_data,"age")
                client_data=convert_column_data_data_item_to_int(client_data,"balance")
                client_data=convert_column_data_data_item_to_int(client_data,"day")
                client_data=convert_column_data_data_item_to_int(client_data,"duration")
                client_data=convert_column_data_data_item_to_int(client_data,"previous")
                client_data=convert_column_data_data_item_to_int(client_data,"pdays")
                client_data=convert_column_data_data_item_to_int(client_data,"campaign")
                client_data=convert_month_to_number(client_data)
                client_data=convert_pdays_to_minus_one(client_data)
                print("Quel format souheteriez vous")
                format_choice=input("csv/json : ")
                client_data.save_data(format_choice)
                print("Appuiez sur oui(o) ou non(n) pour avoir les différente Statistique")
                statistic_choice=input("o/n")
                if statistic_choice=="o" or statistic_choice=="O":
                    dat_stats=[]
                    for key,value in client_data.columns_data.items():
                        dat_stats.append({key:value.get_column_state()})
                        with open("statics.json","a",newline="") as file:
                            json.dump(dat_stats,file,indent=1)
            if choice==5:
                client_data=convert_column_data_data_item_to_int(client_data,"age")
                client_data=convert_column_data_data_item_to_int(client_data,"balance")
                client_data=convert_column_data_data_item_to_int(client_data,"day")
                client_data=convert_column_data_data_item_to_int(client_data,"duration")
                client_data=convert_column_data_data_item_to_int(client_data,"previous")
                client_data=convert_column_data_data_item_to_int(client_data,"pdays")
                client_data=convert_column_data_data_item_to_int(client_data,"campaign")
                print("Liste des valeurs unique de chaque colonne")
                for key1 in client_data.columns_data.keys():
                    for key2,value in client_data.columns_data.items():
                        if key1==key2:
                            print({key2:client_data.columns_data[key2].unique()})
            if choice==6:
                client_data=convert_column_data_data_item_to_int(client_data,"age")
                client_data=convert_column_data_data_item_to_int(client_data,"balance")
                client_data=convert_column_data_data_item_to_int(client_data,"day")
                client_data=convert_column_data_data_item_to_int(client_data,"duration")
                client_data=convert_column_data_data_item_to_int(client_data,"previous")
                client_data=convert_column_data_data_item_to_int(client_data,"pdays")
                client_data=convert_column_data_data_item_to_int(client_data,"campaign")
                for key1 in client_data.columns_data.keys():
                    print(f"{key1} => {client_data.columns_data[key1].value_counts()}")
        except Exception as err:
            print(f"Erreur : {err.args} {TypeError(err)}")

        if choice==3:
            client_data=load_csv_data("bank.csv")
            print("1 Convertir la colonne Month en Numérique")
            print("2 Remplacer pdays 999->-1")
            print("3 Supprimer les lignes ayant plus de 10 valeurs manquantes")
            print("")
            choice=int(input("Entrer le numero de l'opération : "))

            try:
                if choice==1:
                    print(f"Colonne de départ sous forme de chaîne :{list(client_data.columns_data["month"].data)[0:5]}......")
                    print(f"Colonne convertie : {list(convert_month_to_number(client_data).columns_data["month"].data)[0:5]}.....")
        
                if choice==2:
                    print("Remplacement de pdays 999=>-1")
                    convert_pdays_to_minus_one(client_data)
                    print(f"{list(client_data.columns_data["pdays"].data)[0:9]}.....")
                if choice==3:
                    print("Suppression des lignes avec 10 valeurs manquantes")
            except Exception as err:
                print(f"Erreur : {err.args} {TypeError(err)}") 

        if choice==4:
            client_data=load_csv_data("bank.csv")
            print("1- Filtrer les clients par âge")
            print("2- Calculer le Pourcentage de client ayant souscrit")
            print("3- Trouve le métier le plus fréquent")
            choice_for_analyse_operation=int(input("Entrer le numero de l'opération : "))
            if choice_for_analyse_operation==1:
                min_age=int(input("Entrer l'age minimum : "))
                max_age=int(input("Entrer l'age max : "))

                if min_age!=0 and max_age!=0:
                    print(f"Les clients qui ont un âge compris entre {min_age} et {max_age}")
                    all_clients_filter=filter_by_max_or_min_age(client_data,min_age,max_age)
                    for i in range(5):
                        print(f"{i+1}- {all_clients_filter[i]}")
                else:
                    all_clients_filter=filter_by_max_or_min_age(client_data)
                    for i in range(5):
                        print(all_clients_filter[i])

            if choice_for_analyse_operation==2:
                print("2- Calculer le Pourcentage de client ayant souscrit")
                dict_of_subscriptions=calculate_subscription_rate(client_data)
                number_of_no_subscription=dict_of_subscriptions["no"]
                number_of_subscription=dict_of_subscriptions["yes"]
                number_of_adherant=number_of_no_subscription+number_of_subscription
                new_dict_of_scription={}
                new_dict_of_scription["souscrit"]=number_of_subscription
                new_dict_of_scription["non-souscrit"]=number_of_no_subscription
                print(f"Le nombres d'adhérents : {new_dict_of_scription}")
                print(f"Pourcentage de souscription : {round((number_of_subscription/number_of_adherant)*100,3)} %")

            if choice_for_analyse_operation==3:
                print("3- Trouve le métier le plus fréquent")

                dict_for_common_jobs=most_common_job(client_data)
                dict_for_jobs=[job for job in zip(dict_for_common_jobs.keys(),dict_for_common_jobs.values())]
                print("liste des metiers les plus exercer par ordre decroissant")
                print(dict_for_common_jobs)
                print("")
                print(f"Le métier le plus exercer : {dict_for_jobs[0]}")

        print("Voulez vous continuer Oui/o ou non/n")
        choice_for_continue=input("o/n : ")
        if choice_for_continue=="o" or choice_for_continue=="O":
            continue
        else:
            break


