- **Cosa si intende con configuratore?**

 :  : VOC Id="SKIA0010" Txt="Cosa si intende con configuratore?"
Il termine Configuratore, indica un generico insieme di domande. Non è espressamente riferito ad un software per la configurazione di un articolo.
- **Quale è l'oggetto che identifica un configuratore?**

 :  : VOC Id="SKIA0020" Txt="Quale è l'oggetto che identifica un configuratore?"
Un configuratore è identificato da un oggetto di tipo RE. Il parametro consente di identificare il tipo di configuratore, ovvero di determinare il comportamento del configuratore.
- **Sai cosa si intende con configurazione?**

 :  : VOC Id="SKIA0030" Txt="Sai cosa si intende con configurazione?"
La configurazione era inizialmente definita come un insieme di risposte, ottenute dalla compilazione di  un configuratore. Successivamente si è esteso il concetto includendo LOCK, MDV, setup e tutto quanto viene memorizzato nel file B£MEDE.
- **La configurazione a che oggetto Sme.Up corrisponde?**

 :  : VOC Id="SKIA0040" Txt="La configurazione a che oggetto Sme.Up corrisponde?"
 :  la configurazione è un oggetto di tipo CF, il parametro è composto dal tipo del configuratore concatenato al codice del configuratore, e da un codice.
- **Quali sono i principali tipi di configuratori definiti in Sme.Up?**

 :  : VOC Id="SKIA0050" Txt="Quali sono i principali tipi di configuratori definiti in Sme.Up?"
I tipi principali sono : 
- i questionari, oggetti di tipo Q-, sono configuratori generici, la definizione spetta all'utente.
- i configuratori di manutenzione delle tabelle Sme.Up, oggetti di tipo T- (Settore), la definizione è vincolata all'installazione di Sme.Up.
- i configuratori definiti in script.
- **Da cosa è composto un configuratore?**

 :  : VOC Id="SKIA0060" Txt="Da cosa è composto un configuratore?"
Un configuratore è composto da un insieme di domande, raggruppate in una o più sezioni. Una sezione si può immaginare come una pagina. Alcuni configuratori possono avere delle regole che guidano l'utente nella compilazione e nella validazione delle risposte.
- **Sai quali sono le modalità di presentazione dei configuratori?**

 :  : VOC Id="SKIA0070" Txt="Sai quali sono le modalità di presentazione dei configuratori?"
I configuratori si possono presentare sotto forma di wizard, in cui le sezioni sono si presentano come un insieme di schede, con un albero di navigazione e la sezione corrente, oppure con un'unica sezione. Nei primi l'utente può saltare da una sezione all'altra, nei secondi l'ordine di compilazione va dalla prima sezione all'ultima.
- **Cosa si intende con Questionario e quale è il suo utilizzo principale?**

 :  : VOC Id="SKIA0080" Txt="Cosa si intende con Questionario e quale è il suo utilizzo principale?"
Un questionario è un configuratore di tipo Q-. La struttura è definita dall'utente/installatore e nasce per risolvere specifici problemi applicativi, ad esempio per configurare un prodotto per raccogliere il feedback di persone ecc ecc. E' utile in tutti i caso in cui si ha la necessità di porre domande e raccogliere le risposte.
- **Da cosa è composto un questionario?**

 :  : VOC Id="SKIA0090" Txt="Da cosa è composto un questionario?"
Un questionario è composto da un insieme di sezioni, di domande e da un insieme di regole. Una sezione è composta da un gruppo di domande. Le regole sono facoltative, possono essere legate al questionario, alle sezioni e/o alle singole domande.
Un questionario presenta la prima sezione, una volta completata, l'utente passa a compilare la sezione successiva e così via fino all'ultima sezione.
- **Esistono dei questionari predefiniti?**

 :  : VOC Id="SKIA0100" Txt="Esistono dei questionari predefiniti?"
