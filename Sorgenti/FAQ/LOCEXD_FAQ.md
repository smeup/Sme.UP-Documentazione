- \*\*Esiste differenza nel visualizzare una scheda da Web.UP e LoocUP?\*\*

 :  : VOC Id="00000" Txt="Esiste differenza nel visualizzare una scheda da Web.UP e LoocUP?"
Si, esistono alcune differenze sostanziali.

La differenza principale consiste nei componenti, la maggior parte la compaibilità esiste sopratutto per i principali di classe A. E chiaro che per alcuni la cosa risulta impossibili,
e quindi alcuni componenti che in Web.UP funzionano in LoocUP potrebbero non funzionare, sopratutto per quelli sviluppati più recentemente. Per alcuni è il contrario, in LoocUP erano stati sviluppati
mentre in Web.UP non sono mai stati ri-sviluppati.

Altre modifiche potrebbero essere più specifiche, quindi riguardare il singolo attributo di setup che da una parte potrebbe andare mentre dall'altra no.

- \*\*Che differenza c'è tra G.SUB.DYN e G.DIN?\*\*

 :  : VOC Id="00010" Txt="Che differenza c'è tra G.SUB.DYN e G.DIN?"
 1. G.SUB.DYN definisce come dinamico il componente da utilizzare per visualizzare una sezione di scheda.
 In particolare, il componente viene ricavato da quello specificato nella chiamata D.FUN.STD (es. D.FUN.STD F(EXB;\*OAV;) -> matrice)
 2. G.DIN indica che una sezione induce dinamicità in un'altra.
 Ad esempio, se scegliendo un oggetto di un albero mostrato nella sezione X condiziono il  comportamento della sezione Y dovrò indicare G.DIN nella definizione della sezione X.

- \*\*Perchè non si usa sempre G.SUB.DYN?\*\*

 :  : VOC Id="00020" Txt="Perchè non si usa sempre G.SUB.DYN?"
 Non tutti i componenti vengono riconosciuti dal G.SUB.DYN.  Inoltre, può essere necessario specificare un componente per la visualizzazione diverso da quello indicato
 nella chiamata alla funzione (ad esempio grafico invece che matrice)

- \*\*Come richiamo direttamente un membro di scheda? Una sottoscheda? Quali \*\*

 :  : VOC Id="00030" Txt="Come richiamo direttamente un membro di scheda? Una sottoscheda? Quali sono le risalite?"
 Vedere l'help del servizio scheda (DOC_OGG/P_JATRE_18) alla voce Funzioni/metodi

- \*\*che tipi di caricamenti di sezioni esistono?\*\*

 :  : VOC Id="00040" Txt="che tipi di caricamenti di sezioni esistono?"
I caricamenti delle varie sezioni possono essere immediati o differiti, nel primo caso la sezione verrà caricata alla aperutra della scheda. Nel secondo caso invece
la sezione non verrà caricata alla apertura delle scheda, ma ci sarà bisogno che tramite un dimanimso qualcuno la carichi.

- \*\*Quali sono i vari tipi di posizionamento del Load=\*\*

 :  : VOC Id="00050" Txt="Quali sono i vari tipi di posizionamento del Load="D" e i loro effetti?"
 Data una sezione A che induce dinamicità in una sezione B è possibile specificare il caricamento differito della sezione B in due modi.
 \* Nel G.DIN Where="B" nella sezione A :  indica che quando si clicca sulla sezione A è necessario poi cliccare sulla sezione B per ricaricarla e vedere gli aggiornamenti. Questo è utile, ad esempio, se ho 3 sezioni A1, A2, A3 che inducono dinamicità in B :  se nei loro G.DIN specifico Load="D", posso scegliere i 3 valori e poi cliccare su B dopo aver valorizzato tutte le variabili necessarie.
 \* Nel G.SET.xxx della sezione B :  indica che la sezione B non viene caricata fino a quando non viene cliccato su almeno una delle sezioni che inducono dinamicità in B, dopo di che tutti i clic successivi su tali sezioni causano il ri-caricamento immediato della sezione B.

