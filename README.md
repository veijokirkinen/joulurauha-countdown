# 🎄 JoulurauhaCountdown

Kaunis ja interaktiivinen joulurauha-laskuri, joka laskee ajan seuraavaan joulurauhaan (24.12 klo 12:00).

## Ominaisuudet

- ⏰ Reaaliaikainen countdown joulurauhaan
- 🇫🇮 Suomen aikavyöhyke (Europe/Helsinki)
- 🎨 Kauniisti tyylitelty käyttöliittymä
- 📱 Responsiivinen design
- 🔄 Automaattinen päivitys sekunnin välein
- 🎯 Älykäs vuosien vaihto (siirtyy seuraavaan vuoteen kun joulurauha on mennyt)

## Asennus ja käyttö

### 1. Luo virtuaaliympäristö
```powershell
# Luo virtuaaliympäristö
python -m venv .venv

# Aktivoi (PowerShell)
.venv\Scripts\Activate.ps1
```

### 2. Asenna riippuvuudet
```powershell
pip install -r requirements.txt
```

### 3. Käynnistä sovellus
```powershell
streamlit run app.py
```

Sovellus avautuu selaimessa osoitteessa `http://localhost:8501`

## VS Code -asetukset

### Python Interpreter
1. Avaa Command Palette (`Ctrl+Shift+P`)
2. Kirjoita "Python: Select Interpreter"
3. Valitse `.venv\Scripts\python.exe`

### Workspace-asetukset (valinnainen)
Luo `.vscode/settings.json`:
```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}\\.venv\\Scripts\\python.exe",
  "python.terminal.activateEnvironment": true
}
```

## Toimintaperiaate

Sovellus:
1. Laskee seuraavan joulurauha-hetken (24.12 klo 12:00 Suomen aikaa)
2. Jos joulurauha on jo mennyt tänä vuonna, siirtyy automaattisesti seuraavaan vuoteen
3. Päivittää laskuria reaaliaikaisesti sekunnin välein
4. Näyttää kauniin jouluviestin kun joulurauha alkaa

## Teknologia

- **Python 3.13** - Pääohjelmointikieli
- **Streamlit** - Web-sovelluskehys
- **pytz** - Aikavyöhykkeiden käsittely
- **CSS** - Kaunis tyylittely

## Julkaisu internetiin

### 🚀 Streamlit Cloud (ilmainen ja nopea!)

1. **Lataa koodi GitHubiin:**
```bash
git init
git add .
git commit -m "🎄 Initial commit"
git remote add origin https://github.com/KÄYTTÄJÄ/joulurauha-countdown.git
git push -u origin main
```

2. **Deploy Streamlit Cloudiin:**
   - Mene [share.streamlit.io](https://share.streamlit.io)
   - Kirjaudu GitHubilla
   - Valitse repositorio ja `app.py`
   - Klikkaa "Deploy!"

3. **Widget-käyttö sivustoilla:**
```html
<!-- Iframe-upotus -->
<iframe 
  src="https://your-app.streamlit.app/?embed=true" 
  width="100%" 
  height="400px" 
  frameborder="0">
</iframe>

<!-- Suora linkki -->
<a href="https://your-app.streamlit.app/">🎄 Joulurauha-laskuri</a>
```

### 📱 Widget-optimoitu versio
Käytä `app_widget.py` kompaktimpaan näyttöön:
- `?embed=true` piilottaa Streamlit-branding
- Pienempi fonttikoko ja tiiviimpi layout
- Sopii paremmin iframe-upotuksiin

### 🔄 Muut hosting-vaihtoehdot
- **Railway** - railway.app (ilmainen tier)
- **Render** - render.com (ilmainen tier)  
- **Heroku** - heroku.com (maksullinen)

## Kehitysideoita

- 🎵 Joulumusiikki taustalle
- 🌟 Animoituja lumihiutaleita
- 📊 Tilastot kuinka monta joulua on kulunut
- 🎁 Laskurit myös muille juhlapäiville
- 🌐 Monikielisyys
- 📧 Sähköposti-ilmoitukset

## Vianmääritys

### "Unable to import 'streamlit'"
- Varmista että virtuaaliympäristö on aktivoitu
- Asenna riippuvuudet: `pip install -r requirements.txt`
- Valitse oikea Python interpreter VS Codessa

### VS Code jää "Configuring Python Environment" -tilaan
- Valitse interpreter manuaalisesti: `Ctrl+Shift+P` → "Python: Select Interpreter"
- Restart VS Code: `Ctrl+Shift+P` → "Developer: Reload Window"
- Tarkista että `.venv` on luotu oikein

---

🎄 *Hyvää joulua ja rauhallista joulunodotusta!* ❄️