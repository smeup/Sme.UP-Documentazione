- \*\*A cosa serve la tabella D5Z?\*\*

 :  : VOC Id="10001" Txt="A cosa serve la tabella D5Z?"
 La tabella D5Z è una tabella puramente descrittiva molto utile per separare i valori di budget da quelli di consuntivo o da quelli progressivi.
 Nel caso in cui si abbia l'esigenza di dover tenere separati (per esempio dati di budget da dati di consuntivo), non conviene creare temi diversi,
 ma espandere il singolo tema aggiungendo una chiave ulteriore che punta al'oggetto TAD5Z.
 I programmi di ripresa da sistemi conferenti permettono infatti di specificare nei propri parametri anche un elemento della tabella D5Z,
 che verrà quindi ripreso dal programma e scritto nel record del D5COSO (se fa parte della chiave).
 In questo modo si può specificare nelle singole riprese il tipo di dati che riprendono, evitando di creare temi uguali fra di loro.
 I codici contenuti sono modificabili dall'utente a proprio piacimento.

- \*\*Cosa è il minicubo?\*\*

 :  : VOC Id="10002" Txt="Cosa è il minicubo?"
 Il minicubo permette di analizzare i dati del D5COSO confrontando fra loro più record e potendo ordinarli per valore o scostamento.
 Per accedere al minicubo bisogna andare nella gestione del dettaglio del D5COSO e premere F14 sul valore da analizzare.

- \*\*Come gestire i valori di budget?\*\*

 :  : VOC Id="10003" Txt="Come gestire i valori di budget?"
 Per inserire i valori di budget conviene appoggiarsi al modulo MP, dedicato all'inserimento di valori distribuiti nei periodi e successivamente
 impostare un passo di ripresa da MPPIAN a D5COSO per riprendere i valori.
 Nel menù del D5 è presente una chiave per andare direttamente nella gestione dei dati del modulo MP.

- \*\*Dove salvare i valori di budget nel D5?\*\*

 :  : VOC Id="10004" Txt="Dove salvare i valori di budget nel D5?"
 Per tenere separati i valori di budget da quelli di consuntivo conviene aggiungere una chiave nel tema (tabella D5O) contenente la tabella D5Z (vedi FAQ su tabella D5Z).

- \*\*Si possono distribuire dei valori su più oggetti?\*\*

 :  : VOC Id="10005" Txt="Si possono distribuire dei valori su più oggetti?"
 Per distribuire un valore su più oggetti bisogna utilizzare un indice di distribuzione (tabella D5I).
 Gli indici ricevono in ingresso 1 o 2 oggetti di tipo specificato nella tabella e restituiscono una lista di oggetti con una loro distribuzione percentuale.
 Per dettagli ulteriori si rimanda all'help della tabella D5I e della D5M.

- \*\*Come faccio a sapere quali sono gli oggetti e i valori ripresi dai programmi?\*\*

 :  : VOC Id="10006" Txt="Come faccio a sapere quali sono gli oggetti e i valori ripresi dai programmi?"
 Dall'esecuzione flusso azioni basta mettere una H nel campo opzione del passo di ripresa interessato :  viene visualizzato un help inerente il programma di ripresa.
 Nell'help sono descritti gli oggetti riportati, i valori e le varie logiche di ripresa.
- \*\*Sai cos'è Delt.up?\*\*

 :  : VOC Id="SKIA0010" Txt="Sai cos'è Delt.up?"
Delt.up è il modulo di Sme.up che permette di monitorare i processi aziendali e rilevare gli    scostamenti rispetto ad un obiettivo predefinito mediante l'utilizzo di procedure
di importazione e trasformazione dei dati dal sistema gestionale o da sistemi esterni
- \*\*Sai qual'è l'archivio base di Delt.up?\*\*

 :  : VOC Id="SKIA0020" Txt="Sai qual'è l'archivio base di Delt.up?"
D5COSO0F
- \*\*Sai cos'è il contesto?\*\*

 :  : VOC Id="SKIA0030" Txt="Sai cos'è il contesto?"
E' l'oggetto che definisce le entità che devomno essere monitorate nell'attività di controllo.
- \*\*Sai come si definisce un contesto?\*\*

 :  : VOC Id="SKIA0040" Txt="Sai come si definisce un contesto?"
I contesti sono gestiti nella tabella D5S.
Devono essere oggetti presenti nella tabella \*CNTT oppure generici '\*\*'.
- \*\*Sai quali sono i contesti più comuni?\*\*

 :  : VOC Id="SKIA0050" Txt="Sai quali sono i contesti più comuni?"
AR    Articoli
CC    Centri di costo
CM    Commesse
CO    Conti Contabili
CNCLI Clienti
CNFOR Fornitori
CNAZI Aziende
- \*\*Sai come si impostano le chiavi dell'archivio?\*\*

 :  : VOC Id="SKIA0060" Txt="Sai come si impostano le chiavi dell'archivio?"
La prima chiave è il codice del contesto (Es. per il contesto AR la prima chiave sarà il codice dell'articolo)
Al contesto deve essere sempre legato il Tema (tabella D5O + sottosettore), nel tema si possono
definire fino a tre chiavi aggiuntive
Ad esempio :  se in un tema collegato al contesto AR si definisce una chiave aggiuntiva (CNCLI)
si potranno elaborare i valori per ARTICOLO/CLIENTE (ad esempio per analizzare la marginalità
degli articoli di un cliente)
- \*\*Sai come si definiscono i valori del D5COSO?\*\*

 :  : VOC Id="SKIA0070" Txt="Sai come si definiscono i valori del D5COSO?"
Mediante la compilazione della tabella IGISS (SS=Sottosettore). Ad ognuno dei 99 valori
corrisponderà un elemento della tabella avente codice corrispondente al relativo valore
(Es :  l'elemento 01 della tabella IGI corrisponderà al primo dei 99 valori del D5COSO
- \*\*Sai come si imposta il periodo?\*\*

 :  : VOC Id="SKIA0080" Txt="Sai come si imposta il periodo?"
Si possono utilizzare tutti i periodi definiti nella tabella PER. Possono essere di tipo A=esercizio contabile o P=Periodo (Anno/mese o periodi definiti dall'utente)
