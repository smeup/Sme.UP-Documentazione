# Calcolo costo interattivo di un oggetto
Dato un oggetto il programma ne calcola il costo, presenta in una lista il risultato e, se opportunamente impostato, può memorizzare il costo calcolato.

## Formato di input
![D0BASE_51](http://localhost:3000/immagini/MBDOC_OGG-P_D0CO01A/D0BASE_51.png)Sono possibili le seguenti impostazioni : 
 \* **Contesto**; è il tipo di oggetto di cui si vuole calcolare il costo, al momento sono previsti AR, DR, OP, CM
 \* **Tipo costo**; è il tipo costo che sarà memorizzato
 \* **Data**; è la data a fronte della quale sarà eseguita la memorizzazione, la stessa data viene utilizzata nelle eventuali scansioni distinta e ciclo
 \* **Oggetto**; dipende dal contesto, è l'istanza di cui eseguire il calcolo costo, la descrizione del campo varia dinamicamente in funzione del contesto scelto
 \* **Tipo costo**; hhhh
 \* **Quantità calcolo**; se impostata una quantità i vari elementi di costo vengono calcolati anche per la qtà indicata
 \* **Quantità lotto**; hhhhhhhh
 \* **Politiche %**; se il contesto è articolo è possibile indicare una distribuzione di poltiche anche mista, in assenza si utilizzano le politiche di pianificazione
 \* **Esplosione distinta**; se il contesto è un articolo è possibile eseguire il ricalcolo dei costi dei componenti di distita, oppure per i componenti, se ci sono si possono usare i costi letti senza ricalcolo, se si è chiesto il ricalcolo costo dei componenti è possibile scegliere di memorizzarlo. Valori previsti :  Blank = non ricalcolare i costi dei componenti di distinta, 1 = ricalcolare senza memorizzare, 2= ricalcolare e memorizzare i costi
 \* **Tipo di calcolo**; Blank = Tutti (vengono ricalcolati tutti i costi), M = solo mancanti (si ricalcolano solo i costi mancanti), P = solo presenti (si ricalcolano solo i costi presenti)
 \* **Impostazioni**; contiene le impostazioni del calcolo (vedi paragrafo successivo). **Nota**, se questo campo non è blank, con il bottone laterale è possibile interrogare le impostazioni presenti nell'apposito formato, se invece questo campo è blank, si può accedere con possibilità di modifica alle impostazioni del calcolo

Sul piede del formato ci sono dei comandi funzione con il significato seguente : 
 \* **F06 = Conferma**, lancia l'elaborazione
 \* **F07 = Dati programmazione**, attiva/disattiva la visione dei dati tecnici
 \* **F14 = Autorizzazioni**, apre la gestione autorizzazioni per la classe = ABILITA e la funzione = D0CO01A che regolano la possibilità per l'utente di utilizzare il programma
 \* **F15 = Memorizza Impostazioni**, permette di salvare le impostazioni eseguite nell'apposito formato con il nome indicato in questo campo.

- [Impostazioni di calcolo costo](Sorgenti/OJ/PGM/D0CO01I)
