- **Sai cosa è la gestione tabelle in SmeUP?**

 :  : VOC Id="SKIA0010" Txt="Sai cosa è la gestione tabelle in SmeUP?"
è un modo comune di trattare tutte le tabelle di parametrizzazione (es. tab. assoggettamento IVA, tab. tipo documento V5, tab. tipo ordine produzione) o di classificazione (es. tab. classe programmazione, tab. sett. merceologico, ..) utilizzate all'interno delle applicazioni SmeUP.
Per modo comune si intende :  stessa modalità di definizione campi tabella, stesse modalità di interazione input output, stessi archivi, stesse /copy di interrogazione e gestione, stesse autorizzazioni, ...
Attraverso questa gestione è possibile anche creare tabelle non fornite a standard per funzioni specifiche di una installazione presso un cliente.

Per una informazione più completa vedi documentazione : 
- [Introduzione](Sorgenti/DOC/TA/B£AMO/B£TABE_01)
- [Definizione di una tabella](Sorgenti/DOC/TA/B£AMO/B£TABE_02)

- **Sai come sono strutturate le tabelle?**

 :  : VOC Id="SKIA0020" Txt="Sai come sono strutturate le tabelle?"
La gestione tabelle in SmeUP è strutturata in 3 archivi : 
- TABDS00F dove sono descritti i settori/sottosettori delle tabelle (ogni tabella, es. BRA, è un settore)
- TABDC00F dove sono descritti i campi delle tabelle
- TABEL00F dove è scritto il contenuto delle tabelle (in questo archivio esiste un recod per ogni elemento di ogni tabella) - nota :  in casi particolari, tabelle particolari, risiedono in archivi diversi dal TABEL00F (es. TABELA0F per gli elementi della tab. MEA).

- **Sai quali sono gli archivi dove sono contenuti i dati delle tabelle?**

 :  : VOC Id="SKIA0030" Txt="Sai quali sono gli archivi dove sono contenuti i dati delle tabelle?"
- TABEL00F, che contiene, salvo casi particolari, tutti i dati delle tabelle utilizzate
- TABELA0F, che contiene i dati delle tabelle MEAxx dei menù e delle azioni SmeUP
- TABELV0F, che contiene i dati di tabelle di impostazione standard (es. V§*xx)
- TABELG0F, che contiene i dati delle tabelle di gruppo in una implementazione multiambiente dove alcune applicazioni sono comuni.

- **Sai cosa sono i sottosettori di una tabella?**

 :  : VOC Id="SKIA0040" Txt="Sai cosa sono i sottosettori di una tabella?"
Ogni tabella è caratterizzata da un settore a cui appartengono un nome ed un tracciato record. Il settore può essere replicato in tanti diversi sottosettori che conservano tutti lo stesso tracciato record.
L'utilizzo dei sottosettori è utile quando si vogliono differenziare raggruppamenti diversi di tabelle che hanno la stessa impostazione e finalità es. le tabelle dei tipi riga dei documenti V5 del ciclo esterno che sono diversificate per tipo documento, le tabelle dei conti contabili che possono essere diversificate per azienda.

- **Sai se possono esistere archivi tabelle diversi da quelli comuni? Come si **

 :  : VOC Id="SKIA0050" Txt="Sai se possono esistere archivi tabelle diversi da quelli comuni? Come si impostano?"
Si, ad esempio per rendere comuni a più ambienti alcune tabelle (es. tab. BRA, tab, V5D, Tab. V5axx, ...).
In definizione tabelle si imposta l'archivio di riferimento (è un codice lungo 1 che sostituisce le x nel codice file TABELx0F).

Per una informazione più completa : 
- [Definizione di una tabella](Sorgenti/DOC/TA/B£AMO/B£TABE_02)

- **Sai definire i campi di una tabella?**

 :  : VOC Id="SKIA0060" Txt="Sai definire i campi di una tabella?"
Si utilizza la funzione B£DT10 > Opzione 06 (utility UP DEF).

Per una informazione più completa : 
- [Definizione di una tabella](Sorgenti/DOC/TA/B£AMO/B£TABE_02)
- **Sai associare un programma di controllo particolare ad una tabella?**

 :  : VOC Id="SKIA0070" Txt="Sai associare un programma di controllo particolare ad una tabella?"
Si utilizza la funzione B£DT10 > Opzione 02 (utility UP DEF), tra i campi da compilare c'è anche quello relativo al programma di controllo. Questo programma permette di eseguire controlli particolari in manutenzione della tabella.

Per una informazione più completa : 
- [Definizione di una tabella](Sorgenti/DOC/TA/B£AMO/B£TABE_02)
- **Sai cos'è una tabella ad elemento fisso?**

 :  : VOC Id="SKIA0080" Txt="Sai cos'è una tabella ad elemento fisso?"

Una tabella che ha un solo elemento codificato con "*", di solito si tratta di una tabella con le impostazioni di base di un'applicazione, es. GM1, C51, BR!, ..
- **Sai come fare per avere l'azienda come sottosettore?**

 :  : VOC Id="SKIA0090" Txt="Sai come fare per avere l'azienda come sottosettore?"
Si utilizza la funzione B£DT10 > Opzione 02 (utility UP DEF), tra i campi da compilare c'è anche quello relativo all'oggetto in sottosettore.

