import csv, glob, re, collections

junk = re.compile(r"honda|daytime running|[^\x00-\x7f]|berapa|\bjam\b|menit|gratis|gratuit|\bzu\b|\bpour\b|\bpara\b|corrida|ciclismo|\bbike\b|cycling|\brug\b|\bgas\b|\bkids?\b|\bdogs?\b|horse|\bcar\b|truck|lights?\b|boards?\b|\bcats?\b|\bski\b|swim|safety shoes|work shoes|triathlon|reddit|youtube|amazon|walmart|\bpdf download\b")
relevant = re.compile(r"run|marathon|5k|10k|8k|15k|couch|taper|pace|strava|runna|garmin|training|plan|half|race|nike run|coach|trainasone|trainingpeaks|decathlon")

v2 = {}
for p in sorted(glob.glob("data/autocomplete_raw_v2_part*.csv")):
    for r in csv.DictReader(open(p, encoding="utf-8")):
        v2.setdefault(r["keyword"], r["seed"])
v1 = {r["keyword"] for r in csv.DictReader(open("data/autocomplete_raw.csv", encoding="utf-8"))}

clean = {k: s for k, s in v2.items() if not junk.search(k) and relevant.search(k)}
new_only = {k: s for k, s in clean.items() if k not in v1}
print("v2 raw", len(v2), "clean", len(clean), "overlap with v1", sum(1 for k in clean if k in v1), "new", len(new_only))

with open("data/autocomplete_raw_v2.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["keyword", "seed", "in_v1_set", "source", "date", "geo"])
    for k, s in sorted(clean.items()):
        w.writerow([k, s, "yes" if k in v1 else "no", "Google Autocomplete (gl=in,hl=en), competitor-derived seeds", "2026-10-21", "IN"])

themes = collections.OrderedDict([
    ("levels (novice/beginner/intermediate/advanced)", r"novice|beginner|intermediate|advanced"),
    ("week-length plans (8-24 weeks)", r"\b\d{1,2}[ -]?weeks?\b"),
    ("goal times (sub-x, PB, BQ)", r"\bsub[ -]?\d|personal best|\bpb\b|boston|qualif|break(ing)? \d"),
    ("couch to / run-walk / new to running", r"couch|run[ -]walk|new to running|learn to run|from scratch|zero to"),
    ("strength / cross-training / 80-20", r"strength|cross[ -]train|80[ /]20|gym"),
    ("base / taper / recovery / long run", r"base training|taper|recovery|long run|post marathon"),
    ("weight loss", r"weight loss|lose weight|fat"),
    ("trail / ultra / 50k", r"trail|ultra|50k|100 mile|50 mile"),
    ("odd distances (8k, 15k, 10 mile)", r"\b8k\b|\b15k\b|10 mile|10-mile|\b5 mile"),
    ("heat / pollution / working professionals (India)", r"heat|hot weather|humid|pollution|aqi|working|office|busy|monsoon|summer"),
    ("apps / tools / generators / free / pdf", r"\bapp\b|generator|calculator|free|printable|template|excel|spreadsheet|\bpdf\b"),
    ("competitors / alternatives / reviews", r"runna|nike run club|strava|garmin|trainasone|trainingpeaks|decathlon|alternative|review|vs "),
    ("km / pace chart / heart rate", r"\bkm\b|pace chart|heart rate|\bhr\b|zone"),
    ("India places", r"india|mumbai|delhi|bengaluru|bangalore|chennai|hyderabad|pune|kolkata"),
])
print()
for name, pat in themes.items():
    allm = [k for k in clean if re.search(pat, k)]
    newm = [k for k in new_only if re.search(pat, k)]
    print("%-52s all %4d  new %4d" % (name, len(allm), len(newm)))
    print("    new examples:", " | ".join(sorted(newm, key=len)[:8]))

with open("data/new_keywords_v2_only.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["keyword", "seed"])
    for k, s in sorted(new_only.items()):
        w.writerow([k, s])
