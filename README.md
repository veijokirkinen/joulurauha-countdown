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

### Streamlit Cloud (ilmainen)
1. Lataa projekti GitHubiin
2. Mene [share.streamlit.io](https://share.streamlit.io)
3. Yhdistä GitHub-repositorio
4. Sovellus on käytettävissä julkisessa osoitteessa

### Muut vaihtoehdot
- **Heroku** - Pilvipalvelu
- **Railway** - Moderni deployment
- **Render** - Yksinkertainen hosting

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