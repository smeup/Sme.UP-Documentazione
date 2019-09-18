- **Quale è la logica di denominazione delle UPP?**

 :  : VOC Id="00001" Txt="Quale è la logica di denominazione delle UPP?"
Un'istanza di upp ha un codice strutturato in modo significativo. E' infatti sempre definito nel seguente modo : 
\* Due caratteri che definiscono l'applicazione di appartenenza
\* Un underscore
\* 3 caratteri alfanumerici univoci :  questi caratteri da soli identificano già di per se in modo univoco la "upp"

Avremo quindi codici simili a questi : 
\* A£_001
\* C5_002

E' importante rimarcare nuovamente che gli ultimi 3 caratteri sono univoci di per loro e che quindi non esisterà mai un upp C5_001, in quanto il codice 001 è stato già usato dall'upp A£_001.

I caratteri univoci possono essere sia numerici che alfa e non hanno un significato particolare, se non che il carattere inziale X :  esso infatti identifica il fatto che la upp è un upp custom di un cliente non un upp standard.

Esiste poi la UPP personale che esiste solo nella libreria W_utente che ha codice fisso A£_USR.

- **Tutte le UPP saranno nell'UppStore?**

 :  : VOC Id="00002" Txt="Tutte le UPP saranno nell'UppStore?"
No, ci saranno pubblicate solo le UPP con un valore applicativo commerciale. Il fatto che un UPP sia pubblicata nell'UPP store è determinato dall'apposito campo dell'anagrafica dell'UPP.

- **Come e dove fisso i prerequisiti di una UPP?**

 :  : VOC Id="00003" Txt="Come e dove fisso i prerequisiti di una UPP?"
I requisiti per far funzionare l'UPP possono essere descritti nei seguenti modi : 
\* Tramite la documentazione applicativa
\* Tramite lo script "Oggetti aggiuntivi", disponibile fra gli enabler

- **Come controllo i prerequisiti?**

 :  : VOC Id="00004" Txt="Come controllo i prerequisiti?"
Se è stato creato lo script "Oggetti aggiuntivi", nel menù di gestione dell'UPP si attiva automaticamente la voce "Oggetti e prerequisti" sotto "Configurare", da cui è possibile monitorare l'esistenza degli oggetti previsti.

- **Posso sviluppare una UPP da un cliente?**

 :  : VOC Id="00005" Txt="Posso sviluppare una UPP da un cliente?"
Si. Basta che venga creata come UPP "custom". Tramite questa indicazione la codifica automatica applicherà una X iniziale al codice univoco dell'UPP.

- **Posso bloccare una UPP per sviluppi esterni al laboratorio?**

 :  : VOC Id="00006" Txt="Posso bloccare una UPP per sviluppi esterni al laboratorio?"
Si. Basta andare sull'azione "modifica" del menù di gestione dell'UPP e da li mettere livello rilascio "E", cioè "bloccato.

- **Posso avere una UPP personale per esercitazione?**

 :  : VOC Id="00007" Txt="Posso avere una UPP personale per esercitazione?"
Si. Nel menù del comando UPP, è possibile lanciare la creazione di un UPP personale. Verrà creata nella propria libreria W_ e sarà possibile poi utilizzarla solo da li.

Se si vuole poi trasformare l'UPP personale in una UPP comune, basta utilizzare l'azione di "copia".

- **Posso avere più servizi (o schede) per una UPP?**

 :  : VOC Id="00008" Txt="Posso avere più servizi (o schede) per una UPP?"
Si. Già la gestione degli enabler suggerisce automaticamente il nomer da attribuire al primo servizio/scheda e a quello successivo se ne esistono già.

- **Posso ridenominare, cancellare una UPP?**

 :  : VOC Id="00009" Txt="Posso ridenominare, cancellare una UPP?"
Per ridenominare un UPP è necessario copiarla e poi cancellarla. Con questo si ha quindi risposto anche alla seconda parte della domanda :  si è possibile cancellare l'UPP.
Si ricorda che la copia dell'UPP comporta la copia di tutti i sorgenti collegati all'UPP.

- **Posso eseguire il download di una UPP quando sono da un cliente?**

 :  : VOC Id="00010" Txt="Posso eseguire il download di una UPP quando sono da un cliente?"
Prossimamente si, sarà possibile scaricare il savf con tutti i sorgenti relativi all'UPP. Nel caso l'UPP abbia dei prerequisiti sarà necessario attuare le operazioni necessarie alla soddisfazione di tali prerequisit.

- **Una UPP può usare i prototipi?**

 :  : VOC Id="00011" Txt="Una UPP può usare i prototipi?"
Si è prevista sono previsti negli enabler applicativi. In particolare qui si evidenzia che creando dalla gestione enabler : 
\* La scheda base
\* La cartella PRO
\* Lo script dei prototipi
Sarà possibile usare in modo immediato il propotipo di esempio, che viene richiamato nelle sezioni della scheda base.

