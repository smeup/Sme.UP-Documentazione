- **Messaggi di controllo documenti**

 :  : VOC Id="B£DOCU"   Txt="Messaggi di controllo documenti"
In questo documento sono raccolti i messagggi che ritorna il controllo di un documento.
Il prefisso indica il tipo di azione
- A - Riga aggiunta
- C - Cambiamento (alla tag o al paragrafo)
- E - Riga eliminata
Ogni messaggio ha, come attributo, un livello di gravità di due caratteri.
Esso, preceduto dal carattere L, identifica una ulteriore voce :  in questo modo si può documentare il livello del messaggio. Ad esempio il livello 10 si documenta nella voce L10.
Il programma di controllo documentazione ritorna il livello massimo dei messaggi, che costituisce quindi il risultato del controllo.
Ci sono alcuni messaggi di massima gravità, che nnon derivano dal  livello degli altri messaggi 'di riga' ma sono attribuiti gobalmente dal controllo :  e sono L80, L90, L91 e L92.

- **Nessun errore**

 :  : VOC Id="L00"      Txt="Nessun errore"  Liv="00"
Nessun errore o azioni previste nella sintassi

- **Sistemazioni **

 :  : VOC Id="L10"      Txt="Sistemazioni " Liv="10"
Sistemazioni locali

- **Incongruenze eliminate**

 :  : VOC Id="L20"      Txt="Incongruenze eliminate"  Liv="20"
Inconguenze locali eliminate :  righe in posizione non ammessa

- **Sviluppo incompleto**

 :  : VOC Id="L30"      Txt="Sviluppo incompleto"  Liv="30"
Documento non completamente sviluppato :  Inclusioni non risolte


- **Documento vuoto**

 :  : VOC Id="L80"      Txt="Documento vuoto"  Liv="80"
Il documento originale è vuoto

- **Documento pieno**

 :  : VOC Id="L90"      Txt="Documento pieno"  Liv="90"
Il documento originale è troppo grande

- **Documento riempito da include**

 :  : VOC Id="L91"      Txt="Documento riempito da include" Liv='91'
Il documento, durante le inclusioni, è diventato troppo grande

- **Documento riempito da espansione**

 :  : VOC Id="L92"      Txt="Documento riempito da espansione" Liv='92'
Il documento, durante i completamenti, è diventato troppo grande


- **Eliminazione prevista**

 :  : VOC Id="E00"      Txt="Eliminazione prevista"  Liv="00"
La riga viene eliminata perchè previsto :  riga di inclusione, TAGxxx, REMxxx

- **Inclusione di membro non eseguita**

 :  : VOC Id="E01"      Txt="Inclusione di membro non eseguita" Liv="30"
L'inclusione di un membro (o di una parte di esso) non ha prodotto nessuna riga

- **Inclusione di servizio non eseguita**

 :  : VOC Id="E02"      Txt="Inclusione di servizio non eseguita" Liv="30"
L'inclusione del risultato di un servizio non ha prodotto nessuna riga

- **Inclusione eliminata**

 :  : VOC Id="E03"      Txt="Inclusione eliminata" Liv="30"
L'inclusione all'interno di un inclusione non è ammessa

- **Riga di blocco eliminata**

 :  : VOC Id="E04"      Txt="Riga di blocco eliminata" Liv="20"
All'interno di un blocco PAR/PAR.END non può esserci una riga di questo tipo.

- **Riga elminata :  fine blocco**

 :  : VOC Id="E05"      Txt="Riga elminata :  fine blocco" Liv="20"
All'esterno di un blocco PAR/PAR.END non può esserci una riga di questo tipo.

- **Riga eliminata :  estranea alla tabella**

 :  : VOC Id="E06"      Txt="Riga eliminata :  estranea alla tabella" Liv="20"
All'interno di un blocco TAB/TAB.END non può esserci una riga di questo tipo.