Di solito l'azienda nel sottosettore è utilizzata in implementazioni multiazienda dove si possono avere, per la stessa tabella, elementi diversi per aziende diverse.

Per una informazione più completa : 
- [Definizione di una tabella](Sorgenti/DOC/TA/B£AMO/B£TABE_02)
- **Sai come tradurre dinamicamente i campi della tabella?**

 :  : VOC Id="SKIA0100" Txt="Sai come tradurre dinamicamente i campi della tabella?"

Si utilizza la funzione B£DT10 > Opzione 02 (utility UP DEF), tra i campi da compilare c'è anche quello relativo alla traduzione dinamica.

Per una informazione più completa : 
- [Definizione di una tabella](Sorgenti/DOC/TA/B£AMO/B£TABE_02)
- **Sai cos'è una tabella deviata?**

 :  : VOC Id="SKIA0110" Txt="Sai cos'è una tabella deviata?"

Un metodo attraverso il quale si presenta a SmeUP il contenuto di una tabella esterna al posto del contenuto di una tabella interna.
Es. devinado la tab. IVA sulla tabella assoggettamenti di un altro gestionale possiamo far si che non sia necessario tenere allineate entrambe le tabelle ma si legge direttamente la tabella esterna al posto della tab. IVA.

- **Sai impostare una deviazione di tabella?**

 :  : VOC Id="SKIA0120" Txt="Sai impostare una deviazione di tabella?"
In definizione settore si deve dire che la tabella è deviata ("**" nel campo applicazione specifica).
In tab. B£I si deve inserire un elemento che ha lo stesso nome del settore tabella deviata.
L'elemento B£I deve riportare le indicazioni per collegarsi ai dati origine (nome tabella e ambiente, archivio, programma di lettura, ...)

Per una informazione più completa : 
- [Definizione di una tabella](Sorgenti/DOC/TA/B£AMO/B£TABE_02)
- [B£I - Deviaz. tabella](Sorgenti/OG/TA/TA_B£I)

- **Sai aggiungere campi utente ad una tabella standard?**

 :  : VOC Id="SKIA0130" Txt="Sai aggiungere campi utente ad una tabella standard?"

Usando l'utility UP DEF in Definizione campi si trova il comando funzione F15 con cui si passa alla definizone campi utente.

Dopo la definizione bisogna generare la /copy perchè i programmi siano in grado di leggere questi campi utente.
- **Sai usare le funzioni di servizio di copia?**

 :  : VOC Id="SKIA0140" Txt="Sai usare le funzioni di servizio di copia?"

Con l'utility UP FTB si possono copiare settori / campi di settore / elementi.
- **Sai importare le tabelle dal modello?**

 :  : VOC Id="SKIA0150" Txt="Sai importare le tabelle dal modello?"
Nelle funzioni oggetto del settore (raggiungibili es. con utility UP FUN) esiste la funzione "Gestione modello" con la quale vengono mostrati gli elmenti che sono : 
- presenti nell'ambiente corrente e mancanti nel modello
- presenti nel modello e mancanti nell'ambiente corrente
- presenti nei 2 ambienti ma diversi
- presenti nei 2 ambienti e uguali
Tra le varie possibilità c'è anche la copia da modello

Le stesse funzioni di fasatura da modello sono disponibili dalla scheda del modulo B£TABE

- **Sai verificare la differenza tra le tabelle cliente e quelle del modello?**

 :  : VOC Id="SKIA0160" Txt="Sai verificare la differenza tra le tabelle cliente e quelle del modello?"

Usando le funzioni di fasatura (UP FTB oppure scheda B£TABE)
- **Sai quali sono le autorizzazioni necessarie per la manutenzione di una tab**

 :  : VOC Id="SKIA0170" Txt="Sai quali sono le autorizzazioni necessarie per la manutenzione di una tabella?"
Per gestire settori e campi di tabella, Classe = GEDETA, Funzione = B£DT10

Per gestire settori e campi di tabella, Classe = RITSM, Funzione = nome del settore


- **Sai quali sono le autorizzazioni necessarie per controllare la manutenzion**

 :  : VOC Id="SKIA0180" Txt="Sai quali sono le autorizzazioni necessarie per controllare la manutenzione di singoli elementi di tabella?"
In definizione della tabella inserire nel campo "Funzione per autorizzazione" un codice che è lo stesso della tabella seguito da un "-" (meno).
Es. per la tab. GMC inserire GMC-

Autorizzare l'utente alla classe RITSM e mettere nella funzione il codice inserito in "Funzione per autorizzazione" concatenato con l'elemento da autorizzare.
Es. GMC-1003

Per una informazione più completa vedi documentazione : 
 :  : DEC T(MB) P(DOC_TAB£P) K(RITSM)
- **Sai a cosa servono le /copy delle tabelle?**

 :  : VOC Id="SKIA0190" Txt="Sai a cosa servono le /copy delle tabelle?"
Si utilizza dove le tabelle hanno anche altri campi oltre codice e descrizione, la /copy serve per fare in modo che i programmi possano interpretare gli elementi contenuti nella tabella stessa.
- **Sai come creare una /copy di una tabella?**

 :  : VOC Id="SKIA0200" Txt="Sai come creare una /copy di una tabella?"
Opzione 14 dalla utility UP DEF.
