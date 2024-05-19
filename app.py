import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# Carica i ticker dei componenti da un file CSV
def load_ticker_group(file):
    df = pd.read_csv(file)
    tickers = df['Ticker'].tolist()
    return tickers

# Calcolare la data di inizio come il primo giorno dell'anno corrente
current_year = datetime.now().year
start_date_default = datetime(current_year, 1, 1)

# Titolo dell'app
st.title('Indagine su Chiusure Negative Consecutive di Titoli Azionari')

# Input per i ticker dei titoli azionari o il caricamento di un file CSV con i ticker
ticker_source = st.radio('Scegli la fonte dei ticker:', ['Inserimento manuale', 'Caricamento da file CSV'])

if ticker_source == 'Inserimento manuale':
    # Inserimento manuale di default
    default_tickers = ['GOOGL', 'AAPL', 'MSFT', 'CRM']
    tickers_input = st.text_area('Inserisci i ticker dei titoli azionari separati da virgole o il codice di un indice (separati da virgole)', ', '.join(default_tickers))
    tickers = [ticker.strip().upper() for ticker in tickers_input.split(',') if ticker.strip()]
else:
    ticker_file = st.file_uploader('Carica un file CSV con i ticker. Il file deve contenere un intestazione chiamata "Ticker".', type=['csv'])
    if ticker_file is not None:
        tickers = load_ticker_group(ticker_file)
    else:
        tickers = []

# Data di inizio e fine per il download dei dati
start_date = st.date_input('Data di inizio', start_date_default)
end_date = st.date_input('Data di fine', pd.to_datetime('today'))

# Se sono stati forniti dei ticker
if tickers:
    # Calcola la data di ieri

    today = datetime.today()
    day_of_week = today.weekday()
    
    if day_of_week == 6:  # se Domenica (6)
        yesterday = datetime.now() - timedelta(days=2)

    elif day_of_week == 0: # se Lunedì (0)
        yesterday = datetime.now() - timedelta(days=3)

    else: # per tutti gli altri giorni, anche per sabato
        yesterday = datetime.now() - timedelta(days=1)

    yesterday_str = yesterday.strftime('%Y-%m-%d')

    # Itera su ciascun ticker
    for ticker in tickers:

        ticker_info = yf.Ticker(ticker)
        company_name = ticker_info.info['longName']
        st.subheader(f'Dati per {company_name} ({ticker})')

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
            st.dataframe(consecutive_negatives.tail())

            # Determinare il risultato
            if not consecutive_negatives.empty:
                last_date = consecutive_negatives.index[-1].strftime('%Y-%m-%d')
                last_close_negative = consecutive_negatives['Close'].iloc[-1]
                latest_close = data['Close'].iloc[-1]

                if last_date == yesterday_str:
                    result = f"<span style='color:green'>**Risultato per {ticker}: Positivo**</span>"
                else:
                    result = f"**Risultato per {ticker}: Negativo**"
                    # Calcolare il delta percentuale
                    delta_percent = ((latest_close - last_close_negative) / last_close_negative) * 100
                    st.write(f"Delta percentuale rispetto all'ultima chiusura negativa consecutiva: {delta_percent:.2f}%")
            else:
                result = f"**Risultato per {ticker}: Nessuna chiusura negativa consecutiva trovata**"

            # Mostrare il risultato in grassetto e in verde se positivo
            st.markdown(result, unsafe_allow_html=True)


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
