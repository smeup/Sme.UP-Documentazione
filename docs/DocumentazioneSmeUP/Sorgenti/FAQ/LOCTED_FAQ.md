### **Cosa è il componente **TED**?**

 E' il componente che permette di modificare contenuti di tipo HTML. Attualmente il contenuto è  letto e scritto su membri di AS400 in quanto utilizza le medesime FUN del componente EDT ma  in futuro il repository dei dati potrà essere tutt'altro.

### **Come si può utilizzare all'interno di una scheda personalizzata?**


Tramite la sintassi di componente :    :  : G.SEZ Pos(1)                      :  : G.SUB.TED Tit="Mio Text Editor"        :  : D.FUN.STD F(TED;\*EDTLET;LET) 1(MB;[file];[membro]) 2(OJ;\*LIB;[libreria])   
 oppure richiamato come fun da un altro componente (es. BTN)             
 F(TED;\*EDTLET;LET) 1(MB;[file];[membro]) 2(OJ;\*LIB;[libreria])           
### **E' possibile inibire alcune funzionalità?**

 Si, agendo tramite configurazione del setup del componente tramite gli attributi :   -ReadOnly                                                                           -ShowSubmit                                                                           -ShowReload                                                                           -ToolbarTemplate

### **E' presente un wizard che aiuti nella sinstassi?**

No, non è previsto un Wizard ma di fatto si tratta di un editor con funzionalità comuni a tutti gli editor in commercio o a strumenti di word processing come Word o Libreoffice.
