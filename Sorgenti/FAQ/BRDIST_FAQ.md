- **Sai qual è la tabella guida?**

 :  : VOC Id="SKIB0010" Txt="Sai qual è la tabella guida?"
La tabella BRL.

Per una informazione più completa vedi documentazione tabella : 
- [BRL - Tipo distinta](Sorgenti/OG/TA/BRL)
- **Sai cos'è il coefficiente di impiego?**

 :  : VOC Id="SKIB0020" Txt="Sai cos'è il coefficiente di impiego?" Als="comm"
è la quantità di componente che serve per produrre un assieme
- **Sai se esistono vari tipi di esplosione / implosione, ne conosci i signifi**

 :  : VOC Id="SKIB0030" Txt="Sai se esistono vari tipi di esplosione / implosione, ne conosci i significati?" Als="comm"
Si possono vedere tutti dalla interrogazione distinta : 
* Esplosione : 
** 1 = tecnica :  vengono mostrati tutti i legami del primo livello
** 2 = scalare :  vengono mostrati tutti i legami a tutti i livelli (fino alla materia prima)
** 3 = di produzione :  vengono mostrati solo i legami validi al primo livello
** 4 = di produzione totale :  come l'esplosione a scalare solo che vengono considerati solo i legami validi
** 5 = ai materiali base :  presenta solo i componenti all'ultimo livello (il coeficiente di impiego è il prodotto del C.I. a tutti i livelli)
** 6 = riepilogata :  presenta i componenti una sola volta per articolo e somma i C.I. a parità di articolo
** 7 = riepilogata ai materiali base :  come la 5 ma somma i C.I. a partità di articolo
** 8 = riepilogata di produzione :  come la 6 ma solo per i legami validi

* Implosione :  valgono le stesse regole viste per l'eplosione, con direzione inversa (dai componenti ai prodotti finiti)
- **Conosci il significato di sequenza?**

 :  : VOC Id="SKIB0040" Txt="Conosci il significato di sequenza?" Als="comm"
Esistono 2 sequenze : 
* prima del componente
* dopo il componente
hanno l'obiettivo principale di poter inserire lo stesso componente in più legami di distinta per lo stesso assieme (magari con coefficienti di impiego diversi per diverse date di validità, o per indicare operazioni di impiego diverse).
- **Sai se è possibile  impostare distinte in cui assiemi o componenti non sia**

 :  : VOC Id="SKIB0050" Txt="Sai se è possibile  impostare distinte in cui assiemi o componenti non siano articoli?" Als="comm"
In tabella BRL si possono impostare i tipi oggetto per assieme e per componenti (per la distinta base entrambi AR)
- **Sai perchè ci sono data inizio validità e data fine validità**

 :  : VOC Id="SKIB0060" Txt="Sai perchè ci sono data inizio validità e data fine validità" Als="comm"
