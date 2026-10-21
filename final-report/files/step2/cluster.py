import csv,re,collections
rows=list(csv.DictReader(open("autocomplete_raw.csv",encoding="utf-8")))
junk=re.compile(r"honda|hrv (daytime|running (board|light))|daytime running|[^\x00-\x7f]|berapa|\bjam\b|menit|gratis|gratuit|\bzu\b|\bpour\b|\bde\b|\bpara\b|\bcon\b|corrida|ciclismo|bike|cycling|rug|\bgas\b|fuel marathon jacket|nutrition sponsor|first marathon in space|\bkids?\b|dog|horse|car\b|truck|lights?\b|boards?\b|cat\b|ski|swim|walk(ing)? shoes|safety shoes|work shoes")
C=[("india_races",r"mumbai|delhi|bengaluru|bangalore|chennai|hyderabad|kolkata|pune|tata|airtel|india|aims|vadodara|chandigarh|comrades"),
("goal_time",r"\bsub[ -]?\d|under \d|break(ing)? (\d|four|three|two)|\d hour marathon|negative split"),
("ai_app",r"\bapp\b|coach|runna|strava|nike run club|\bnrc\b|garmin (training|coach)|apple watch|alternative|adaptive|\bai\b|watch"),
("calculators",r"calculator|predictor|prediction|pace chart|converter"),
("fueling",r"fuel|nutrition|\bgels?\b|carb|hydrat|electrolyte|eat"),
("shoes",r"shoes?|sneakers|trainers|footwear"),
("hr_recovery",r"hrv|heart rate|zone 2|zones|recovery|resting|sleep|vo2"),
("taper_longrun",r"taper|long run|miss(ed|ing)|rest day|skipp|injur|back on track"),
("plans_5k_10k",r"5k|10k|couch|c25k|5 km|10 km"),
("plans_half",r"half"),
("plans_marathon",r"marathon|first marathon|42"),
("beginner_howto",r"beginner|how to|start running|run longer|tips")]
out=[];n=0
for r in rows:
    k=r['keyword']
    if junk.search(k) or not re.search(r"run|marathon|5k|10k|couch|taper|pace|strava|runna|hrv|garmin|training|shoe|half|race",k): continue
    cl="unclassified"
    for name,pat in C:
        if re.search(pat,k): cl=name;break
    out.append((k,cl,r['seed']))
c=collections.Counter(x[1] for x in out);print(len(out),c)
with open("kw_clean.csv","w",newline="",encoding="utf-8") as f:
    w=csv.writer(f);w.writerow(["keyword","cluster","seed"]);w.writerows(out)
