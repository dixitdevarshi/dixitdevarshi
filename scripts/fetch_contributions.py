import json,re,requests
from bs4 import BeautifulSoup
from pathlib import Path
u="dixitdevarshi"; s=BeautifulSoup(requests.get(f"https://github.com/users/{u}/contributions",headers={"User-Agent":"Mozilla/5.0"},timeout=30).text,"html.parser"); days=[]
for e in s.select("td.ContributionCalendar-day"):
 d=e.get("data-date"); l=e.get("data-level"); a=e.get("aria-label",""); m=re.search(r"(\\d+)\\s+contribution",a)
 if d: days.append({"date":d,"level":int(l or 0),"count":int(m.group(1)) if m else 0})
Path("data").mkdir(exist_ok=True); Path("data/contributions.json").write_text(json.dumps({"username":u,"days":days},indent=2))
