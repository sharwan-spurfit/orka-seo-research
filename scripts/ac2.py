"""Re-seeded Google Autocomplete expansion (India, English).

Seeds come from competitor plan taxonomies (Hal Higdon, Runna, Nike, Strava, Mottiv, Marathon Handbook,
TrainingPeaks, India guides), not from Orka's own features.
Usage: python ac2.py <part 0-2>
"""
import csv, datetime, json, string, sys, time, urllib.parse, urllib.request

SEEDS = [
    # distances and plan types (competitor nav structures)
    "5k training plan", "8k training plan", "10k training plan", "15k training plan", "10 mile training plan",
    "half marathon training plan", "marathon training plan", "ultra marathon training plan", "50k training plan",
    "running training plan", "running plan", "running program",
    # levels and audiences (Hal Higdon, Mottiv)
    "novice marathon training plan", "beginner marathon training plan", "intermediate marathon training plan",
    "advanced marathon training plan", "beginner half marathon training plan", "beginner 10k training plan",
    "senior marathon training plan", "walkers half marathon training plan", "marathon training plan for women",
    "first marathon training plan", "first half marathon training plan", "new to running plan", "learn to run plan",
    "couch to 5k", "couch to marathon", "5k to marathon plan",
    # lengths and schedules
    "12 week marathon training plan", "16 week marathon training plan", "20 week marathon training plan",
    "12 week half marathon training plan", "8 week 10k training plan", "marathon training plan 3 days a week",
    "marathon training plan for busy people", "fast track marathon plan", "marathon plan for slower runners",
    # goals
    "sub 4 hour marathon training plan", "sub 2 hour half marathon training plan", "sub 50 10k training plan",
    "sub 20 5k training plan", "personal best marathon plan", "boston qualifying training plan",
    # plan components and phases
    "base training plan running", "marathon taper", "post marathon recovery plan", "strength training for runners",
    "marathon training plan with strength training", "80/20 marathon training plan", "run walk marathon plan",
    "running plan weight loss", "trail running training plan", "marathon long run", "winter running training plan",
    # plan formats and tools
    "marathon training plan pdf", "marathon training plan free", "marathon training plan app",
    "running training app", "pace chart marathon", "heart rate zone running plan", "marathon plan generator",
    "personalised running plan", "adaptive running plan", "ai running coach",
    # competitors and comparisons
    "runna", "nike run club", "strava training plans", "garmin coach", "trainasone", "trainingpeaks running plans",
    "decathlon coach running", "runna alternative", "runna review", "best running coach app",
    "best marathon training app", "free running coach app",
    # India framing
    "marathon training plan india", "running plan india", "marathon training india beginners",
    "running in hot weather marathon", "marathon training working professionals", "running in india air pollution",
    "mumbai marathon training", "bangalore marathon training", "delhi half marathon training",
]

part = int(sys.argv[1])
seeds = SEEDS[part::3]
mods = [""] + list(string.ascii_lowercase)
out = {}


def get(q):
    u = ("https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=in&q="
         + urllib.parse.quote(q))
    try:
        r = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=10)
        return json.loads(r.read().decode("utf-8", "ignore"))[1]
    except Exception:
        return []


for s in seeds:
    for m in mods:
        for sug in get(s + (" " + m if m else "")):
            out.setdefault(sug.strip().lower(), s)
        time.sleep(0.08)
    print(s, len(out), file=sys.stderr)

d = datetime.date.today().isoformat()
with open("autocomplete_raw_v2_part%d.csv" % part, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["keyword", "seed", "source", "date", "geo"])
    for k, s in sorted(out.items()):
        w.writerow([k, s, "Google Autocomplete (gl=in,hl=en), competitor-derived seeds", d, "IN"])
print(len(out))
