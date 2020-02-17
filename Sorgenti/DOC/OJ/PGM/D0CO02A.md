# Documentazione del calcolo costo di un oggetto
Dato un oggetto il programma mostra le righe che documentano come ne è stato calcolato il costo, l'emissione può essere a video o in stampa.

_7_Documentazione in fase di sviluppo

## Formato di lancio
![D0BASE_57](https://doc.smeup.com/immagini/MBDOC_OGG-P_D0CO02A/D0BASE_57.png)Sono necessarie le seguenti impostazioni : 
 \* **Modalità_; Visualizzazione / Stampa
 \* **Informazioni chiave caratteristiche dell'eleborazione di cui si vuole la documentazione** : 
 \*\* __Tipo sessione__;
 \*\* __Codice sessione__;
 \*\* __Contesto__;
 \*\* __Tema__;
 \*\* __Periodo__;
 \*\* __Codice __;
 \*\* __Tipo costo__.

## Formato di lista
![D0BASE_58](https://doc.smeup.com/immagini/MBDOC_OGG-P_D0CO02A/D0BASE_58.png)Significato delle colonne : 
 \* **Identificativo_; hhhh
 \* **TRe - Tipo record**; 00 = Intestazioni, vengono riportati i parametri di impostazione del calcolo utilizzati, 10 = hjkhjk, 13 = mm,., 99 = uiouoiu;
 \* **C**; hhhh
 \* **Tipo oggetto**;
 \* **Codice oggetto**;
 \* **Descrizione oggetto**;
 \* **Quantità**; hhhhhhhh
 \* **Costo**; shhhh
 \* **E**; hhhh
 \* **L**; hhhho
 \* **Z**; hhhh
 \* **TCO - Tipo costo**; shhhh
 \* **Data costo**; hhhhhhhh
 \* **M**; hhhh
 \* **N**; hhhho

Sul piede della lista ci sono dei comandi funzione con il significato seguente : 
 \* **F18 = Errori**, emette la lista degli errori collegati a questo calcolo (vedi)
 \* **F19 = Distinta**, emette l'esplosione scalare della distinta dell'oggetto intestatario (vedi)

- [Analisi errori](Sorgenti/DOC/OJ/PGM/D0CO03A)

### Formato esplosione di distinta
![D0BASE_60](https://doc.smeup.com/immagini/MBDOC_OGG-P_D0CO02A/D0BASE_60.png)
















C = Componente
      = No
    1 = Si
E = Errore costo
    0 = Warning
    1 = Vincolante
L = Livello errore
    1 = Livello proprio
    2 = Livello inferiore
    3 = Livello proprio e inferiore
Z = Costo Zero
      = No
    1 = Si
M = Memorizzazione costo
      = No
    1 = Si
N = Memorizzazione politiche
      = No
    1 = Si
