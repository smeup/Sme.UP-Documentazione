## Struttura e contenuto documentazione operativa
Obiettivo della documentazione operativa è spiegare all'utente tutte le possibilità che ha a disposizione ogni volta che si trova di fronte a una qualsiasi finestra di SmeUP. Per raggiungere questo scopo si è deciso di strutturare la documentazione operativa in 4 capitoli principali con i relativi sottocapitoli : 
 \* Obiettivo :  riporta la finalità dell'interrogazione
 \* Formato guida :  all'interno del formato guida va specificato il significato di tutti i campi presenti. Inoltre al suo interno è necessario inserire i seguenti sottocapitoli : 
 \*\* Impostazioni :  riporta il dettaglio di tutti i campi presenti all'interno delle impostazioni
 \*\* Tasti funzionali :  riporta il significato di tutti i tasti funzionali disponibili
 \*\* Tips&tricks :  in questo paragrafo sono riportate tutte le possibilità presenti all'interno del formato guida e che non sono specificate nella parte sopra (es :  disponibilità mdv, disponibilità parzializzazioni, caratteri speciali per le ricerche, possibilità di inserire date dinamiche, ecc.). In questo sottocapitolo sono incluse, quindi, alcune possibilità 'generali' di SmeUP :  queste caratteristiche sono generalmente documentate all'interno del modulo B£ è, quindi, necessario inserire il riferimento alla documentazione specifica.
 \* Formato lista :  all'interno del formato lista vanno specificate le informazioni riportate per ogni record. al suo interno è necessario specificare i seguenti sottocapitoli : 
 \*\* Opzioni :  vanno specificate tutte le opzioni disponibili per ogni record
 \*\* Impostazioni :  se non sono state documentate le impostazioni all'interno del formato guida (perché non presente) specificarle all'interno del formato lista; in caso contrario inserire un richiamo alla documentazione del formato guida
 \*\* Tasti funzionali :  se non sono stati documentati all'interno del formato guida (perché non presente) specificarli all'interno del formato lista; in caso contrario inserire un richiamo alla documentazione del formato guida
 \*\* Tips&Tricks :  in questo paragrafo sono riportate tutte le possibilità presenti all'interno del formato lista e che non sono specificate nella parte sopra (es :  ricerche di stringhe tramite F1, stampa delle liste tramite F4, utilizzo del campo posizionamento, parzializzazioni, ecc.). Se queste possibilità sono documentate riportare il link alla documentazione.
 \* Formato dettaglio :  vanno specificate tutte le informazioni di dettaglio visualizzate. Sottocapitoli da documentare : 
 \*\* Tasti funzionali :  riportare il significato di tutti i tasti funzionali disponibili
 \*\* Tips&Tricks :   in questo paragrafo sono riportate tutte le possibilità presenti all'interno del formato dettaglio e che non sono specificate nella parte sopra (es :  accesso alle schede oggetti di LoocUP cliccando sulle icone, ecc).

 La struttura dello script della documentazione operativa deve seguire la seguente : 
![B£DOCU_001](http://doc.smeup.com/immagini/B£DOCU_12/BXDOCU_001.png)
## Inclusione di altri documenti
Il comando I.INC.MBR Fil(NomeFile) Mem(NomeMembro) permette di includere altri documenti all'interno di un testo. In particolare utilizzando questo comando il documento scritto nel membro indicato verrà esploso : 
Durante il processo di inclusione è possibile, attraverso opportuni parametri, l'importazione di una parte del documento richiesto : 
-  Sec - Importa solo il tag richiesto
-  SAt - Una volta incontato il tag richiesto, questo deve possedere l'attributo richiesto per poter essere imporato. Questi valori possono essere multipli (Separati da spazio) solo se trattasi di membri SCP_CFG.
-  SeE - Una volta incontrato il tag richiesto, ferma l'importazione quando incontri il tag righiesto. Non attivo se trattasi di membgri SCP_CFG.
Vengono applicate le seguenti limitazioni : 
-  Se presente l'attributo Id(...) il SAt(...)  deve corrispondere.
-  Se titolo il SAt(...) deve corrispondere al titolo
-  Negli altri casi il SAt(...) deve essere presente nella riga
L'importazione viene interrotta quando si incontra lo stesso Sec(...) di inizio.
L'importazione non viene interrotta al primo evento, ma viene scansionato l'intero membro dando così la possibilità di includere più elementi anche non sequenziali fra loro.
in alternativa si può utilizzare il parametro
-  SeE - Importa tutto il documento fermandosi quando si incontra il tag impostato.

_3_Esempio di esplosione della voce Upper processes con comando INC.MBR Sec(VOC) SAt(UP) : 
- [Acronimi Sme.up](Sorgenti/MB/DOC_VOC/GLO_ACR_01)
_3_Fine esempio di esplosione di documento con comando INC.MBR : 

_3_Esempio di esplosione dello Sviluppo personalizzazioni e interfacce e termine al primo sottotitolo con comando INC.MBR Sec(T02) SAt(Sviluppo personalizzazioni e interfacce) SeE(T03) : 
- [Implementazione](Sorgenti/DOC/TA/B£AMO/A£BASE_P0G)
SeE(###)
_3_Fine esempio di esplosione di documento con comando INC.MBR : 

_3_Esempio di esplosione della Customizzazione tabelle con termine al primo sottotitolo con comando INC.MBR Sec() SAt() SeE(T03) : 
- [Implementazione](Sorgenti/DOC/TA/B£AMO/A£BASE_P0G)
_3_Fine esempio di esplosione di documento con comando INC.MBR : 

_3_Esempio di esplosione del Indipendenza dalla piattaforma  con comando INC.MBR Sec(T03) SAt(Tasti funzionali) : 
- [Definizioni interfacce](Sorgenti/DOC/TA/B£AMO/A£BASE_SF)
_3_Fine esempio di esplosione di documento con comando INC.MBR : 

_3_Esempio di esplosione di documento con comando INC.MBR : 
- [Liste oggetti](Sorgenti/DOC_OPE/TA/B£AMO/B£_LIS)
_3_Fine esempio di esplosione di documento con comando INC.MBR : 

## Link ad altri documenti
Attraverso il comando DEC è possibile introdurre un link a un altro documento che sarà possibile esplodere o meno settando il parametro L (si veda il wizard per maggiori dettagli)
_3_Esempio di inserimento di un link a un documento con comando DEC : 
- [Liste oggetti](Sorgenti/DOC_OPE/TA/B£AMO/B£_LIS)
_3_Fine esempio di inserimento di un link a un documento con comando DEC : 

## Elementi grafici del documento
Tutti gli elementi costitutivi del corredo grafico del documento che viene generato sono immagini di oggetti.
Per elementi costitutivi del corredo grafico del documento si intende :  la copertina prima pagina, il logo aggiuntivo della prima pagina, la copertina di fine documento, l'header di pagina ed il footer di pagina.
La loro eventuale personalizzazione passa per la personalizzazione delle immagini degli oggetti.
Gli elementi e gli oggetti SmeUP relativi sono : 
-  Sfondo prima pagina :  oggetto VO; COD_SEL; SFO_000
-  Sfondo ultima pagina :  oggetto VO; COD_SEL; SFO_002
-  Logo prima pagina :  oggetto VO; COD_SEL; LOG_000
-  Header di pagina :  oggetto VO; COD_SEL; HEA_000
-  Footer di pagina :  oggetto VO; COD_SEL; FOO_000
