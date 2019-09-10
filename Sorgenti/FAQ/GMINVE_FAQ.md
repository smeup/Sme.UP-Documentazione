- **Quali sono gli obiettivi dell'inventario fisico?**

 :  : VOC Id="SKIA0010" Txt="Quali sono gli obiettivi dell'inventario fisico?" Als="comm"
Adeguare le giacenze teoriche alle effettive qtà fisiche rilevate.
Verificare la bontà della gestione giacenze (minori sono le rettifiche migliore è la gestione)
- **Conosci le modalità di inventario fisico supportate da SmeUP?**

 :  : VOC Id="SKIA0020" Txt="Conosci le modalità di inventario fisico supportate da SmeUP?" Als="comm"
In SmeUP esistono 2 modalità di esecuzione inventario fisico : 
- con cartellini
- con liste di conta
- **Conosci il processo tipico di un inventario con cartellini?**

 :  : VOC Id="SKIA0030" Txt="Conosci il processo tipico di un inventario con cartellini?" Als="comm"
Vengono predisposti n. cartellini di conta con una propria numerazione.
I cartellini possono essere suddivisi in blocchi (lotti di conta), ogni lotto identifica un gruppo di cartellini con numerazione progressiva e senza buchi intermedi.
Ciascun blocco può essere affidato ad un responsabile.
I responsabili battono a tappeto l'area da inventariare, per ogni articolo/contenitore, segnano sul cartellino :  magazzino, area, tipo giacenza, articolo, codice collo, eventuali altri dati caratteristici della giacenza (es. ubicazione, lotto, ..) quantità contata. Dopo averlo registrato sul cartellino il responsabile marca (es con un bollino adesivo) l'articolo/contenitore registrato.
A fine inventario tutti i cartellini inutilizzati vengono annullati.
I cartellini utili vengono inseriti nel sistema.
Per ogni lotto di conta viene eseguito un controllo di congruenza sulla numerazione onde verificare che tutti i cartellini validi siano stati inseriti.
Viene lanciato un programma che totalizza a parità di chiave giacenza i cartellini registrati.
La lista ottenuta dalla totalizzazione viene confrontata con la giacenza teorica alla data e vengono calcolate le differenze.
Le differenze possono essere analizzate ed eventualmente si ripetono delle conte modificando la quantità effettiva.
Per le differenze finali vengono lanciate le rettifiche di giacenza.
- **Conosci il processo tipico di un inventario con liste di conta?**

 :  : VOC Id="SKIA0040" Txt="Conosci il processo tipico di un inventario con liste di conta?" Als="comm"
Vengono preparate delle liste di conta (es. dalla giacenza teorica).
Le liste di conta vengono stampate (di solito senza indicare la quantità) e consegnate ai responsabili.
I responsabili battono a tappeto l'area da inventariare, per ogni articolo/contenitore, segnano sulla lista la quantità contata. Dopo averlo registrato sulla lista il responsabile marca (es con un bollino adesivo) l'articolo/contenitore registrato.
Le quantità registrate nelle liste di conta vengono inserite nel sistema.
La quantità contata viene confrontata con la giacenza teorica alla data e vengono calcolate le differenze.
Le differenze possono essere analizzate ed eventualmente si ripetono delle conte modificando la quantità effettiva.
Per le differenze finali vengono lanciate le rettifiche di giacenza.
- **Sai quali sono le tabelle guida per l'inventario con cartellini?**

 :  : VOC Id="SKIA0050" Txt="Sai quali sono le tabelle guida per l'inventario con cartellini?"
Tabella GMI, che contiene la lista degli inventari con le relative impostazioni (data esecuzione, modalità di creazione liste di conta, metodo per rifasatura qtà teorica, ...).
Tabella GML, dove sono codificati i lotti di conta previsti per un inventario, le regole di numerazione e controllo cartellini, e la possibilità di vedere la giacenza teorica in fase di inserimento quantità cartellino.

