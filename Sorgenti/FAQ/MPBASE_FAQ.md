- \*\*Sai cos'è la periodicità?\*\*

 :  : VOC Id="SKIM0010" Txt="Sai cos'è la periodicità?"
La periodicità è una suddivisione dell'orizzonte temporale in N periodi che possono essere fatti di giorni, settimane, mesi, quindicine, trimestri , etc. E' definita nella tabella A£Q, leggere l'help di tabella.
- \*\*Sai come si fa a definire un Piano ?\*\*

 :  : VOC Id="SKIM0020" Txt="Sai come si fa a definire un Piano ?"
Si immette un elemento nella tabella MPP, e poi si immette un record qualsiasi nel piano. In questo modo vengono creati i quindici records nel file MPPIAN0F che definiscono il piano.
- \*\*Sai come si fa a definire una vista che poi mostri i decimali ?\*\*

 :  : VOC Id="SKIM0030" Txt="Sai come si fa a definire una vista che poi mostri i decimali ?"
C'è un campo nella tabella MPC (viste di piano) che specifica la visibilità dei decimali, che sono comunque registrati nel record del piano.
- \*\*Sai come si fa a definire un flusso che generi automaticamente il piano su\*\*

 :  : VOC Id="SKIM0040" Txt="Sai come si fa a definire un flusso che generi automaticamente il piano su cui lavorare?"
Si mette come prima azione del flusso una azione che chiami il pgm di generazione piano (MPAP01) e poi nella tabella B£H del flusso (il codice flusso) si specifica come azione di impostazione quella di definizione piano.
- \*\*Sai definire una priodicità di 17 giorni e 4 mesi che non lasci periodi vu\*\*

 :  : VOC Id="SKIM0050" Txt="Sai definire una priodicità di 17 giorni e 4 mesi che non lasci periodi vuoti anche se il piano inizia il 2 marzo?"
Basta compilare con un + il campo "flag giorni". In questo caso vengono generati N periodi , con N maggiore  o uguale a 17 che arrivano fino a fine mese.
- \*\*Sai definire una sintesi delle righe di una vista , in modo da poter cance\*\*

 :  : VOC Id="SKIM0060" Txt="Sai definire una sintesi delle righe di una vista , in modo da poter cancellare solo le righe di una certa classe materiale?"
Si agisce sulla tabella C£S dove si definiscono le sintesi di oggetti. Questa tabella può puntare ad un sottosettore della tabella C£Z, dove si definiscono gli OAV dell'oggetto da utilizzarsi per la sintesi. Indi, si memorizza un filtro della vista da cancellare selettivamente , utilizzando l'F13 nella visualizzazione delle viste di piano.
- \*\*Sai memorizzare una impostazione di cancellazione  di una vista con selezi\*\*

 :  : VOC Id="SKIM0070" Txt="Sai memorizzare una impostazione di cancellazione  di una vista con selezione tarmite OAV di una chiave?"
Per prima cosa bisogna definire l'OAV di quella chiave come "sintesi" della chiave. Bisogna compilare opportunamente un elemento della tabella C£S (con codice l'oggetto della chiave) ed uno della tabella C£Zxx (il sottosettore è definito nella tabella C£S precedentemente compilata).
Poi bisogna memorizzare tramite MEDAV la selezione di quei record che si vuole cancellare , utilizzando il pgm di Eliminazione selettiva dati piano (MPGP02G) che permette di registrare con un unico codice di medav la vista che si vuole cancellare ed i criteri di selezione.
- \*\*Sai definire un flusso di azioni che a metà cambia piano su cui lavorare?\*\*

 :  : VOC Id="SKIM0080" Txt="Sai definire un flusso di azioni che a metà cambia piano su cui lavorare?"
E' sufficiente mettere a metà flusso la creazione di un nuovo piano (pgm MPAP01) e da quel passo in poi il flusso lavorerà sul piano impostato
- \*\*Sai costruire un flusso di azioni partendo dalle azioni funizzabili a disp\*\*

 :  : VOC Id="SKIM0090" Txt="Sai costruire un flusso di azioni partendo dalle azioni funizzabili a disposizione per l'MPS?"