Con il termine Questionario identifichiamo un configuratore liberamente definibile, pertanto non ne esistono di predefiniti. Tutti i configuratori presenti in Sme.Up aiutano utenti, sviluppatori e responsabili del CED in varie attività (manutenzione di tabelle, editazione di script di schede, configurazione di Looc.Up ecc.)
- **Perché nella scheda CFBASE sono definiti così tanti tipi di tracciato?**

 :  : VOC Id="SKIA0110" Txt="Perché nella scheda CFBASE sono definiti così tanti tipi di tracciato?"
Perché un tracciato identifica l'origine delle domande di un configuratore e/o il tipo di configurazione. Esistono in Sme.Up configurazioni che non hanno un configuratore definito :  ad esempio la MDV. Aver catalogato tutte le configurazioni consente di memorizzarle in un unico archivio.
- **Quale è il significato dei tipi di tracciato?**

 :  : VOC Id="SKIA0120" Txt="Quale è il significato dei tipi di tracciato?"
Con tipo di tracciato si intende la struttura, ovvero le domande che hanno originato la configurazione. Nel caso in cui non esista un configuratore che ha originato la configurazione, si intende un tipo di configurazione gestibile da uno specifico programma.
Vediamo nel dettaglio il significato delle varie strutture : 
-  F. Fonte (LOA15) :  c'è un costruttore LOA15 che è una specie di cubo, viene scritto un file per ogni estrazione, e questa fonte permette di analizzare il file specifico dell'estrazione
- F- File :  permette di avere la struttura di configuratori associati a file Sme.Up :  ogni colonna crea una domanda. NON UTILIZZATO
- T- Settore (tabelle Sme.Up) permette di avere la struttura delle tabelle Sme.Up
- T. - permette di avere in ritorno tutti i campi della tabella, file + sottostringhe di TTLIBE/TTUSER compresi
- T/ :  Settore completo - TO DO da completare
- R- :  Formato libero - TO DO da completare
- Q- :  Questionario, permette di avere la struttura dei questionari utente.
- Q. :  Query, permette di avere la struttura dei questionari di ricerca di oggetti.
- O- :  in pratica ti ritorna tutti gli attribuiti di un oggetto
- M. :  Modello - consente di avere la struttura dei questionari di modello
- C- :  non sono implementati. Ritorna l'elenco dei parametri collegati da un elemento della C£E
- G- :  erano/sono utilizzati nei setup di loocup?
- L- :  Setup esteso, consente di avere la struttura di questionari/configurazioni di wizard e/o setup
- U- :  configurazioni utente :  permette di avere i setup utente, il relativo configuratore è spesso un frammento di uno script SCP_CFG
- M- :  MDV consente di accedere alle MDV
- K- :  LOCK - consente di avere accesso ai lock
- I- :  non implementati
- S- :  Script configurazione - configurazioni di modulo
- J- :  Setup di componente
- V. :  permette di analizzare un tracciato parametrizzato del D5COSO
- S. :  erano/sono utilizzati nei setup di loocup?
- **Quale è l'utilizzo prevalente dei configuratori Q- (Questionari)?**

 :  : VOC Id="SKIA0130" Txt="Quale è l'utilizzo prevalente dei configuratori Q- (Questionari)?"
L'utilizzo prevalente dei configuratori Q- è nella creazione di questionari (es. q. di gradimento) o per configurare prodotti (articoli, ecc, ecc).  In questi configuratori, si possono associare delle regole esplicite che guidano nella compilazione. Tali regole possono visualizzare o nascondere sezione e/o domande, aggiungere e/o rimuovere opzioni alle domande chiuse e validare le risposte.
- **Dove sono definite le domande?**

 :  : VOC Id="SKIA0140" Txt="Dove sono definite le domande?"
