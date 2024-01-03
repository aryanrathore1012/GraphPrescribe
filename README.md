# ❄️ GraphPrescribe
Also known as ***"Cost-effective Digital Prescription using Pharmaceutical Knowledge Graph"*** is a AranongoDB-based knowledge graph containing comprehensive medication data. When provided with a prescription, the system efficiently analyzes the medicines and suggests reliable, cost-effective alternatives. 

* For instance, if the initial prescription costs 900 rupees for three medicines priced at 300 rupees each, the software identifies trustworthy substitutes priced at 100 rupees each, totaling 300 rupees. This results in substantial savings of 600 rupees for the user, maintaining reliability while significantly cutting costs.

* ***This is a group project made during  internship at AICOE JIO by Aryan Rathore and Reva Bharara*** under the careful guidance of our mentor ***Mr. Krishna Kumar Tiwari (head of knowledge graph platform at AICOE JIO platforms limited)***
* *This project is proof of concept and is at a prototyping phase*

## ❓Need of the application
***Having witnessed the financial strain caused by my father's battle with bone TB and the ensuing ICU expenses, I was motivated to create this project. We aim to help families in similar situations by providing cost-effective healthcare solutions. This software uses a medicine database to offer affordable alternatives, aiming to ease the financial burden while ensuring quality care for those facing substantial medical expenses.***

## 🔬 Research article

* Our work has been successfully been accepted and published in ***Asian Journal of Research in Computer Science***
* A PDF of the published paper has been attached on github and links are attached below
* https://www.researchgate.net/publication/376431111_Cost-effective_Digital_Prescription_using_Pharmaceutical_Knowledge_Graph
* https://journalajrcos.com/index.php/AJRCOS/article/view/395 
* DOI- 10.9734/ajrcos/2023/v16i4395


# 🏁 Result

