- \*\*Sai come si fa a codificare un agente?\*\*

 :  : VOC Id="SKIP0010" Txt="Sai come si fa a codificare un agente?"
Per creare un agente è necessario creare un elemento della tabella AGE.
Tale tabella contiene anche il riferimento al codice dell'anagrafica fornitori per legare il codice fornitore al codice agente.
- \*\*Sai quali sono i file coinvolti nella gestione provvigioni?\*\*

 :  : VOC Id="SKIP0015" Txt="Sai quali sono i file coinvolti nella gestione provvigioni?"
I file della gestione provvigioni sono : 
- V5PROV0F file nel quale vengono scritti i record delle provvigioni
- V5PRIM0F file nel quale vengono scritti i record delle provvigioni liquidate
- D5COSO0F file nel quale vengono scritti i record per agente/periodo della situazione contributiva all'atto del calcolo dei contributi
- \*\*Sai quali sono le tabelle coinvolte nella gestione delle provvigioni e la \*\*

 :  : VOC Id="SKIP0020" Txt="Sai quali sono le tabelle coinvolte nella gestione delle provvigioni e la loro funzionalità?"
- Tabella AGE codifica agenti
- Tabella B£4 date per la chiusura periodica delle liquidazioni e del calcolo contributivo
- Tabella V58 Parametrizzazione provvigioni per definire il comportamento ed i parametri base delle provvigioni
- Tabella V5P Tipo provvigione definisce le caratteristiche delle provvigioni per tipologia (è possibile creare diversi tipi di provvigioni con caratterstiche e comportamenti differenti)
- Tabella V6S Piano Liquidazioni. Definisce in modo più articolato il calcolo delle provvigioni.
- Tabella V6Z Piano Anticipi. Definisce le modalità di calcolo degli anticipi automatici da corrispondere agli agenti.
- \*\*Sai cos'è la periodicità della provvigione e come si imposta?\*\*

 :  : VOC Id="SKIP0025" Txt="Sai cos'è la periodicità della provvigione e come si imposta?"
La periodicità definisce l'intervallo di tempo che trascorre tra una liquidazione e l'altra.
L'impostazione della periodicità può essere definita per agente sulla tabella AGE oppure a livello generale per azienda sulla tabella V58.
Possono esistere agenti con periodicità diverse, in qeusto caso sarà necessario effettuare liquidazioni diverse per ciascuna periodicità.
- \*\*Sai cosa si intende per Liquidazione delle provvigioni?\*\*

 :  : VOC Id="SKIP0030" Txt="Sai cosa si intende per Liquidazione delle provvigioni?"
La liquidazione delle provvigioni è quell'azione che definisce gli importi che devono essere corrisposti all'agente a titolo di provvigione.
Di solito viene prodotto un prospetto che riepiloga la situazione delle provvigioni da corrispondere.
- \*\*Sai mettere in sequenza le operazini Liquidazione, Ripresa, Calcolo, delle\*\*

 :  : VOC Id="SKIP0035" Txt="Sai mettere in sequenza le operazini Liquidazione, Ripresa, Calcolo, delle provvigioni?"
La ripresa delle provvigioni è la prima azione da eseguire :  legge i documenti contabilizzati e trascrive sul fiel V5PROV0F le provvigioni, totalizzandole per cliente, docuemnto e tipo provvigione.
Il calcolo è la seconda azione da eseguire :  viene stabilito l'ammontare delle provvigioni che verranno poi liquidate.
La liquidazione è l'azione finale e definisce, atraverso la stampa di prospetti ordinati per agente, cliente e fattura l'importo delle provvigioni da liquidare.
- \*\*Sai quando si liquidano le provvigioni?\*\*

 :  : VOC Id="SKIP0040" Txt="Sai quando si liquidano le provvigioni?"
Le provvigioni si liquidano in funzione della periodicità.
La periodicità più comune è Mensile o Trimestrale.
- \*\*Sai se è possibile e come annullare una liquidazione definitiva delle prov\*\*

 :  : VOC Id="SKIP0045" Txt="Sai se è possibile e come annullare una liquidazione definitiva delle provvigioni?"
E' possibile effettuare l'annullamento dell'ultima liquidazione eseguita in definitivo attraverso il programma di riallineamento provvigioni.
- \*\*Sai cos'è la gestione contributiva, collegata alla gestione delle provvigi\*\*

 :  : VOC Id="SKIP0050" Txt="Sai cos'è la gestione contributiva, collegata alla gestione delle provvigioni?"