Per i configuratori Q- le domande sono definite o nella tabella CFD e sottosettori, o dentro i membri del file SCP_CFG. Per i configuratori di wizard o setup sono definite dentro i membri del file SCP_CFG. Per i configuratori T- sono definite nel file TABDC, mentre per gli altri casi, le domande sono implicite o non esistono :  l'interpretazione della configurazione è fatta da programma.
- **Sai cosa sono le regole?**

 :  : VOC Id="SKIA0150" Txt="Sai cosa sono le regole?"
Le regole sono dei vincoli che guidano nella compilazione del configuratore. Possono essere implicite o esplicite. Le regole implicite sono derivate dalla definizione delle domande :  obbligatoria/facoltativa, con elenco di valori associati o tipizzati ecc. Esplicite sono le regole espresse nel linguaggio delle regole. Queste in funzione delle risposte fornite possono validare la risposta, modificare la struttura del configuratore, o assegnare risposte. Per la definizione delle regole fare riferimento al manuale tecnico, disponibile nel modulo CFBASE.
- **Conosci come sono organizzate le regole e l'ordine di valutazione?**

 :  : VOC Id="SKIA0160" Txt="Conosci come sono organizzate le regole e l'ordine di valutazione?"
Le regole sono organizzate per questionario, sezione e domanda.
Sono a valutazione preventiva (PRE) o posticipata (POS). Tutte le regole sono facoltative.
All'avvio di una nuova configurazione, il motore delle regole, inizia a valutare le pre regole del configuratore (se presenti), poi valuta le pre regole della prima sezione. Ad ogni risposta fornita, per ogni domanda vengono valutate le preregole della prima domanda, poi le post regole della prima domanda e così via per tutte le domande della prima sezione. Questo comportamento è determinato dal fatto che l'ordine di compilazione delle domande all'interno di una sezione non è predeterminato e in ogni caso, devo garantire la congruenza a fronte di una modifica delle risposte fornite. Quando l'utente preme il pulsante avanti, verranno valutate le post regole della prima sezione. L'ordine di valutazione delle regole prosegue in modo analogo per ogni sezione.
Alla conclusione dell'ultima sezione verranno valutate le posteregole del configuratore.
- **Conosci come è possibile costruire i questionari Q-?**

 :  : VOC Id="SKIA0170" Txt="Conosci come è possibile costruire i questionari Q-?"
I questionari Q- sono definiti nel settore CFQ. Per la loro costruzione è possibile utilizzare il settore CFS   oppure utilizzare gli script SCP_CFG. Nel caso di utilizzo delle tabelle CFS sarà necessario specificare il sottosettore e il questionario potrà attingere alle sole sezioni definite in quel sottosettore.
Nel caso si decida di utilizzare uno script, questo dovrà essere creato nel file EDT_SCH.
La costruzione della struttura del questionario mediante le tabelle CFQ, CFS, e CFD consente la maggiore flessibilità nella costruzione dei questionari.
Per contro l'utilizzo degli script consente una maggiore velocità nella costruzione.
- **Conosci come è possibile associare le sezioni a un configuratore?**

 :  : VOC Id="SKIA0180" Txt="Conosci come è possibile associare le sezioni a un configuratore?"
Un configuratore come default attinge a tutte le sezioni presenti nel sottosettore indicato, è però anche possibile definire un prefisso oppure indicare le sezioni che gli appartengono mediante il parametro CF1. L'utilizzo del parametro consente grande flessibilità nella costruzione dei questionari perché potrei utilizzare un unico sottosettore per tutti i questionari e associare le sezioni in base alla necessità. Per contro va posta attenzione alle modifiche delle parti comuni.
- **Conosci come è possibile associare le domande a una sezione?**

 :  : VOC Id="SKIA0190" Txt="Conosci come è possibile associare le domande a una sezione?"
