# Calcolo costo di massa di oggetti
Dato un tipo il programma calcola e memorizza il costo di una lista di oggetti.

## Formato di input
![D0BASE_56](https://doc.smeup.com/immagini/MBDOC_OGG-P_D0CO01B/D0BASE_56.png)Sono possibili le seguenti impostazioni : 
 \* **Contesto**; è il tipo di oggetto di cui si vuole calcolare il costo, al momento sono previsti AR, DR, OP, CM
 \* **Tipo costo**; è il tipo costo che sarà memorizzato
 \* **Data**; è la data a fronte della quale sarà eseguita la memorizzazione, la stessa data viene utilizzata nelle eventuali scansioni distinta e ciclo
 \* **Tipo di calcolo**; Blank = Tutti (vengono ricalcolati tutti i costi), M = solo mancanti (si ricalcolano solo i costi mancanti), P = solo presenti (si ricalcolano solo i costi presenti)
 \* **Impostazioni**; contiene le impostazioni del calcolo (vedi paragrafo successivo). **Nota**, se questo campo non è blank, con il bottone laterale è possibile interrogare le impostazioni presenti nell'apposito formato, se invece questo campo è blank, si può accedere con possibilità di modifica alle impostazioni del calcolo
 \* **Parzializzazioni**
 \*\* __Interne__; lancia il parzializzatore standard per il tipo oggetto scelto
 \*\* __Esterne__; permette di impostare le parzializzazioni esterne per il tipo oggetto scelto
 \* **Per ogni oggetto estrarre**
 \*\* __I suoi padri (Implosione di distinta)__; è possibile eseguire il ricalcolo dei costi dei padri di distinta. Valori previsti :  Blank = non ricalcolare i costi dei padri di distinta, 1 = ricalcolare e memorizzare i costi
 \*\* __I suoi figli (Esplosione di distinta)__; è possibile eseguire il ricalcolo dei costi dei componenti di distinta, oppure per i componenti, se ci sono si possono usare i costi letti senza ricalcolo, se si è chiesto il ricalcolo costo dei componenti è possibile scegliere di memorizzarlo. Valori previsti :  Blank = non ricalcolare i costi dei componenti di distinta, 1= ricalcolare e memorizzare i costi, 2 = ricalcolare senza memorizzare, 3 = ricalcolare solo i componenti configurati ma senza memorizzare

Sul piede del formato ci sono dei comandi funzione con il significato seguente : 
 \* **F06 = Conferma**, lancia l'elaborazione
 \* **F11 = Parametri esecuzione**, apre le impostazioni GPE (gestione parametri esecuzione)
 \* **F07 = Dati programmazione**, attiva/disattiva la visione dei dati tecnici
 \* **F14 = Autorizzazioni**, apre la gestione autorizzazioni per la classe = ABILITA e la funzione = D0CO01A che regolano la possibilità per l'utente di utilizzare il programma
 \* **F15 = Memorizza Impostazioni**, permette di salvare le impostazioni eseguite nell'apposito formato con il nome indicato in questo campo.

- [Impostazioni di calcolo costo](Sorgenti/DOC/OJ/PGM/D0CO01I)