- \*\*Perchè le variabili che passo nel parametro di chiamata a una scheda non \*\*

 :  : VOC Id="00060" Txt="Perchè le variabili che passo nel parametro di chiamata a una scheda non funzionano?"
 I nomi delle variabili non dovrebbero finire con un numero, come ad esempio PAR1, altrimenti si genera confusione nella chiamata.
 Ad esempio, D.SCH Nam(Scheda) P(PAR1(valore)) viene letta come se la chiamata fosse D.SCH Nam(Scheda) 1(valore)..., come se valore fosse passato nel parametro dell'oggetto 1.

- \*\*Cosa significa l'errore 'Sezione S non definita nel layout'?\*\*

 :  : VOC Id="00070" Txt="Cosa significa l'errore 'Sezione S non definita nel layout'?"
 È probabile che nello script sia definita una sezione senza che ne sia specificato il nome (obbligatorio).
 In altre parole, nello script della scheda dovrebbe essere presente una specifica G.SEZ senza il parametro Pos.

- \*\*Cosa significa il simbolo del cerchio barrato\*\*

 :  : VOC Id="00080" Txt="Cosa significa il simbolo del cerchio barrato"
 Le possibilità sono due : 
 1. Non è stato abilitato il Drag in quella sezione
 2. Il drag sulla sezione è abilitato ma non il drop. Per completare l'azione occorre rilasciare l'elemento selezionato nella sezione apposita.
 A livello visivo è possibile notare che all'ingresso di una sezione in cui è abilitato il drop, il puntatore del mouse diventa un quadratino grigio vuoto al centro.

- \*\*In una matrice non riesco a selezionare più di un elemento\*\*

 :  : VOC Id="00090" Txt="In una matrice non riesco a selezionare più di un elemento"
 Per selezionare più di un elemento nella matrice non basta selezionare due campi su due righe diverse, ma bisogna selezioanre tutta la riga.
 E' possibile farlo cliccando all'estrema sinistra della matrice, nella parte grigia prima delle righe dove viene visualizzata una freccia per indicare il posizionamento sulla riga.
 Oppure usando solo la tastiera, tenendo premuto CTRL selezionare le righe interessate premendo SPAZIO.

- \*\*Non vengono visualizzati gli elementi trasferiti\*\*

 :  : VOC Id="00100" Txt="Non vengono visualizzati gli elementi trasferiti"
 E' possibile che una volta completato il drag & drop la sezione di arrivo non visualizzi i nuovi elementi.
 Ciò può essere dovuto alle seguenti cause : 
 1. L'elemento è già presente nella lista. Normalmente i record non vengono duplicati.
 2. Potrebbe non essere presente il Notify (Reload) nella sezione di arrivo per cui i dati non vengono caricati correttamente.

- \*\*Sai perchè, in una matrice di aggiornamento, a volte non riesco a completar\*\*

 :  : VOC Id="00110" Txt="Sai perchè, in una matrice di aggiornamento, a volte non riesco a completare l'inserimento di un record?"
Ci possono essere diversi motivi per cui l'inserimento non può essere completato.
Tipicamente i due casi più frequenti sono i seguenti : 
1) Il servizio di aggiornamento una volta ricevuti i dati da inserire, possiede dei criteri per cui non può accettare la richiesta di inserimento del record. Di norma il servizio emette errore, visibile nella barra dei mesaggi, ma alcuni servizi potrebbero semplicemente annullare l'inserimento e "far sparire" il record inserito.
2) In caso l'inserimento venga annullato addirittura prima dell'invio dei dati al servizio, è possibile che il problema risieda nei dinamismi definiti nello script di scheda per la matrice. Se, ad esempio, è stato definito un dinamismo al "ChangeRow" che produce come effetto un cambio fuoco (o su una sezione che è predisposta a spostare il fuoco su se stessa), l'inserimento viene annullato dalla matrice stessa a causa della perdita del fuoco.

Possono generarsi anche altri casi, che vanno analizzati nello specifico, data la complessità di combinazioni consentite dagli script di scheda e la potenza espressiva del componente EXD.

- \*\*Sai come dividere la scheda in segmenti orizzontali e verticali?\*\*

 :  : VOC Id="00120" Txt="Sai come dividere la scheda in segmenti orizzontali e verticali?"
