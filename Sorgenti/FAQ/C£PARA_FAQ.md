- **Sai cosa sono i parametri in SmeUP?**

 :  : VOC Id="SKIA0010" Txt="Sai cosa sono i parametri in SmeUP?" Als="comm"
Si tratta di una struttura (tabelle, archivi, programmi) con cui si possono associare ad uno o ad una coppia di oggetti un elenco di informazioni aggiuntive.
Le informazioni aggiuntive possono essere singole o multiple, possono essere datate e possono essere numeri, date, caratteri liberi oppure oggetti.

- **Sai a cosa servono i parametri ?**

 :  : VOC Id="SKIA0020" Txt="Sai a cosa servono i parametri ?"
Possono servire per estendere le caratteristiche anagrafice di un oggetto (es. per un articolo macchina potrebbero essere i dati di targa :  tensione, frequenza, numero colpi, ...) o per descrivere informazioni aggiuntive riferite ad una coppia di oggetti (es. per la coppia articolo / tipo pressa potrebebro essere :  lo stampo, la temperatura, la velocità, ....).
- **Sai quali sono le tabelle principali?**

 :  : VOC Id="SKIA0030" Txt="Sai quali sono le tabelle principali?"
La tabella principale è la tab. C£E (categoria parametri) dove sono specificate le informazioni principali del conenitore parametri (oggetti a cui si collega, come costruire l'elenco parametri, autorizzazioni applicate, progammi controllo, ...).

La seconda tabella fondamentale è la B£N dove sono descritti i singoli parametri.

Per una informazione più completa vedi : 
- [C£E - Categoria parametri](Sorgenti/OG/TA/C£E)
- [B£N - Parametri variabili](Sorgenti/OG/TA/B£N)
- **Sai quali sono le autorizzazioni?**

 :  : VOC Id="SKIA0040" Txt="Sai quali sono le autorizzazioni?"
Esiste una autorizzazione generale sulla categoria parametri :  Classe = C£CR01,  Funzione = Catategoria parametri (elemento della tab. C£E).

Si può anche autorizzare il singolo singolo parametro, in questo caso abbiamo 2 tipi di autorizzazioni (da impostare nella tab. C£E campo "Tipo Gest.Autorizz.") : 
* Classe STATI / Funzione = PA
* Classe PLC-C£CONR / Funzione = cat. parametri (elemento C£E)

Con la classe STATI nell'elemento della tab. B£N nel campo "Livello protezione" dobbiamo inserire un valore tra 00 e 99 - L'autorizzazione può bloccare la visualizzazione del parametro (e di conseguenza la manutenzione)

Con la classe PLC- il valore da inserire nell'elemento della B£N varia da 01 a 05 e possiamo scegliere se bloccare la visualizzazione e/o la manutenzione.
- **Sai in quale archivio sono memorizzati i parametri?**

 :  : VOC Id="SKIA0050" Txt="Sai in quale archivio sono memorizzati i parametri?"
I parametri sono memorizzati normalmente nel file C£CONR0F.
- **Sai se si possono utilizzare anche e altri archivi?**

 :  : VOC Id="SKIA0060" Txt="Sai se si possono utilizzare anche e altri archivi?"
Si, generalmente in un ambiente complesso (es. multiazienda) dove possiamo avere alcune informazioni  comuni (es. articoli, clienti, fornitori) ed altre informazioni specifiche, può essere necessario avere parametri comuni (di gruppo) ed altri parametri specifici (di azienda), in questo caso gli archivi devono essere differenziati.
Per differenziare gli archivi si deve impostare opportunamente il campo "File appartenenza" in tab. C£E, il nome file sarà C£CONx0F dove x è il valore del campo.
- **Sai se si possono impostare delle risalite ad altre categorie?**

 :  : VOC Id="SKIA0070" Txt="Sai se si possono impostare delle risalite ad altre categorie?"
Si, impostando opportunamente il campo "Parametri per risalita" della tab. C£E.

Le categorie associate per la risalita devono avere uguali il sottosettore dei valori.

La risalita è attiva solo per gli oggetti (AR=Articolo, CN=Contatti/Enti e RI=Risorse). Il tipo di informazione con cui risalire viene derivato dalla griglia della categoria stessa. Nel caso in cui la griglia accetti **, il riferimento superiore di una categoria può essere la categoria stessa.
- **Sai se i valori validi per un parametro sono contenuti in una tabella sai **

 :  : VOC Id="SKIA0080" Txt="Sai se i valori validi per un parametro sono contenuti in una tabella sai come fare per attivare direttamente la ricerca in fase di inserimento?"
In tab. C£E impostare a "1" il campo "Ricerca automatica"
- **Sai come impostare la richiesta conferma aggiornamento con F6?**

 :  : VOC Id="SKIA0090" Txt="Sai come impostare la richiesta conferma aggiornamento con F6?"
In tab. C£E impostare a "1" il campo "Richiesta conferma"
- **Sai come attivare programmi specifici di visualizzazione e/o controllo?**

 :  : VOC Id="SKIA0100" Txt="Sai come attivare programmi specifici di visualizzazione e/o controllo?"
In tab. C£E impostare opportunamente i campi "Programma specifico di visualizzazione" e "Programma specifico di controllo"
- **Sai come condizionare la presentazione dei parametri per una determinata c**

 :  : VOC Id="SKIA0110" Txt="Sai come condizionare la presentazione dei parametri per una determinata categoria?"
Nella tab. C£E ci sono : 
* 3 campi "Prefisso codice valori" che permettono di filtrare tra gli elementi della tab. B£N
* i campi "Limite selezione iniziale / finale" che si confrontano con i valori presenti in tab. B£N nel campo
- **Sai come impostare un ordinamento diverso da quello alfabetico per codice **

 :  : VOC Id="SKIA0120" Txt="Sai come impostare un ordinamento diverso da quello alfabetico per codice parametro?"
In tab. B£N c'è il campo "Sequenza ordinamento" che si concatena con il codice parametro per determinare l'ordine di presentazione
- **Per un parametro sai come risalire ai codici  di default della stessa cate**

 :  : VOC Id="SKIA0130" Txt="Per un parametro sai come risalire ai codici  di default della stessa categoria?"
Nella tabella B£N c'è il campo risalita che se impostato con un valore tra :  1, 2, A, B; permette di risalire ai parametri che hanno nel codice 1 o nel codice 2 il valore "**".

I valori inseriti nel campo determinano il tipo di risalita. Vedi documentazione : 
- [B£N - Parametri variabili](Sorgenti/OG/TA/B£N)

