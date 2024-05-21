# 2 Times Negative In

# Indagine su Chiusure Negative Consecutive di Titoli Azionari

**Disclaimer:**
Questa applicazione è realizzata a scopo didattico per testare le funzionalità di Python e le librerie utilizzate. Non deve essere utilizzata come strumento finanziario su cui basare le proprie strategie di investimento. L'autore non si assume alcuna responsabilità per eventuali decisioni finanziarie prese sulla base delle informazioni fornite da questa applicazione.

## Descrizione dell'Applicazione

### Scopo dell'Applicazione
L'applicazione è progettata per analizzare le chiusure negative consecutive di titoli azionari e fornire informazioni sui relativi indicatori tecnici, come RSI e MACD, per aiutare gli utenti a comprendere meglio il trend di mercato dei titoli selezionati.

### Funzionalità Principali
1. **Inserimento dei Ticker**:
   - Gli utenti possono inserire manualmente i ticker delle azioni o caricare un file CSV contenente i ticker.

2. **Recupero dei Dati**:
   - Utilizza la libreria `yfinance` per ottenere i dati storici dei titoli azionari, inclusi i prezzi di chiusura, e calcolare gli indicatori tecnici.

3. **Calcolo degli Indicatori Tecnici**:
   - **RSI (Relative Strength Index)**: Calcola l'RSI per valutare le condizioni di ipercomprato o ipervenduto del titolo.
   - **MACD (Moving Average Convergence Divergence)**: Calcola il MACD e la linea di segnale per identificare le tendenze rialziste o ribassiste del titolo.

4. **Visualizzazione dei Dati**:
   - Mostra una tabella con le date di chiusure negative consecutive per ciascun titolo.
   - Fornisce interpretazioni dei risultati di RSI e MACD, indicando i possibili trend di mercato.
   - Consente il download dei risultati in formato CSV.

5. **Analisi delle Chiusure Negative Consecutive**:
   - Identifica le date con due chiusure negative consecutive e calcola la variazione percentuale rispetto all'ultima chiusura negativa consecutiva.

### Utilizzo dell'Applicazione
1. **Selezione della Fonte dei Ticker**:
   - L'utente sceglie se inserire i ticker manualmente o caricare un file CSV.

2. **Inserimento o Caricamento dei Ticker**:
   - L'utente inserisce i ticker separati da virgole o carica un file CSV con i ticker.

3. **Selezione delle Date**:
   - L'utente seleziona la data di inizio e la data di fine per l'analisi dei dati storici dei titoli.

4. **Visualizzazione dei Risultati**:
   - L'applicazione elabora i dati e visualizza i risultati, inclusi RSI, MACD e chiusure negative consecutive, fornendo una comprensione approfondita del trend di mercato per ciascun titolo.

### Tecnologie Utilizzate
- **Streamlit**: Per creare l'interfaccia web interattiva.
- **yfinance**: Per recuperare dati finanziari dai ticker delle azioni.
- **Pandas**: Per la manipolazione e l'elaborazione dei dati.
- **Streamlit Extras**: Per aggiungere elementi interattivi come il pulsante "Buy Me a Coffee".

Questa applicazione è utile per gli investitori che desiderano analizzare le chiusure negative consecutive dei titoli azionari e comprendere meglio le tendenze di mercato attraverso indicatori tecnici come RSI e MACD.

Provalo ora qui: https://firo-2timesnegativein.streamlit.app/

<a href="https://www.buymeacoffee.com/firo"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=☕&slug=firo&button_colour=FFDD00&font_colour=000000&font_family=Cookie&outline_colour=000000&coffee_colour=ffffff" /></a>