Attraverso il tag della sezione  :  : G.SEZ tramite l'attributo Pos(), se si utilizza un posizionamento numerico, es. Pos(1), si ottiene un segmento orizzontale; mentre attraverso un posizionamento alfabetico, Pos(A), un segmento verticale.

La disposizione delle sezioni dipende dall'ordinamento crescente (numerico o alfabetico), partendo dall'angolo in alto a sinistra dell'area di pertinenza.

E' possibile suddividere una sezione in sottosezioni, la cui rappresentazione grafica è determinata dalla sequenza di lettere e numeri dell'attributo Pos() : 

Es : 
 :  : G.SEZ Pos(A)
 :  : G.SEZ Pos(A1)
 :  : G.SEZ Pos(A1A)

In questo caso avremo una sezione verticale A, che contiene una sezione orizzontale 1, che a sua volta contiene un'ulteriore sezione verticale A.

- \*\*Sai come ricercare i tag utilizzabili nella scheda?\*\*

 :  : VOC Id="00130" Txt="Sai come ricercare i tag utilizzabili nella scheda?"
Attraverso il wizard, durante l'editazione della scheda, è possibile ricercare il tag e i loro attributi di compilazione.

I tag sono specificati nel membro SMEDEV/SCP_CFG(EDT_SCH).

- \*\*Sai come attivare il debug sui dinamismi?\*\*

 :  : VOC Id="00140" Txt="Sai come attivare il debug sui dinamismi?"
Attraverso il tasto funzionale CTRL+F8, si attiva una finestra di debug, dove vengono evidenziati i dinamismi che vengono attivati durante l'utilizzo della scheda. La sua disattivazione si ottiene sempre attraverso lo stesso tasto funzionale (ricordarsi di impostare il fuoco sul componente con il dinamismo).

- \*\*Sai come attivare un dinamismo?\*\*

 :  : VOC Id="00150" Txt="Sai come attivare un dinamismo?"
Il dinamismo è attivabile attraverso il tag  :  : G.DIN, nel attributo when='' si può specificare quando far partire il dinamismo, where='' dove farlo scattare (specificare ID di sezione di arrivo).

- \*\*Sai come condizionare l'attivazione di un dinamismo?\*\*

 :  : VOC Id="00160" Txt="Sai come condizionare l'attivazione di un dinamismo?"
Il dinamismo può essere attivato solo se si verifica una determinata condizione, per abilitare questa funzionalità bisogna elencare la condizione di esecuzione attraverso l'attributo Enabled="{<Condizione>}"

- \*\*Sai come autorizzare la scheda?\*\*

 :  : VOC Id="00170" Txt="Sai come autorizzare la scheda?"
La scheda può essere autorizzata tramite la classe LO.EXD con funzione il nome della scheda stessa.
Su ogni sezione deve essere definito il livello di autorizzazione desiderato.

- \*\*Sai come autorizzare le sezioni allo USRLVL?\*\*

 :  : VOC Id="00180" Txt="Sai come autorizzare le sezioni allo USRLVL?"
Su ogni sezione può essere definito lo USRLVL al quale la sezione viene resa disponibile.

- \*\*Sai come nascondere il titolo di una sezione?\*\*

 :  : VOC Id="00190" Txt="Sai come nascondere il titolo di una sezione?"
Per nascondere il titolo di una sezione occorre specificare nell'attributo del titolo \*NONE, es.  :  : G.SUB.xxx Tit="\*NONE"

- \*\*Sai cosa comporta un caricamento differito di una sezione?\*\*

 :  : VOC Id="00200" Txt="Sai cosa comporta un caricamento differito di una sezione?"
Il caricamento differito di una sezione, ottenibile tramite la specifica Load="D" nel setup, consente di non visualizzare immediatamente i dati al richiamo della funzione.

Per renderli visibili occorre cliccare sulla sezione, oppure tramite un dinamismo lanciare il caricamento della sezione stessa.

- \*\*Sai come dividere una sezione in più Tabsheet?\*\*

 :  : VOC Id="00210" Txt="Sai come dividere una sezione in più Tabsheet?"
Una sezione può contenere diversi Tabsheet che verranno visualizzati in base all'ordine dello script.
Ogni Tabsheet corrisponde ad un Tag  :  : G.SUB all'interno di una sezione.