Nel menu dell'applicazione c'è l'azione "funzioni per MPS" che racchiude tutte le azioni funizzabili che possono essere aggiunte ad un flusso
- \*\*Sai come si fa a controllare il peso di un giorno all'interno di una setti\*\*

 :  : VOC Id="SKIM0100" Txt="Sai come si fa a controllare il peso di un giorno all'interno di una settimana o di un mese?"
Si lancia il pgm B£DIRV - S&P DISTRIBUZIONE QUANTITA'- che permette di vedere quanto è imporatnte (pesante) un giorno all'interno di una settimana o di un mese.
- \*\*Sai qual è il calendario che regola la costruzione di una periodicità?\*\*

 :  : VOC Id="SKIM0110" Txt="Sai qual è il calendario che regola la costruzione di una periodicità?"
Quello della risorsa che è riportata sulla periodicità stessa.
- \*\*Sai come si fa ad importare i dati di una vista / piano in un'altra Vista/\*\*

 :  : VOC Id="SKIM0120" Txt="Sai come si fa ad importare i dati di una vista / piano in un'altra Vista/piano?"
Con un flusso che , applicato al piano di destinazione, contenga una azione con il pgm mpap02f, opportunamente parametrizzata per pescare i dati dall'origine desiderata.
- \*\*Sai come si fa ad aumentare i dati di una vista del 23 % ?\*\*

 :  : VOC Id="SKIM0130" Txt="Sai come si fa ad aumentare i dati di una vista del 23 % ?"
Con un flusso che contenga una azione con il pgm mpap03a, opportunamente parametrizzata. Oppure con il pgm MPBMPR0, che permette di modificare con le operazioni elementari il contenuto di una vista.
- \*\*Sai come si fa a disperdere una quantità annuale in una periododicità di u\*\*

 :  : VOC Id="SKIM0140" Txt="Sai come si fa a disperdere una quantità annuale in una periododicità di un piano in base ai giorni lavorativi?"
Usando il pgm MPBMPR0, gestione del budget
- \*\*Sai come si fa a disperdere una quantità qualsiasi proporzionalmente ad un\*\*

 :  : VOC Id="SKIM0150" Txt="Sai come si fa a disperdere una quantità qualsiasi proporzionalmente ad una serie di quantità in una vista/piano?"
Con il pgm MPBMPR0, che permette una serie di operazioni su una vista, facendo riferimento al contenuto di un'altra vista/piano
- \*\*Sai come si fa a sviluppare una vista /piano in un'altra che ha come chiav\*\*

 :  : VOC Id="SKIM0160" Txt="Sai come si fa a sviluppare una vista /piano in un'altra che ha come chiave un attributo della chiave della vista origine?"
Con una azione di flusso che operi una "sintesi" :  è ottenuta con il pgm MPAP05A, opportunamente parametrizzato.
- \*\*Sai come si fa a valorizzare una vista?\*\*

 :  : VOC Id="SKIM0170" Txt="Sai come si fa a valorizzare una vista?"
Con una azione di flusso che operi una "valorizzazione" :  è ottenuta con il pgm MPAP06A, opportunamente parametrizzato.
- \*\*Sai come si fa ad ottenere da una vista , un'altra che ha come chiave un O\*\*

 :  : VOC Id="SKIM0180" Txt="Sai come si fa ad ottenere da una vista , un'altra che ha come chiave un OAV della chiave della prima vista?"
Utilizzando il pgm che realizza una sintesi di una vista , MPAP05A, e naturalmente preparando nella tabella C£Zxx un elemento che utilizza l'OAV desiderato
- \*\*Sai come si fa ad ottenere da una vista che rappresenta il venduto per naz\*\*

 :  : VOC Id="SKIM0190" Txt="Sai come si fa ad ottenere da una vista che rappresenta il venduto per nazione, un'altra che lo dettaglia nel venduto per cliente?"
Con una azione di flusso che operi un "adeguamento dettaglio al totale" :  è ottenuta con il pgm MPAP07A, opportunamente parametrizzato.
- \*\*Sai come si fa a sviluppare un MRP in una vista/piano?\*\*

 :  : VOC Id="SKIM0200" Txt="Sai come si fa a sviluppare un MRP in una vista/piano?"
