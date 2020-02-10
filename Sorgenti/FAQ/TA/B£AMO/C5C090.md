### **Sai cos'è il sistema di rilevazione Intrastat?**

E' un sistema di rilevazione statistica che misura gli scambi di merci e servizi tra stati Cee.
### **Sai qual è il giorno della scadenza dichiarativa?**

Il 25 del mese per i dati da dichiarare del periodo precedente (mese o trimestre).
### **Sai come si identificano gli Stati qualificati come Intracee?**

Nella tabella V§N (codici Nazioni) tramite apposito flag.
### **Sai che differenza c'è tra un acquisto e una vendita (cessione) Intracee?**

La fattura di vendita CEE è una normale fattura con IVA esente (art.41), quella di acquisto deve essere registrata con il sistema cosiddetto dell'IVA reverse charge.
### **Sai come codificare i codici IVA necessari alle registrazioni di documenti Intracee?**

Nella tabella IVA un codice di questo tipo deve avere il flag 'Operazione Intracee' acceso.
### **Sai come codificare gli automatismi di supporto alle registrazioni di documenti Intracee?**

Nella tabella C5U devono esistere tanti codici IVAACxx, dove xx è il codice IVA presente nella tabella IVA con flag acceso come operazione Intracee. Deve poi esistere anche l'elemento IVACE.
### **Sai  che particolarità ha un ente Intracee nei suoi dati fiscali identificativi?**

Il codice Nazione deve essere uno degli stati CEE identificati nella tabella V§N, inoltre la partita IVA CEE ha un campo dedicato.
### **Sai cos'è una nomenclatura combinata?**

E' un codice doganale che codifica la tipologia di merce acquistata o venduta.
### **Sai cos'è il codice servizio?**

E' un codice doganale che codifica il tipo di servizio acquistato o venduto.
### **Sai quali sono le tabelle necessarie alla corretta installazione del servizio?**

Tabella V5E per le impostazioni di base.
Tabella BRN delle nomenclature combinate.
Tabelle V§\*IA-B-C-E-F-G-H-R dedicate alla gestione Intracee.
Tabelle CCO e SPE per gestione parametri di calcolo costo statistico.
Tabella C5V per default natura transazione da causale contabile.
### **Sai cos'è il costo statistico da rilevare?**

E' il costo calcolato aggiungendo il valore del trasporto al valore del bene acquistato o venduto.
### **Sai come rilevare una rettifica?**

Inserendo movimenti con periodo competenza precedente al periodo dichiarativo.
### **Sai cos'è l'unità di misura supplementare?**

E' l'unità di misura secondaria che alcune nomenclature combinate richiedono di specificare oltre alla massa da dichiarare espressa in kg.
### **Sai come collegare la gestione movimenti Intracee alla gestione registrazioni contabili?**

Agendo sull'apposito flag nella tabella C51.
### **Sai che periodicità può avere la dichiarazione Intracee?**

Mensile o trimestrale.
### **Sai se ci sono eventuali esenzioni o semplificazioni alla dichiarazione Intracee?**

Il costo statistico non viene dichiarato per ammontare annuale acquisti o vendite inferiore ai 20.000.000 di Euro.
### **Sai che tipo di modulistica deve essere approntata per la dichiarazione?**

Modelli PDF separati per acquisti e vendite, divisi in un frontespizio, un dettaglio fatture e un dettaglio rettiche, ulteriormente diviso tra merci e servizi.
### **Sai come scaricare su file la dichiarazione?**

Effettuando una stampa definitiva dei modelli, viene creato il file C5IS80TF, che può poi essere scaricato su pc come SCAMBI.CEE e utilizzato per la trasmissione telematica.
### **Sai come inoltrare la dichiarazione?**

Va inoltrata solo per via telematica, non più presso la Dogana.
### **Sai come utilizzare il software Intraweb?**

Si/No.
### **Sai come relazionare un articolo alla nomenclatura combinata?**

Nell'anagrafica articolo, dati aggiuntivi.
### **Sai cos'è il rappresentante fiscale di un soggetto?**

E' una terza parte che, di fatto, rappresenta fiscalmente in Italia un soggetto residente in stati non CEE (ad esempio la Svizzera) ma verso cui si effettua la dichiarazione.
Si qualifica come tale per mezzo di una estensione (£42) da associare ad un ente.
