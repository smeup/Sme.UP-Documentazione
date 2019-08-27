- **Conosci il significato di autorizzazioni applicative?**

 :  : VOC Id="SKIA0010" Txt="Conosci il significato di autorizzazioni applicative?"
Le autorizzazioni applicative permettono di differenziare tra i vari utenti le attività che questi possono eseguire e/o le informazioni che possono trovare/leggere.
- **Sai come funziona la risalita autorizzazioni?**

 :  : VOC Id="SKIA0020" Txt="Sai come funziona la risalita autorizzazioni?"
Il programma verifica prima l'esistenza di un'autorizzazione (classe) a livello utente/funzione, se manca va a cercare la stessa autorizzazione a livello di gruppo utente/funzione, se manca cerca l'autorizzazione valida per tutti/funzione, se manca ripete il giro (utente, gruppo, tutti) con funzione generica, l'ultimo default è classe generica/funzione generica/utente generico : 

-- Classe / Utente / Funzione
--- Classe / Gruppo Utente / Funzione
---- Classe / ** / Funzione
----- Classe / Utente / **
------ Classe / Gruppo Utente / **
------- Classe / ** / **
-------- ** / ** / **
- **Sai cosa sono CLASSE e FUNZIONE nella gestione autorizzazioni?**

 :  : VOC Id="SKIA0030" Txt="Sai cosa sono CLASSE e FUNZIONE nella gestione autorizzazioni?"
La classe è l'autorizzazione propriamente detta, la funzione è una sottoclasse.
Es. per le testate documento la classe è V5DO01 e la funzione è il tipo documento (DA, OA, OP, ...) se la funzione è "**" allora l'autorizzazione per la classe V5DO01 è valida per tutti i tipi documento.
- **Conosci le tabelle principali della gestione autorizzazioni?**

 :  : VOC Id="SKIA0040" Txt="Conosci le tabelle principali della gestione autorizzazioni?"
La tabella B£P, dove sono definite tutte le classi di autorizzazione.
La tabella B£S, dove sono definiti i possibili significati delle opzioni/funzioni operative.

Per una informazione più completa vedi documentazione tabelle : 
- [B£P - Classi Autorizzazione](Sorgenti/OG/TA/TA_B£P)
- [B£S - Significato protezioni applic.](Sorgenti/OG/TA/TA_B£S)
- **Sai qual'è l'archivio di riferimento?**

 :  : VOC Id="SKIA0050" Txt="Sai qual'è l'archivio di riferimento?"
Il file AUTOAP0F
- **Sai come reperire le classi di autorizzazione di un'applicazione?**

 :  : VOC Id="SKIA0060" Txt="Sai come reperire le classi di autorizzazione di un'applicazione?"
Nella scheda dell'applicazione (TAB£A) c'è la sezione "SET'N PLAY / Oggetti utilizzati" che contiene gli oggetti utilizzati dall'applicazione, tra cui le classi di autorizzazione.
- **Sai cove trovare le autorizzazioni di un programma in emulazione 5250?**

 :  : VOC Id="SKIA0070" Txt="Sai cove trovare le autorizzazioni di un programma in emulazione 5250?"
Mettendo uno slash "/" nel campo opzioni.
- **Sai come reperire la documentazione delle classi particolari di autorizzaz**

 :  : VOC Id="SKIA0080" Txt="Sai come reperire la documentazione delle classi particolari di autorizzazione? (es. ABILITA, RIS-, B£FUN0)"
Le classi particolari sono quelle che non sono collegate alle opzioni del programma di gestione (non si recuperano con lo "/") e che hanno comportamenti che sono fortemente condizionati dalla funzione utilizata.

Es. la classe ABILITA, se la funzione è MOV-MAG2 controlla le autorizzazioni sulle causali di movimentazione che hanno groppo autorizzazione = 2; se la funzione è V5BO01A controlla le autorizzazioni alla stampa bolla.
- **Conosci le autorizzazioni a livello campo?**

 :  : VOC Id="SKIA0090" Txt="Conosci le autorizzazioni a livello campo?"
