from groq import Groq
from dotenv import load_dotenv
import os
import csv
import pandas as pd
import xml.etree.ElementTree as ET
import time 
import ast
from groq import Groq
import random
from trova_esempi import *
from trova_lunghezze import *

load_dotenv()   # carica le variabili del file .env

print(os.environ.get("Groq_API"))

client = Groq(
    api_key=os.environ.get("Groq_API")
)

LUNGHEZZA_TARGET= trova_lunghezze(lunghezze)
MAX_TOKENS= LUNGHEZZA_TARGET + 30

esempi_1 = trova_esempi(set2_4)

#genero il set di id

set_file= "set_id.txt"

set_id = set()

if os.path.exists(set_file):
    with open(set_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.isdigit():
                set_id.add(int(line))




for i in range(30):

    with open ("coppie_usate.txt", "r", encoding= "utf-8") as file:
        coppie_usate= ast.literal_eval(file.read())
        


    esempi= random.sample(esempi_1, 2)
    esempio_1= esempi[0]
    esempio_2 = esempi[1]


    coppia=(esempio_1,esempio_2)

    
    while coppia in coppie_usate:

        
        esempi= random.sample(esempi_1, 2)
        esempio_1= esempi[0]
        esempio_2 = esempi[1]


        coppia= (esempio_1,esempio_2)


    coppie_usate.add(coppia)
    with open ("coppie_usate.txt", "w", encoding="utf-8") as file:
        file.write(str(coppie_usate))
    



    
    prompt= (
    "Scrivi un testo in italiano completamente originale ispirato allo stile linguistico e stile di scrittura dei due esempi. "
    "Non copiarli. Non parafrasare gli esempi. Non fare premesse, non dare avvisi. Produci solo il testo originale.\n\n"
    f"=== ESEMPIO 1 ===\n{esempio_1}\n\n"
    f"=== ESEMPIO 2 ===\n{esempio_2}\n\n"
    "=== TESTO DA GENERARE ==="
)
    
    
    
    
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "Sei un bambino di 12 anni che frequenta la seconda media."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="llama-3.3-70b-versatile",
        

        temperature= 1.2,

        top_p= 1,

        max_completion_tokens= MAX_TOKENS,


        frequency_penalty=1.3

    )

    

    testi_generati= chat_completion.choices[0].message.content
    testi_generati= testi_generati.strip()
    dati_generati= tronca_testo(testi_generati, MAX_TOKENS)



    
    doc_id= random.randint(1000,6000)
    while doc_id in set_id:
        doc_id = random.randint(1000, 6000)

    set_id.add(doc_id)

    with open(set_file, "a", encoding="utf-8") as f:
        f.write(f"{doc_id}\n")

    


    xml_path= "synthetic_data\\dataset_t1.2.xml"

    if not os.path.exists(xml_path):
        root = ET.Element("dataset")
        tree = ET.ElementTree(root)
    else:
        tree = ET.parse(xml_path)
        root = tree.getroot()

    
    
    doc = ET.SubElement(root, "doc", id=str(doc_id))
    doc.text = dati_generati
  
    
    tree.write(xml_path, encoding="utf-8", xml_declaration=True)

    tsv_path= "synthetic_data\\essay.tsv\\essay2_4.tsv"


    if not os.path.exists(tsv_path):
        with open (tsv_path, "w", encoding = "utf-8") as outfile:

            outfile.write("Essay_1\tOrder_1\n")
  
            



    with open (tsv_path, "a", encoding = "utf-8") as outfile:
        outfile.write(f"{doc_id}\t2_4\n")

    #minuti = 60
    #time.sleep(minuti * 1)




