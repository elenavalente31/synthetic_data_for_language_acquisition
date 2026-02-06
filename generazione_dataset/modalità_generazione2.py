import json
import random
import xml.etree.ElementTree as ET
import os
from trova_lunghezze import *
from trova_testo import *
from dotenv import load_dotenv
from groq import Groq

## definisco i percorsi dei file utilizzati. Secondo questa modalità di generazione, il dataset viene prodotto iterando su ogni singolo studente. 4
##Per fare ciò, è stato creato un file .json in cui ad ogni studente corrisponde un dizionario, che contiene coppie chiave-valore. 
##Ciascuna coppia chiave-valore è formata da ID dell'essay scritto dallo studente e periodo in cui quell'essay è stato scritto. 
## Ad esempio, Studente_1: {"3456":"1_2"}
##In questo modo si è cercato di replicare degli studenti artificiali. 

xml_reale = "training_set_cita\\Essays_CItA.xml"
xml_path = "dati_sintetici_train\\dataset_t1.5.xml"
json_output = "dati_sintetici_train\\studenti_sintetici_train_1.5.json"
set_file = "set_id.txt"

os.makedirs("dati_sintetici_train", exist_ok=True)


# Carico i file di input


with open("studenti_train.json", "r", encoding="utf-8") as f:
    studenti = json.load(f)

if os.path.exists(json_output):
    with open(json_output, "r", encoding="utf-8") as f:
        studenti_sintetici = json.load(f)
else:
    studenti_sintetici = {}

# definisco il set degli ID da usare

set_id = set()
if os.path.exists(set_file):
    with open(set_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip().isdigit():
                set_id.add(int(line.strip()))


if os.path.exists(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
else:
    root = ET.Element("dataset")
    tree = ET.ElementTree(root)


load_dotenv()
client = Groq(api_key=os.environ.get("API_groq"))



# ciclo di iterazione su ciascuno studente


for studente, id_order_map in studenti.items():

    if studente in studenti_sintetici:
        print(f"[SKIP] {studente} già generato")
        continue

    print(f"[GEN] {studente}")
    studenti_sintetici[studente] = {}

    for id_reale, order in id_order_map.items():

        #utilizzo la funzione trova_lunghezze per definire la lunghezza che il testo generato deve avere
        
        LUNGHEZZA_TARGET = trova_lunghezze(lunghezze)
        MAX_TOKENS = LUNGHEZZA_TARGET + 30
        
        esempio = trova_testo(xml_reale, id_reale)

        prompt = (
            "Scrivi un testo in italiano completamente originale ispirato "
            "allo stile linguistico e di scrittura dell'esempio. "
            "Non copiarlo. Non parafrasarlo. Produci solo il testo.\n\n"
            f"=== ESEMPIO ===\n{esempio}\n\n"
            "=== TESTO DA GENERARE ==="
        )

        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "Sei un bambino che frequenta la scuola media"},
                {"role": "user", "content": prompt}
            ],
            model="llama-3.3-70b-versatile",
            temperature=1.5,
            top_p=1,
            max_completion_tokens=MAX_TOKENS,
            frequency_penalty=1.3
        )

        testo = chat_completion.choices[0].message.content.strip()
        testo = tronca_testo(testo, MAX_TOKENS)

        #definisco un ID per il testo generato, assicurandomi che non ne sia già presente uno uguale
        
        doc_id = random.randint(1000, 6000)
        while doc_id in set_id:
            doc_id = random.randint(1000, 6000)

        set_id.add(doc_id)
        with open(set_file, "a", encoding="utf-8") as f:
            f.write(f"{doc_id}\n")

        # definisco e scrivo il file .xml

        xml_path= "dati_sintetici_train\\dataset_t1.5.xml"

        if not os.path.exists(xml_path):
            root = ET.Element("dataset")
            tree = ET.ElementTree(root)
        else:
            tree = ET.parse(xml_path)
            root = tree.getroot()

    
    
        doc = ET.SubElement(root, "doc", id=str(doc_id))
        doc.text = testo
  
    
        tree.write(xml_path, encoding="utf-8", xml_declaration=True)


        # JSON
        studenti_sintetici[studente][str(doc_id)] = order

# salvo tutti i dati in un nuovo file .json


        with open(json_output, "w", encoding="utf-8") as f:
            json.dump(studenti_sintetici, f, indent=2, ensure_ascii=False)

        print("✅ Generazione completata correttamente")

