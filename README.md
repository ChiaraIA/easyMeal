# easyMeal 🥗

App per contare le macro dei piatti che cuciniamo, pensata per essere usata in due.

## Come funziona

1. **Dispensa** — inserisci gli ingredienti con i valori dell'etichetta **per 100 g**:
   carboidrati, grassi, di cui saturi, fibre, proteine, sale.
2. **Ricetta** — cerchi gli ingredienti, scrivi i grammi usati e l'etichetta nutrizionale
   del piatto si aggiorna in tempo reale (totale, per porzione, per 100 g, più le kcal
   stimate con i fattori UE).
3. **Salva nel ricettario** se vuoi tenerla, **Annulla** se volevi solo fare il conto
   (c'è anche "Ripristina" per qualche secondo, nel caso).
4. **Ricettario** — tutte le ricette salvate, cercabili anche per ingrediente; ognuna si può
   riaprire nell'editor per cambiare le grammature.

Le ricette salvate conservano una copia dei valori degli ingredienti: se poi modifichi o
elimini un ingrediente dalla dispensa, le ricette già salvate non cambiano.

## Struttura

| File | Cosa contiene |
|---|---|
| `src/easymeal.html` | Il sorgente dell'app (HTML + CSS + JS, nessuna dipendenza). È il file pubblicato come Artifact su claude.ai. |
| `build.py` | Avvolge il sorgente in una pagina HTML completa → `index.html`. |
| `index.html` | Versione standalone generata: si apre direttamente nel browser. **Non modificarlo a mano.** |

```bash
python3 build.py
```

## Dove finiscono i dati

- **Su claude.ai (Artifact)**: dispensa e ricettario stanno in un database condiviso legato
  all'Artifact. Chi ha il link con permesso di modifica vede e modifica gli stessi dati,
  aggiornati in tempo reale.
- **`index.html` aperto in locale / GitHub Pages**: i dati restano nel `localStorage` di quel
  browser (in alto compare "Salvato solo su questo dispositivo").

Il piatto che stai componendo resta comunque salvato come bozza nel tuo browser, così non lo
perdi se chiudi la pagina.
