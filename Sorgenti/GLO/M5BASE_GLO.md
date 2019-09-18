- **MRP**

 :  : VOC Id="000010" Txt="MRP"
MRP  :  Material requirement Planning. E' lo strumento con cui si pianificano i materiali da costruire o acquistare in azienda per soddisfare i fabbisogni principali dell'azienda.
- **Fonte**

 :  : VOC  Id="000020" Txt="Fonte"
Fonte :  è l'evento che produce (se positiva) o consuma (se negativa) il materiale; vedere help di tabelle M5E ed M5F
- **Gruppo Fonti**

 :  : VOC  Id="000025" Txt="Gruppo Fonti"
Gruppo fonti :  è un raggruppamento delle fonti
- **Leadtime di rettifica**

 :  : VOC Id="000030" Txt="Leadtime di rettifica"
Leadtime di rettifica :  sono i giorni desiderati di anticipo rispetto alla data di disponibilità; rappresentano il tempo necessario per collaudare, o imballare, o protettivo dei ritardi di consegna.
- **Leadtime variabile**

 :  : VOC  Id="000040" Txt="Leadtime variabile"
Leadtime variabile :  sono i giorni necessari per trasformare un lotto standard; permette di variare il leadtime di un suggerimento in funzione della quantità del suggerimento LeadTime=Qty/LOTSTD \* Leadtime variabile
- **Leadtime fisso**

 :  : VOC  Id="000050" Txt="Leadtime fisso"
leadtime fisso :  sono i giorni che intercorrono tra la data suggerimento e l'inizio della produzione; in assenza di lt variabile e di rettifica l'inizio produzione coincide con la fine produzione e con la data di disponibilità, quindi il lt fisso diventa il lt totale
- **ATP**

 :  : VOC Id="000060" Txt="ATP"
ATP  :  Available To Promise; è il processo attraverso cui viene calcolata la data di consegna di un'ordine di vendita, in funzione dei leadtimes di tutti i componenti della distinta base e della disponibilità libera degli stessi
- **Disponibilità materiale**

 :  : VOC Id="000070" Txt="Disponibilità materiale"
Disponibilità Materiale :  è la funzione che , dato un gruppo fonti, rappresenta nel tempo la quantità disponibile di un materiale.
- **Disponibilità libera**

 :  : VOC Id="000080" Txt="Disponibilità libera"
Disponibilità libera  :  parte da una disponibilità materiali ed è  una funzione che rappresenta nel tempo la quantità di materiale che si può prelevare senza inficiare i prelievi previsti, ossia senza mandare in negativo la funzione disponibilità materiale da cui viene calcolata la disponibilità libera. Dovendo servirsi di un gruppo fonti di partenza, è chiamata "Metafonte".


- **CTP**

 :  : VOC Id="000090" Txt="CTP"
CTP :  Capacity To Promise, è la funzione che permette, dopo aver eseguito una analisi ATP di un fabbisogno, di analizzare se esistono le risorse (generalmente ore di calendario lavorativo) necessarie per supportare le attività di trasformazione che l'ATP ha ipotizzato nel determinare la data di riordino.
- **Ordinamento fonti**

 :  : VOC Id="000100" Txt="Ordinamento fonti"
E' la possibilità di ordinare le fonti a parità di data
- **Fabbisogno principale**

 :  : VOC Id="000110" Txt="Fabbisogno principale"
E' la necessità di materiale da cui si parte per elaborare l'MRP, ossia la domanda principale.
Potrebbe essere di tipo incerto ( le previsioni) o di tipo certo (ordine di vendita confermato).
Normalmente riguarda i prodotti finiti, quelli che hanno livello minimo di distinta = 0.
Ma potrebbe anche riguardare articoli componenti ( Livello minimo di distinta > 0).
- **Fabbisogno dipendente**

 :  : VOC Id="000120" Txt="Fabbisogno dipendente"
Si tratta di un fabbisogno generato dall'eplosione di distinta base di un riordino ( pianificato o rilasciato) di uno degli assiemi di cui è componente. E' quindi un impegno pianificato o rilasciato di un riordino di un assieme superiore.
- **Scorta di sicurezza**

 :  : VOC Id="000130" Txt="Scorta di sicurezza"
E' la quantità che si vuole avere disponibile in magazzino per rispondere ad esigenze impreviste di materiale. E' un fabbisogno previsivo , quindi incerto.
- **Punto di riordino**

 :  : VOC Id="000140" Txt="Punto di riordino"
E' la quantità negativa che, se non coperta da giacenza o da ordine di copertura, deve essere coperta con la ricopertura di un lotto economico
- **Lotto economico**

 :  : VOC Id="000150" Txt="Lotto economico"
E' la quantità di riordino utilizzata nelle politiche di pianificazione dette " a punto di riordino"
- **Make to stock**

 :  : VOC Id="000160" Txt="Make to stock"
E' il tipo di politica di pianificazione che punta a generare una copertura del magazzino in funzione di previsti (incerti) fabbisogni, e non in funzione di ordini clienti certi.
- **Make to order**

 :  : VOC Id="000170" Txt="Make to order"
E' il tipo di politica di pianificazione che punta a coprire solo gli ordini clienti , ossia i fabbisogni certi.