Con una azione di flusso che operi una "esplosione distinta con nettificazione gruppo fonti" :  è ottenuta con il pgm MPAP32, opportunamente parametrizzato.
- \*\*Sai quali sono i limiti dello sviluppo di un MRP in una vista / Piano con \*\*

 :  : VOC Id="SKIM0210" Txt="Sai quali sono i limiti dello sviluppo di un MRP in una vista / Piano con periodicità mensile?"
Il limite è che i leadtimes inferiori ad un mese non cambiano l'attribuziuone del mese degli impegni pianificati, per cui l'mrp siffatto non anticipa i riordini (restano nello stesso mese del fabbisogno..)
- \*\*Sai come si fa a caratterizzare i numeri liberi di una vista?\*\*

 :  : VOC Id="SKIM0220" Txt="Sai come si fa a caratterizzare i numeri liberi di una vista?"
Tramite la definizione di un elemento della tabella C£I (parametri impliciti) e collegandolo nell'apposito campo della vista
- \*\*Sai cosa sono le statistiche di una vista?\*\*

 :  : VOC Id="SKIM0230" Txt="Sai cosa sono le statistiche di una vista?"
Un insieme di indici che caratterizzano i valori medi e le deviazioni del contenuto della vsita
- \*\*Sai come si fa a calcolare un piano di produzione a capacità finita?\*\*

 :  : VOC Id="SKIM0240" Txt="Sai come si fa a calcolare un piano di produzione a capacità finita?"
Con una azione di flusso che operi una "schedulazione a capacità finita" :  è ottenuta con il pgm MPAP37, opportunamente parametrizzato.
- \*\*Sai come si fa a riprendere da una vista anche i record con tutti zero?\*\*

 :  : VOC Id="SKIM0250" Txt="Sai come si fa a riprendere da una vista anche i record con tutti zero?"
Valorizzando nei parametri di ripresa il flag "riprendi anche zeri". Altrimenti, i record con tutti zeri vengono ignorati
- \*\*Sai come si fa a totalizzare una vista di due chiavi in una da una chiave \*\*

 :  : VOC Id="SKIM0260" Txt="Sai come si fa a totalizzare una vista di due chiavi in una da una chiave sola?"
Con una azione di flusso che operi una "totalizzazione" :  è ottenuta con il pgm MPAP04A, opportunamente parametrizzato.
- \*\*Sai come si fa a definire una ripresa dati dall'ultimo piano con determina\*\*

 :  : VOC Id="SKIM0270" Txt="Sai come si fa a definire una ripresa dati dall'ultimo piano con determinata radice?"
parametrizzando opportunamente la ripresa, indicando solo la radice del piano di ripresa ed il flag "ultimo piano". E' una azione fondamentale per avere flussi ripetibili ogni mese mantenendo fissa la parametrizzazione
- \*\*Sai come si fa a riprendere i dati del primo trimestre nel secondo trimest\*\*

 :  : VOC Id="SKIM0280" Txt="Sai come si fa a riprendere i dati del primo trimestre nel secondo trimestre, solamente per gli articoli con un certo OAV?"
Parametrizzando opportunamente la azione di ripresa :  indicare metodo di ripresa diretta, specificare da che periodo riprendere e dove caricare.

- \*\*Sai come è calcolata la vista che sottintende al calcolo CTP?\*\*

 :  : VOC Id="SKIM0300" Txt="Sai come è calcolata la vista che sottintende al calcolo CTP?"
Deve essere calcolata a capacità finita, consumando tutta la capacità al più presto e lasciando ore libere al termine del workload
- \*\*Sai cos'è il metodo statistico Holt Winters?\*\*

 :  : VOC Id="SKIM0310" Txt="Sai cos'è il metodo statistico Holt Winters?" Als="comm"
E' un metodo per la costruzione delle previsioni numeriche di una serie numerica conosciuta. In altre parole, partendo dalla storia che contenga almeno due stagionalità, questo metodo costruisce i numeri del futuro.
- \*\*Sai cosa rappresentano i fattori di smorzamento alfa, beta e gamma nel met\*\*

 :  : VOC Id="SKIM0320" Txt="Sai cosa rappresentano i fattori di smorzamento alfa, beta e gamma nel metod Holt Winters?"