Esistono i seguenti metodi per reperire le domande di una sezione : 
- Domande con Prefisso=Sezione (le domande sono definite nel settore CFD)
- Definite in parametro  (le domande sono definite nel settore CFD)
- Con prefisso indicato  (le domande sono definite nel settore CFD)
- Da programma utente  (le domande sono costruite da programma)
- File  (le domande sono lette dalle definizioni delle colonne)
- Tabella   (Settore)
- Questionario (le domande sono lette dal questionario indicato).  Questo consente di
-- superare il vincolo del sottosettore
-- superare il vincolo di usare solo lo script :  il questionario di esempio potrebbe attingere la sua struttura da script e potrei comunque utilizzare le sezioni definite nella CFD.

- Cat.parametri  restituisce le domande della categoria parametri indicata. Va posta attenzione a questa possibilità in quanto si rischia che le domande abbiano codice ripetuto. Il configuratore ha bisogno che ogni domanda abbia un codice univoco.
- **Costruzione di Questionari Q- :  meglio un sottosettore di CFS e CFD per ogn**

 :  : VOC Id="SKIA0200" Txt="Costruzione di Questionari Q- :  meglio un sottosettore di CFS e CFD per ogni questionario o raggruppare le sezioni e o domande?"
Utilizzare un sottosettore per ogni configuratore consente la massima facilità di manutenzione ma riduce le possibilità di riutilizzo, per contro utilizzare un solo sottosettore per tutti i configuratori complica la manutenzione ma consente il massimo riutilizzo.
- **Sai quali sono i limiti per i vari oggetti in gioco?**

 :  : VOC Id="SKIA0210" Txt="Sai quali sono i limiti per i vari oggetti in gioco?"
Il codice del configuratore non deve essere più lungo di 8 caratteri in quanto viene concatenato al tipo e utilizzato come parametro dell'oggetto CF.
Si consiglia di limitare il codice delle sezioni a 3/4 caratteri e quello delle domande a massimo 13 caratteri.
Le regole devono essere più corte di 25.000 caratteri :  in caso di regole molto lunghe distribuirle su più oggetti

Per le configurazioni salvate sul CFVARI : 
La lunghezza della risposta di una domanda è di massimo 100 caratteri
La somma delle lunghezze delle risposte di una domanda configurata è di 100 caratteri. Venendo memorizzate in modalità posizionale contano anche le risposte non fornite.
Non è possibile memorizzare configurazioni in cui le sezioni e/o le domande sono ripetibili.

Per le configurazioni memorizzate nel B£MEDE : 
Devono essere lunghe al max 30.000 caratteri.
- **Conosci l'utilizzo dell'induzione dinamica?**

 :  : VOC Id="SKIA0220" Txt="Conosci l'utilizzo dell'induzione dinamica?"
L'induzione dinamica è una tecnica che consente di estendere le potenzialità del configuratore :  è possibile agganciare alla risposta fornita il richiamo di un programma su AS400. Questo programma può aggiungere domande,  variare le opzioni disponibili e  modificare le risposte. Per agganciare il programma vedere la documentazione della tabella CFD. Programmi di esempio sono i CFVLD_xx.
- **Conosci le sezioni ripetibili o con inclusione?**

 :  : VOC Id="SKIA0230" Txt="Conosci le sezioni ripetibili o con inclusione?"
Le sezioni di un configuratore possono essere compilate più volte o includere un configuratore (con tutte le sue sezioni).
Il numero di ripetizioni può essere fisso, oppure posso condizionarlo ad una domanda.
L'inclusione consente di includere un intero configuratore, mantenendolo diviso in tutte le sue sezioni.
Queste due possibilità si possono combinare.
Si faccia riferimento alla documentazione della tabella CFS per i dettagli.
- **Dove trovo la documentazione delle regole?**

 :  : VOC Id="SKIA0240" Txt="Dove trovo la documentazione delle regole?"
La documentazione delle regole è disponibile nel documento CFBASE_TEC
- **Come e dove sono salvate le risposte di un questionario?**

 :  : VOC Id="SKIA0250" Txt="Come e dove sono salvate le risposte di un questionario?"
