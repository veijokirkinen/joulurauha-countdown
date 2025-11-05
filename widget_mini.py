"""
🎄 JoulurauhaCountdown - Kompakti widget-versio
Optimoitu pieneen tilaan sivustojen widget-käyttöön
"""

import datetime
import time
import streamlit as st
import pytz


def get_next_christmas_eve():
    """Laskee seuraavan joulurauha-hetken (24.12 klo 12:00)"""
    finland_tz = pytz.timezone('Europe/Helsinki')
    now = datetime.datetime.now(finland_tz)

    current_year = now.year
    christmas_eve = finland_tz.localize(
        datetime.datetime(current_year, 12, 24, 12, 0, 0)
    )

    if now >= christmas_eve:
        christmas_eve = finland_tz.localize(
            datetime.datetime(current_year + 1, 12, 24, 12, 0, 0)
        )

    return christmas_eve


def calculate_time_left(target_time):
    """Laskee jäljellä olevan ajan ja palauttaa sen osina"""
    finland_tz = pytz.timezone('Europe/Helsinki')
    now = datetime.datetime.now(finland_tz)

    time_left = target_time - now

    if time_left.total_seconds() <= 0:
        return None

    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return {
        'days': days,
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds,
        'total_seconds': int(time_left.total_seconds())
    }


def main():
    """Kompakti widget-versio"""
    
    st.set_page_config(
        page_title="🎄 Joulurauha Widget",
        page_icon="🎄",
        layout="centered",
        initial_sidebar_state="collapsed"
    )

    # Pienet widget-tyylit
    st.markdown("""
    <style>
    /* Piilota kaikki Streamlit-UI elementit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp > header[data-testid="stHeader"] {display: none;}
    .stDeployButton {display: none;}
    
    /* Kompakti container */
    .main .block-container {
        padding-top: 0.5rem;
        padding-bottom: 0.5rem;
        padding-left: 0.5rem;
        padding-right: 0.5rem;
        max-width: 300px;
    }
    
    /* Pieni otsikko */
    .widget-title {
        text-align: center;
        color: #165B33;
        font-size: 1rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
    }
    
    /* Kompakti countdown-container */
    .countdown-mini {
        background: linear-gradient(135deg, #165B33, #22863a);
        border-radius: 8px;
        padding: 0.5rem;
        margin: 0.25rem 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.2);
    }
    
    /* Pienet countdown-boksit */
    .countdown-mini-box {
        background: rgba(255,255,255,0.95);
        border-radius: 6px;
        padding: 0.3rem;
        margin: 0.1rem;
        text-align: center;
        box-shadow: 0 1px 4px rgba(0,0,0,0.1);
        border: 1px solid #FFD700;
        min-height: 50px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    
    /* Pienet numerot */
    .countdown-mini-number {
        font-size: 1.2rem;
        font-weight: bold;
        color: #B22222;
        text-shadow: 1px 1px 1px rgba(0,0,0,0.2);
        line-height: 1;
    }
    
    /* Pienet labelit */
    .countdown-mini-label {
        font-size: 0.6rem;
        color: #165B33;
        font-weight: bold;
        margin-top: 0.1rem;
        line-height: 1;
    }
    
    /* Jouluviesti kompaktina */
    .christmas-mini {
        background: linear-gradient(135deg, #FFD700, #FFA500);
        border-radius: 8px;
        padding: 0.5rem;
        text-align: center;
        margin: 0.25rem 0;
        box-shadow: 0 2px 8px rgba(255,215,0,0.3);
        font-size: 0.8rem;
    }
    </style>
    """, unsafe_allow_html=True)

    # Kompakti otsikko
    st.markdown('<div class="widget-title">🎄 JOULURAUHA</div>', unsafe_allow_html=True)

    # Laskuri
    christmas_eve = get_next_christmas_eve()
    time_left = calculate_time_left(christmas_eve)

    if time_left is None:
        st.markdown("""
        <div class="christmas-mini">
            <strong>🎄 HYVÄÄ JOULUA! 🎄</strong><br>
            Joulurauha on alkanut! 🕊️
        </div>
        """, unsafe_allow_html=True)
    else:
        # Kompakti countdown
        st.markdown('<div class="countdown-mini">', unsafe_allow_html=True)

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.markdown(f"""
            <div class="countdown-mini-box">
                <div class="countdown-mini-number">{time_left['days']}</div>
                <div class="countdown-mini-label">PV</div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div class="countdown-mini-box">
                <div class="countdown-mini-number">{time_left['hours']:02d}</div>
                <div class="countdown-mini-label">H</div>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
            <div class="countdown-mini-box">
                <div class="countdown-mini-number">{time_left['minutes']:02d}</div>
                <div class="countdown-mini-label">MIN</div>
            </div>
            """, unsafe_allow_html=True)

        with col4:
            st.markdown(f"""
            <div class="countdown-mini-box">
                <div class="countdown-mini-number">{time_left['seconds']:02d}</div>
                <div class="countdown-mini-label">SEK</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    # Auto-refresh
    time.sleep(1)
    st.rerun()


if __name__ == "__main__":
    main()