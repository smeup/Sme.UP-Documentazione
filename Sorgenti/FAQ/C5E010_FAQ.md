- **Sai cos'è il bilancio di verifica?**

 :  : VOC Id="SKIB0010" Txt="Sai cos'è il bilancio di verifica?" Als="comm"
E' una lista di conti e relativi saldi alla data selezionata, suddivisa in sezioni (patrimoniale ed economica).
- **Sai quali tipi di formati sono disponibili per il bilancio di verifica?**

 :  : VOC Id="SKIB0020" Txt="Sai quali tipi di formati sono disponibili per il bilancio di verifica?"
Sono disponibili i formati a scalare e a sezioni contrapposte.
- **Sai come trasferire il bilancio di verifica in un file esterno?**

 :  : VOC Id="SKIB0030" Txt="Sai come trasferire il bilancio di verifica in un file esterno?"
Utiliizando l'opzione di trasferimento con una memorizzazione del percorso di scarico del file.
- **Sai quale selezione viene effettuata nel periodo scelto sui filtri per for**

 :  : VOC Id="SKIB0040" Txt="Sai quale selezione viene effettuata nel periodo scelto sui filtri per formare il saldo di ogni conto?"
Per data registrazione.
- **Sai come includere nel calcolo saldi i movimenti gestionali e/o i moviment**

 :  : VOC Id="SKIB0050" Txt="Sai come includere nel calcolo saldi i movimenti gestionali e/o i movimenti provvisori?"
Mediante gli appositi flag di pertinenza e condizione sui filtri.
- **Sai se è possibile includere nella lista conti anche i singoli enti?**

 :  : VOC Id="SKIB0060" Txt="Sai se è possibile includere nella lista conti anche i singoli enti?"
Si, impostando il parametro 'Dettaglio soggetti' nelle impostazioni sotto F17.
- **Sai se dall'interrogazione del bilancio di verifica è possibile effettuare**

 :  : VOC Id="SKIB0070" Txt="Sai se dall'interrogazione del bilancio di verifica è possibile effettuare manutenzione sulle registrazioni?"
Si, se si sceglie il formato a scalare e si dispone delle autorizzazioni del caso, nonchè i movimenti non siano stampati in definitivo sui bollati oppure consolidati in qualche modo.
- **Sai cos'è una riclassifica di bilancio?**

 :  : VOC Id="SKIB0090" Txt="Sai cos'è una riclassifica di bilancio?" Als="comm"
Riclassificare un bilancio significa ordinarlo in modo diverso dalla classica forma di base divisa per stato patrimoniale (attività e passività) e conto economico (costi e ricavi).
Il bilancio CEE è un esempio classico, peraltro richiesto dalla normativa vigente, di bilancio riclassificato, ma ad uso gestionale si possono creare riclassifiche anche parziali dei conti esistenti, ad esempio del solo conto economico per il calcolo del margine.
- **Sai come si configura la struttura di una riclassifica di bilancio?**

 :  : VOC Id="SKIB0100" Txt="Sai come si configura la struttura di una riclassifica di bilancio?"
Nelle tabella C5M deve essere configurata la struttura che si vuol dare alla riclassifica, poi nella tabella C5Nxx (dove xx è un sottosettore con codice riclassifica) vanno codificate le linee di riclassifica desiderate.
- **Sai come si effettuano i collegamenti tra i conti e una riclassifica di bi**

 :  : VOC Id="SKIB0110" Txt="Sai come si effettuano i collegamenti tra i conti e una riclassifica di bilancio?"
Mediante la funzione di collegamento conti/linee sul menu dell'analisi di bilancio, scegliendo la riclassifica da codificare.
- **Sai come confrontare i saldi di due o più esercizi contabili?**

 :  : VOC Id="SKIB0120" Txt="Sai come confrontare i saldi di due o più esercizi contabili?"
