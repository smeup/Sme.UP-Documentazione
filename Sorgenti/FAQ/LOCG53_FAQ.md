- **Sai su che script si basano le generazioni tramite componente G53?**

 :  : VOC Id="SKIBA0010" Txt="Sai su che script si basano le generazioni tramite componente G53?"
SCP_G53
- **Sai qual'è la /copy alla base dell'utilizzo del componente G53?**

 :  : VOC Id="SKIBA0020" Txt="Sai qual'è la /copy alla base dell'utilizzo del componente G53?"
H53
- **Sai la differenza fra /copy G53 e componente G53?**

 :  : VOC Id="SKIBA0030" Txt="Sai la differenza fra /copy G53 e componente G53?"
- **Conosci la relazione fra componente G53 e servizio B£SER_43**

 :  : VOC Id="SKIBA0040" Txt="Conosci la relazione fra componente G53 e servizio B£SER_43"
Il B£SER_43 è il servizio che permette di simulare la creazione di un pdf tramite il componente G53 basandosi su uno script SCP_G53
- **Sai la differenza fra specifiche di definizione e specifiche di simulazio**

 :  : VOC Id="SKIBA0050" Txt="Sai la differenza fra specifiche di definizione e specifiche di simulazione negli script del componente G53"
Le specifiche di definizione mettono a disposzione delle strutture da poter utilizzare nella costruzione del layout del documento. Le specifiche di simulazione permettono di simulare la creazione di un documento passando dei parametri alla funzione di creazione o cablandoli nelle specifiche di simulazione
- **Sai come impostare il formato del foglio del documento generato**

 :  : VOC Id="SKIBA0060" Txt="Sai come impostare il formato del foglio del documento generato"
Tramite la specifica  :  : STR.SET ad inizio dello script
- **Sai come definire un tipo pagina nello script G53?**

 :  : VOC Id="SKIBA0070" Txt="Sai come definire un tipo pagina nello script G53?"
Tramite la specifica  :  : STR.PAG, assegnandogli un nome univoco nello script
- **Sai come definire lo header di pagina?**

 :  : VOC Id="SKIBA0080" Txt="Sai come definire lo header di pagina?"
Va definito, in una pagina, un  :  : STR.BOX con Typ "HEADER"
- **Sai come definire il footer di pagina?**

 :  : VOC Id="SKIBA0090" Txt="Sai come definire il footer di pagina?"
Va definito, in una pagina, un  :  : STR.BOX con Typ "FOOTER"
- **Sai come utilizzare l'attributo Ha nella specifica BOX?**

 :  : VOC Id="SKIBA0100" Txt="Sai come utilizzare l'attributo Ha nella specifica BOX?"
Il suo valore è la percentuale di pagina che il BOX occuperà. Quindi un valore di 3 indica che tale BOX occuperò il 3% della pagina cui appartiene
- **Sai come definire delle righe all'interno di un BOX?**

 :  : VOC Id="SKIBA0110" Txt="Sai come definire delle righe all'interno di un BOX?"
Con la specifica  :  : STR.RIG
- **Sai come usare l'attributo Dim della specifica RIG?**

 :  : VOC Id="SKIBA0120" Txt="Sai come usare l'attributo Dim della specifica RIG?"
Il valore assegnato a Dim indica quante volte la RIG starà, verticalmente, nella BOX cui appartiene. Un valore di 3 indica che la ROW starà nella BOX 3 volte
- **Sai come suddividere la riga un colonne (orizzontalmente)?**

 :  : VOC Id="SKIBA0130" Txt="Sai come suddividere la riga un colonne (orizzontalmente)?"
Tramite la specifica  :  : STR.COL
- **Sai come utilizzare l'atributo Dim della specifica COL?**

 :  : VOC Id="SKIBA0140" Txt="Sai come utilizzare l'atributo Dim della specifica COL?"
Il valore assegnato a Dim indica la percentuale di spazio (orizzontale) che verrà assegnata alla colonna  nella RIG cui appartiene
- **Sai come inserire un'immagine di oggetto in una specifica COL?**

 :  : VOC Id="SKIBA0150" Txt="Sai come inserire un'immagine di oggetto in una specifica COL?"
Tramite la specifica  :  : IMG, assegnando all'attributo File la variabile oggetto in questione tramite la sintassi
- **Sai come inserire una matrice originata da una funzione Looc.UP in una sp**

 :  : VOC Id="SKIBA0160" Txt="Sai come inserire una matrice originata da una funzione Looc.UP in una specifica COL?"
Tramite la specifica BOX, assegnando poi, tramite l'attributo Txt, una funzione che origini una matrice
- **Sai come inserire un grafico originato da una funzione Looc.UP in una spe**

 :  : VOC Id="SKIBA0170" Txt="Sai come inserire un grafico originato da una funzione Looc.UP in una specifica COL?"
Tramite la specifica BOX, assegnando poi, tramite l'attributo Txt, una funzione che origini un Chart
- **Sai come inserire un barcode in una specifica COL?**

 :  : VOC Id="SKIBA0180" Txt="Sai come inserire un barcode in una specifica COL?"
Tramite la specifica BCD, assegnando poi, tramite l'attributo A01 il tipo barcode desiderato, e tramite l'atrributo Txt il valore del barcode
- **Sai dove trovare la documentazione del componente G53?**

 :  : VOC Id="SKIBA0190" Txt="Sai dove trovare la documentazione del componente G53?"
Nella sezione Documentazione della scheda del componente
- **Sai come simulare la generazione di un PDF tramite componente G53?**

 :  : VOC Id="SKIBA0200" Txt="Sai come simulare la generazione di un PDF tramite componente G53?"
Tramite una F con componente G53, servizio B£SER_43, metodo STR.SIM, utilizzando uno script MB SCP_G53 che presenti delle specifiche  :  : SIM