Per una informazione più completa vedi documentazione tabelle : 
- [GMI - Codice inventario](Sorgenti/OG/TA/GMI)
- [GML - Lotto di conta inventariale](Sorgenti/OG/TA/GML)
- **Sai quali sono gli archivi di riferimento per l'inventario con cartellini?**

 :  : VOC Id="SKIA0060" Txt="Sai quali sono gli archivi di riferimento per l'inventario con cartellini?"
Il file GMRIIN0F, che contiene i cartellini inventario organizzati per lotto di conta.
Il file GMDAIN0F, che contiene le conte e/o i cartellini totalizzati di un inventario.

Per una informazione più completa vedi documentazione archivi : 
- [GMRIIN0F Righe cartellini di conta](Sorgenti/OJ/FILE/GMRIIN0F)
- [GMDAIN0F Dati&-x2f;Rettifiche di inventario](Sorgenti/OJ/FILE/GMDAIN0F)
- **Sai quali sono le tabelle guida per l'inventario con liste di conta?**

 :  : VOC Id="SKIA0070" Txt="Sai quali sono le tabelle guida per l'inventario con liste di conta?"
Tabella GMI, che contiene la lista degli inventari con le relative impostazioni (data esecuzione, modalità di creazione liste di conta, metodo per rifasatura qtà teorica, ...).

Per una informazione più completa vedi documentazione tabella : 
- [GMI - Codice inventario](Sorgenti/OG/TA/GMI)
- **Sai quali sono gli archivi guida per l'inventario con liste di conta?**

 :  : VOC Id="SKIA0080" Txt="Sai quali sono gli archivi guida per l'inventario con liste di conta?"
Il file GMDAIN0F, che contiene le conte e/o i cartellini totalizzati di un inventario.

Per una informazione più completa vedi documentazione archivio : 
- [GMDAIN0F Dati&-x2f;Rettifiche di inventario](Sorgenti/OJ/FILE/GMDAIN0F)
- **Sai quali sono i vari modi di creazione cartellini?**

 :  : VOC Id="SKIA0090" Txt="Sai quali sono i vari modi di creazione cartellini?"
I cartellini possono essere acquistati prestampati, in questo caso di solito si fanno anche numerare dal fornitore. Nel cartellino, a cura dell'esecutore dovranno essere compilati :  Cod. Inventario, Lotto di conta, Articolo, Quantità, Esecutore, Area, Tipo giacenza, eventuali altri dati caratteristici della giacenza (es. lotto, ubicazione, collo, ...)
I cartellini possono anche essere creati direttamente nel programma, partendo da una estrazione liste di conta (es. estrazione da giacenza) e poi creandoli per lotto di conta. In questo secondo caso le varie informazioni, con esclusione dell'esecutore e della qtà contata, sono già presenti e stampabili.
- **Sai come estrarre i cartellini dalle liste di conta create in precedenza?**

 :  : VOC Id="SKIA0100" Txt="Sai come estrarre i cartellini dalle liste di conta create in precedenza?"
Utilizzando il programma di gestione GMSI03, attivando l'opzione "Cartellini di conta" e successivamente "Estrazione da inventario".
- **Sai come numerare i cartellini?**

 :  : VOC Id="SKIA0110" Txt="Sai come numerare i cartellini?"
I cartellini posso essere pre-stampati e pre-numerati, in questo caso nella tabella GML devono essere inseriti il numero iniziale e quello finale.
Se invece devono essere stampati dal programma di gestione, in fase di creazione si può utilizzare un numeratore, da inserire in tab. GML, oppure si può far numerare a partire dal numero iniziale di tab. GML.
Anche le opzioni di numerazione sono in  tab. GML.
- **Sai come inserire le qtà contate?**

 :  : VOC Id="SKIA0120" Txt="Sai come inserire le qtà contate?"
Utilizzando il programma di gestione GMSI03, attivando l'opzione "Cartellini di conta" e successivamente "Gestione in lista" (utilizzabile per modificare cartellini già inseriti oppure etratti in precedenza), oppure "Gestione per Lotto di conta o Articolo"
- **Sai come inserire nuovi cartellini non creati in precedenza?**

 :  : VOC Id="SKIA0130" Txt="Sai come inserire nuovi cartellini non creati in precedenza?"