La modalità con la quale vengono salvate le risposte di un questionario dipende dall'attributo "Salvataggio esteso" della tabella CFQ. Il default è blank, ovvero le risposte sono memorizzate in verticale nel CFVARI :  ogni risposta è memorizzata in un record. E' possibile accedere alle risposte utilizzando gli OAV C/cod_conf/domanda.  Nel caso di salvataggio esteso le risposte sono memorizzate nel B£MEDE in formato XML :   vi è un unico record.
- **Esistono degli OAV per leggere le risposte di una configurazione?**

 :  : VOC Id="SKIA0260" Txt="Esistono degli OAV per leggere le risposte di una configurazione?"
Se la configurazione è memorizzata nel CFVARI, è possibile utilizzare gli OAV C/codice_configurazione/codice_domanda.
- **Come faccio ad associare un'immagine alla risposta?**

 :  : VOC Id="SKIA0270" Txt="Come faccio ad associare un'immagine alla risposta?"
E' necessario agire sul campo "Parametro di presentazione" della tabella CFD. Si può decidere quale formato e se abilitare o meno la risalita. Le opzioni possibili per il formato sono le seguenti : 
blank :  Non mostrare immagine
1 :  Immagine piccola  :  verrà cercata l'immagine "codice_immagine"_1.xxx
2 :  Immagine media  :  verrà cercata l'immagine "codice_immagine"_2.xxx
3 :  Immagine grande  :  verrà cercata l'immagine "codice_immagine"_3.xxx
L :  Formato libero  :  verrà cercata l'immagine "codice_immagine".xxx
D :  Dimensioni come default  :  verrà cercata l'immagine "codice_immagine".xxx e impostata la larghezza di 400 pixel, mantenendo le proporzioni.
L'immagine verrà ricercata secondo le logiche descritte nel documento LOBASE_06, eventualmente effettuando tutte le risalite se abilitata.
- **Si possono utilizzare le immagini per scegliere le risposte?**

 :  : VOC Id="SKIA0280" Txt="Si possono utilizzare le immagini per scegliere le risposte?"
Sì, fare riferimento alla documentazione della tabella CFD, campo Parametro di presentazione.
- **Conosci le categorie delle domande?**

 :  : VOC Id="SKIA0290" Txt="Conosci le categorie delle domande?"
La categoria della domanda è un parametro che consente di definire come la domanda si presenta. Fare riferimento alla documentazione della tabella CFD.
- **Conosci le domande configurate e come utilizzare le risposte?**

 :  : VOC Id="SKIA0300" Txt="Conosci le domande configurate e come utilizzare le risposte?"
Le domande configurate consentono di raggruppare più domande in un'unica. Possono essere a risposta singola o a risposta multipla.
Le risposte aggiuntive vengono memorizzate in un campo di 100 caratteri e formattate a larghezza fissa. I numeri vengono memorizzati nel formato usato per scrivere nel TABEL.
Per utilizzare le risposte, va definita una schiera che rispecchi la struttura della domanda configurata, e va mosso il campo C£PARA nella struttura definita.

- **Quali sono i limiti dell utilizzo delle sezioni con ripetizione e/o inclus**

 :  : VOC Id="SKIA0236" Txt="Quali sono i limiti dell utilizzo delle sezioni con ripetizione e/o inclusione?"
Utilizzando questa modalità di costruzione dei questionari, le risposte verranno restituite in formato XML e memorizzate nel B£MEDE. La struttura delle risposte rispecchierà quella del questionario :  se ad esempio una sezione è ripetuta avrò n blocchi di risposte legati alla sezione.
In questo caso non saranno disponibili gli OAV per accedere alle risposte fornite, ma si dovrà procedere scrivendo un apposito programma.
- **Conosci le opzioni del campo Parametro di presentazione nella tabella CFD?**

 :  : VOC Id="SKIA0265" Txt="Conosci le opzioni del campo Parametro di presentazione nella tabella CFD?"
