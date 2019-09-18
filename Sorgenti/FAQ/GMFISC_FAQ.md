- \*\*Sai quali sono le attività a rilevanza fiscale dell'applicazione GM?\*\*

 :  : VOC Id="SKIA0010" Txt="Sai quali sono le attività a rilevanza fiscale dell'applicazione GM?"
Sono le attività supportate dal modulo GMFISC : 
- creazione annuale della giacenza del magazzino fiscale
- lista movimenti fiscali dell'anno
- \*\*Sai cos'è la sintesi di magazzino in questo modulo?\*\*

 :  : VOC Id="SKIA0020" Txt="Sai cos'è la sintesi di magazzino in questo modulo?"
In questo modulo le azioni relative alla sintesi di magazzino sono quelle preposte alla creazione, manutenzione, interrogazione e stampa della giacenza fiscale.
Si utilizza il termine "sintesi" perchè questa è una gicenza totalizzata (di norma totale per articolo, ma si possono avere casi un cui la giacenza è totalizzta per articolo e altro oggetti, es. articolo/configurazione, articolo/commessa, articolo/matricola, ...) invece che una giecenza a dettaglio per area/tipo giacenza.
- \*\*Conosci i 2 metodi per ottenere la sintesi?\*\*

 :  : VOC Id="SKIA0030" Txt="Conosci i 2 metodi per ottenere la sintesi?"
Si possono avere : 
- metodo delle chiusure mensili :  ogni mese si sommano alla sintesi giacenza del mese precedente tutti i movimenti di carico e si tolgono tutti i movimenti di scarico, ottenendo così la nuova giacenza del fine mese. Annualmente la giecenza di fine anno viene congelata dell'archivio delle sintesi fiscali e si sommano tutti i carichi e gli scarichi dell'anno
- metodo dala giacenza attuale :  annualmente si lancia il programma inserendo la data di fine esercizio fiscale (fine anno) ed il tipo costo da utilizzare. Il programma, per ogni articolo calcola la giacenza a fine esercicio e la scrive, recupera la giecenza di fine esercizio precedente e la copia come giacenza di inizio esercizio del periodo successivo, se la differenza è positiva viene compilato anche il campo "carichi" se la differenza è negativa si compila il campo scarichi"

Si consiglia di utilizzare il secondo metodo perchè è meno sensibile a variazioni di impostazioni tabellari (es. nascita di nuove causali di movimentazione)
- \*\*Sai come ottenere il riepilogo movimenti carico scarico?\*\*

 :  : VOC Id="SKIA0040" Txt="Sai come ottenere il riepilogo movimenti carico scarico?"
Si utilizza il programma GMVA10 com impostazioni diverse a scenda che si ottengano le sintesi : 
- da chiusura mensile, devono essere selezionati i movimenti con rilevanza fiscale
- da giacenza attuale, devono essere selezionati tutti i movimenti che interessano le aree con rilevanza fiscale
- \*\*Sai quali sono le tabelle guida?\*\*

 :  : VOC Id="SKIA0050" Txt="Sai quali sono le tabelle guida?"
Tabella GM3, che contiene le impostazioni guida di costruzione dello scenario di magazzino fiscale.
Tabella MAF, dove sono descritti i magazzini fiscali.
Tabella MAG, dove si imposta la corrispondenza tra un magazzino fisico (plant) ed il relativo magazzino fiscale.
Tabella GMR, dove sono stabilite le aree con rilevanza fiscale (metodo da giacenza attuale).
Tabella GMC, dove sono stabilite le causali di movimentazione con rilevanza fiscale (metodo da chiusure periodiche).

Per una informazione più completa vedi documentazione tabelle : 
- [GM3 - Scenari di magazzino fiscale](Sorgenti/OG/TA/GM3)
- [MAF - Magazzini fiscali](Sorgenti/OG/TA/MAF)
- [MAG - Magazzino](Sorgenti/OG/TA/MAG)
- [GMR - Area](Sorgenti/OG/TA/GMR)
- [GMC - Causali di movimentazione](Sorgenti/OG/TA/GMC)
- \*\*Sai qual'è l'archivio di riferimento?\*\*

 :  : VOC Id="SKIA0060" Txt="Sai qual'è l'archivio di riferimento?"
Archivio GMSIAN0F dove, per ogni esercizio e per articolo, abbiamo :  giacenza iniziale, carichi totali, scarichi totali, giacenza finale, costo medio.

Per una informazione più completa vedi documentazione file : 
- [GMSIAN0F Sintesi Annuale Magazzino](Sorgenti/OJ/FILE/GMSIAN0F)
- \*\*Sai come assegnare rilevanza fiscale ad un'area giacenza?\*\*

 :  : VOC Id="SKIA0070" Txt="Sai come assegnare rilevanza fiscale ad un'area giacenza?"
Nella tabella di riferimento GMR c'è il campo trattamento fiscale, le aree che hanno in questo campo il valore F o S sono aree con rilevanza fiscale.

