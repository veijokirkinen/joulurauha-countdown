"""
🎄 JoulurauhaCountdown - Widget-optimoitu versio
Laskee ajan seuraavaan joulurauhaan (24.12 klo 12:00)
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
    """Widget-optimoitu pääfunktio"""
    
    # Tarkista onko embed-mode
    query_params = st.query_params
    is_embed = query_params.get("embed", "false").lower() == "true"
    
    st.set_page_config(
        page_title="🎄 Joulurauha Countdown",
        page_icon="🎄",
        layout="wide" if is_embed else "centered",
        initial_sidebar_state="collapsed"
    )

    # Kompaktimmat tyylit widget-käyttöön
    embed_styles = """
    <style>
    .main-title {
        text-align: center;
        color: #165B33;
        font-size: 2rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }
    
    .countdown-container {
        background: linear-gradient(135deg, #165B33, #22863a);
        border-radius: 15px;
        padding: 1rem;
        margin: 1rem 0;
        box-shadow: 0 4px 16px rgba(0,0,0,0.2);
    }
    
    .countdown-box {
        background: rgba(255,255,255,0.95);
        border-radius: 10px;
        padding: 1rem;
        margin: 0.25rem;
        text-align: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        border: 1px solid #FFD700;
    }
    
    .countdown-number {
        font-size: 1.8rem;
        font-weight: bold;
        color: #B22222;
        text-shadow: 1px 1px 1px rgba(0,0,0,0.2);
    }
    
    .countdown-label {
        font-size: 0.9rem;
        color: #165B33;
        font-weight: bold;
        margin-top: 0.25rem;
    }
    
    .info-text {
        text-align: center;
        color: #2F4F4F;
        font-size: 0.9rem;
        margin: 0.5rem 0;
    }
    
    .christmas-message {
        background: linear-gradient(135deg, #FFD700, #FFA500);
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 4px 16px rgba(255,215,0,0.3);
    }
    
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        max-width: 100%;
    }
    
    /* Piilota Streamlit-branding widget-moodissa */
    .stApp > header[data-testid="stHeader"] {
        display: none;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display:none;}
    </style>
    """ if is_embed else """
    <style>
    .main-title {
        text-align: center;
        color: #165B33;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .countdown-container {
        background: linear-gradient(135deg, #165B33, #22863a);
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: 0 8px 32px rgba(0,0,0,0.2);
        border: 1px solid rgba(255,255,255,0.1);
    }
    
    .countdown-box {
        background: rgba(255,255,255,0.9);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 0.5rem;
        text-align: center;
        box-shadow: 0 4px 16px rgba(0,0,0,0.1);
        border: 2px solid #FFD700;
    }
    
    .countdown-number {
        font-size: 3rem;
        font-weight: bold;
        color: #B22222;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
    }
    
    .countdown-label {
        font-size: 1.2rem;
        color: #165B33;
        font-weight: bold;
        margin-top: 0.5rem;
    }
    
    .info-text {
        text-align: center;
        color: #2F4F4F;
        font-size: 1.1rem;
        margin: 1rem 0;
    }
    
    .christmas-message {
        background: linear-gradient(135deg, #FFD700, #FFA500);
        border-radius: 15px;
        padding: 2rem;
        text-align: center;
        margin: 2rem 0;
        box-shadow: 0 8px 32px rgba(255,215,0,0.3);
    }
    
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    </style>
    """

    st.markdown(embed_styles, unsafe_allow_html=True)

    # Otsikko
    title = "🎄 JOULURAUHA ❄️" if is_embed else "🎄 JOULURAUHA COUNTDOWN ❄️"
    st.markdown(f'<h1 class="main-title">{title}</h1>', unsafe_allow_html=True)

    # Laskuri
    christmas_eve = get_next_christmas_eve()
    time_left = calculate_time_left(christmas_eve)

    if time_left is None:
        st.markdown("""
        <div class="christmas-message">
            <h2>🎄 HYVÄÄ JOULUA! 🎄</h2>
            <p>Joulurauha on alkanut! 🕊️</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        if not is_embed:
            st.markdown(f"""
            <div class="info-text">
                Joulurauhaan {christmas_eve.strftime('%d.%m.%Y klo %H:%M:%S')}
            </div>
            """, unsafe_allow_html=True)

        # Countdown-laskuri
        st.markdown('<div class="countdown-container">', unsafe_allow_html=True)

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.markdown(f"""
            <div class="countdown-box">
                <div class="countdown-number">{time_left['days']}</div>
                <div class="countdown-label">PÄIVÄÄ</div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div class="countdown-box">
                <div class="countdown-number">{time_left['hours']:02d}</div>
                <div class="countdown-label">TUNTIA</div>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
            <div class="countdown-box">
                <div class="countdown-number">{time_left['minutes']:02d}</div>
                <div class="countdown-label">MINUUTTIA</div>
            </div>
            """, unsafe_allow_html=True)

        with col4:
            st.markdown(f"""
            <div class="countdown-box">
                <div class="countdown-number">{time_left['seconds']:02d}</div>
                <div class="countdown-label">SEKUNTIA</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

        if not is_embed:
            st.markdown("""
            <div class="info-text">
                ⭐ Joulurauha alkaa 24. joulukuuta kello 12:00 ⭐
            </div>
            """, unsafe_allow_html=True)

    # Auto-refresh
    time.sleep(1)
    st.rerun()


if __name__ == "__main__":
    main()