La gestione contributiva riguarda il calcolo dei contributi che l'azienda è tenuta a versare a favore e per conto dell'agente che la rappresenta.
I contributi sono : 
Contributo periodico ENASARCO sulle provvigioni maturate nel periodo, da versare ogni trimetre all'ente ENASRACO.
Contributo annuale FIRR da accantonare e versare annulamente all'Ente.
ISC indennità suppletiva di clientela da accontare annualmente e corrispodnere a finer apporto all'agente.

- \*\*Sai quali sono le tabelle che è necessario impostare per attivare la gesti\*\*

 :  : VOC Id="SKIP0055" Txt="Sai quali sono le tabelle che è necessario impostare per attivare la gestione contributiva?"
V6T - Piano Enasarco. Definisce i parametri di calcolo dei contributi dell'Enasarco.
V6U - Paino FIRR. Definisce i parametri di calcolo del FIRR.
V6V - Piano ISC.  Definisce i parametri di calcolo dell'Indennità Suppletiva di Clientela.
- \*\*Sai Cosa sono ENARCO, FIRR ed ISC e come si calcolano?\*\*

 :  : VOC Id="SKIP0060" Txt="Sai Cosa sono ENARCO, FIRR ed ISC e come si calcolano?" Als="comm"
ENASARCO è una percentuale sulle provvigioni di ogni periodo che va divisa equamente tra Agente ed Azienda, l'azienda si impegna a versarla all'ente preposto e trattiene la quota parte di competenza dell'agente dalla fattura delle provvigioni per verserla per conto dell'agente all'Ente.

FIRR è una percentuale sulle provvigioni liquidate nell'anno, che l'azienda deve accantonare e riconoscere all'agente annualmente versando il valore all'ente preposto entro il 31/03 dell'anno successivo a quello di riferimento.
La sommatoria degli importi versati all'Ente verrà liquidata da quest'ultimo all'agente, al
termine del rapporto con l'azienda.

ISC è l'indennità supplettiva di clientela da riconoscersi e versarsi all'agente in sede di scioglimento del rapporto d'agenzia. Viene calcolata in rapporto alle provvigioni liquidate e agli anni di durata del rapporto.
- \*\*Sai come definire un Piano Enasarco, FIRR ed ISC e come assegnarli ad un a\*\*

 :  : VOC Id="SKIP0065" Txt="Sai come definire un Piano Enasarco, FIRR ed ISC e come assegnarli ad un agente?"
Si devono definire i piani ENASARCO, FIRR, ISC attraverso le tabelle preposte (V6T, V6U, V6V).
Poi è necessario assegnare all'elemento della tabella AGE corrispondente all'agente i paini precedentemente definiti.
- \*\*Sai come calcolare il piano contributivo e come storicizzarlo?\*\*

 :  : VOC Id="SKIP0070" Txt="Sai come calcolare il piano contributivo e come storicizzarlo?"
