import streamlit as st
import yfinance as yf
import pandas as pd

# Titolo dell'app
st.title('Indagine su Chiusure Negative Consecutive di Titoli Azionari')

# Input per i ticker dei titoli azionari separati da virgole
tickers_input = st.text_input('Inserisci i ticker dei titoli azionari separati da virgole', 'AAPL, CRM, GOOGL')

# Data di inizio e fine per il download dei dati
start_date = st.date_input('Data di inizio', pd.to_datetime('2024-01-01'))
end_date = st.date_input('Data di fine', pd.to_datetime('today'))

# Se l'utente ha inserito dei ticker
if tickers_input:
    # Suddividi l'input in una lista di ticker
    tickers = [ticker.strip().upper() for ticker in tickers_input.split(',')]
    
    # Itera su ciascun ticker
    for ticker in tickers:
        st.subheader(f'Dati per {ticker}')
        
        # Scaricare i dati storici del titolo azionario
        data = yf.download(ticker, start=start_date, end=end_date)
        
        if not data.empty:
            # Aggiungere una colonna per le variazioni percentuali giornaliere
            data['Daily Change'] = data['Close'].pct_change()

            # Aggiungere una colonna per indicare se la chiusura è stata negativa
            data['Negative Close'] = data['Daily Change'] < 0

            # Individuare due chiusure negative consecutive
            data['Two Consecutive Negatives'] = data['Negative Close'] & data['Negative Close'].shift(1)

            # Filtrare i dati per visualizzare solo le righe con due chiusure negative consecutive
            consecutive_negatives = data[data['Two Consecutive Negatives']]

            # Visualizzare i risultati
            st.write(f'Date con due chiusure negative consecutive per {ticker}')
            st.dataframe(consecutive_negatives)

            # Opzione per scaricare i risultati
            csv = consecutive_negatives.to_csv().encode('utf-8')
            st.download_button(
                label=f"Scarica i risultati in CSV per {ticker}",
                data=csv,
                file_name=f'{ticker}_consecutive_negatives.csv',
                mime='text/csv',
            )
        else:
            st.write(f'Nessun dato disponibile per il ticker {ticker}.')
