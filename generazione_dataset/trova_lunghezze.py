import pandas as pd
import xml.etree.ElementTree as ET
import random
import regex as re


file = "training_set_cita\\Essays_CItA.xml"
tree = ET.parse(file)
root = tree.getroot()

lunghezze = [len("".join(elem.itertext()).strip().split()) for elem in root.findall(".//doc")]

def trova_lunghezze(lunghezze):
    if not lunghezze:
        raise ValueError("Non ci sono più lunghezze disponibili!")
    # Seleziona una lunghezza casuale
    scelta = random.choice(lunghezze)
    # Rimuovila dalla lista per non riutilizzarla
    lunghezze.remove(scelta)
    
    return scelta



def tronca_testo(testo, max_tokens):
    """
    Tronca il testo fino all'ultimo punto prima di max_tokens token.
    """
    tokens = testo.split()
    
    # Limitiamo al numero massimo di token
    tokens = tokens[:max_tokens]
    testo_limitato = " ".join(tokens)
    
    # Cerchiamo l'ultimo punto, punto esclamativo o interrogativo
    match = list(re.finditer(r'[.!?]', testo_limitato))
    if match:
        # Ultimo match prima del limite
        ultimo = match[-1].end()
        return testo_limitato[:ultimo]
    else:
        # Se non ci sono punteggiature, torniamo tutto il testo limitato
        return testo_limitato