Nelle funzioni di inserimento quantità contata c'è anche un bottone F10 per l'inserimento di un nuovo cartellino.
- **Sai come cancellare i cartellini di un lotto?**

 :  : VOC Id="SKIA0140" Txt="Sai come cancellare i cartellini di un lotto?"
Utilizzando il programma di gestione GMSI03, attivando l'opzione "Cartellini di conta" e successivamente "Cancellazione Lotto di conta"
- **Sai come stampare i cartellini?**

 :  : VOC Id="SKIA0150" Txt="Sai come stampare i cartellini?"
Utilizzando il programma di gestione GMSI03, attivando l'opzione "Cartellini di conta" e successivamente "Stampa"
- **Sai come modificare di massa lo stato dei cartellini?**

 :  : VOC Id="SKIA0160" Txt="Sai come modificare di massa lo stato dei cartellini?"
Utilizzando il programma di gestione GMSI03, attivando l'opzione "Cartellini di conta" e successivamente "Gestione stato"
- **Sai cosa si ottiene totalizzando i cartellini?**

 :  : VOC Id="SKIA0170" Txt="Sai cosa si ottiene totalizzando i cartellini?"
Si leggono i cartellini in stato di "contato" presenti per l'inventario e, a parità di chiave giacenza, si sommano sommando la quantità contata alle liste di conta (se il record  manca viene creato, altrimenti viene aggiornato sommando la quantità)
- **Sai come totalizzare i cartellini?**

 :  : VOC Id="SKIA0180" Txt="Sai come totalizzare i cartellini?"
Utilizzando il programma di gestione GMSI03, attivando l'opzione "Cartellini di conta" e successivamente "Totalizzazione cartellini"
- **Sai come stornare la totalizzazione cartellini?**

 :  : VOC Id="SKIA0190" Txt="Sai come stornare la totalizzazione cartellini?"
Utilizzando il programma di gestione GMSI03, attivando l'opzione "Cartellini di conta" e successivamente "Annulla totalizzazione cartellini"
- **Sai quali sono i vari modi di estrazione liste di conta?**

 :  : VOC Id="SKIA0200" Txt="Sai quali sono i vari modi di estrazione liste di conta?"
I modi di estrazione lista di conta vengono impostati in tab. GMI e sono : 
1. Partendo dall'anagrafico articoli viene utilizzata la giacenza calcolata alla data di inventario (Campo DATA ESECUZIONE). ATTENZIONE  :  Il calcolo alla data viene eseguito tramite la £GMC per ogni singolo articolo. Verrà pertanto ritornato un valore per articolo, totalizzato in funzione delle parzializzazioni
scelte sui codici di giacenza. Per ogni estrazione è obbligatorio indicare area e tipo giacenza.
2. Partendo dall'anagrafico articoli viene utilizzata la giacenza della Foto (Campo FOTO PARTENZA) e alla data inventario (Campo DATA ESECUZIONE).
3. Partendo dall'anagrafico articoli viene utilizzata la giacenza al momento dell'elaborazione.
4. Viene utilizzata la giacenza di una Foto partendo direttamente dall'anagrafico delle FOTO (Campo FOTO DI PARTENZA) e alla data inventario (Campo DATA ESECUZIONE).
5. Viene utilizzata la giacenza al momento dell'elaborazione partendo direttamente dall'anagrafico giacenze.
6. Viene lanciato il programma di estrazione utente.
- **Sai come inserire le qtà contate in lista?**

 :  : VOC Id="SKIA0210" Txt="Sai come inserire le qtà contate in lista?"
Utilizzando il programma di gestione GMSI03, attivando l'opzione "Liste di conta" e successivamente "Gestione in lista". Oppure "Gestione per Giacenza o Articolo". Oppure da una matrice modificabile di looc_up in "Gestione",  "Modifica liste di conta con Matrice"
- **Sai come inserire una qtà contata a zero in lista?**

 :  : VOC Id="SKIA0220" Txt="Sai come inserire una qtà contata a zero in lista?"
