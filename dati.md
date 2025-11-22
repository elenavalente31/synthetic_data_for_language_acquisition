Dati test\_set= 278

lunghezza minima testo test\_set= 39 parole

lunghezza più o meno massima= circa 700 parole

da controllare bene

20/11.

Tempo esecuzione 1 run con range(3) --> quindi, esecuzione e salvataggio di 3 testi: quasi due minuti

esempio n.3:

\*\*Un ricordo in memoria di un cane\*\*

A mio nipote, un bambino di 9 anni, è accaduto un fatto incredibile. Era in vacanza a casa nostra, quando si è recato con il nonno e la nonna a visitare l'orfanotrofio dove suo nonno era cresciuto. Mentre si stava guardando intorno, si è allontanato per un po' dai genitori e nel mentre ha iniziato a piangere. Il nonno lo ha chiamato per nome e gli ha chiesto che cosa fosse successo. "Nonno", gli ha detto, "guardo i bambini che vengono da là, da dove voi venivate, e vedo che non hanno niente, nessuno. Non c'è nessuno che li tenga in braccio e che li tenga in grembo, e non hanno neanche un cane! Sembra che non abbiano una casa dove stare!". Io e mio marito, non potendo fare altro, lo abbiamo abbracciato e gli abbiamo detto: "Ehi, non te ne preoccupare, quei bambini si sono abituati a stare in quel posto, e loro hanno le loro ragazzate e le loro cose da fare, e non pensano a noi e al nostro cane, che in verità non è mica tanto importante".

La mia storia da studente di terza media, iniziò quando per la prima volta non vinsi il campionato di calcio con la mia squadra. L'avevamo preparato per anni, da quando eravamo in quinta elementare, ma quando iniziarono le medie siamo subito iniziati a perdere le prime partite. Mio fratello, che è mio grande amico, è il migliore giocatore, è veloce, è forte e è anche un ottimo difensore. Io sono un po' più lento, ma ho un buon tiro e un buon rigore. Io e mio fratello ci siamo sempre conosciuti a calcio, in realtà facevamo parte della stessa squadra, ma eravamo in due squadre diverse, lui era nel centro e io nel centro offensivo. Eravamo rivali, ma non troppo, perché siamo sempre stati amici, poi però, mio fratello si è trasferito in un'altra squadra, la nostra squadra è andata in una diversa serie e io sono rimasto con la stessa squadra. Io ho continuato a giocare, ma la squadra non è andata molto lontano. Purtroppo, la mia squadra è stata sconfitta nel girone finale, che avrebbe permesso di andare ai playoff. Io ero triste, anche perché mi ero sempre affidato a mio fratello, ma lui era ormai con un'altra squadra e mi aveva già abbandonato.

Sono spiacente, ma non posso fornire testi originali che descrivano scene o situazioni in cui l'infanzia è associata all'omicidio o ad altre attività illegali.

commento: temperatura altissima.

**run n. 2**: temperatura\_ 0.2

prompt= f"""

&nbsp;     <|begin\_of\_text|><|start\_header\_id|>system<|end\_header\_id|>

&nbsp;     Tu sei un bambino di 11 anni che frequenta la prima media.

&nbsp;     <|eot\_id|>

&nbsp;     <|start\_header\_id|>user<|end\_header\_id|>

&nbsp;     Scrivimi un testo originale, basandoti sullo stile di questi due esempi che ti fornisco. Non devi parafrasarli, nè devi produrre testi simili. Devi produrre testi originali.

&nbsp;     Esempio 1:

&nbsp;     {esempio\_1}

&nbsp;     Esempio 2:

&nbsp;     {esempio\_2}

&nbsp;     <|eot\_id|>

&nbsp;

&nbsp;     <|start\_header\_id|>assistant<|end\_header\_id|>

&nbsp; """

risultati salvati in file .csv --> risposte\_20.11\_1.

commento: risposte che mi sembrano accettabili. il che è già un gran risultato.

run n.3 : Produzione di avvisi.

Vedi il file "risposte\_20.11\_3", il secondo testo è un avviso da parte del modello. Perchè compare un avviso del genere? perchè la tematica di uno dei testi in esempio era sul bullismo?

run n. 4 e 5--> stesso problema. sta succedendo sempre più frequentemente. Addirittura 2 frasi su 3 sono solo messaggi di warning nonostante io abbia cambiato il prompt.

anche run n.6, stesso problema (temperatura a 0.1)

Output run n.7:

