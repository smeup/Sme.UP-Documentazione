## OAV remoti

In uno script di OAV remoti potranno essere presenti una o più SEZ di tipo Cod="OAV".

Questo è un esempio per l'oggetto Provincia (TAV§P).

 :  : SEZ.OAV Sub="GO.A06.001" Var="Authorization(Bearer &AUT) Accept(application/json) IdFile(xxx)" Sca="\values(\*)\(4)"
 :  : AUT Sub="GO.A01.001" Var="Content-Type(application/x-www-form-urlencoded)" Pay="client_secret=xxx&grant_type=refresh_token&refresh_token=xxxx" Ind="access_token"
 :  : OAV Cod="U/01" Ind="\values(\*)\(3)" Txt="Numero Abitanti" Ogg="NR" Len="9" Cnv="\*ANGNUM"

 :  : SEZ.OAV Sub="GO.B01.001" Var="Via_e_civico() Città(&CO.CD%I/T$DESC) Nazione(Italia) API_KEY(xxxxxxxxxxxxxxxxxxxx)"
 :  : OAV Cod="U/02" Ind="\results(1)\geometry\location\lat" Txt="Latitudine" Ogg="" Cnv="\*NUMTOTEXT" CnvVar="DECSEP(.) DECNUM(7)" IntVar="U02"
 :  : OAV Cod="U/03" Ind="\results(1)\geometry\location\lng" Txt="Longitudine" Ogg="" Cnv="\*NUMTOTEXT" CnvVar="DECSEP(.) DECNUM(7)" IntVar="U03"

 :  : SEZ.OAV Sub="RS.S16.B01" Var="LAT(&CO.U02) LNG(&CO.U03)"
 :  : OAV Cod="U/04" Ind="\words" Txt="What3Words" Ogg=""

Sono state definite 3 sezioni SEZ Cod="OAV", una sezione per webservice interrogato.

Le informazioni del webservice interrogato sono scritte nel tag  :  : SEZ Tramite l'attributo Var è possibile passare variabili al webservice. Se il webservice necessita di autenticazione è necessario aggiungere un tag  :  : AUT. Il relativo token ottenuto potrà essere utilizzato nello script attraverso la variabile &AUT.

Nel tag  :  : OAV si trovano le specifiche di definizione del singolo OAV. Il tag Ind indica la parte di dati nel json restituito dal WS che darà il valore dell'OAV. Tramite il tag Cnv è possibile definire la modalità di conversione dei dati. Ad esempio la conversione \*ANGNUM permette di convertire un numero in formato anglossassone (ovvero col punto come separatore decimale) in un oggetto numero di Sme.UP.

E' possibile definire delle variabili interne in maniera tale da poterle utilizzare nel calcolo degli OAV successivi. In questo modo si possono definire OAV remoti di OAV remoti. Nel caso d'esempio l'OAV U/04 è un OAV remoto ottenuto passando al webservice del What3Words latitudine e longitudine della provincia, anch'essi attributi remoti ma ottenuti dal webservice di localizzazione di Google.

Si tenga presente che una volta definiti gli OAV va lanciata la funzione COS ALL per il ricalcolo dei campi di un oggetto. Per lanciarla in looc.UP : 
- digitare API £OAV
- cliccare su Programma di Test
- scrivere in Funzione COS, in Metodo ALL, in Tipo/Parametro il tipo/parametro desiderato ad esempio TA V§P
- cliccare invio
- uscire e rientrare da Looc.UP

Si noti infine che tuttora non è possibile sovrascrivere OAV già esistenti. Ad esempio l'OAV "I/T$V§PA" è già presente nell'oggetto TAV§P. Ridefinirlo come OAV remoto nello script non ha nessun effetto. Il suo valore sarà comunque recuperato dalle tabelle interne a Sme.UP. Nel caso di OAV di oggetti remoti, poichè non sono descritti in tabelle Sme.UP, qualsiasi definizione di OAV inserita nello script sarà invece considerata. Si tenga comunque presente che per oggetti remoti si possono definire solo OAV di tipo I/.

