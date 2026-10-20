import urllib.request, urllib.parse, json, csv, time, string, datetime, sys
seeds = ["marathon training plan","half marathon training plan","10k training plan","5k training plan","running training plan","running app","ai running coach","adaptive training plan running","marathon pace calculator","marathon time predictor","race time predictor","marathon fueling","marathon nutrition","running shoes","best running shoes for","running watch","garmin training plan","hrv running","heart rate zone running","how to run a marathon","first marathon","sub 4 marathon","sub 2 half marathon","sub 50 10k","marathon india","mumbai marathon","delhi half marathon","bengaluru marathon","tata mumbai marathon training","running for beginners","couch to 5k","strava alternative","nike run club alternative","runna alternative","missed run training plan","marathon taper","long run","race readiness","marathon calendar india","running coach app"]
mods = [""]+list(string.ascii_lowercase)
out={}
def get(q):
    u="https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=in&q="+urllib.parse.quote(q)
    try:
        r=urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=10)
        return json.loads(r.read().decode("utf-8","ignore"))[1]
    except Exception as e: return []
for s in seeds:
    for m in mods:
        for q in ([s+" "+m] if m else [s]):
            for sug in get(q):
                out.setdefault(sug.strip().lower(),s)
        time.sleep(0.08)
    print(s,len(out),file=sys.stderr)
d=datetime.date.today().isoformat()
with open("autocomplete_raw.csv","w",newline="",encoding="utf-8") as f:
    w=csv.writer(f);w.writerow(["keyword","seed","source","date","geo"])
    for k,s in sorted(out.items()): w.writerow([k,s,"Google Autocomplete (gl=in,hl=en)",d,"IN"])
print(len(out))
