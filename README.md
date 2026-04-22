# Amazing Group

## Descrizione
Questo progetto consiste nella generazione di un labirinto tramite l'esecuzione di `a_maze_ing.py`, passando come argomento il file di configurazione `config.txt`. All'interno del file di configurazione andremo a specificare le caratteristiche che il labirinto dovrà avere.

## Parametri di configurazione

Parametri obbligatori:
- `WIDTH` → Larghezza del labirinto
- `HEIGHT` → Altezza del labirinto
- `ENTRY` → Cella di entrata (formato `x,y`)
- `EXIT` → Cella di uscita (formato `x,y`)
- `OUTPUT_FILE` → Percorso del file di output in cui salvare il labirinto
- `PERFECT` → Se `True`, il labirinto avrà una sola strada tra ogni coppia di celle (nessun ciclo)

Parametri opzionali:
- `SEED` → Valore iniziale per il generatore casuale (permette risultati riproducibili)
- `ALGORITHM` → Algoritmo di generazione da utilizzare

## Utilizzo

```bash
python a_maze_ing.py config.txt
```

## Parsing della configurazione

Il primo passo è leggere e validare i valori presenti in `config.txt`, per poi passarli alla classe `Maze` e stabilire le fondamenta del labirinto. Questo viene gestito dalla funzione `parse_config(path)`, definita in `config.py`, che legge il file, valida ogni parametro e restituisce un oggetto `MazeConfig` pronto all'uso.
  
