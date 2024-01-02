'''
    # 5
        Goal : given a prescription of medicines in this case ["Augmentin 625 Duo Tablet", "Bignac SP Tablet", "Doxypen 100 Capsule", "Azithral 500 Tablet", "ZX 200 DT Tablet", "Xomet 10mg Tablet", "Vesbal 24 Tablet"]
        find alternative medicines that are lower in cost and show the comparision graph

    # TO DO: add proper GUI to this code
    # By - Aryan rathore (backend), Reva bharara (GUI)

'''

import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from arango import ArangoClient
import matplotlib as mlp

client=ArangoClient(hosts="http://localhost:8529/")
med_db=client.db(name="drug_repurposing_3" , username="root", password="")

def make_graph(medicine_name, medicine_price):
    cursor=med_db.aql.execute(f'for med in Medicine filter med.name=="{medicine_name}" return med._id')

    medicine_id=str
    for med_id in cursor:
        medicine_id=med_id

    cursor=med_db.aql.execute(f'for v,e in 1..1 outbound "{medicine_id}" graph drug_kg_approach_3_ filter IS_SAME_COLLECTION("has_chemical",e) return {{"chemical":v._id, "concentration": e.weight}}')
    med_composition=pd.DataFrame(cursor)
    
    chem_dataframes={}
    for i in range(len(med_composition)):
        cursor=med_db.aql.execute(f'for v,e in 1..1 inbound "{med_composition.iloc[i,0]}" graph drug_kg_approach_3_ filter IS_SAME_COLLECTION("has_chemical",e) and e.weight=="{med_composition.iloc[i,1]}" return {{"medicine":v._id, "concentration": e.weight}}')
        chem_dataframes[f"chem{i+1}"]=pd.DataFrame(cursor)

    intersection = set(chem_dataframes['chem1'].medicine)
    for chem_df in chem_dataframes.values():
        intersection=intersection&set(chem_df.medicine)

    for i in intersection:
        cursor=med_db.aql.execute(f'let data = (for v,e in 1..1 outbound "{i}" graph drug_kg_approach_3_ filter IS_SAME_COLLECTION("has_chemical",e) return {{"chemical":v._id, "concentration": e.weight}})return length(data)')
    
    alt_medicine=[]
    for i in intersection:
        cursor=med_db.aql.execute(f'let data = (for v,e in 1..1 outbound "{i}" graph drug_kg_approach_3_ filter IS_SAME_COLLECTION("has_chemical",e) return {{"chemical":v._id, "concentration": e.weight}})return length(data)')
        for j in cursor:
            if j==len(med_composition):
                alt_medicine.append(i)

    alt_med_lst=list()
    for medicine in alt_medicine:
        cursor=med_db.aql.execute(f"return document('{medicine}')")
        for i in cursor:
            alt_med_lst.append(i)
        
    alt_med_price_df=pd.DataFrame(alt_med_lst)   
    alt_med_price_df.drop(columns=['_key','_rev'], inplace=True)
    alt_med_price_df.set_index('_id', inplace=True)

    filter_price=alt_med_price_df['MRP']<alt_med_price_df.loc[medicine_id,'MRP']
    alt_med_price_df=alt_med_price_df.loc[filter_price]

    alt_med_name=[]
    for med in alt_medicine:
        cursor=med_db.aql.execute(f"return document('{med}').name")
        for m in cursor:    
            alt_med_name.append(m)

    alt_med_name_less_price=alt_med_price_df[['name',"MRP"]].sort_values("MRP")
    alt_med_name_less_price = alt_med_name_less_price.iloc[0:1]

    alt_name = alt_med_name_less_price.iloc[0, 0]
    alt_mrp = alt_med_name_less_price.iloc[0,1]
    print(f"{medicine_name}, ({medicine_price}) Rs./- has the alternate medicine: {alt_name}, price: ({alt_mrp}) Rs./-")

    return alt_mrp

alternate_prices = []
medicine_names = ["Augmentin 625 Duo Tablet", "Bignac SP Tablet", "Doxypen 100 Capsule", "Azithral 500 Tablet", "ZX 200 DT Tablet", "Xomet 10mg Tablet", "Vesbal 24 Tablet"]
medicine_prices = [452, 415, 469, 105, 237, 459, 440]
for i in range(len(medicine_names)):
    alt_mrp = make_graph(medicine_names[i], medicine_prices[i])
    alternate_prices.append(alt_mrp)
    
print(alternate_prices)

plt.style.use("seaborn-dark")

for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
    plt.rcParams[param] = '#212946'  # bluish dark greyfor param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
    plt.rcParams[param] = '0.9'  # very light greyax.grid(color='#2A3459')

alternate_prices = [12, 12, 14, 10, 15, 49, 12]
medicine_names = ["Augmentin 625 Duo Tablet", "Bignac SP Tablet", "Doxypen 100 Capsule", 
                  "Azithral 500 Tablet", "ZX 200 DT Tablet", "Xomet 10mg Tablet", "Vesbal 24 Tablet"]
medicine_prices = [452, 415, 469, 105, 237, 459, 440]

font = {'family' : 'DejaVu Sans',
        'weight' : 'bold',
        'size'   : 12}

mlp.rc('font', **font)

plt.plot(medicine_names, medicine_prices,color='green',marker="o",linestyle="--",label="original price") # makes the line graph but dosent acutally show it


plt.plot(medicine_names, alternate_prices, color='red',marker="o",linestyle="--", label="alternate price")

plt.title("original medicine price vs alternate medicine price comparision") 
plt.xticks(rotation = 90)
plt.ylabel("count")
plt.grid(True)
plt.legend()
plt.show()

# By - Aryan rathore (backend), Reva bharara (GUI)