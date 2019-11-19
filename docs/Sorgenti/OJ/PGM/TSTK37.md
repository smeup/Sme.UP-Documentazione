
 # Obiettivo
 Leggere dati da un Json.

 # Prerequisiti
 Necessita di avere in linea la libreria specifica per il parsing Json, copyright di Scott C.  Klement. Per ulteriori dettagli vedere qui : 
- [Parsing Json](Sorgenti/DOC/TA/B£AMO/WSBASE_01)

 ## Funzione GET metodo ATR. Reperisci attributo.
 Permette di reperire il valore di un attributo.

 ## Funzione GET metodo DEF. Reperisci definizione attributo.
 Permette di reperire la sola definizione di un attributo. Le definizioni degli attributi  sono indicate negli script SCP_INT, pertanto bisogna indicare nel campo £K37I_TI lo script  da cui reperirle.

 ## Funzione GET metodo ALL. Reperisci valore e definizione attributo.
 Permette di reperire tutte le informazioni di un attributo.

 Nel campo £K37I_PF va impostato il percorso IFS dove è presente il file Json.

 Nel campo £K37I_PA va impostato il percorso dell'attributo da reperire in questa modalità : 
 Nodo1\Nodo2\Array1(7)\Nodo3\Array2(5)\Attributo
 Il separatore è il "\" e la differenza tra il nodo e l'elemento array è l'indice tra parentesi.

 In output nel campo £K37O_NN viene riportato il nome dell'attributo (senza percorso, solo per  eventuale verifica) e nel campo £K37O_TA il tipo di attributo : 
 S - Stringa
 B - Booleano
 N - Numerico
 \* - null (indica il valore null per qualsiasi dei 3 tipi precedenti)

 Per il tipo Stringa e Booleano il valore verrà restituito nel campo £K37O_AL. Il campo £K37O_M5  può contenere il valore CONT per indicare che il valore continua, è pertanto rieseguire l'API  con gli stessi parametri per avere il resto del valore, se invece il campo £K37O_MS contiene FINE  è stato letto tutto il valore.
 Per il tipo Numerico il valore verrà restituito nel campo £K37O_NU

 Tutti gli altri campi di output, per i metodi che prevedono la restituzione della definizione  dell'attributo, provengono dalla definizione nello script in SCP_INT indicato nel parametro  £K37I_TI.

 ## Funzione POS metodo OGG. Posizionamento iniziale ai nodi di un oggetto.
 Nel campo £K37I_PA va impostato il percorso dell'oggetto su cui si vuole posizionarsi, per  poi procedere con la funzione LET metodo OGG per leggere i nodi in esso contenuti.

 ## Funzione LET metodo OGG. Lettura nodo successivo.
 In output nel campo £K37O_NN è presente il nome del nodo e nel campo £K37O_TA  è presente il tipo di nodo.
 Per eventualmente leggere il relativo valore utilizzare la funzione GET metodo ATR,  è possibile poi continuare la lettura dei nodi successivi, non viene perso il posizionamento.

 ## Funzione CLO. Chiudi json. RACCOMANDATO.
 Chiude il Json liberando l'area di memoria allocata. E' SEMPRE NECESSARIO eseguire questa funzione
 al termine dell'utilizzo di questa API per non lasciare impegnata memoria inutilmente.