Con l'opzione "C" = Forza contato
- **Sai come inserire delle conte che non erano presenti in lista?**

 :  : VOC Id="SKIA0230" Txt="Sai come inserire delle conte che non erano presenti in lista?"
Con il bottone F10 di inserimento nuova conta. Oppure da una matrice modificabile di looc_up in "Gestione",  "Immissione liste di conta con Matrice"
- **Sei come valorizzare con un tipo costo le liste di conta?**

 :  : VOC Id="SKIA0240" Txt="Sei come valorizzare con un tipo costo le liste di conta?"
Utilizzando il programma di gestione GMSI03, attivando l'opzione "Liste di conta" e successivamente "Completamento a valore".
Il tipo costo / livello da utilizzare è specificato in tab. GM1.
- **Sai come stampare le liste di conta?**

 :  : VOC Id="SKIA0250" Txt="Sai come stampare le liste di conta?"
Utilizzando il programma di gestione GMSI03, attivando l'opzione "Liste di conta" e successivamente "Stampa".
- **Sai che è possibile importare la qtà contata da un foglio excel?**

 :  : VOC Id="SKIA0260" Txt="Sai che è possibile importare la qtà contata da un foglio excel?"
Utilizzando il programma di gestione GMSI03, attivando l'opzione "Liste di conta" e successivamente "Import contato da Excel". Il csv deve essere in IFS e deve avere un tracciato prestabilito.
- **Sai come modificare di massa lo stato delle liste di conta ed eventualment**

 :  : VOC Id="SKIA0270" Txt="Sai come modificare di massa lo stato delle liste di conta ed eventualmente azzerare la qtà contata?"
Utilizzando il programma di gestione GMSI03, attivando l'opzione "Liste di conta" e successivamente "Gestione stato e pulizia quantità effettiva".
- **Sai eliminare dalla lista le righe con delta = zero?**

 :  : VOC Id="SKIA0280" Txt="Sai eliminare dalla lista le righe con delta = zero?"
Utilizzando il programma di gestione GMSI03, attivando l'opzione "Liste di conta" e successivamente "Cancellazione scostamento nullo".
- **Sai come aggiornare la qtà prevista nelle liste di conta?**

 :  : VOC Id="SKIA0290" Txt="Sai come aggiornare la qtà prevista nelle liste di conta?"
Utilizzando il programma di gestione GMSI03, attivando l'opzione "Ripresa giacenza".
- **Sai quali sono i diversi metodi di aggiornamento qtà prevista?**

 :  : VOC Id="SKIA0300" Txt="Sai quali sono i diversi metodi di aggiornamento qtà prevista?"
1. Ripresa quantità giacenza alla data.
2. Ripresa quantità giacenza da Foto (Campo FOTO-RIFASAT.INVENTARIO) alla data (CAMPO DATA-RIFASAT.INVENTARIO).
3. Ripresa quantità giacenza attuale.

I vari metodi sono impostati nella tabella GMI.
- **Sai lanciare le rettifiche di inventario?**

 :  : VOC Id="SKIA0310" Txt="Sai lanciare le rettifiche di inventario?"
Utilizzando il programma di gestione GMSI03, attivando l'opzione "Rettifiche".
- **Sai stornare le rettifiche precedentemente lanciate?**

 :  : VOC Id="SKIA0320" Txt="Sai stornare le rettifiche precedentemente lanciate?"
Utilizzando il programma di gestione GMSI03, attivando l'opzione "Storno Rettifiche".
- **Sai quali sono classe/funzione per autorizzare le funzioni dell'inventario**

 :  : VOC Id="SKIA0330" Txt="Sai quali sono classe/funzione per autorizzare le funzioni dell'inventario?"
Funzione ABILITA e funzioni GMSI03 e GMSI03_xx.
- **Sai come trovare classe/funzione di autorizzazione?**

 :  : VOC Id="SKIA0340" Txt="Sai come trovare classe/funzione di autorizzazione?"
In LoocUP lanciare la funzione GMSI03 e mettere uno slash "/" nel campo opzione.
