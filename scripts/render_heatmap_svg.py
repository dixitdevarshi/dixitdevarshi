import json,datetime as dt,html
from pathlib import Path
D=json.loads(Path("data/contributions.json").read_text()); A=sorted(D["days"],key=lambda x:x["date"]); P=["#161b22","#0e4429","#006d32","#26a641","#39d353"]; total=sum(x["count"] for x in A); start=dt.date.fromisoformat(A[0]["date"]); start-=dt.timedelta(days=(start.weekday()+1)%7); cell=10;gap=3;left=42;top=48; weeks=max((dt.date.fromisoformat(x["date"])-start).days//7 for x in A)+1; W=left+weeks*13+30; H=155
S=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}"><style>.t{{font:12px ui-monospace,monospace;fill:#8b949e}}.h{{font:14px ui-monospace,monospace;fill:#e6edf3}}.c{{opacity:0;animation:a .18s forwards}}@keyframes a{{to{{opacity:1}}}}</style><rect x="1" y="1" width="{W-2}" height="{H-2}" rx="10" fill="#0d1117" stroke="#30363d"/><text class="h" x="18" y="27">{total} contributions in the last year</text>']
for x in A:
 d=dt.date.fromisoformat(x["date"]); wi=(d-start).days//7; row=(d.weekday()+1)%7; xx=left+wi*13; yy=top+row*13; lev=max(0,min(4,x["level"])); S.append(f'<rect class="c" x="{xx}" y="{yy}" width="10" height="10" rx="2" fill="{P[lev]}" style="animation-delay:{(wi+row)*.008:.3f}s"><title>{x["count"]} contributions on {d}</title></rect>')
S.append("</svg>"); Path("contrib-heatmap.svg").write_text("\\n".join(S))