Questo parametro consente operare sulle modalità di presentazione della domanda e sulle modalità di compilazione. Posso ad esempio decidere di agganciare una nota o di mostrare l'immagine della risposta. Per i dettagli fare riferimento alla documentazione della tabella CFD.
- **Posso agganciare una regola a una domanda configurata?**

 :  : VOC Id="SKIA0310" Txt="Posso agganciare una regola a una domanda configurata?"
No, non è possibile agganciare una regola ad una domanda configurata. E' però possibile sapere quante risposte sono state fornite ed accedere ai valori di ogni sotto domanda.  Posso pertanto agganciare il controllo alla domanda successiva oppure ad una postregola della sezione
- **Conosci gli script del file SCP_CFG**

 :  : VOC Id="SKIA0320" Txt="Conosci gli script del file SCP_CFG"
Gli script presenti nel file SCP_CFG sono dei configuratori.
Possono essere monoquestionario o multi questionario, ad esempio EDT_SCH è multi questionario :  ogni tag è un configuratore che può avere una sola sezione (es. G.SET.LAB) o multi sezione (es. G.SET.MAT).
Gli script multi questionario sono composti da 4 parti :  nella prima parte ci sono le parti comuni a più tag, segue poi una parte in cui vengono definiti quali sono i vari configuratori (TAG), e come le risposte devono essere formate, segue poi la parte di definizione dei configuratori ed infine la parte con le opzioni.
Negli script mono questionario manca la parte di definizione dei configuratori.
Gli script EDT_xxx sono dedicati alla manutenzione di script, ad esempio EDT_SCH contiene le definizioni dei tag presenti negli script di scheda, EDT_DOC contiene le definizioni dei tag degli script di documentazione ecc. ecc.
Esistono poi degli script che hanno codice di 6 caratteri, composto da AAMMMM, ovvero AA=codice applicazione e MMMM=codice modulo, sono utilizzati nel relativo modulo SmeUp.

E' importante sapere che si possono definire script liberamente, o per utilizzarli nella definizione di questionari oppure per richiedere parametri quando si lanciano servizi, utilizzando la tecnica dell'SP.
- **Conosci come fare dipendere una domanda da una altra?**

 :  : VOC Id="SKIA0330" Txt="Conosci come fare dipendere una domanda da una altra?"
Esistono vari metodi e dipendono dal tipo di questionario :  se ho un questionario posso scrivere una regola, posso definire il tipo di un oggetto come dipendente da un'altra risposta, oppure posso usare i campi Soggetto condizionamento  / Oggetto condizionamento.
Se invece ho non ho un questionario posso utilizzare solo la tipizzazione dipendente da un'altra risposta.
Vediamo queste tre opzioni.
Per la scrittura di una regola fare riferimento al manuale LOBASE_TEC, se invece si desidera tipizzare una domanda usando una risposta di un'altra vanno usate le parentesi quadre : 
.Tip Tipo oggetto                       OG                      002
.Par Parametro                          OG                 020
Infine per l'utilizzo dei campi Oggetto condizionamento / soggetto condizionamento fare riferimento alla documentazione della tabella CFD
- **Conosci gli oggetti J5?**

 :  : VOC Id="SKIA0340" Txt="Conosci gli oggetti J5?"
Gli oggetti J5 consentono di racchiudere in un'unica domanda un'intera configurazione. Nel parametro dell'oggetto viene espresso il configuratore e il formato della risposta, mentre il codice è la configurazione.
Ad esempio tipo=J5, parametro= EDT_SCH/G.SET.MAT;P significa che verrà costruito un questionario utilizzando le domande definite nello script EDT_SCH, tag G.SET.MAT e il formato della risposta sarà Dom1(Risp1) Dom2(Ris2) ...DomN(RisN).
Altri formati supportati sono quello XML-Like :  Dom1="Ris1" e il formato posizionale.

Va posta attenzione se si desidera utilizzarli nei questionari (Configuratori Q-) :  la lunghezza massima della risposta è di 100 caratteri.

