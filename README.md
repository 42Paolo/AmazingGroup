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
  
## Struttura Labirinto

La classe `Maze` (in `mazegen/maze.py`), rappresenta la **struttura del labirinto**. Internamente usa una griglia di interi dove ogni cella è un numero da 0 a 15: ogni bit indica la presenza di un muro in una delle quattro direzioni (W=su, D=destra, S=giù, A=sinistra, scelto per pura semplita).

I metodi disponibili della classe sono:

- `has_wall(x, y, direction)` → restituisce `True` se la cella ha un muro nella direzione indicata
- `open_wall(x, y, direction)` → rimuove il muro in una direzione (abbatte entrambe le facce con la cella vicina, sia della cella in cui siamo che in quella a cui stiamo puntando)
- `close_wall(x, y, direction)` → aggiunge un muro in una direzione
- `in_bounds(x, y)` → restituisce `True` se la cella esiste nella griglia
- `neighbors(x, y)` → restituisce le celle (W,A,S,D) valide, ognuna con le direzioni da usare per aprire il muro condiviso

Questi metodi sono le fondamenta sul quale l'algoritmo di generazione si appoggia.