Interrogando il bilancio riclassificato con la scheda dedicata è possibile mettere a confronto i saldi di esercizi o periodi diversi, ottenendo anche gli scostamenti dei saldi per importo e %.
- **Sai effettuare calcoli aritmetici e scostamenti nel confronto tra saldi di**

 :  : VOC Id="SKIB0130" Txt="Sai effettuare calcoli aritmetici e scostamenti nel confronto tra saldi di due o più esercizi contabili?"
Utilizzando una riclassifica per interrogare il bilancio dalla scheda con confronto tra esercizi gli scostamenti vengono calcolati automaticamente. Se però si deve operare con interfaccia classica, è possibile configurare le colonne del prospetto emesso nelle impostazioni sotto F17, servendosi dell'help della gestione colonne.
- **Sai effettuare calcoli aritmetici utilizzando linee di riclassifica di sub**

 :  : VOC Id="SKIB0140" Txt="Sai effettuare calcoli aritmetici utilizzando linee di riclassifica di subtotale?"
Agendo sugli elementi della tabella C5Nxx che compongono la riclassifica, è possibile fare uso di due campi denominati 'Linea di destinazione' e 'Segno di destinazione'. Il primo serve per destinare il saldo di una linea in un'altra linea, a formare quindi un valore calcolato diversamente dal saldo normalmente ottenuto dalla somma dei conti sottostanti la linea di destinazione stessa. Mediante il segno di destinazione è possibile definire con che segno destinare l'importo alla linea prescelta, quindi volendo anche invertendone il segno naturale.
- **Sai a cosa serve la destinazione per segno inverso su una linea di riclass**

 :  : VOC Id="SKIB0150" Txt="Sai a cosa serve la destinazione per segno inverso su una linea di riclassifica?"
Per destinare conti su linee diverse in base al saldo. Un tipico esempio è riferibile alle banche nel bilancio CEE :  queste, se hanno saldo Dare, vanno indicate nella sezione patrimoniale attiva, mentre se hanno saldo Avere vanno spostate nella sezione patrimoniale passiva.
- **Sai cosa sono gli indici di bilancio?**

 :  : VOC Id="SKIB0160" Txt="Sai cosa sono gli indici di bilancio?" Als="comm"
Sono quozienti o rapporti tra grandezze diverse dello stato patrimoniale e del conto economico del bilancio, utili per valutare lo stato di 'salute' dell'azienda e per la programmazione e controllo della gestione futura. Solitamente questi indici consentono di analizzare : 
- la struttura patrimoniale dell'azienda (indici strutturali);
- la capacità di essere solvibile nel medio-lungo periodo (indici patrimoniali);
- la capacità di avere un equilibrio finanziario nel breve periodo (indici finanziari);
- la capacità di produrre risultati economici positivi nel tempo (indici di redditività).
- **Sai come calcolare gli indici di bilancio di un'azienda?**

 :  : VOC Id="SKIB0170" Txt="Sai come calcolare gli indici di bilancio di un'azienda?"
Dopo aver riclassificato il bilancio secondo la struttura CEE, si utilizza la funzione specifica presente nel menu di analisi di bilancio, impostando sotto F17 gli esercizi da confrontare (massimo 3) e le informazioni che si desidera vengano presentate.
- **Sai cosa sono le liste allegati saldi?**

 :  : VOC Id="SKIB0180" Txt="Sai cosa sono le liste allegati saldi?"
Sebbene il bilancio possa essere interrogato anche con il dettaglio dei saldi clienti/fornitori, di solito per brevità il bilancio CEE viene preparato con il dato di sintesi. Queste liste forniscono quindi il dettaglio dei saldi sopra indicati come alleato del bilancio stesso.
- **Sai cosa sono i conti d'ordine?**

 :  : VOC Id="SKIB0080" Txt="Sai cosa sono i conti d'ordine?" Als="comm"
Sono una serie di conti che vengono utilizzati per registrarvi ciò che, di fatto, non costituisce nè un attivo o un passivo patrimoniale nè un costo o ricavo economico. Un classico esempio può essere rappresentato dai conti delle fidejussioni.