* ***Finding a alternative medicine for 1 prescription***
![image](https://github.com/aryanrathore1012/calorie_tracker_ml/assets/91218998/c360bac6-7c8d-467b-a137-834b0114b0eb)

* ***The original prescription was Rs.2577 but GraphPrescribe found an alternative prescription of  Rs.114 saving 2463 Rs/-***
![image](https://github.com/aryanrathore1012/calorie_tracker_ml/assets/91218998/e2251486-a7d7-4638-b54a-eb7521b5d9d5)

![image](https://github.com/aryanrathore1012/calorie_tracker_ml/assets/91218998/98ff7670-4332-4b72-8ac3-b3c45cbaa145)

* Finding a alternative medicine for 1 medicine (Corex LS Sugar Free Syrup)
![image](https://github.com/aryanrathore1012/calorie_tracker_ml/assets/91218998/fce94bb5-57a9-4e20-b1a8-f0d7af479b7a)


![image](https://github.com/aryanrathore1012/calorie_tracker_ml/assets/91218998/87b59583-07fe-4271-b56e-6bc713f9c8d3)

***The original medicines was Rs.103 but GraphPrescribe found an alternative medicines named Ascoril LS Syrup which Rs.97 saving 6 Rs/-***

![image](https://github.com/aryanrathore1012/GraphPrescribe/assets/91218998/a84adc4f-731c-43e0-926f-8de2d48aa0a5)

* for Augmentin 625 Duo Tablet (original 452/- alternative 12/-)
![image](https://github.com/aryanrathore1012/calorie_tracker_ml/assets/91218998/ce01e53c-05d7-4fe1-990c-7c4c43eb8a2a)

* The medical_knowledge_graph formed
![image](https://github.com/aryanrathore1012/calorie_tracker_ml/assets/91218998/704a0f7b-b8bc-40b1-8a1a-dc5ba1d70527)

![image](https://github.com/aryanrathore1012/calorie_tracker_ml/assets/91218998/2415e35c-5958-41dc-a1af-6af6f859a388)

![image](https://github.com/aryanrathore1012/calorie_tracker_ml/assets/91218998/58560b57-0083-44d0-9b8d-7c795ebb0b67)

## 💽Prerequisites to understand the approach
#### 💡 What are knowledge graphs and how to build them? 

* The blog series attached is a 3-part series also made in our JIO internship. this will familiarize you with the concepts needed to understand the approach of this project.
* https://medium.com/everythingisconnected


### 📚 About the dataset

#### ***📕 a_to_z_medicine_data_web_scraping.csv***

* This csv contains all the info of the medicines.
* This dataset has 38074 rows where each row represents one medicine.

| # | Column            | Non-Null Count | Dtype |
|---| :------:            | :--------------: | :-----: |
| 0 | name              | 38074 non-null | object|
| 1 | manufacturer      | 38074 non-null | object|
| 2 | chemicals         | 38074 non-null | object|
| 3 | uses              | 38074 non-null | object|
| 4 | side_effects      | 38074 non-null | object|
| 5 | Habit Forming     | 38074 non-null | object|
| 6 | Therapeutic Class | 38074 non-null | object|
| 7 | Chemical Class    | 38074 non-null | object|
| 8 | Action Class      | 38074 non-null | object|
| 9 | MRP               | 38074 non-null | int64 |

![image](https://github.com/aryanrathore1012/GraphPrescribe/assets/91218998/becc9e11-071a-4b19-9e07-01882fd2f446)


# 🖋️ insights

![image](https://github.com/aryanrathore1012/GraphPrescribe/assets/91218998/69c1bdf8-f541-419e-bef0-00766ea29ae2)

![image](https://github.com/aryanrathore1012/GraphPrescribe/assets/91218998/0d31f771-c5c4-4f7c-84b9-0237c0526e26)

![image](https://github.com/aryanrathore1012/GraphPrescribe/assets/91218998/8310a660-08fb-40b3-b6c8-e2d91c41a1cf)

![image](https://github.com/aryanrathore1012/GraphPrescribe/assets/91218998/5553b6c1-449b-4ac3-8778-5075c90ba4ec)

![image](https://github.com/aryanrathore1012/GraphPrescribe/assets/91218998/631be179-e93e-4c8c-a5e6-3e5ba91dbf71)

# 🛣️ Roadmap of the project

#### **🌐 1_medicine_data_web_scraping.ipynb**

* Objective: The primary goal of this notebook is to execute web-scraping procedures on publicly accessible medicine websites.

* Data Collection: Utilize web-scraping techniques to extract relevant data from diverse public medicine websites.

* Dataset Creation: Compile the extracted information into a comprehensive medicine dataset.

* Saved Dataset: The Compile data was stored in the a_to_z_medicine_data_web_scraping.csv

![image](https://github.com/aryanrathore1012/calorie_tracker_ml/assets/91218998/91ab9b72-9dd6-4a7d-99cf-ee705a9e2b42)

#### ***🛠️ 2_medicine_data_statistics_insights.ipynb***

- **Objective**: This notebook aims to conduct Preliminary, Exploratory data analysis and extract meaningful insights from the gathered medicine dataset before integrating it into the knowledge graph.

- The insights have been attached above.

#### ***🕸️ 3_main_graph_creation.ipynb***

* **Objective**: The primary objective of this notebook is to construct a knowledge graph of medicines. This graph will serve the purpose of identifying medicine replacements and uncovering hidden insights within the dataset

* Data Acquisition: Read data from the "a_to_z_medicine_data_web_scraping.csv" file containing medicine information.

* Database Setup: Create the "drug_repurposing_3" database on ArangoDB and upload columns as collections.

* Graph Construction: Construct edge collections and upload the remaining dataset, organizing them as edges in the knowledge graph.

![image](https://github.com/aryanrathore1012/GraphPrescribe/assets/91218998/c35340d3-5a3b-4b60-a068-f08fe36d5e67)

![image](https://github.com/aryanrathore1012/calorie_tracker_ml/assets/91218998/cde73d31-7a61-4c2f-8e89-18e0778ca52b)

#### ***💊 4_graph_queries_medical_kg.ipynb***
* **Objective**: using qraph aql and a medicine name find an alternative maedicine with a lower cost
![image](https://github.com/aryanrathore1012/calorie_tracker_ml/assets/91218998/fa64b85c-cc89-4c3d-b631-d53729565386)
#### ***🗔 5_final_prescription_test.py***

* **Objective**: given a prescription of medicines find alternative medicines that are lower in cost and show the comparision graph
* **TO DO**: add proper GUI to this code


# 🔜 future ugrades

* The project as of now is just a proof of concept so i does not has proper website or GUI.
* Only 38k~ medicines have been added for this to be functional we will need to add more medicines
* Special filters for paitents with medical conditions like sugar, BP or pregnancy need to be added
* Make a project of the idea rather than a proof of concept.

# 👥credits and contact info:-

* 🧑‍🏫 ***Krishna Kumar Tiwari***
* email: krishna.tiwari@ril.com
* LinkedIn : https://www.linkedin.com/in/agentkk/
* 👨***Aryan Rathore***
* LinkedIn : https://www.linkedin.com/in/aryan-rathore-b15459215/
* email: aryanrathore13572002@gmail.com, aryan.rathore2021@vitbhopal.ac.in
* 👩 ***Reva Bharara***
* email: bhararareva@gmail.com, revabharara@gmail.com
* LinkedIn : https://www.linkedin.com/in/reva-bharara-a83a78241/



