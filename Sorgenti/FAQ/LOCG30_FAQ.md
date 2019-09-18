- \*\*Sai cosa si intende con configuratore?\*\*

 :  : VOC Id="SKI10" Txt="Sai cosa si intende con configuratore?"
Il termine Configuratore, indica un generico questionario. Non è espressamente riferito ad una parte di Loocup dedicata alla configurazione di prodotti. In SmeUp, un configuratore è qualunque insieme di domande.
Altro concetto importante è la separazione tra presentazione delle domande e loro definizione.
Posso in questo modo creare archvi di domande che posso riutilizzare in più configuratori.
- \*\*Sai cosa si intende con configurazione?\*\*

 :  : VOC Id="SKI20" Txt="Sai cosa si intende con configurazione?"
La configurazione è un insieme di risposte o di impostazioni. Queste informazioni possono essere ottenute sia rispondendo a un insieme di domande, sia da un'insieme di operazioni grafiche (es. filtro su una matrice).
Altre configurazioni sono costituite dall'MDV.
- \*\*Quale è l'oggetto che identifica un configuratore?\*\*

 :  : VOC Id="SKI15" Txt="Quale è l'oggetto che identifica un configuratore?"
Un configuratore è identificato da un oggetto di tipo RE. Il parametro consente di identificare il tipo di configuratore.
- \*\*La configurazione a che oggetto SmeUp corrisponde?\*\*

 :  : VOC Id="SKI40" Txt="La configurazione a che oggetto SmeUp corrisponde?"
la configurazione è un oggetto di tipo CF, il parametro dipende dal configuratore che l'ha generata.
Le configurazioni di questionari Q- sono normalmente memorizzate nel CFVARI, mentre tutte le altre sono memorizzate nel B£MEDE.
Una configurazione può essere anche pensata come un setup.
- \*\*Sai quali sono i tipi di configuratori principali definiti in SmeUp?\*\*

 :  : VOC Id="SKI50" Txt="Sai quali sono i tipi di configuratori principali definiti in SmeUp?"
I tipi principali sono :  i questionari generici Q-,  i questionari di manutenzione delle tabelle SmeUp T- (Settore),i questionari definiti in script  L- (Setup esteso).
Nella scheda CFBASE sono visibili molti altri tipi di strutture :  quelli che vengono mostrati sono i tipi di configuratori/configurazioni possibli.
C'è una certa ambiguità tra tipo di configurazione e configuratore :  in teoria un configuratore di tipo X genera una configurazione di tipo X, in realtà esistono configurazioni non generate da un configuratore esplicito, ad esempio la MDV di un programma è l'insieme dei valori che l'utente ha inserito, ma non esiste l'insieme delle domande perchè queste sono cablate nella maschera.
Per i configuratori Q-, T- o L- invece le domande sono definite o nelle tabelle CFD o nel file TABDC o negli script del file SCP_CFG.
- \*\*Che tipi di configuratore sono definibili in SmeUp\*\*

 :  : VOC Id="SKI60" Txt="Che tipi di configuratore sono definibili in SmeUp"
I configuratori in SmeUp sono divisi per modalità di presentazione e di utilizzo :  abbiamo i configuratori in cui le sezioni vengono proposte all'utente una dopo l'altra (Questionari ), altri in cui le sezioni sono visibili come schede in cui non è stabilito un ordine di compilazione (Wizard), ed infine i configuratori mono sezione (Settore).
- \*\*Da cosa è composto un questionario?\*\*

 :  : VOC Id="SKI70" Txt="Da cosa è composto un questionario?"
Un questionario è composto da un insieme di sezioni, di domande e da un insieme di regole. Una sezione è composta da un gruppo di domande. Le regole sono facoltative, possono essere legate al questionario, alle sezioni e/o alle singole domande.
Un questionario presenta la prima sezione, una volta completata, viene presentata la sezione successiva.
- \*\*Esistono dei questionari predefiniti?\*\*

 :  : VOC Id="SKI80" Txt="Esistono dei questionari predefiniti?"
Con il termine Questionario identifichiamo un configuratore liberamente definibile, pertanto non ne esistono di predefiniti (esempi esclusi). Tutti i configuratori presenti in SmeUp guidano utenti, sviluppatori e responsabili del CED in varie attività (manutenzione di tabelle, editazione di script di schede, configurazione di LoocUp)
- \*\*Quale è l'utilizzo prevalente dei configuratori Q-\*\*

 :  : VOC Id="SKI90" Txt="Quale è l'utilizzo prevalente dei configuratori Q-"
l'utilizzo prevalente dei configuratori in cui le sezioni vengono proposte una dopo l'altra è nella creazione di questionari (es. q. di gradimento) o per configurare (articoli, ecc, ecc).  In questi configuratori, si possono associare delle regole esplicite che guidano nella compilazione. Tali regole possono attivare o diasattivare sezione e/o domande, aggiungere e/o rimuovere valori alle risposte.
- \*\*Sai cosa sono le regole\*\*

 :  : VOC Id="SKI100" Txt="Sai cosa sono le regole"
le regole sono dei vincoli che guidano nella compilazione del configuratore. Possono essere implicite o esplicite. Le regole implicite sono derivate dalla definizione delle domande :  obbligatoria/facoltativa, con elenco di valori associati o tipizzati ecc. Esplicite sono le regole espresse nel linguaggio delle regole. Queste in funzione delle risposte fornite possono validare la risposta, modificare la struttura del configuratore, assegnare risposte. Per la definizione delle regole fare riferimento al manuale
- \*\*Conosci come sono organizzate le regole e l'ordine di valutazione?\*\*

 :  : VOC Id="SKI110" Txt="Conosci come sono organizzate le regole e l'ordine di valutazione?"
Le regole sono organizzate per questionario, sezione e domanda.
Sono a valutazione preventiva (PRE) o posticipata (POS). Tutte le regole sono facoltative.
All'avvio di una nuova configurazione, il motore delle regole, inzia a valutare le pre regole del configuratore (se presenti), poi valuta le pre regole della prima sezione e le preregole delle domande della prima sezione. ad ogni risposta fornita, per ogni domanda vengono valutate le preregole della prima domanda, poi le post regole della prima domanda e così via per tutte le domande della prima sezione. Quando l'utente preme il pulsante avanti, verranno valutate le post regole della prima sezione. L'ordine di valutazione delle regole prosegue in modo analogo per ogni sezione.
Alla conclusione dell'ultima sezione verranno valutate le posteregole del configuratore.

