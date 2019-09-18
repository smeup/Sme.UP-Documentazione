- \*\*E' possibile cambiare il colore di sfondo di una label?\*\*

 :  : VOC Id="00010" Txt="E' possibile cambiare il colore di sfondo di una label?"
Il componente LAB ha molti attributi di setup, uno dei quali è 'BackColor' che consente di impostare il colore di sfondo della label.

- \*\*Posso gestire una variabile all'interno di una label?\*\*

 :  : VOC Id="00020" Txt="Posso gestire una variabile all'interno di una label?"
Si, è possibile passare a una label una variabile.

- \*\*Il componente label supporta i dinamismi?\*\*

 :  : VOC Id="00030" Txt="Il componente label supporta i dinamismi?"
Si, è possibile associare alla label dei dinamismi come ad esempio il click.

- \*\*Come posso inserire del testo in una label che mi venga disposto \*\*

 :  : VOC Id="00040" Txt="Come posso inserire del testo in una label che mi venga disposto verticalmente?"
Una tecnica per avere questo risultato è inserire più D.OGG nella scheda, in modo che ogni testo sia disposto sotto il precedente.

- \*\*Se ho più D.OGG nella mia sezione, posso disporli a piacere?\*\*

 :  : VOC Id="00050" Txt="Se ho più D.OGG nella mia sezione, posso disporli a piacere?"
Per fare questo basta creare uno script SCP_LAY, che disponga a nostro piacimento i nostri D.OGG.

- \*\*Se ho più D.OGG posso gestirne la grandezza del carattere singolarmente?\*\*

 :  : VOC Id="00060" Txt="Se ho più D.OGG posso gestirne la grandezza del carattere singolarmente?"
Anche in questo caso bisogna utilizzare un SCP_LAY in cui definiamo uno stile da applicare ad ogni D.OGG.

- \*\*Come posso creare uno stile personalizzato da applicare ai miei D.OGG?\*\*

 :  : VOC Id="00070" Txt="Come posso creare uno stile personalizzato da applicare ai miei D.OGG?"
Bisogna creare nello script di scheda un tag chiamato G.STY, in cui oltre al nome(che servirà per richiamarlo nell'SCP_LAY) defianiamo
tutte le cartteristiche grafiche che avrà il nostro stile appena creato.                          