Le autorizzazioni a livello campo regolano la possibilità per un utente di vedere o modificare il valore contenuto in un campo di un formato video.
Es. possibilità di vedere o modificare un prezzo in una riga documento di vendita.

Le classi di questa famiglia di autorizzazioni sono PLC-xxxxxx, dove xxxxxx è l'oggetto a cui si applica l'autorizzazione, es. PLC-BRARTI, PLC-V5RDOC.
- **Sai come fare a reperire i gruppi di informazioni usati nelle autorizzazio**

 :  : VOC Id="SKIA0100" Txt="Sai come fare a reperire i gruppi di informazioni usati nelle autorizzazioni a livello campo?"
Bisogna aprire con il SEU il programma del formato video e trovare gli indicatori che regolano la visualizzazione e la protezione dei campi video.
- **Sai cosa fare per autorizzare singoli elementi di una tabella qualsiasi? (**

 :  : VOC Id="SKIA0110" Txt="Sai cosa fare per autorizzare singoli elementi di una tabella qualsiasi? (es. tab. B£4)"
Nella definizione della tabella (up DEF > 02) di cui si vogliono autorizzare singoli elementi inserire un codice (es. DATE) nel campo "Funzione per autorizzazione" Assegnare le autorizzazioni per la Classe RITSM e la funzione appena inserita (DATE).

Per una informazione più completa vedi documentazione : 
 :  : DEC T(MB) P(DOC_TAB£P) K(RITSM)
- **Sai come autorizzare delle voci di menù?**

 :  : VOC Id="SKIA0120" Txt="Sai come autorizzare delle voci di menù?"
Esistono 2 metodi che sono dipendenti da come è stato definito in "UT5" l'ingresso utente per l'ambiente : 
- se il tipo accesso è "G" = Menù SMEUP :  Param. Gruppo B£U,  le autorizzazioni vanno date con l'utility UT5 opzione "Menù a Parametri per gruppo utente"
- se il tipo accesso è "S" = Menù SMEUP,  le autorizzazioni vanno date con la classe MENU e funzione pari alla "Categoria di protezione" inserita nella tabella MEA.

Per una informazione più completa vedi documentazione : 
- [Menu a parametri per gruppo utente](Sorgenti/OJ/PGM/P_B£UT54)
 :  : DEC T(MB) P(DOC_TAB£P) K(MENU)
- **Sai cosa fare per autorizzare singoli elementi delle azioni B£J?**

 :  : VOC Id="SKIA0130" Txt="Sai cosa fare per autorizzare singoli elementi delle azioni B£J?"
Si utilizza la classe TABB£J e la funzione è l'elemento della tabella B£H che richiama la B£J in questione.

Per una informazione più completa vedi documentazione : 
 :  : DEC T(MB) P(DOC_TAB£P) K(TABB£J)
- **Sai come assegnare le autorizzazioni ad una scheda o a una sezione?**

 :  : VOC Id="SKIA0140" Txt="Sai come assegnare le autorizzazioni ad una scheda o a una sezione?"
Tutte le autorizzazioni specifiche di Looc.UP hanno classe autorizzazione che inizia per LO.xxx dove xxx è  tipico del componente grafico da autorizzare.
Es. per le schede la classe è LO.EXD e la funzione è la scheda stessa.

Le autorizzazioni sono date a livello di codice di protezione che è un numero di due cifre dove la prima descrive la categoria e il secondo il livello di importanza, categoria e livello di importanza sono a loro volta numeri di 1 cifra da 0 a 9 (0 = protezione bassa, 9 = protezione massima).

Per una informazione più completa vedi documentazione : 
- [Autorizzazioni MENU e accessi - V4R1](Sorgenti/DOC/TA/B£AMO/B£AUTO_04)
- **Sai qual'è il codice di protezione di default assegnato alle schede LoocUP**

 :  : VOC Id="SKIA0150" Txt="Sai qual'è il codice di protezione di default assegnato alle schede LoocUP?"
05
- **Sai come reperire il livello di autorizzazione di una scheda?**

 :  : VOC Id="SKIA0160" Txt="Sai come reperire il livello di autorizzazione di una scheda?"
Visualizzando l'XML di una scheda (o di una sottoscheda), si possono leggere, nel tag AUT, funzione e il livello minimo richiesti per l'autorizzazione della scheda stessa.

Es. se leggo l'XML della sottoscheda "dati commerciali" di un ente, noto : 
<Setup>
<Program>
<EXD>
<AUT Lev="05" Cls="LO.EXD" Src="CN_COM"/>
- **Sai come impostare nelle schede un codice di protezione diverso dal defaul**

 :  : VOC Id="SKIA0170" Txt="Sai come impostare nelle schede un codice di protezione diverso dal default?"
Nello script della scheda usare l'istruzione :  S.EXD.AUT
- **Esistono schede LoocUP solo ad uso esclusivo degli sviluppatori o del gest**

 :  : VOC Id="SKIA0180" Txt="Esistono schede LoocUP solo ad uso esclusivo degli sviluppatori o del gestiore del sistema, sai come evitare che vengano viste dagli utenti finali?"
Esiste la classe di autorizzazione USRLVL con funzione = ** che prevede 4 livelli di autorizzazione : 
- 00 = End user
- 01 = Gestore sistema (resp. EDP)
- 02 = Installatore / Implementatore del sistema
- 03 = Sviluppo / Test

Negli script di scheda si possono impostare i  livelli operativi specificando l'attributo Usr="nn", dove nn=00, 01, 02, 03 (default 02).

Per una informazione più completa vedi documentazione : 
- [Autorizzazioni operative Looc.up](Sorgenti/DOC/TA/B£AMO/B£AUTO_05)
- **Sai come reperire le autorizzazioni sui campi del V5STAT?**

 :  : VOC Id="SKIA0190" Txt="Sai come reperire le autorizzazioni sui campi del V5STAT?"
Nella scheda dell'oggetto file V5STAT0F c'è la colonna autorizzazioni
- **Sai come assegnare le auorizzazioni ai campi del V5STAT?**

 :  : VOC Id="SKIA0200" Txt="Sai come assegnare le auorizzazioni ai campi del V5STAT?"
Classe = LO.FLD, Funzione = V5STAT0F (oppure **V5)
- **Sai come assegnare le auorizzazioni ai campi del LOA15?**

 :  : VOC Id="SKIA0210" Txt="Sai come assegnare le auorizzazioni ai campi del LOA15?"
In casi particolari possono essere definite a livello di script del LOA15. Il default è Classe = LO.FLD, Funzione = **.

Nota :  i file che hanno autorizzazioni sui campi sono impostati nel programma B£EQRY_AO. In implementazioni locali, se si vogliono autorizzare altri files oltre a quelli standard usare l'exit B£EQRY_AOX.
- **Conosci la scheda autorizzazioni?**

 :  : VOC Id="SKIA0220" Txt="Conosci la scheda autorizzazioni?"
- **Sai cos'è e come attivare il log delle autorizzazioni?**

 :  : VOC Id="SKIA0230" Txt="Sai cos'è e come attivare il log delle autorizzazioni?"
Il log delle autorizzazioni, quando attivato per un utente, permette di vedere tutte le autorizzazioni che vengono chiamate dai vari programmi che l'utente sta utilizzando. In questo modo si riescono ad individuare le autorizzazioni specifiche che nel bloccano l'attività.

Per attivare il log :  andare nella scheda B£AUTO > Set'n play > Log > Seguire le istruzioni del tab Documentazione

Nota; dopo avere eseguito le verifiche è bene togliere l'attivazione per non intasare il log.
- **Sai cos'è lo SWITCH UTENTE?**

 :  : VOC Id="SKIA0240" Txt="Sai cos'è lo SWITCH UTENTE?"
Un modo per attribuire ad un utente le autorizzazioni di un altro (es. per backup in assenza del titolare).

Per una informazione più completa vedi documentazione : 
- [Switch utente &-x2f; gruppo utenti](Sorgenti/DOC/TA/B£AMO/B£AUTO_06)
- **Conosci le funzioni di servizio sugli utenti?**

 :  : VOC Id="SKIA0250" Txt="Conosci le funzioni di servizio sugli utenti?"
Sono svolte dal programma B£UT78A e permettono la copia delle autorizzazioni di un utente ad un altro.
