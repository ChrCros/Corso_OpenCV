# Leggere, scrivere e visualizzare immagini in OpenCV e Python
## Ambiente di sviluppo
> Creare ambiente di sviluppo venv
```sh
python -m venv venv
```

> attivare ambiente di sviluppo venv
```sh
C:> venv\Scripts\activate.bat
```

## Errori dovuti all'importazione librerie
> Per evitare vi sia un errore, è meglio lanciare il comando di seguito per assicurarsi che le libreire necessarie siano installate corretamente
```sh
pip install -r .\requirements.txt
```

## Lancio programma
> Per lanciare il programma bisogna passare i parametri image 
```sh
python .\out\01_load_show_save.py -i .\Images\01_image.bmp
```


# Aggiungi al PERCORSO su Windows 10
> 1. Apri Inizia ricerca, digita 
```sh
env
``` 
> 2. scegli "Modifica le variabili di ambiente di sistema" 
> 3. Fare clic sul pulsante "Variabili d'ambiente..."
> 4. Nella sezione "Variabili di sistema" (la metà inferiore), individua la riga con "Path" nella prima colonna e fai clic su Modifica.
> 5. Apparirà l'interfaccia utente "Modifica variabile di ambiente". Qui puoi fare clic su "Nuovo" e digitare il nuovo percorso che desideri aggiungere. Da questa schermata puoi anche modificarli o riordinarli.
> 6. Chiudere tutte le finestre di dialogo scegliendo "OK". Le tue modifiche sono salvate!
> 7. Testarlo, nella nuova finestra di PowerShell, digitare
```sh
$env:PATH
``` 
> N.B.: Probabilmente dovrai riavviare le app affinché rilevino la modifica. Il riavvio della macchina assicurerebbe che tutte le app vengano eseguite con la modifica del PATH

