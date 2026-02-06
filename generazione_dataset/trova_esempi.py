#definizione funzione trova_esempi ---> trovo gli esempi degli essay scritti nel primo anno
import pandas as pd
import xml.etree.ElementTree as ET


df= pd.read_csv("data\\LangLearn_Training_Data\\Training_CItA.tsv", sep= "\t")

filtro = df["Order_1"].str.startswith("1_") | df["Order_2"].str.startswith("1_")
df_filtrato = df[filtro]

#essay 1_1

lista1_1= []
for index, row in df_filtrato.iterrows():
    if "1_1" in row["Order_1"]:
        lista1_1.append(row["Essay_1"])
set1_1= set(lista1_1) #len=104


#essay 1_2

lista1_2= []

for index, row in df_filtrato.iterrows():
    if "1_2" in row["Order_1"]:
        lista1_2.append(row["Essay_1"])
    elif "1_2" in row["Order_2"]:
        lista1_2.append(row["Essay_2"])
set1_2= set(lista1_2) #len=102



#essay1_3
lista1_3= []

for index, row in df_filtrato.iterrows():
    if "1_3" in row["Order_1"]:
        lista1_3.append(row["Essay_1"])
    elif "1_3" in row["Order_2"]:
        lista1_3.append(row["Essay_2"])
set1_3= set(lista1_3) #len=45



#essay 1_4
lista1_4= []

for index, row in df_filtrato.iterrows():
    if "1_4" in row["Order_1"]:
        lista1_4.append(row["Essay_1"])
    elif "1_4" in row["Order_2"]:
        lista1_4.append(row["Essay_2"])
set1_4= set(lista1_4) #len=64



#essay 1_5
lista1_5= []

for index, row in df_filtrato.iterrows():
    if "1_5" in row["Order_1"]:
        lista1_5.append(row["Essay_1"])
    elif "1_5" in row["Order_2"]:
        lista1_5.append(row["Essay_2"])
set1_5= set(lista1_5) #len=69


#essay 1_6
lista1_6= []

for index, row in df_filtrato.iterrows():
    if "1_6" in row["Order_1"]:
        lista1_6.append(row["Essay_1"])
    elif "1_6" in row["Order_2"]:
        lista1_6.append(row["Essay_2"])
set1_6= set(lista1_6) #len= 20




df= pd.read_csv("data\\LangLearn_Training_Data\\Training_CItA.tsv", sep= "\t")

filtro2 = df["Order_1"].str.startswith("2_") | df["Order_2"].str.startswith("2_")
df_filtrato2 = df[filtro2]


#essay 2_1

lista2_1= []

for index, row in df_filtrato2.iterrows():
    if "2_1" in row["Order_1"]:
        lista2_1.append(row["Essay_1"])
    elif "2_1" in row["Order_2"]:
        lista2_1.append(row["Essay_2"])
set2_1= set(lista2_1) #len= 108


#essay 2_2

lista2_2= []

for index, row in df_filtrato2.iterrows():
    if "2_2" in row["Order_1"]:
        lista2_2.append(row["Essay_1"])
    elif "2_2" in row["Order_2"]:
        lista2_2.append(row["Essay_2"])
set2_2= set(lista2_2) #len=87



#essay 2_3
lista2_3= []

for index, row in df_filtrato2.iterrows():
    if "2_3" in row["Order_1"]:
        lista2_3.append(row["Essay_1"])
    elif "2_3" in row["Order_2"]:
        lista2_3.append(row["Essay_2"])
set2_3= set(lista2_3) #len=107



#essay 2_4
lista2_4= []

for index, row in df_filtrato2.iterrows():
    if "2_4" in row["Order_1"]:
        lista2_4.append(row["Essay_1"])
    elif "2_4" in row["Order_2"]:
        lista2_4.append(row["Essay_2"])
set2_4= set(lista2_4) #len=100


#essay 2_5
lista2_5= []

for index, row in df_filtrato2.iterrows():
    if "2_5" in row["Order_1"]:
        lista2_5.append(row["Essay_1"])
    elif "2_5" in row["Order_2"]:
        lista2_5.append(row["Essay_2"])
set2_5= set(lista2_5) #len=33


#definisco funzione trova_esempi

def trova_esempi(set_id, file= "data\\LangLearn_Training_Data\\Essays_CItA.xml"):
    
    esempi= []
    mancanti= []


    tree= ET.parse(file)
    root= tree.getroot()

    for element in set_id:
        mio_id= element
        testo = root.find(f".//*[@id='{mio_id}']")

        if testo is None:
            print("Nessun esempio trovato")
            mancanti.append(mio_id)
        else:
            esempio= "".join(testo.itertext()).strip()
            esempi.append(esempio)
    

    return(esempi)

