### **Valore attuale**

Attualizzazione di un valore :  dato un montante (valore finale), la data iniziale e finale, e un valore di interesse, viene ritornato il valore attualizzato, che porta al montante, in caso di interesse composto su base annuale.

![B£MATE_A](http://localhost:3000/immagini/MBDOC_VOC-B£MATE_GLO/BXMATE_A.png)
### **Numero Elementi**

È il  numero di elementi della serie. Se è il caso, questo valore tiene conto dei "tagli" alla serie (senza zeri, senza massimo e minimo, tra estremi non nulli).


### **Somma**

È la somma degli elementi della serie. Se è il caso, questo valore tiene conto dei "tagli" alla serie (senza zeri, senza massimo e minimo, tra estremi non nulli).


### **Media**

È la media degli elementi della serie. Se è il caso, questo valore tiene conto dei "tagli" alla serie (senza zeri, senza massimo e minimo, tra estremi non nulli).


### **Varianza**

Si indica con S2 (esse quadro).
È data dalla somma dei quadrati delle differenze tra ogni valore della serie e il valor medio della serie, divisa per il numero degli elementi della serie meno uno. È un indice della dispersione dei valori della serie attorno al valore medio :  è espressa in un'unità di misura pari alla seconda potenza di quella della serie. Per questo motivo si preferisce l'utilizzo della deviazione standard, che è pari alla sua radice, e che quindi è nella stessa unità di misura della serie. Se è il caso, viene calcolato con i valori che tengono conto dei "tagli" alla serie (senza zeri, senza massimo e minimo, tra estremi non nulli).

![B£MATE_S2](http://localhost:3000/immagini/MBDOC_VOC-B£MATE_GLO/BXMATE_S2.png)

### **Deviazione standard**

Si indica con S (esse).
È data dalla somma dei quadrati delle differenze tra ogni valore della serie e il valor medio della serie, divisa per il numero degli elementi della serie meno uno, il tutto posto sotto radice quadra. È un indice della dispersione dei valori della serie attorno al valore medio :  è espressa nella stessa unità di misura della serie. Corrisponde alla radice quadrata della varianza. Suoi sinonimi sono :  "Scarto tipo", "Scarto quadratico medio", "Sigma". Se è il caso, viene calcolato con i valori che tengono conto dei "tagli" alla serie (senza zeri, senza massimo e minimo, tra estremi non nulli).
Con questa formula viene calcolata la deviazione standard con correzione di Gauss.

![B£MATE_S](http://localhost:3000/immagini/MBDOC_VOC-B£MATE_GLO/BXMATE_S.png)

### **MAD**

È l'acronimo di mean absolute deviation (deviazione media assoluta).   tra i dati e la media. È data dalla somma del valore assoluto delle differenze tra ogni valore della serie e il valor medio della serie, divisa per il numero degli elementi della serie. Rappresenta lo scostamento medio (in valore assoluto) dei valori della serie rispetto alla media, ed è espresso nella stessa unità di misura della serie. Se è il caso, viene calcolato con i valori che tengono conto dei "tagli" alla serie (senza zeri, senza massimo e minimo, tra estremi non nulli).

![B£MATE_MAD](http://localhost:3000/immagini/MBDOC_VOC-B£MATE_GLO/BXMATE_MAD.png)

### **MSD**

È l'acronimo di mean squared deviation (deviazione media quadratica).  tra i dati e la media. È data dalla somma dei quadrati delle differenze tra ogni valore della serie e il valor medio della serie, divisa per il numero degli elementi della serie. Se è il caso, viene calcolato con i valori che tengono conto dei "tagli" alla serie (senza zeri, senza massimo e minimo, tra estremi non nulli).

![B£MATE_MSD](http://localhost:3000/immagini/MBDOC_VOC-B£MATE_GLO/BXMATE_MSD.png)

### **CV**

È l'acronimo di Coefficiente di Variazione tra i dati e la media. È dato dal rapporto, moltiplicato per 100, tra la deviazone standard ed il valore assoluto della media. Essendo una percentuale, dà un'idea immediata della deviazione standard, indipendentemente dalla sua unità di misura.
Se è il caso, viene calcolato con i valori che tengono conto dei "tagli" alla serie (senza zeri, senza massimo e minimo, tra estremi non nulli).


### **Mediana**

Si ordina la serie :  se ha un numero di elementi dispari si prende il valore centrale; se ha un numero di elementi pari si prende la media dei due valori centrali.


### **CP**

Stima la capacità del processo considerando che la media sia centrata tra 2 limiti inferiore e superiore delle specifiche. Si assume che il risultato del processo sia distribuito secondo una distribuzione normale.

![B£MATE_CP](http://localhost:3000/immagini/MBDOC_VOC-B£MATE_GLO/BXMATE_CP.png)

### **CPL**

Stima la capacità del processo considerando se la specifica consiste solo del limite inferiore. Si assume che il risultato del processo sia distribuito secondo una distribuzione normale.

![B£MATE_CPL](http://localhost:3000/immagini/MBDOC_VOC-B£MATE_GLO/BXMATE_CPL.png)

### **CPU**

Stima la capacità del processo considerando se la specifica consiste solo del limite superiore. Si assume che il risultato del processo sia distribuito secondo una distribuzione normale.

![B£MATE_CPU](http://localhost:3000/immagini/MBDOC_VOC-B£MATE_GLO/BXMATE_CPU.png)

### **CPK**

Stima la capacità del processo considerando che la media potrebbe NON essere centrata tra 2 limiti inferiore e superiore delle specifiche. (Se la media non è centrata CP sovrastima la capacità del processo). CPK < 0 quando il processo cade al di fuori dei limiti di specifica. Si assume che il risultato del processo sia distribuito secondo una distribuzione normale.

![B£MATE_CPK](http://localhost:3000/immagini/MBDOC_VOC-B£MATE_GLO/BXMATE_CPK.png)

### **CPM**

Stima la capacità del processo attorno ad un obiettivo (target T). CPM è sempre > 0. Si assume che il risultato del processo sia distribuito secondo una distribuzione normale. È anche conosciuto come indice di capacità TAGUCHI

![B£MATE_CPM](http://localhost:3000/immagini/MBDOC_VOC-B£MATE_GLO/BXMATE_CPM.png)

### **CPKM**

Stima la capacità del processo attorno ad un obiettivo (target T) e considera che la media non sia centrata tra i limiti. Si assume che il risultato del processo sia distribuito secondo una distribuzione normale.

![B£MATE_012](http://localhost:3000/immagini/MBDOC_VOC-B£MATE_GLO/BXMATE_012.png)

### **Accuracy**

Per ogni elemento della serie si calcola il modulo della differenza percentuale tra la serie 2 e la serie 1, e se ne calcola il complemento a 100, portando a zero i valori negativi.
Se i valori sono uguali l'accuracy è 100. Se l'errore percentuale è maggiore del 100% l'accuracy è 0. Questo indice quindi "appiattisce" gli scostamenti elevati.
