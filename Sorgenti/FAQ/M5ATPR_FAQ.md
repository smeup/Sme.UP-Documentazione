- \*\*Sai a cosa serve l'ATP?\*\*

 :  : VOC Id="SKIC0010" Txt="Sai a cosa serve l'ATP?" Als="comm"
Serve a determinare la data di consegna di una quantità di un articolo. può essere operato sia in modalità di simulazione ( se un cliente mi ordinasse questa quantità quando potrei consegnarla?) , sia in modalità definitiva, a partire da una riga di ordine inserita.
- \*\*Sai far partire l'ATP su una riga d'ordine di vendita?\*\*

 :  : VOC Id="SKIC0020" Txt="Sai far partire l'ATP su una riga d'ordine di vendita?"
Si attiva mettendo nel tipo riga (tab V5B) il modello di atp prescelto, mettendo sul tipo documento (tab V5D) il flag di attivazione ATP, ed inserendo nel flusso di inserimento riga (Tab B£H e B£J) il programma V5FUATP
- \*\*Sai impostare un gruppo fonti per la disponibilità libera di un ATP?\*\*

 :  : VOC Id="SKIC0030" Txt="Sai impostare un gruppo fonti per la disponibilità libera di un ATP?"
Il gruppo fonti per la disponibilità libera deve contenere le fonti di origine IR = impegni provvisori) e non dovrebbe contenere fonti di tipo previsivo , come la scorta minima o le previsioni......
- \*\*Sai impostare un gruppo fonti per un ATP multiplant?\*\*

 :  : VOC Id="SKIC0040" Txt="Sai impostare un gruppo fonti per un ATP multiplant?"
Un gruppo fonti per un ATP multiplant ha una proprietà particolare , un flag che indica che il magazzino di calcolo viene ricevuto e quindi NON è da impostare nel gruppo fonti !
- \*\*Sai impostare modelli di ATP diversi per tipi riga d'ordine diversi?\*\*

 :  : VOC Id="SKIC0050" Txt="Sai impostare modelli di ATP diversi per tipi riga d'ordine diversi?"
Essendo il modello ATP impostabile sul tipo riga V5, ogni diverso tipo riga può avere un modello diverso
- \*\*Sai leggere i risultati dell'ATP?\*\*

 :  : VOC Id="SKIC0060" Txt="Sai leggere i risultati dell'ATP?"
Bisogna utilizzare il formato completo (da impostare tramite F17), poi è utile visualizzare il percorso critico (F23), poi conviene andare all'inizio ed alla fine di ogni segmento (opzione I e F sulla riga).
Bisogna allenarsi un pò perchè non é banale.
- \*\*Sai far partire l' ATP solo dopo una certa data\*\*

 :  : VOC Id="SKIC0070" Txt="Sai far partire l' ATP solo dopo una certa data"
E' una delle opzioni del modello ATP (Tab M5H)
- \*\*Sai impostare un ATP che non lottizzi i riordini?\*\*

 :  : VOC Id="SKIC0080" Txt="Sai impostare un ATP che non lottizzi i riordini?"
E' una delle opzioni del modello ATP (tab M5H)
- \*\*Sai quali sono le fonti tipiche dell'ATP, che servono solo all'ATP?\*\*

 :  : VOC Id="SKIC0090" Txt="Sai quali sono le fonti tipiche dell'ATP, che servono solo all'ATP?"
Sono le fonti di origine IR, impegno provvisorio :  leggono i record del file M5IMPE0F che è il file dove vengono registrate le analisi ATP confermate , ossia quelle che provengono dall'inserimento ordini di vendita. Le simulazioni ATP che non si trasformano in ordine di vendita NON lasciano nessun record nel file M5IMPE0F.
- \*\*Sai cos'è un CTP ?\*\*

 :  : VOC Id="SKIC0110" Txt="Sai cos'è un CTP ?" Als="comm"
Il CTP , Capacity to promise, è una analisi ATP che dopo aver determinato cosa deve costruire per rispondere alla richiesta cliente, verifica anche che ci siano le capacità di risorse necessarie alla costruzione prevista.
- \*\*Sai far partire un CTP al termine dell'ATP?\*\*

 :  : VOC Id="SKIC0120" Txt="Sai far partire un CTP al termine dell'ATP?"
E' una delle opzioni del modello ATP (tab M5H)
- \*\*Sai preparare i dati di disponibiltà di risorsa per il CTP?\*\*

 :  : VOC Id="SKIC0130" Txt="Sai preparare i dati di disponibiltà di risorsa per il CTP?"
La preparazione della capacità residua da offrire alla analisi CTP prevede una schedulazione a capacità finita degli impegni di risorsa già esistenti. Notare che questi impegni potrebbero derivare sia da ordini di produzione rilasciati (quindi di origine VP) che da ordini di produzione pianificati (quindi di origine M5). Il che significa che anche l'MRP deve produrre impegni di risorsa !
Generalmente la costruzione della capacità residua si effettua in un piano MPS , con un flusso particolare che include una azione di "schedulazione" (pgm MPAP37)
- \*\*Sai impostare un CTP che avanzi la data in funzione della periodicità del \*\*

 :  : VOC Id="SKIC0140" Txt="Sai impostare un CTP che avanzi la data in funzione della periodicità del piano ?"