- **Conosci gli oggetti J1 STR_xxx?**

 :  : VOC Id="SKIA0350" Txt="Conosci gli oggetti J1 STR_xxx?"
Gli oggetti J1 STR_xxx sono oggetti utilizzati principalmente negli script di configurazione e consentono l'editazione di stringhe in formato controllato dal servizio B£SER_17.

Abbiamo ad esempio l'oggetto STR_SQL che consente l'immissione di stringhe SQL e utilizzato nel comando UP SQL, l'oggetto STR_MGRU per la definizione dei gruppi di una matrice.
- **Sai dove sono gli esempi e gli ambienti di test?**

 :  : VOC Id="SKIA1000" Txt="Sai dove sono gli esempi e gli ambienti di test?"
Un esempio applicativo è sull'SRVAMM.SMEUP.COM ambiente D33.
In questo ambiente, è stata preparata una scheda che consente di gestire i campioni.
Il configuratore aiuta nella definizione dei campioni, le risposte raccolte vengono poi utilizzate per completare distinta e ciclo.
Per chiarimenti contattare Paolo Belotti.

Gli esempi per comprendere come costruire un configuratore sono disponibili sull'AS400A.SMEA.IT ambiente D35.

- **Conosci i servizi utilizzati dal configuratore?**

 :  : VOC Id="SKIA0360" Txt="Conosci i servizi utilizzati dal configuratore?"
I servizi utilizzati dal configuratore sono il CFSER_01 e il CFSER_02, CFVPU_xx e CFVLD_xx.

Il primo restituisce le configurazioni salvate e informazioni sugli oggetti in gioco (Questionario, Sezioni, Domande e Valori) .
Il secondo si occupa della costruzione della struttura dei questionari e del salvataggio delle configurazioni.
CFVPU_xx è una categoria di servizi che possono essere utilizzati per la costruzione di sezioni in modo personalizzato :  si veda la documentazione della tabella CFS
CFVLD_xx è una categoria di servizi per la gestione dell'induzione dinamica. Si veda la documentazione della tabella CFD per i dettagli.
- **Come posso utilizzare le risposte fornite per configurare un'articolo?**

 :  : VOC Id="SKIA0370" Txt="Come posso utilizzare le risposte fornite per configurare un'articolo?"
Il Configuratore non nasce con l'obbiettivo di personalizzare un'articolo generico.
Il suo scopo è quello di raccogliere risposte e depositarle nel CFVARI o B£MEDE.

Per passare dalle risposte raccolte ad un articolo finito, è necessario un intervento mediante un programma scritto ad hoc.

Una tecnica che consente di minimizzare le operazione è quella di dare alle domande un codice corrispondente alla colonna del BRARTI.

Un'altra tecnica è di personalizzare il CFSER_02,  aggiungendo dopo il salvataggio il richiamo del programma che utilizza le risposte.
- **Come posso aggiungere una descrizione esplicativa a sezioni e domande di u**

 :  : VOC Id="SKIA0380" Txt="Come posso aggiungere una descrizione esplicativa a sezioni e domande di un Questionario?"
Nel caso sia necessario aggiungere delle descrizioni aggiuntive a sezioni e domande va abilitata l'opzione "Descrizioni Estese" sulla sezione.
Il questionario cercherà delle note strutturate associate alla sezione e alle domande contenute.

Per i dettagli consultare la documentazione della tabella CFS.
- **Sai quali sono i passi minimi per creare un Questionario?**

 :  : VOC Id="SKIA0085" Txt="Sai quali sono i passi minimi per creare un Questionario?"
1) Definzione del sottosettore della CFS e della CFD (opzionale ma fortemente consigliato)
2) Creazione elemento tabella B£G (Obbligatorio :  definisce il metodo di salvataggio della configurazione). Si consiglia
3) Creazione di un elemento nella tabella CFQ
4) Definzione delle sezioni
5) Definizione delle domande