Il calcolo del piano contributivo può essere eseguito solo dopo che è stata effettuata la liquidazione definitiva.
Può essere lanciato in provvisorio e ed in definitivo.
Tale calcolo genera un record nel D5COSO0F intestato all'agente e con periodo di riferimetno il periodo di liquidazione (mese o triemstre). Sul record vengono memoerizzate le provvigioni del periodo, i contributi per il periodo calcolati in base alla parametrizzazione impostata, la ritenuta d'acconto (se l'agente è soggetto a tale trattamento).
Lanciando il calcolo del piano contributivo in definitivo vi è la possibilità di creare dei documenti di cilco passivo di riepilgo che sarà poi possibile stampare.
I documenti verranno poi collegati alla fattura ins ede di contabilizzazione.
- \*\*Sai Come consultare o verificare il piano contributivo di un agente?\*\*

 :  : VOC Id="SKIP0075" Txt="Sai Come consultare o verificare il piano contributivo di un agente?"
Attraverso un programma di stampa è possibile ottenere dei prospetti riassuntivi della situazione contributiva degli agenti.
Tali prospetti possono essere dettagliati o sintetici per agente.
Inotre tramite questo programma è possibile anche ottenere una certificazione per le somme contributive versate.
- \*\*Sai se è possibile creare una fattura proforma che sintetizzi i dati delle\*\*

 :  : VOC Id="SKIP0080" Txt="Sai se è possibile creare una fattura proforma che sintetizzi i dati delle provvigioni liquidate?"
Sì è possibile creare un documento di ciclo passivo, al momento del calcolo definitivo del piano contributivo.
E' possibile stamparla attraverso il programma di stampa che può anche essere personalizzato (V5PR06S).
- \*\*Sai quali sono i prerequisiti per creare la fattura proforma da inviare al\*\*

 :  : VOC Id="SKIP0085" Txt="Sai quali sono i prerequisiti per creare la fattura proforma da inviare all'agente?"
Nella tabella V5P - Tipo provvigioni devono essere compilati i campi : 
Tipo Doc.Fat.Agente
Mod.Fat.Agente
Inoltre nella tabella AGE deve essere compilato il campo : 
Tipo contatto
Codice contatto
- \*\*Sai se è possibile e come annulare un piano contributivo calcolato in defi\*\*

 :  : VOC Id="SKIP0090" Txt="Sai se è possibile e come annulare un piano contributivo calcolato in definitivo?"
Attraverso il programma di Riallineamento Collegamento Fatturazione è possibile annullare l'ultima elaborazione definitiva eseguita del calcolo contributivo, con la possibilità di cancellare anche i documenti di ciclo passivo generati.
- \*\*Sai se è possibile e come si fa ad importare in contabilità i costi delle \*\*

 :  : VOC Id="SKIP0095" Txt="Sai se è possibile e come si fa ad importare in contabilità i costi delle provvigioni?"
E' possibile importare in contabilità i valori delle provvigioni attraverso l'azione specifica di contabilizzazione provvigioni.
La contabilizzazione importa il costo delle provvigioni, ovvero le provvigioni calcolate di un determinato periodo che vengono normalmente caricati su un conto di costo, con contropartita un conto patrimoniale di debito (es. Provvigioni da liquidare)
- \*\*Sai se è possibile e come si fa ad importare in contabilità i costi dei co\*\*

 :  : VOC Id="SKIP0100" Txt="Sai se è possibile e come si fa ad importare in contabilità i costi dei contributi ?"
E' possibile importare in contabilità i valori dei contributi attraverso l'azione specifica di contabilizzazione contributi.
La contabilizzazione importa : 
Costo dell'ENASARCO, ovvero il contributo calcolato di un determinato periodo che viene normalmente caricato  sul conto di costo, con contropartita un conto patrimoniale di debito (es. Enasarco/contributi da versare)
Costo dell'FIRR, ovvero il contributo calcolato di un determinato periodo che viene normalmente caricato  sul conto di costo, con contropartita un conto patrimoniale di debito (es. FIRR/contributi da versare)
Costo dell'ISC, ovvero l'indennità calcolata di un determinato periodo che viene normalmente caricato  sul conto di accantonamento, con contropartita un conto patrimoniale.
- \*\*Sai se è possibile e come si fa ad importare in contabilità il valore dell\*\*

 :  : VOC Id="SKIP0105" Txt="Sai se è possibile e come si fa ad importare in contabilità il valore delle provvigioni liquidate?"
E' possibile importare in contabilità i valori delle provvigioni attraverso l'azione specifica di contabilizzazione provvigioni.
La contabilizzazione importa  il valore del Liquidato, ovvero i valori della liquidazione che normalmente storna il conto di debito (es. Provvigioni da liquidare ) e carica l'attesa fattura degli agenti, che verrà poi stornata con la registrazione della fattura effettiva dell'agente.
- \*\*Sai cos'è il Calcolo delle provvigioni?\*\*

 :  : VOC Id="SKIP0032" Txt="Sai cos'è il Calcolo delle provvigioni?"
Il calcolo delle provvigioni è quell'azione che permette di stabilire se la provvigione è liquidabile.
Il suo comportamento è condizionato alla tipologia di liquidzione della provvigione, se la provvigione fosse sul fatturato, il programma che viene lanciato non fa nessuna ricerca, ma assume che tutto l'importo della provvigione è liquidabile.
Se la provvigione fosse sul pagato o saldato il programma di calcolo legge la contabilità e determina gli incassi per cliente e fattura e stabilisce l'importo della provvigione da liquidare.
