
- \*\*E' possibile visualizzare un dato sullo SpreadSheet come un numero con X \*\*

 :  : VOC Id="10001" Txt="E' possibile visualizzare un dato sullo SpreadSheet come un numero con X decimali?"

Sì basta definire il formato numerico e il numero di decimali sulla cella del corrispondente template Excel.

- \*\*E' possibile visualizzare una variabile Sme.UP sullo SpreadSheet, ad esempi\*\*

 :  : VOC Id="10002" Txt="E' possibile visualizzare una variabile Sme.UP sullo SpreadSheet, ad esempio la variabile \*SYSTEM?"

Sì basta scrivere nella cella del corrispondente template Excel :  ${smeupvars.eval('[\*SYSTEM]')}

- \*\*Come è possibile mostrare dati sullo SpreadSheet provenienti dal server e \*\*

 :  : VOC Id="10003" Txt="Come è possibile mostrare dati sullo SpreadSheet provenienti dal server e far si che le modifiche sullo SpreadSheet siano propagate sul server?"

Basta collegare al componente un servizio come viene fatto per matrice di aggiornamento ed input panel, attraverso gli attributi di setup UpdSvc, UpdPar, UpdExt. Il protocollo di comunicazione tra il servizio e il componente è lo stesso della matrice di aggiornamento e dell'input panel.