Nel caso in cui un Tabsheet deve contenere al suo interno altri Tabsheet è necessario che il primo richiami una sottoscheda, in cui sono specificate le  :  : G.SUB

es :   :  : G.SEZ Pos(A)
 :  : G.SUB.MAT Tit="Tabsheet 1"
 :  : D.FUN.STD F(EXB;xxx;yyy)
 :  : G.SUB.SCH Tit="Tabsheet 2"
 :  : D.SCH Nam(ZZZ)
 :  : G.SUB.SCH Tit="Tabsheet 3"
 :  : D.SCH Nam(JJJ)

- \*\*Sai come dimensionare e posizionare una sezione all'interno di una scheda?\*\*

 :  : VOC Id="00220" Txt="Sai come dimensionare e posizionare una sezione all'interno di una scheda?"
Per il dimensionamento di una sezione occorre usare l'attributo Dim() del Tag  :  : G.SEZ, può essere espresso in percentuale o in valore assoluto(pixel).

E' inoltre possibile specificare da dove far partire il dimensionamento della sezione :  se il numero o percentuale è positivo, la sezione inizierà il dimensionamento dal limite superiore o sinistro dell'area (dipendente dall'orientamento della sezione); se il numero o percentuale è negativo, la sezione inizierà il dimensionamento dal limite inferiore o destro dell'area.

E' possibile inserire il valore Dim(0), che comporta una sezione nascosta.

- \*\*Sai quali sono le possibili modalità di lancio di un dinamismo?\*\*

 :  : VOC Id="00230" Txt="Sai quali sono le possibili modalità di lancio di un dinamismo?"
Un dinamismo può essere attivato all'esecuzione delle seguenti azioni : 

.Change :            Allo scorrimento
.Click :             Al click del mouse
.DblClick :          Al doppio click del mouse
.Return :            Al ritorno da un richiamo funzione
.Expand :            All'espansione di un nodo dell'albero
.Focus :             All'acquisizione del fuoco (se input panel)
.LostFocus :         Alla perdita del fuoco (se input panel)
.ChangeRow :         Al cambio di riga (se matrice)
.ChangeCol :         Al cambio di colonna (se matrice)
.Drop :              Al DROP (files system)
.Update :            All'aggiornamento (Solo matrice aggiornabile)
.Init :              Crea solo le variabili sulla sezione corrente
.\*ALL :              Sempre

- \*\*Sai come si fa ad aprire una sezione in una nuova finestra?\*\*

 :  : VOC Id="00240" Txt="Sai come si fa ad aprire una sezione in una nuova finestra?"
Per far aprire una sezione in una nuova finestra occorre specificare, nel lancio della funzione, il modello grafico NFI.
es. G(NFI)

E' inoltre possibile dimensionare la finestra tramite il tag  :  : S.EXD.LAY

Es.
 :  : S.EXD.LAY Width="380" Height="400" PosX="100" PosY="100"

- \*\*Sai come si fa ad usare una sottoscheda e passargli i parametri?\*\*

 :  : VOC Id="00250" Txt="Sai come si fa ad usare una sottoscheda e passargli i parametri?"
In una sezione è possibile richiamare una scheda o una sottoscheda attraverso il tag  :  : G.SUB.SCH.
In caso di scheda occorre specificare nel D.FUN.STD il nome della scheda nella seguente sintassi

 :  : D.FUN.STD F(EXD;\*SCO;) 1(;;) 2(MB;SCP_SCH;XXX) 4(;;YYY) P()

Nell'oggetto 2 occorre specificare il nome della scheda XXX, e, se occorre, nell'oggetto 4 il nome YYY della sottoscheda.

In caso di sottoscheda dichiarata all'interno dello script la sintassi è la seguente
 :  : D.SCH Nam(XXX) P()

che fa riferimento al

 :  : I.SCH Nam(XXX)
 :  : I.SCH.END

Il passaggio di parametri avviene nella forma : 
- scheda chiamante  :  : D.SCH Nam(XXX) P(Par1(ABC) Par2(DEF))
- scheda chiamata &PA.Par1, &PA.Par2

- \*\*Sai come si usano all'interno di una scheda i Gauge?\*\*

 :  : VOC Id="00260" Txt="Sai come si usano all'interno di una scheda i Gauge?"
Per utilizzare il componente Gauge (Cruscotto) occorre usare il Tag  :  : G.SUB.GAU e il setup  :  : G.SET.GAU
La rappresentazione può essere effettuata attraverso diverse modalità che specifichino i 5 valori fondamentali per definire il Gauge : 
Min= Valore minimo assumibile
Max= Valore massimo assumibile
Soglia1= Primo valore evidenziato sul cruscotto
Soglia2= Secondo valore evidenziato sul cruscotto
Valore= punto del cruscotto in cui si posiziona l'indicatore.

Attraverso Xml : 
é possibile stabilire un minimo e un massimo del cruscotto (attributi Min e Max), due soglie (attributi Soglia1 e Soglia2) e il valore che rappresenta la posizione dell'indicatore (Attributo Valore).

Es.  :  : D.GAU.XML Min="-30" Max="30" Soglia1="-5" Soglia2="5" Valore="&OA.J/I01"

Attraverso servizio Std : 
é possibile passare come parametri i valori necessari per rappresentare il cruscotto.

Es.  :  : D.FUN.STD F(GAU;LOSER_02;GAU) P(VAL(&OA.J/H03) MIN(00) MAX(100) SG1(33) SG2(66))

Attraverso un servizio personalizzato che passi i valori necessari con la seguente chiamata : 

EVAL      £JaxMN=                                  MINIMO
EVAL      £JaxMX=                                  MASSIMO
EVAL      £JaxS1=                                  SOGLIA 1
EVAL      £JaxS2=                                  SOGLIA 2
EVAL      £JaxVA=                                  VALORE
EXSR      £JAX_ADDE

- \*\*Sai dove si trova la documentazione per la creazione delle schede?\*\*

 :  : VOC Id="00270" Txt="Sai dove si trova la documentazione per la creazione delle schede?"
La documentazione per la creazione delle schede si trova nel modulo LOCEXD e nella documentazione di ciascun componente.

- \*\*Sai quali sono le variabili usabili in una scheda e come visualizzarle?\*\*

 :  : VOC Id="00280" Txt="Sai quali sono le variabili usabili in una scheda e come visualizzarle?"
I tipi di varibili usabili in una scheda di Looc.Up sono le seguenti : 

Loo.Var    Variabili di LOOC.up
Com.Var    Variabili di componente
Sch.Var    Variabili di scheda
Ssc.Var    Var. sotto sch. (nomsc.nomvar)

Le variabili di Looc.Up sono tutte quelle settate a livello di client e che valgono fintanto che Loo.Up rimane attivo.  Es. le varibili dell'SCP_CLO
Le variabili di componente sono quelle settate in una scheda e che valgono per tutte le schede aperte o che verranno aperte fino alla cancellazione delle variabili stesse.
Le variabili di scheda sono tutte quelle settate a livello di scheda e che rimangono valide fintanto che si rimane all'interno della scheda.
Le varibili di sottoscheda sono quelle settate a livello di sottoscheda e che rimangono valide solo all'interno della sottoscheda in cui sono dichiarate.

Sono settabili in testata dello script tramite la seguente sintassi : 
 :  : S.VAR.VAL xxx.Var="Nome(valore)"

- \*\*Sai se le istruzioni degli script sono case-sensitive?\*\*

 :  : VOC Id="00290" Txt="Sai se le istruzioni degli script sono case-sensitive?"
Le istruzioni degli script sono tutte case-sensitive. Il mancato rispetto di maiuscole e minuscole comporta l'inserimento di istruzioni non valide, il cui risultato è difficile da prevedere.

- \*\*Sai quali e cosa sono le varibili statiche?\*\*

 :  : VOC Id="00300" Txt="Sai quali e cosa sono le varibili statiche?"
Le variabili statiche, della forma &VAR, sono le variabili valorizzate automaticamente in base agli oggetti passati nella chiamata alla scheda.

Si distinguono in : 

variabili di Oggetto : 
- &OG.T1, &OG.P1, &OG.K1, &OG.D1 :  Restituiscono il tipo, parametro, codice e descrizione dell'Oggetto 1
- &OA.xxx, &OD.xxx, &OT.xxx, &OP.xxx, &OI.xxx :  Restituiscono il valore (OA) o la descrizione (OD) o il tipo (OT) o il parametro(OP) o l'intestazione (OI) dell'attributo xxx dell'Oggetto 1

variabili di parametro : 
-&PA.xxx :  Restituiscono il valore di un parametro passato alla scheda nel Parametro. xxx è il nome con cui è stato passato il parametro, a discrezione dell'utente. La variabile restituisce la stringa di tutti i parametri.

variabili di INPUT : 
- &IN.xxx :  Restituiscono il valore di un parametro passato alla scheda nel Parametro INPUT. xxx è il nome con cui è stato passato il parametro, a discrezione dell'utente. La variabile restituisce la stringa di tutti i parametri

varaibili di Ambiente :  
- &AM.AZ :  Azienda
- &AM.UT :  Utente
- &AM.DT :  Data attuale (dell'utente)
- &AM.MG :  Magazzino unico (da B£2)

- \*\*Sai quali sono gli elementi fondamentali per costruire una matrice di \*\*

 :  : VOC Id="00310" Txt="Sai quali sono gli elementi fondamentali per costruire una matrice di aggiornamento?"
Una matrice di aggiornamento è una matrice in cui alcuni campi sono editabili.
Il salvataggio dei dati può avvenire sia in modalità immediata (all'invio o al cambio di riga), oppure differita (all'uscita dalla scheda, viene presentato un messaggio per salvare o meno le modifiche effettuate).

Nel caso della matrice in update, il caricamento dei dati (FUN) ed il loro aggiornamento/scrittura (UpdSvc) sul database sono due attività delegate a due programmi/servizi distinti.

Inoltre è necessario specificare nella scheda l'attributo UpdSvc nel tag  :  : G.SUB.EXU, che specifichi il nome del servizio, e se necessario l'attributo UpdPar, per passare al servizio i parametri.


- \*\*Sai come visualizzare il contenuto di un file?\*\*

 :  : VOC Id="00320" Txt="Sai come visualizzare il contenuto di un file?"
Per poter visualizzare il contenuto di un file occorre definire la sezione della scheda con  :  : G.SUB.HTM e  :  : D.HTM.URL

L'indirizzo del file è da passare nella forma : 

::D.HTM.URL http://it.wikipedia.org/wiki/&PA.Txt

- \*\*Sai come creare un bottone per il lancio di un'azione?\*\*

 :  : VOC Id="00330" Txt="Sai come creare un bottone per il lancio di un'azione?"
Per eseguire il lancio di un'azione da un bottone occorre definire una sezione con  :  : G.SUB.BTN.

L'azione può essere specificata in due modi : 
- in un caso l'azione viene specificata nel tag  :  : D.OGG

Es.  :  : D.OGG D(Nome Bottone) E(A(B£Q301X;GES;02)

- nell'altro l'azione viene specificata nel tag  :  : G.DIN legato al bottone e nel  :  : D.OGG il nome visualizzato sul bottone

Es.  :  : G.DIN When="Click" Exec="F(OPN;PATH;) 1(J1;PATHDIR;)"

- \*\*Sai come creare un albero in una scheda?\*\*

 :  : VOC Id="00340" Txt="Sai come creare un albero in una scheda?"
L'albero in scheda è identificato dal tag  :  : G.SUB.TRE.

La rappresentazione dell'albero è possibile attraverso diverse modalità : 

- richiamando un servizio contente le seguenti istruzioni RPG
£JaxT1 (Tipo=" ")
£JaxP1 (Parametro=" ")
£JaxK1 (Codice=" ")
£JaxD1 (Testo=" "). Se assente e si tratta di un oggetto viene assegnata la decodifica dell'oggetto
£JaxOP (Exec="F(;;) 1(;;) P()"). Facoltativa. Nella forma standard dell'oggetto J1FUN.
£JaxNM (Nome=" "). Pprefisso per le variabili associate a tale nodo
£JaxLF (Leaf="Yes/No"). Se presente "Yes" in un albero ad espansione dinamica non appare il simolo di espansione (carattere +)
£JAXEN Chiusura. '/>' se non ci sono sottolivelli, '>' per aprire un nuovo livello
£JAXFL (Fld=" "). Lista dei campi con separatore come per le righe di una matrice

e le seguenti \copy : 
£JAX_ADDO Aggiunge un nodo all'albero
£JAX_CLOO Chiude il livello precedente

- una funzione che restituisce un XML

Es :   :  : D.FUN.STD F(TRE;\*TBL;) 1(TA;MAG;)

- \*\*Sai i diversi modi per creare un input panel?\*\*

 :  : VOC Id="00350" Txt="Sai i diversi modi per creare un input panel?"
Per creare un input panel esistono diverse modalità legate all'utilizzo di funzioni diverse : 

- Utilizzo del costruttore LOA08 :  permette definendo un membro del file scp_cfg di creare un input panel da cui reperire i parametri da passare ad una sottoscheda o ad un'altra scheda. Per poterlo utilizzare occorre definire una sezione  :  : G.SUB.SCH

Es.  :  : D.FUN.A08 A08Ori="H" A08Nde="1" A08Eim="&PA.EIM" A08Q3="CM" A08Ric="C"  A08Tf="S-" A08Pf="BRCOMM/B" A08Cf="\*JOB" A08Fil="SCP_SCH" A08Sch="BRCOMM_OGB"   A08Ssc="LIS" A08Exit="BRCOMM_A08"

- Show Input :  consente di aprire un input panel per passare i parametri di lancio di una sottoscheda. Occorre specificare una sezione  :  : G.SUB.SCH e un set  :  : G.SET.INP e poi richiamare la scheda con da esempio seguente.

Es.  :  : D.SCH Nam(SUBINP_SWF) P(Tip(-(O;CN;OG;Tipo;TIP;02)) Par(-(O;;OG(TIP);Parametro;PAR;10)) Cod(-(O;;(TIP)(PAR);Codice;COD;15)) )

- Servizio con matrice di Update :  la gestione dei campi dell'input panel è lasciata al servizio RPG costruito allo stesso modo della matrice di aggiornamento, e chiamato all'interno della scheda con una sintassi simile alla seguente.

Es.  :  : G.SET.INP Parent="A01" CtrlObj="Yes" ShowMatrix="LEFT" ReadOnly="No" UpdSvc="LOSUP_13"
UpdPar="ExitPar(CUpd(&OG.K1))" ModPendMsg="Yes" ShowMsgBar="Yes"

- \*\*Come faccio a ricaricare una sezione ogni n secondi?\*\*

 :  : VOC Id="00360" Txt="Come faccio a ricaricare una sezione ogni n secondi?"
E' possibile definire per ogni sezione presente nella scheda un attributo di setup chiamato 'Refresh' che permette di specificare ogni quanti secondi quella sezione deve ricaricarsi.

- \*\*Come posso aprire una scheda in un dialog?\*\*

 :  : VOC Id="00370" Txt="Come posso aprire una scheda in un dialog?"
Per far aprire una nuova scheda all'interno di una finestra di dialog e sufficiente inserire la specifica G(NFIR) all'interno della FUN che viene lanciata per aprire la scheda.

- \*\*Esistono altri modi oltre al dialog per aprire una scheda non a tutto \*\*

 :  : VOC Id="00380" Txt="Esistono altri modi oltre al dialog per aprire una scheda non a tutto schermo?"
Si, esitono altri modi.

Esistono le apreture a slide :  top(PNLT), down(PNLB), left(PNLL) e right(PNLR).

E' possibile aprire una finestra di dialog senza bottoni nell'header (NFIR)

E' possibile far aprire il dialog in una nuova finestra del browser (NFIT)

E' possibile, MA SOLO IN LOOCUP, specificare anche (DLG) e (DLGR), la prima consente di aprire un dialog a tutto schermo senza la possibilità di tornare alla finestra sotto, se non chiudendo il dialog. Nel secondo caso invece apre un dialog piccolo che non consente di premere sulla scheda sotto, ES. F4 di loocup.

- \*\*Come faccio a entrare in debug su una scheda di Web.UP?\*\*

 :  : VOC Id="00390" Txt="Come faccio a entrare in debug su una scheda di Web.UP?"
Basta premere la combinazione di tasti Ctrl+Shift+F8 è inserire la password di accesso, impostabile dalla configurazione iniziale di Web.UP


