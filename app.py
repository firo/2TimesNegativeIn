import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# Calcolare la data di inizio come il primo giorno dell'anno corrente
current_year = datetime.now().year
start_date_default = datetime(current_year, 1, 1)

# Titolo dell'app
st.title('Indagine su Chiusure Negative Consecutive di Titoli Azionari')

# Input per i ticker dei titoli azionari separati da virgole
tickers_input = st.text_input('Inserisci i ticker dei titoli azionari separati da virgole', 'AAPL, MSFT, GOOGL')

# Data di inizio e fine per il download dei dati
start_date = st.date_input('Data di inizio', start_date_default)
end_date = st.date_input('Data di fine', pd.to_datetime('today'))

# Se l'utente ha inserito dei ticker
if tickers_input:
    # Suddividi l'input in una lista di ticker
    tickers = [ticker.strip().upper() for ticker in tickers_input.split(',')]
    
    # Calcola la data di ieri
    yesterday = datetime.now() - timedelta(days=1)
    yesterday_str = yesterday.strftime('%Y-%m-%d')
    
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

            # Determinare il risultato
            if not consecutive_negatives.empty:
                last_date = consecutive_negatives.index[-1].strftime('%Y-%m-%d')
                last_close_negative = consecutive_negatives['Close'].iloc[-1]
                latest_close = data['Close'].iloc[-1]
                
                if last_date == yesterday_str:
                    result = "**Risultato per {ticker}: Positivo**"
                else:
                    result = "**Risultato per {ticker}: Negativo**"
                    # Calcolare il delta percentuale
                    delta_percent = ((latest_close - last_close_negative) / last_close_negative) * 100
                    st.write(f"Delta percentuale rispetto all'ultima chiusura negativa consecutiva: {delta_percent:.2f}%")
            else:
                result = "**Risultato per {ticker}: Nessuna chiusura negativa consecutiva trovata**"
            
            # Mostrare il risultato in grassetto
            st.markdown(result)
            
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
