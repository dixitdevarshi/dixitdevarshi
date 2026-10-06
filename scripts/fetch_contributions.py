import json,re,requests
from bs4 import BeautifulSoup
from pathlib import Path
U="dixitdevarshi"
r=requests.get(f"https://github.com/users/{U}/contributions",headers={"User-Agent":"Mozilla/5.0"},timeout=30); r.raise_for_status()
s=BeautifulSoup(r.text,"html.parser"); days=[]
for e in s.select("td.ContributionCalendar-day"):
    d=e.get("data-date")
    if not d: continue
    m=re.search(r"(\d+)\s+contribution",e.get("aria-label",""))
    days.append({"date":d,"level":int(e.get("data-level") or 0),"count":int(m.group(1)) if m else 0})
Path("data").mkdir(exist_ok=True)
Path("data/contributions.json").write_text(json.dumps({"username":U,"days":days},indent=2),encoding="utf-8")
print("Fetched",len(days),"days")