Bisogna scrivere un pgm chiamato M5M5HC_x che lo faccia ed impostarlo nell'opportuno campo in tabella M5H (modello ATP)
- \*\*Sai qual è la coerenza da mantenere tra le fonti copertura incluse nel gru\*\*

 :  : VOC Id="SKIC0150" Txt="Sai qual è la coerenza da mantenere tra le fonti copertura incluse nel gruppo fonti dell'ATP ed il profilo di carico del CTP ?"
Se il gruppo fonti ATP che definisce la disponibilità libera contiene anche gli ordini di produzione pianificati, BISOGNA costruire il profilo di carico che stà alla base del CTP includendo gli impegni di risorsa di origine M5, ossia quelli derivanti dagli ordini di produzione pianificati.
- \*\*Sai lanciare un ATP batch?\*\*

 :  : VOC Id="SKIC0160" Txt="Sai lanciare un ATP batch?"
Per lanciare un ATP Batch, ossia che analizzi in un colpo solo un insieme di ordini (testate e righe) bisogna fare un programma che esegua i seguenti passi logici : 
Selezione degli ordini da analizzare
Ordinamento della selezione
Applicazione del pgm V5FUATP alla lista ordinata degli ordini selezionati.

Ovviamente tramite la scelta dell'ordinamento si può favorire un cliente o una tipologia di articoli a dispetto della sequenza di ricevimento degli ordini cliente
- \*\*Sai quando gli impegni provvisori confermati vengono cancellati?\*\*

 :  : VOC Id="SKIC0170" Txt="Sai quando gli impegni provvisori confermati vengono cancellati?"
Gli impegni provvisori confermati (sono quelli che derivano dall'inserimento di una riga di vendita analizzata con ATP) vengono cancellati all'inizio dell'MRP.
- \*\*Sai cosa sono gli impegni provvisori provvisori?\*\*

 :  : VOC Id="SKIC0180" Txt="Sai cosa sono gli impegni provvisori provvisori?"
Gli impegni provvisori provvisori sono quelli "volatili" che vengono scritti all'interno di una simulazione ATP (up atp ), in quanto servono solo per tenere conto del consumo di un componente già impegnato nell'analisi di una riga di distinta.
- \*\*Sai cosa sono gli impegni provvisori confermati?\*\*

 :  : VOC Id="SKIC0190" Txt="Sai cosa sono gli impegni provvisori confermati?"
Gli impegni provvisori confermati sono quelli che derivano da una riga di vendita inserita con analisi ATP
- \*\*Sai quando gli impegni provvisori provvisori vengono cancellati?\*\*

 :  : VOC Id="SKIC0200" Txt="Sai quando gli impegni provvisori provvisori vengono cancellati?"
Gli impegni provvisori provvisori vengono cancellati alla fine di una simulazione ATP, ossia quando si esce dal prospetto di analisi per tornare all'inserimento di una nuova analisi.
- \*\*Sai simulare l'esecuzione di un ATP?\*\*

 :  : VOC Id="SKIC0210" Txt="Sai simulare l'esecuzione di un ATP?"
Con il programma M5FUATP , che viene lanciato anche come UP  ATP, o dal menu M5, interogazioni, Presentazione ATP .
- \*\*Sai in che momento l'eliminazione di una riga V5 datata con ATP rimette in\*\*

 :  : VOC Id="SKIC0220" Txt="Sai in che momento l'eliminazione di una riga V5 datata con ATP rimette in gioco tutti i suoi materiali impegnati?"
Immediatamente :  l'eliminazione di una riga V5 cancella anche gli impegni provvisori confermati relativi. Ovviamente, se l'eliminazione avviene dopo che l'MRP ha analizzato la riga e proposto suggerimenti per sostenerla, la fasatura delle coperture è nella applicazione dei suggerimenti MRP.
- \*\*Sai il significato e lo scopo dell'appiattimento al più tardi?\*\*

 :  : VOC Id="SKIC0240" Txt="Sai il significato e lo scopo dell'appiattimento al più tardi?"
La data dell'impegno provvisorio ATP può essere spostata al più tardi per evitare di "mangiare" il materiale troppo in anticipo rispetto al percorso critico determinato dall'ATP. Questo migliora la disponibilità libera vista dal prossimo ATP.
- \*\*Conosci il significato di percorso critico?\*\*

 :  : VOC Id="SKIC0230" Txt="Conosci il significato di percorso critico?"
Il percorso critico di un ATP è la sequenza più lunga di avvenimenti (pianificazione coperture) necessari per sostenere la data ATP. E' un concetto similare a quello di leadtime cumulato di un articolo :  il LT cumulato non è la somma dei singoli leadtime dei vari livelli di distinta , ma è solo la somma del ramo più lungo.
- \*\*Sai quando l'ATP applicato ad una riga di vendita NON anticipa la data ris\*\*

 :  : VOC Id="SKIC0250" Txt="Sai quando l'ATP applicato ad una riga di vendita NON anticipa la data rispetto alla data consegna richiesta sulla riga di vendita?"
Quando nei parametri del programma V5FUATP che è impostato sul flusso di inserimento riga, si imposta la data ATP come data al più presto, allora l'ATP della riga di vendita non anticipa rispetto alla data consegna richiesta.
