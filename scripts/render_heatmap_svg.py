import json,datetime as dt
from pathlib import Path
D=json.loads(Path("data/contributions.json").read_text(encoding="utf-8")); A=sorted(D["days"],key=lambda x:x["date"])
if not A: raise SystemExit("No contribution data")
dates=[dt.date.fromisoformat(x["date"]) for x in A]; first=dates[0]; start=first-dt.timedelta(days=(first.weekday()+1)%7)
cell,gap,left,top=11,3,48,62
weeks=max((d-start).days//7 for d in dates)+1; W=left+weeks*(cell+gap)+34; H=190
P=["#161b22","#0e4429","#006d32","#26a641","#39d353"]; total=sum(x["count"] for x in A)
S=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><style>.t{{font:12px ui-monospace,monospace;fill:#8b949e}}.h{{font:14px ui-monospace,monospace;fill:#e6edf3}}.c{{opacity:0;transform:translateY(-5px);animation:r .26s ease-out forwards}}@keyframes r{{to{{opacity:1;transform:translateY(0)}}}}</style><rect x="1" y="1" width="{W-2}" height="{H-2}" rx="10" fill="#0d1117" stroke="#30363d"/><text class="h" x="18" y="28">{total} contributions in the last year</text>']
seen=set()
for d in dates:
    key=(d.year,d.month)
    if key not in seen and d.day<=7:
        seen.add(key); wi=(d-start).days//7
        S.append(f'<text class="t" x="{left+wi*(cell+gap)}" y="50">{d.strftime("%b")}</text>')
for label,row in [("Mon",1),("Wed",3),("Fri",5)]:
    S.append(f'<text class="t" x="10" y="{top+row*(cell+gap)+10}">{label}</text>')
for x,d in zip(A,dates):
    wi=(d-start).days//7; row=(d.weekday()+1)%7; xx=left+wi*(cell+gap); yy=top+row*(cell+gap); lev=max(0,min(4,int(x["level"])))
    S.append(f'<rect class="c" x="{xx}" y="{yy}" width="{cell}" height="{cell}" rx="2" fill="{P[lev]}" style="animation-delay:{(wi+row)*.012:.3f}s"><title>{x["count"]} contributions on {d}</title></rect>')
ly=top+7*(cell+gap)+22; lx=max(left,W-190)
S.append(f'<text class="t" x="{lx-34}" y="{ly+9}">Less</text>')
for i,c in enumerate(P): S.append(f'<rect x="{lx+i*16}" y="{ly}" width="11" height="11" rx="2" fill="{c}"/>')
S.append(f'<text class="t" x="{lx+88}" y="{ly+9}">More</text></svg>')
Path("contrib-heatmap.svg").write_text("\n".join(S),encoding="utf-8")
print("Rendered",total,"real contributions")