La data di validità è uno dei modi con cui si indica che un legame è valido nelle esplosioni di produzione : 
* la data inizio validità indica da quando un legame diventa valido (blanks = dall'inizio dei tempi)
* la data inizio validità indica fino a quando un legame resta valido (blanks = fino alla fine dei tempi)
- **Conosci l'uso del criterio di selezione?**

 :  : VOC Id="SKIB0070" Txt="Conosci l'uso del criterio di selezione?"
Si utilizza per le distinte "configurate", dove il legame di distinta assume diversi significati in funzione di condizioni esterne (configurazione). I diversi significati possono essere : 
* validità del legame
* cambio del codice componente
* cambio del coefficiente di impiego
* una combinazione dei precedenti

Questi diversi comportamenti si ottengono attraverso l'impostazione del criterio di selezione che è un elemento della tabella BRS.

Per una informazione più completa vedi documentazione tabella : 
- [BRS - Criteri di selezione](Sorgenti/OG/TA/BRS)
- **Sai cosa comporta l'impostazione del legame interno/esterno?**

 :  : VOC Id="SKIB0080" Txt="Sai cosa comporta l'impostazione del legame interno/esterno?"
Se il legame è Interno, significa che sarà considerato solo nel calcolo impegni materiali degli ordini di produzione, se è Esterno sarà considerato solo nel calcolo impegni materiali degli ordini di conto lavoro.
- **Sai cosa comporta l'impostazione del tipo legame?**

 :  : VOC Id="SKIB0090" Txt="Sai cosa comporta l'impostazione del tipo legame?"
Il tipo legame, se presente, si sostituisce al tipo parte dell'articolo e lo può rendere fittizio in assoluto oppure fittizio per produzione o fittizio per C/Lavorazione.
Esempio :  se l'articolo ha tipo parte = 2  ed il tipo legame è = 3, il calcolo degli impegni materiali degli ordini di conto lavoro salta il componente e passa ai suoi figli di distinta
- **Sai cos'è e quando si usa l'operazione di impiego?**

 :  : VOC Id="SKIB0100" Txt="Sai cos'è e quando si usa l'operazione di impiego?"
L'operazione di impiego è la fase del ciclo di lavorazione dell'assieme dove viene utilizzato il componente.

Questa informazione di solito viene utilizzata dove ci sono cicli complessi con un lungo tempo di attraversamento, in questi casi impostare una operazione di impiego, insieme alla modalità di scarico impegni materiali alla fase (tab. P5I), fa si che il sistema scarichi il componente solo quando viene dichiarata la fase corrispondente all'operazione di impiego.
- **Sai impostare il tipo ciclo dove controllare l'operazione di impiego?**

 :  : VOC Id="SKIB0110" Txt="Sai impostare il tipo ciclo dove controllare l'operazione di impiego?"
In tabella BRL c'è il campo "Tipo fase Ciclo"
- **Sai quando usare la quantità lotto?**

 :  : VOC Id="SKIB0120" Txt="Sai quando usare la quantità lotto?"
Se presente è una quantità da aggiungere a quella calcolata attraverso il coeffciente di impiego.

Esempio :  Coefficiente di impiego = 5, Qtà per lotto = 9, Ordine di produzione da 1000; il fabbisogno è 5009 (= 5 X 1000 + 9).
Potrebbe indicare la qtà scartata ad ogni avviamento della produzione.
- **Sai quando usare la percentuale rettifica impiego?**

 :  : VOC Id="SKIB0130" Txt="Sai quando usare la percentuale rettifica impiego?"
La percentuale di rettifica d'impiego indica la percentuale del componente che viene consumata durante la lavorazione (es. quantità del componente scartata mediamente durante la lavorazione).
La quantità dell'impegno viene aumentata della percentuale indicata per sopperire a tale perdita.
- **Sai quando usare la rettifica tempo?**

 :  : VOC Id="SKIB0140" Txt="Sai quando usare la rettifica tempo?"
La rettifica tempo indica al sistema di pianificazione il numero di giorni con cui anticipare la richiesta di disponibilità del componente. Tale numero sostituisce il lead time tipico dell'assieme definito nei parametri di pianificazione. Calcola l'arretramento degli impieghi a partire dalla data di fine pianificata per l'ordine di produzione dell'assieme superiore.

In pianificazione si usa per differenziare la data di fabbisogno di un componente rispetto alla data normalmente calcolata che è uguale a DATA DI FABBISOGNO DELL'ASSIEME meno LEAD TIME DELL'ASSIEME.
- **Sai quando usare il tipo coefficiente = divisore?**

 :  : VOC Id="SKIB0150" Txt="Sai quando usare il tipo coefficiente = divisore?"
Si usa quando il coefficiente di impiego di un componente sarebbe una quantità decimale.

Esempio se abbiamo il componente C che è un cavo gestito a metri e ne viene usati 1 millimetro nell'assieme A, nel legame distinta possiamo mettere 1000 come coefficiente di impiego e impostare il tipo coefficiente = divisore.
In questo modo ad esempio per produrre 10000 assiemi A servono 10 metri di C

Il tipo divisore si utilizza quando la qtà del componente è molto piccola (oltre i 6 decimali)
- **Sai cos'è il Low Level Code?**

 :  : VOC Id="SKIB0160" Txt="Sai cos'è il Low Level Code?" Als="comm"
Il low level code è il livello minimo di distinta in cui si trova il componente.
Se "1" e "2" sono dei prodotti finiti e "C" è un compoente di "A" e di "1" ed "A" è componente di "2"; il low level code di "C" è = 2.
Il LLC viene usato in pianificazione per capire quando calcolare i fabbisogni del componente.
- **Sai come fare in modo che il LLC venga calcolato dinamicamente?**

 :  : VOC Id="SKIB0170" Txt="Sai come fare in modo che il LLC venga calcolato dinamicamente?"
In tabella BRL c'è il campo "Calcolo dinamico llc".

Nota, nella stessa tabella c'è anche il campo"Suff.pgm agg.Lowl.c."
- **Sai come attivare la gestione in formato esteso?**

 :  : VOC Id="SKIB0180" Txt="Sai come attivare la gestione in formato esteso?"
In tabella BRL c'è il campo "Ass.gest.Completa" che se è uguale a : 
* 1, il formato di gestione a righe viene presentato in forma completa (3 righe) 80 colonne
* E, il formato di gestione a righe viene presentato in forma estesa a 132 colonne per decodificare in modo completo gli articoli
- **Sai come lanciare un programma in uscita dalla gestione?**

 :  : VOC Id="SKIB0190" Txt="Sai come lanciare un programma in uscita dalla gestione?"
In tabella BRL c'è il campo "Suff.pgm post Gest."
- **Sai come gestire distinte base presenti su archivi diversi da BRDIST0F?**

 :  : VOC Id="SKIB0200" Txt="Sai come gestire distinte base presenti su archivi diversi da BRDIST0F?"
Esistono 2 modi : 
* la tabella di personalizzazione B£1 dove si imposta l'ambiente della distinta base
* la tab. BRL dove, nel campo "Ambiente dist." è possibile impostare un ambiente specifico per il tipo distinta, se si vuole avere lo stesso ambiente anche in gestione oltre che in interrrogazione allora deve essere impostato anche il campo "Anche in gestione"
- **Sai come permettere o inibire i loop di distinta?**

 :  : VOC Id="SKIB0210" Txt="Sai come permettere o inibire i loop di distinta?"
In tabella BRL c'è il campo "Ammesso ricircolo", ovviamente non deve MAI essere impostato per il tipo distinta base (di solito tipo distinta = ART)
- **Sai come richiedere la conferma F6 in uscita dalla manutenzione?**

 :  : VOC Id="SKIB0220" Txt="Sai come richiedere la conferma F6 in uscita dalla manutenzione?"
In tab. BRL c'è il campo "Conferma uscita"
