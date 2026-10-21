import csv, json, re, sys

brand = re.compile(r"runna|nike|garmin|strava|trainasone|trainingpeaks|decathlon|apple|fitbit|coros|polar|whoop|review|not working|login|download|reddit|jobs|price|cost|free trial|promo|discount|\bapi\b|\buk\b|london|\bus\b|indiana|australia|canada|\bnz\b|ireland|scotland|wales|africa|dubai|singapore|malaysia|philippines")
want = re.compile(r"plan|program|schedule|training|couch|taper|long run|pace|zone|beginner|how to|workout|week|sub \d|strength|gym|weight loss|ultra|50k|8k|15k|10 mile|walk")

done = {r["keyword"] for r in csv.DictReader(open("data/openseo_keyword_metrics_IN.csv", encoding="utf-8"))}
rows = [r["keyword"] for r in csv.DictReader(open("data/autocomplete_raw_v2.csv", encoding="utf-8"))]

prog = re.compile(r"run program|program run|\bcmd\b|linux|python|java|bash|\bc\+\+|powershell|terminal|ubuntu|vscode|matlab|github|notepad|qbasic|\bgdb\b|sap tcode|startup|batch|windows|node js|javascript|html|rust|dosbox|yarn|wine|xwayland|\bmac\b|\bdev\b|\bdos\b|lesson plan|running man|running plan map|route|status|meme|quotes|\bflu\b|cold\b|blues|crazies|tantrum|madness|depression|anxiety|bloating|hunger|headache|sluggish|tiredness|niggles|pains|symptoms|vor |voor |krafttraining|couch to 5k [a-z]+$")
sport = re.compile(r"running|marathon|\b5k\b|\b10k\b|\b8k\b|\b15k\b|\b50k\b|couch|ultra|half|run walk|walk run|learn to run|new to running|10 mile")
cands = []
for k in rows:
    if k in done or len(k) > 80 or brand.search(k) or prog.search(k) or not want.search(k) or not sport.search(k):
        continue
    cands.append(k)

cands.sort(key=lambda k: (len(k.split()), len(k), k))
seen = {}
capped = []
for k in cands:
    g = " ".join(k.split()[:3])
    seen[g] = seen.get(g, 0) + 1
    if seen[g] <= 4:
        capped.append(k)
cands = capped
n = int(sys.argv[1]) if len(sys.argv) > 1 else 700
start = int(sys.argv[2]) if len(sys.argv) > 2 else 0
pick = cands[start:start + n]
print(len(cands), "candidates;", len(pick), "picked", file=sys.stderr)
print(json.dumps(pick, ensure_ascii=False))
