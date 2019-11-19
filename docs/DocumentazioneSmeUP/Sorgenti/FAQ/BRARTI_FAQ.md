### **Sai qual è la tabella guida della gestione articoli?**

La tabella BR1
### **Conosci il significato di tipo parte?**

Il tipo parte è una caratterizzazione storica degli articoli che in Smeup viene utilizzata solo dalla funzione di reperimento politiche di pianificazione che, se non trova altri criteri impostati nei parametri di pianificazione, assegna una politica di produzione ai tipi parte 1 e 2, ed una di acquisto ai tipi parte >= 3.
Un tipo parte particolare è lo 0 (zero) che indica che l'articolo è un Phantom ( o fittizio). Questa informazione è utilizzata dalla funzione di esplosione distinta base che bypassa i livelli phantom.
### **Sai quando è necessario codificare un articolo?**

Per distinguere un oggetto da un'altro ! Non è un concetto banale in quanto non è banale decidere quando distinguere due oggetti diversi , tenendo conto che la diversità di due oggetti potrebbe non essere percepita da chi li utilizza, compra, etc. (ad esempio, quando cambia la tolleranza di una quota del disegno di un articolo, non è necessario cambiare il codice articolo se esso mantiene gli stessi utilizzi)
### **Conosci il significato di gruppo distinta e gruppo ciclo?**

Il gruppo distinta ed il gruppo ciclo sono un "trucco" usato per evitare di scrivere tante distinte ( e cicli) quanti sono gli articoli. In questo trucco si codifica una distinta di un articolo di riferimento (chiamato gruppo distinta) e si dice che tutti gli articoli con eguale distinta hanno questo "gruppo distinta". L'utilizzo del "gruppo distinta" trova anche maggiore efficacia se accoppiato al concetto di "configurazione" di un articolo, in quanto si può rendere il legame di distinta (e di ciclo) sensibile alla "configurazione" dell'articolo. NOTA :  la "configurazione" di un articolo esiste per qualsiasi articolo in qualsiasi installazione, è l'insieme dei suoi attributi. Leggere la "configurazione " di un articolo NON implica gestire l'oggetto CF :  configurazione nel sistema !
### **Conosci il significato del flag esclusione magazzino?**

Se un articolo ha il flag di esclusione da magazzino non vengono eseguiti movimenti di magazzino per quell'articolo e neanche viene pianificato
### **Sai fare in modo che in creazione articolo questo prenda una serie di default (es. unità di misura, classe materiale, ...) ?**

Bisogna agire sul tipo articolo (tab. BRA) dove si possono impostare alcune informazioni di default
### **Sai dove devi agire per associare una categoria parametri ad un gruppo di articoli?**

Nella tabella BRA, tipo articolo.
### **Sai come fare per impostare una codifica guidata articoli?**

Dalla tabella BRA, tipo articolo, si può collegare una procedura di codifica guidata tramite l'aggancio ad un elemento della tabella B£F
