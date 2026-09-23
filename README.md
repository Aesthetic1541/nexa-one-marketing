# NEXA One Marketing Intelligence Website

## Run locally (Windows PowerShell)

```powershell
cd nexa_one_website
py -m venv venv
.env\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Then open: http://127.0.0.1:5000

## Project structure

- `app.py` — Flask server
- `templates/index.html` — complete dashboard
- `static/style.css` — responsive dark analytics UI
- `data.json` — calculated dataset + regression values used by the UI
- `Advertising Data.xlsx` — supplied dataset
- `requirements.txt` — Python dependencies

## Notes

The scenario simulator uses the historical multiple-regression equation and is explicitly presented as a model-based scenario tool, not a causal forecast.