- **Riga di tabella eliminata**

 :  : VOC Id="E07"      Txt="Riga di tabella eliminata" Liv="20"
All'esterno di un blocco TAB/TAB.END non può esserci una riga di questo tipo.

- **Riga eliminata :  sviluppata in colonne**

 :  : VOC Id="E08"      Txt="Riga eliminata :  sviluppata in colonne" Liv="00"
La prima riga all'interno di una tabella, se non presenti TAG.COL espliciti, viene sviluppata in colonne, e quindi eliminata come riga.

- **Commento**

 :  : VOC Id="E09"      Txt="Commento" Liv="00"
Una riga di commento viene eliminata logicamente

- **Titolo unico eliminato**

 :  : VOC Id="E10"      Txt="Titolo unico eliminato" Liv="10"
Nel documento c'è un solo titolo che viene eliminato.
NB :  a differenza di tutte le altre eliminazioni logiche, di cui si tiene conto nel corso dell'elaborazione, questa è eseguita solo alla fine e quindi è opertiva all'interno del documento, quindi è utilizzata, ad esempio, come chiusura implicita.
Non si è ritenuto opportuno eseguire un giro iniziale, per individuare i soli titoli validi, che dovrebbe replicare le logiche di esclusione del successivo giro di controllo.

- **Eliminato titolo di livello troppo basso**

 :  : VOC Id="E11"      Txt="Eliminato titolo di livello troppo basso" Liv="20"
Il titolo, per congruenza con i precedenti, dovrebbe avere un livello minore di uno.
È stato quindi eliminato.

- **Eliminato titolo di livello troppo alto**

 :  : VOC Id="E12"      Txt="Eliminato titolo di livello troppo alto" Liv="20"
Il titolo, per congruenza con i precedenti, dovrebbe avere un livello maggiore di tre.
' stato quindi eliminato.

- **Eliminata TAG estranea ai book**

 :  : VOC Id="E13"      Txt="Eliminata TAG estranea ai book" Liv="20"
Nei documenti di tipo book sono ammesse unicamente le tag : 
- ..LNK
- ..DEC con oggetto di tipo membro (MB) e parametro DOCxx oppure voce (VO)
- ..T0x (titoli)
NB :  anche il puro testo (TAG vuota) non è ammesso e viene quindi eliminato.


- **Aggiunta inizio blocco prevista**

 :  : VOC Id="A01"      Txt="Aggiunta inizio blocco prevista"  Liv='00'
Riga aggiunta se per il blocco è stata scelta la sintassi abbreviata (-, \*)

- **Aggiunta fine blocco prevista**

 :  : VOC Id="A02"      Txt="Aggiunta fine blocco prevista"  Liv='00'
Riga aggiunta se per il blocco è stata scelta la sintassi abbreviata (-, \*)

- **Aggiunta fine blocco interna**

 :  : VOC Id="A03"      Txt="Aggiunta fine blocco interna"  Liv='10'
Riga aggiunta se è stata trovato un titolo, all'interno di blocco aperto

- **Aggiunta fine blocco finale**

 :  : VOC Id="A04"      Txt="Aggiunta fine blocco finale"  Liv='10'
Riga aggiunta se alla fine del documento è ancora aperto un blocco

- **Aggiunta riga di colonna**

 :  : VOC Id="A05"      Txt="Aggiunta riga di colonna"  Liv='00'
Riga di TAB.COL aggiunta perchè definita implictamente nella prima riga di dettaglio tabella


- **Riga di blocco modificata**

 :  : VOC Id="C01"      Txt="Riga di blocco modificata"  Liv='00'
Riga di blocco modificata :  è stata scelta la sintassi abbreviata (-, \*)

- **Titolo modificato**

 :  : VOC Id="C02"      Txt="Titolo modificato"  Liv='10'
Il titolo è stato modificato per congruenza con i precedenti

- **Frequent asked question**

 :  : VOC Id="FAQ" Txt="Frequent asked question"