Nel metodo Holt Winters, i fattori di smorzamento rappresentano quanto considera attendibile l'inizio della storia rispetto alla fine della storia. Se i fattori di smorzamento sono vicini a zero è più importante la fine della storia, viceversa se sono vicino a 1. Essendo la previsione scomponibile in tre componenti, livello, tendenza e stagionalità, ci sono tre fattori di smorzamento che sono rispettivamente alfa, beta e gamma.
- \*\*Sai qual è la base di dati per l'analisi Holt Winters?\*\*

 :  : VOC Id="SKIM0330" Txt="Sai qual è la base di dati per l'analisi Holt Winters?" Als="comm"
Può essere qualsiasi base storica, ma almeno di due stagionalità
- \*\*Sai come impostare una analisi Holt Winters in un ambiente Multiplant?\*\*

 :  : VOC Id="SKIM0340" Txt="Sai come impostare una analisi Holt Winters in un ambiente Multiplant?"
La distinzione tra plants, essendo la analisi di HW basata sui piani MPS, si traduce in una distinzione tra piani diversi, uno per ogni plant
- \*\*Sai cos'è il metodo autofit per l'analisi Holt Winters?\*\*

 :  : VOC Id="SKIM0350" Txt="Sai cos'è il metodo autofit per l'analisi Holt Winters?"
L'autofit è un metodo con cui viene effettuato il calcolo HW con diverse tripplette di alfa, beta e gamma, misurando l'errore delle serie risultanti e scegliendo poi la trippletta col minor errore.
- \*\*Sai cosa si intende per livello di servizio in una analisi Holt Winters?\*\*

 :  : VOC Id="SKIM0360" Txt="Sai cosa si intende per livello di servizio in una analisi Holt Winters?"
Il livello di servizio rappresenta la probabilità che una domanda incontri una disponibilità e viene utilizzato per calcolare la scorta minima HW che corregge opportunamente le previsioni raggiungendo una copertura che assicuri il livello di servizio
- \*\*Sai come si nettificano i dati previsivi derivanti dall'analisi Holt Winte\*\*

 :  : VOC Id="SKIM0370" Txt="Sai come si nettificano i dati previsivi derivanti dall'analisi Holt Winters per fornirli all'MRP?"
Si nettificano stornando l'ordinato dei periodi corrispondenti.
- \*\*Sai come si imposta la scorta integrativa Holt Winters ?\*\*

 :  : VOC Id="SKIM0380" Txt="Sai come si imposta la scorta integrativa Holt Winters ?"
Si imposta mettendo nel metodo di calcol dinamico della scorta (dati magazzino / articolo) l'elemento £01
- \*\*Sai come si fa ad ottenere un livello di servizio per una data classe prev\*\*

 :  : VOC Id="SKIM0390" Txt="Sai come si fa ad ottenere un livello di servizio per una data classe previsiva?"
In tabella MP2 si compila il livello di servizio nell'apposita casella della classe previsiva
- \*\*Sai come si fa ad ottenere un livello di servizio per un specifico articol\*\*

 :  : VOC Id="SKIM0400" Txt="Sai come si fa ad ottenere un livello di servizio per un specifico articolo , differente da quello della sua classe previsiva?"
Nei dati magazzino articolo, tramite la funzione F15 si accede ad una seconda schermata dove è possibile specificare il livello di servizio per l'articolo.
- \*\*Sai come si fa a verificare se una previsione è stata azzeccata?\*\*

 :  : VOC Id="SKIM0410" Txt="Sai come si fa a verificare se una previsione è stata azzeccata?"
Utilizzando il pgm MPCT001 che permette di analizzare i delta tra due viste
- \*\*Sai che relazione c'è tra MAPE, Numero di Toccate e Classe Previsiva?\*\*

 :  : VOC Id="SKIM0420" Txt="Sai che relazione c'è tra MAPE, Numero di Toccate e Classe Previsiva?"
In tabella MP2 si imposta una matrice che permette di assegnare ad un MAPE ed un numero di toccate , una determinata classe previsiva
- \*\*Sai impostare la fonte scorta minima che risalga da HW a standard?\*\*

 :  : VOC Id="SKIM0430" Txt="Sai impostare la fonte scorta minima che risalga da HW a standard?"
Nei parametri di definizione della scorta minima, tabella M5E o M5f (se datata) è possibile definire il tipo di risalita tra scorta HW e scorta GM