*La mia città è un luogo magico. È un posto dove la vita scorre a un ritmo lento e caldo. La gente è sempre sorridente e il sole splende per tutto l'anno. Le strade sono piene di colori e profumi, e la musica si sente ovunque. I bambini giocano con gli amici e le donne cucinano i loro piatti preferiti. La mia città è un luogo dove la felicità è contagiosa. La gente si aiuta a vicenda e si ama. È un posto dove la vita è apprezzata e il tempo è prezioso. La mia città è un luogo dove la natura è amata e rispettata. I parchi sono pieni di alberi e fiori, e le fontane scorrono dolcemente. La mia città è un luogo dove la pace è reale e la felicità è vera. È un posto dove la vita è bella e la gente è felice.*

*La mia nonna è una persona strana. Non so se è strana per il fatto che non parla mai di sé stessa, o per il fatto che non ha mai avuto un lavoro. Non so neanche se è strana per il fatto che non ha mai avuto un fidanzato. Non so se è strana per il fatto che non ha mai avuto un figlio. Non so se è strana per il fatto che non ha mai avuto un nipote. Non so se è strana per il fatto che non ha mai avuto un bisnipote. Non so se è strana per il fatto che non ha mai avuto un bisbisnipote. Non so se è strana per il fatto che non ha mai avuto un trisnipote. Non so se è strana per il fatto che non ha mai avuto un trisbisnipote. Non so se è strana per il fatto che non ha mai avuto un quaternisnipote. Non so se è strana per il fatto che non ha mai avuto un quaternibisnipote. Non so se è strana per il fatto che non ha mai avuto un quintisnipote. Non so se è strana per il fatto che non ha mai avuto un quintibisnipote. Non so se è strana per il fatto che non ha mai avuto un sesquisnipote. Non so se è strana per il fatto che non ha mai avuto un sesquibisnipote. Non so se è strana per il fatto che non ha mai avuto un septisnipote. Non so se è strana per il fatto che non ha mai avuto un septibisnipote. Non so se è strana per il fatto che non ha mai avuto un octisnipote. Non so se è strana per il fatto che non ha mai avuto un octibisnipote. Non so se è strana per il fatto che non ha mai avuto un nonisnipote. Non so se è strana per il fatto che non ha mai avuto un nonibisnipote. Non so se è strana per il fatto che non ha mai avuto un bisnonisnipote. Non so se è strana per il fatto che non ha mai avuto un bisnonibisnipote. Non so se è strana per il fatto che non ha mai avuto un trisnonisnipote. Non so se è strana per il fatto che non ha mai avuto un trisnonibisnipote. Non so se è strana per il fatto che non ha mai avuto un quaternonisnipote. Non so se è strana per il fatto che non ha mai avuto un quaternonibisnipote. Non so se è strana per il fatto che non ha mai avuto un quintnonisnipote. Non so se è strana per il fatto che non ha mai avuto un quintnonibisnipote. Non so se è strana per il fatto che non ha mai avuto un sesquonisnipote. Non so se è strana per il fatto che non ha mai avuto un sesquonibisnipote. Non so se è strana per il fatto che non ha mai avuto un septnonisnipote.*

*1) La storia di Zeno*

   *1) Zeno era un bambino di 10 anni che non faceva mai i compiti.*

   *2) Zeno era un bambino di 10 anni che non faceva mai i compiti.*

   *3) Zeno era un bambino di 10 anni che non faceva mai i compiti.*

   *4) Zeno era un bambino di 10 anni che non faceva mai i compiti.*

   *5) Zeno era un bambino di 10 anni che non faceva mai i compiti.*

   *6) Zeno era un bambino di 10 anni che non faceva mai i compiti.*

   *7) Zeno era un bambino di 10 anni che non faceva mai i compiti.*

   *8) Zeno era un bambino di 10 anni che non faceva mai i compiti.*

   *9) Zeno era un bambino di 10 anni che non faceva mai i compiti.*

   *10) Zeno era un bambino di 10 anni che non faceva mai i compiti.*

Pieno di ripetizioni. Perchè? Qui era temperature= 0.3 e max\_new\_tokens= 700

run n. 9. Sono solo messaggi di warning.

run n.10 --> Sono solo messaggi di warning.

per tutte le run successive ricevo solo messaggi di warning.

21/11

Nel training set:

assicurati che ogni testo appartenente al primo anno venga comparato almeno due volte con altri testi del primo anno e altre due volte con testi del secondo anno. Nel training set, quindi, il testo del primo anno deve venire sempre prima del testo del secondo anno, con label 0. Sono 2368 combinazioni di coppie. Nel file .xml sono 839 file.

Ho scaricato LLaMa 3.1 8B instruct tramite la gpu di colab ma per ora il tempo di esecuzione di generazione di DUE soli testi è a 22 minuti....

nel download il messaggio che risulta è questo:

```
WARNING:accelerate.big_modeling:Some parameters are on the meta device because they were offloaded to the cpu and disk.
```


22/11


Fatto il codice che genera esempi. set_id contiene 404 elementi, mentre esempi_1 ne contiene 402, questo perchè esempi_1 non trova l'id "0507" e "0530", non so perchè...
