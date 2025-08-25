from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from fastapi.responses import HTMLResponse, JSONResponse
from pathlib import Path

app = FastAPI(title="HOI-AM API")

DATA_PATH = Path(__file__).parent / 'data' / 'India_Cities_101_Famous.csv'
data = pd.read_csv(DATA_PATH)

class ScoreRequest(BaseModel):
  hoi: float
  roi: float
  top_n: int = 5

@app.post('/fit-score')
def fit_score(req: ScoreRequest):
  df = data.copy()
  df['distance'] = ((df['hoi']-req.hoi)**2 + (df['roi']-req.roi)**2)**0.5
  top = df.nsmallest(req.top_n, 'distance')
  return top[['name','state','hoi','roi']].to_dict(orient='records')

@app.post('/submit', response_class=HTMLResponse)
def submit(req: ScoreRequest):
  top = fit_score(req)
  items = ''.join(
    f"<li>{c['name']} ({c['state']}) - HOI {c['hoi']} ROI {c['roi']}</li>" for c in top
  )
  html = f"""
  <html><body>
  <h1>Top Cities</h1>
  <ol>{items}</ol>
  </body></html>
  """
  return HTMLResponse(content=html)

@app.post('/submit/pdf')
def submit_pdf(req: ScoreRequest):
  return JSONResponse({'detail': 'PDF generation not implemented'}, status_code=501)