Per una informazione più completa vedi documentazione tabella : 
- [GMR - Area](Sorgenti/OG/TA/GMR)
- \*\*Sai cos'è un'area con trattamento fiscale a storno?\*\*

 :  : VOC Id="SKIA0080" Txt="Sai cos'è un'area con trattamento fiscale a storno?"
Un'area con trattamento fiscale a storno prevede che il valore della sua giacenza sia stornato dal totale del magazzino fiscale.

Un esempio di utilizzo può essere il caso di una fonderia alluminio in cui parte della lega di alluminio venga data dal cliente, in questi casi l'entrata merci dell'alluminio di proprietà del cliente carica sia l'area del magazzino centrale che un'area di storno di conto lavoro attivo. Tutta la movimentazione interna e di produzione avviene come se il materiale fosse di proprietà dell'azienda, alla spedizione al cliente (spedizione di conto lavoro attivo) viene scaricata l'area del conto lavoro attivo.
La gicenza di quest'area viene stornata dalla giacenza fiscale in modo da escludere la quota della lega di proprietà del cliente
- \*\*Sai come assegnare rilevanza fiscale ai movimenti di magazzino?\*\*

 :  : VOC Id="SKIA0090" Txt="Sai come assegnare rilevanza fiscale ai movimenti di magazzino?"
Nella tabella di riferimento GMC c'è il campo elemento di raggruppamento che contraddistingue i movimenti con rilevanza fiscale (carichi, scarichi).

Per una informazione più completa vedi documentazione tabella : 
- [GMC - Causali di movimentazione](Sorgenti/OG/TA/GMC)
- \*\*Sai come modificare il comportamento sulla rilevanza fiscale di un'area?\*\*

 :  : VOC Id="SKIA0100" Txt="Sai come modificare il comportamento sulla rilevanza fiscale di un'area?"
Nella tab. GM3 si imposta il "suffisso programma filtro aree".
Il programma di riferimento è GMVA01_X
- \*\*Sai come escludere un articolo dalla valorizzazione fiscale?\*\*

 :  : VOC Id="SKIA0110" Txt="Sai come escludere un articolo dalla valorizzazione fiscale?"
Normalmente la classe fiscale (Tab. BRF) associata all'articolo ne determina il comportamento in valorizzazione fiscale.
Per gestire casi particolari in tab. GM3 si imposta il "suffisso programma filtro articoli".
Il programma di riferimento è GMVA00_x.
- \*\*Sai come modificare la scrittura del GMSIAN, es. per assegnare un costo pa\*\*

 :  : VOC Id="SKIA0120" Txt="Sai come modificare la scrittura del GMSIAN, es. per assegnare un costo particolare?"
Per gestire casi particolari in tab. GM3 si imposta il "suffisso programma aggiustamento".
Il programma di riferimento è GMVA52_x.
- \*\*Sai come fare per avere un magazzino fiscale per classe materiale invece c\*\*

 :  : VOC Id="SKIA0130" Txt="Sai come fare per avere un magazzino fiscale per classe materiale invece che per articolo?"
Nella tabella GM3 inserire come oggetto di raggruppamento l'OAV di articolo I/10 e impostare "1" nel campo "Raggruppamento sintetico"
- \*\*Sai come fare per avere un magazzino fiscale per articolo più un altro ogg\*\*

 :  : VOC Id="SKIA0140" Txt="Sai come fare per avere un magazzino fiscale per articolo più un altro oggetto (es. articolo/configurazione?"
Nella tabella GM3 impostare "1" nel campo "Gestione oggetto di riferimento" e valorizzare "Tipo / Parametro Oggetto di Riferimento"
- \*\*Sai come avere diversi tipi di valorizzazione?\*\*

 :  : VOC Id="SKIA0150" Txt="Sai come avere diversi tipi di valorizzazione?"
Creare diversi elementi di tab. GM3 (diversi scenari) ciascuno con impostazioni diverse e lanciare n. volte il programma di creazione richiamando i vari scenari.
- \*\*Sai come avere valorizzazioni mensili?\*\*

 :  : VOC Id="SKIA0160" Txt="Sai come avere valorizzazioni mensili?"
Creare uno scenario per le valorizzazioni annuali (es. AA) ed uno per ogni mese per le valorizzazioni mensili (es. GEN, FEB, MAR, ....) impostare negli scenari mensili il campo "Scenario base" con AA.

In questo modo la creazione di uno scenario mensile copia dallo scenario annuale gli esercizi precedenti.


Per una informazione più completa vedi documentazione tabella : 
- [GM3 - Scenari di magazzino fiscale](Sorgenti/OG/TA/GM3)

- \*\*Sai quali diverse valorizzazioni posso avere in stampa sintesi?\*\*

 :  : VOC Id="SKIA0170" Txt="Sai quali diverse valorizzazioni posso avere in stampa sintesi?"
I tipi di valorizzazione che si possono avere utilizzando i programmi di "Valorizzazione sintesi" e "Valorizzazione sintesi estesa" (GMVA40 - GMVA43A) sono : 
\* Lifo
\* Fifo
\* Valorizzato con costo memorizzato in archivio
\* Valorizzato dinamicamente con un tipo costo/livello in input
