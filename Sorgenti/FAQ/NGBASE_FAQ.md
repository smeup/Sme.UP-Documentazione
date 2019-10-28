### **Sai dove si trovano i files di Log di Negoziando?**

I file di log di Negoziando vengono salvati nelle sottocartelle della cartella LogFiles.
La cartella Logfiles si trova allo stesso livello dei programmi eseguibili
### **Sai come è possibile estendere i campi dell'anagrafica Articoli?**

E' possibile estendere l'anagrafica articoli in 2 modi : 
1. Tramite la compilazione delle tabelle STAT/STAC (Titoli Statistici/Codici Statistici) per poter classificare sino a 9 campi della lunghezza massima di 3 caratteri cadauno
2. Tramite la compilazione delle tabelle INFP/ (Informazioni Personalizzate/Tabelle Personalizzate) mediante le quali è possibile estendere, senza limite, gli attributi dell'anagrafica
### **Sai quali sono gli archivi che hanno la possibilità di estendere i campi?**

Gli archivi con possibilità di estensione dei campi sono : 
- Anagrafica Clienti
- Anagrafica Fornitori
- Anagrafica Clienti Fidelizzati
- Anagrafica Società
- Anagrafica Magazzini/Negozi
- Tutte le Tabelle
### **Sai dove si specifica il modello di stampante fiscale/registratore di cassa utilizzato?**

Il modello di stampante fiscale/registratore di cassa viene impostato in : 
Utilità --> Configurazione --> Gestione Configurazione Applicativa --> Parametri Casse Slave
### **Sai cosa è un'Entità?**

Una Entità è una definizione logica di un partner di interscambio dati (tipicamente un fornitore, un sistema ERP, una unità logistica).
All'entità vengono associati i parametri che ne condizionano il comportamento oltre che le relative tabelle di mappatura e di conversione
### **Sai quali sono le modalità di Replenishment che Negoziando Gestisce?**

Le modalità di Replenishment gestite da Negoziando sono : 
- Scorta Minima/Massima
- Previsioni di Vendita
- Venduto
### **Sai cosa succede quando si crea un file DAT per un solo negozio o per un gruppo di essi?**

Quando si cra un file DAT non per la totalità dei negozi, alla prima creazione DAT totale tutti i dati verranno ritrasmessi
### **Sai cosa è il GMROII?**

Il GMROII è un acronimo per Gross Margin Return Over Inventory Investment.
Viene calcolato dividendo il Margine per il valore medio a costo della giacenza nel periodo
### **Sai come si calcola la percentuale del margine di contribuzione?**

La percentuale del margine di contribuzione si calcola con la seguente formula : 
(<VendutoNettoIva>-<CostodelVenduto>)/<VendutoNettoIva>
### **Sai quali sono le regole di risalita per determinare il prezzo di vendita in cassa di uno SKU in un negozio?**

Generalmente il prezzo di vendita viene determinato come segue : 
a. Se si è in un periodo compreso nel Calendario Saldi del negozio :  Viene utilizzato il prezzo definito nel listino Saldi del Negozio
b. Se non si è in Saldo vengono utilizzati i seguenti listini specificati sull'anagrafica magazzini (fermandosi al primo prezzo trovato) :  Listino Speciale 2, Listino Speciale 1, Listino di Vendita.

Se il cliente è un cliente Fidelizzato vengono esplorati i parametri di fidelizzazione e utilizzati i prezzi specificati

I prezzi delle varianti Taglia/Colore vengono inoltre esplorati dando priorità alla data di validità del presso del modello o alla data di validità del colore a seconda di quanto impostato in configurazione