- **Dove devo caricare i file che utilizzo nei prototipi?**

 :  : VOC Id="00012" Txt="Dove devo caricare i file che utilizzo nei prototipi?"
Il percorso dipende sempre da quanto è stato indicato nello script dei prototipi. Si suggerisce però di seguire l'esempio dello sketch, in cui si prevede che i file di prototipo vengano memorizzati nella sottocartella PRO della cartella dell'oggetto SU (citata poi nello script dei prototipi trmaite la dicitura [FLR : SU;;codiceupp].

- **Posso inibire l'uso di una UPP mediante le autorizzazioni?**

 :  : VOC Id="00013" Txt="Posso inibire l'uso di una UPP mediante le autorizzazioni?"
Al momento è ancora un work in progress. Se l'UPP è stata pubblicata in una voce di menù si possono usare le autorizzazioni delle voci di menù,

- **Come posso attivare un Forum per una UPP?**

 :  : VOC Id="00014" Txt="Come posso attivare un Forum per una UPP?"
E' stato previsto un campo dell'anagrafica per poterlo attivare. Questo, attiva una voce nel menù di gestione che richiama la pagina del forum. E' però necessario a quel punto contattare la persona responsabile del laboratorio per chiedere che venga effettivamente creato il forum intestato al codice dell'UPP.

- **Posso utilizzare i membri di documentazione per documentare una UPP?**

 :  : VOC Id="00015" Txt="Posso utilizzare i membri di documentazione per documentare una UPP?"
Tendenzialmente no. Si vuole spingere l'utilizzo della documentazione wiki, attivabile tramite gli appositi campi dell'anagrafica.

- **Come posso contribuire con suggerimenti allo sviluppo di una UPP?**

 :  : VOC Id="00016" Txt="Come posso contribuire con suggerimenti allo sviluppo di una UPP?"
Si, tramite i nice to have presenti, fra le voci di "Imparare" e tramite cui è possibile aggiungere anche nuove voci. E' necessario però che il responsabile abbia attivato questa possibilità dagli enabler.

- **Posso conoscere i TODO (o i Branch) collegati ad una UPP?**

 :  : VOC Id="00017" Txt="Posso conoscere i TODO (o i Branch) collegati ad una UPP?"
No al momento no.

- **Quali componenti vengono distribuiti al cliente?**

 :  : VOC Id="00018" Txt="Quali componenti vengono distribuiti al cliente?"
Tutti i sorgenti e tutti i programmi. Per quel che riguarda i dati vanno invece riprodotti dal cliente.

- **Posso definire un OAV specifico per una UPP?**

 :  : VOC Id="00019" Txt="Posso definire un OAV specifico per una UPP?"
Si è possibile. Creando dagli enabler il programma B£OA_codiceupp. Prevedendo dentro di esso la gestione degli oav e compilando il pgm, si attiverà un'apposita voce di controllo sotto "Configurare", che permetterò di verificare quali oav sono presenti, ma anche di generarne o rigenerarne la definizione.

- **Una UPP può avere un database proprio?**

 :  : VOC Id="00020" Txt="Una UPP può avere un database proprio?"
Si, è possibile creare un file fisico e uno o più logici ad esso collegati, intestati all'UPP. Anche questa funzionalità è presente negli Enabler applicativi.

- **Cosa si intende per UppStore?**

 :  : VOC Id="00101" Txt="Cosa si intende per UppStore?"
L'Upp Store è e sarà la vetrina delle UPP con valore commerciale.

- **Cosa si intende per Sketch?**

 :  : VOC Id="00102" Txt="Cosa si intende per Sketch?"
Lo sketch è la UPP (A£_000) in cui vengono concentrarti i prototipi di tutti gli enabler applicativi. Tutte le volte che un enabler applicativo viene creato, viene in realtà copiato dall'UPP di sketch.

- **Cosa si intende per MOKUP di una UPP?**

 :  : VOC Id="00103" Txt="Cosa si intende per MOKUP di una UPP?"
La scheda di mockup è una scheda che può essere inizialmente creata solo per emulare in modo semplice il funzionamento dell'UPP, tendenzialmente sfruttando i dati provenienti dai prototipi.

- **Cosa si intende per Abstract?**

 :  : VOC Id="00104" Txt="Cosa si intende per Abstract?"
E' la documentazione che permette di definire in modo sintetico il significato applicativo dell'UPP.

- **Cosa si intende per Rating di una UPP?**

 :  : VOC Id="00105" Txt="Cosa si intende per Rating di una UPP?"
Il rating dell'UPP si intende rispetto alla completezza del contenuto tecnico dell'UPP. Non va confuso con le valutazioni degli utenti dell'UPP.
