"""Rescore v3 after OpenSEO-led discovery (India, English, Oct 2026).
Rules written before scoring:
  - Scores 1-5 on relevance, demand, intent fit, competition ease (5 = easy), ranking opportunity, business value.
  - Volume gate: the cluster's biggest volume pool must be >= 1,000 searches a month to be a traffic target.
    Below that it is a section of a core page or a brand/positioning item.
  - Tiers: 1 = score >= 4.0, 2 = 3.5-3.99, 3 = 3.0-3.49, 4 = below 3.0. Confidence is separate (5 = volume and SERP read).
  - Volumes in the same Google Ads pool are not added together.
"""
import csv, os

os.makedirs("outputs", exist_ok=True)

# id, fit, cluster, primary keyword, pool volume, KD, other pools / notes, page type, scores (rel, demand, intent, comp, opp, value), confidence, SERP evidence
C = [
 ("K01", "Core plan", "Marathon training plan pool (plan, schedule, program, guide)", "training schedule for marathon", 18100, "2-15",
  "marathon training plan; marathon training guide; how to run marathon (same pool); marathon distance is a separate answer pool",
  "Marathon plan page", (5, 5, 5, 3, 3, 5), 5,
  "Opportunity cut to 3 after the backlink baseline (Orka 29 referring domains vs 2,300-3,800 for competitors). Top: Hal Higdon, Nike, ASICS PDF, St Jude, Running Clinic, GU, Cancer Research UK. Mid-SERP is PDFs and charity pages; no India page."),
 ("K02", "Core plan", "10K training plan pool", "10k training plan", 1900, "0",
  "training schedule 10k; training program 10k (same pool)", "10K plan page", (5, 3, 5, 3, 3, 4), 5,
  "Hal Higdon, charity PDFs, Nike, Strava, Decathlon Coach."),
 ("K03", "Core plan", "Half marathon training plan pool", "half marathon training plan", 1600, "10",
  "half marathon training schedule 320; running plan half marathon 320 (separate pools, under gate)", "Half marathon plan page", (5, 3, 5, 3, 3, 5), 5,
  "Women's Running, On, PureGym, Runna, charity PDFs."),
 ("K04", "Core plan", "5K training plan pool", "5k training plan", 1000, "14",
  "training schedule 5k; training plan 5k; 5km training plan (same pool)", "5K plan page", (5, 2, 5, 3, 3, 4), 5,
  "Mottiv, Runner's World, Under Armour, PDFs. Volume exactly at the gate."),
 ("K05", "Core plan", "Couch to 5K plans", "couch to 5k training plans", 1300, "25",
  "couch to 5k 1,000 (KD 33)", "Couch to 5K plan page", (5, 3, 5, 2, 3, 4), 5,
  "NHS and c25k own it; Nike, ASICS, a Hyderabad Runners PDF also rank."),
 ("K06", "Training concept", "How to run faster / be a fast runner", "how to run faster", 5400, "0-14",
  "how to be a fast runner 5,400; run fast 2,900", "Guide", (4, 5, 4, 4, 4, 3), 5,
  "Video-heavy, thin written pages (checked earlier)."),
 ("K07", "Training concept", "Build running endurance / stamina", "how to build running endurance", 3600, "10-23",
  "how to gain endurance in running 3,600", "Guide", (4, 4, 4, 4, 4, 3), 5,
  "Peloton, strengthrunning, Gymshark, small blogs (checked earlier)."),
 ("K08", "Training concept", "Intervals and tempo runs", "tempo run", 1900, "17",
  "interval training running 1,600 (KD 15); intervals workout 1,600", "Guide", (4, 3, 4, 4, 4, 3), 5,
  "YouTube, Peloton, Under Armour, Running Warehouse, Reddit, a dictionary page. Weak."),
 ("K09", "Training concept", "Strength training for runners", "strength workout for runners", 1000, "8-13",
  "running and strength training 1,000; strength training for hips 1,300", "Guide", (4, 2, 4, 3, 3, 3), 5,
  "HSS, The Body Coach, YouTube, PureGym, REI, Hydrow."),
 ("K10", "Training concept", "How to start running", "how to start running", 1300, "18",
  "running how to 1,300", "Beginner guide", (4, 3, 4, 2, 3, 4), 5,
  "REI, Runner's World UK, NONE TO RUN, Reddit, adidas India, Hal Higdon, Nike (checked earlier)."),
 ("K11", "Training concept", "Warm up before running", "warm up before running", 1900, "12",
  "warming up before running 1,900", "Guide", (3, 3, 4, 3, 3, 2), 5,
  "YouTube, On, Brooks, TrainingPeaks."),
 ("K12", "Training concept", "Average 10K and 5K times (what is a good time)", "average 10k time", 1300, "3-13",
  "5k running time 1,600; time to run 5km 1,600; average time for 10km run 1,300", "Answer page + calculator", (3, 3, 3, 3, 3, 2), 5,
  "220 Triathlon, tri247, Men's Health, The Running Channel, Quora, Wikipedia."),
 ("K13", "Tool", "Pace calculators", "pace calculator", 8100, "33",
  "running pace calculator 1,900 (KD 34); marathon pace calculator 390 (under gate)", "Calculator page", (4, 4, 5, 2, 3, 3), 5,
  "calculator.net, Active, Strava, McMillan, goandrace (checked earlier)."),
 ("K14", "Tool", "Heart rate zones and zone 2", "zone 2 running", 1300, "10",
  "heart rate zone calculator 320 (under gate)", "Calculator + guide", (4, 3, 4, 4, 4, 3), 4,
  "Tiny tool sites and blogs (checked earlier)."),
 ("K15", "App", "Running apps (running app, best running app, tracker app)", "running app", 4400, "19-47",
  "best running app 1,000 (KD 19); running tracker app 1,000 (KD 47); training apps 1,000 (KD 69)", "App comparison page", (5, 4, 3, 2, 3, 4), 5,
  "Reddit, Play Store, runstreet, bhaagoindia (2022), weeviews, Strava. No current India-focused roundup."),
 ("K16", "App", "Strava running app and runner app (brand confusion)", "strava running app", 3600, "53-69",
  "runner app / runners app 4,400 (likely Runna searches)", "Not a target", (3, 4, 2, 1, 1, 2), 4,
  "Dominated by Strava and Runna."),
 ("K17", "Coach", "Running coach and coach near me", "running coach", 590, "0",
  "running coach near me 590; run coach near me 590", "Coach landing (below gate)", (5, 1, 3, 4, 4, 4), 5,
  "Local pack (TRYSquad, Run&Ride2Fit, runpundit), directories, YouTube, personal sites. Easy but under the gate."),
 ("K18", "Coach", "Run clubs near me", "run club near me", 1300, "n/a",
  "running group near me", "Not a fit", (2, 3, 1, 4, 2, 1), 5,
  "Local pack and directories (Hyderabad Runners, bengalururunners, Endorfin). Needs physical clubs."),
 ("K19", "Adjacent (race events)", "India city marathons (Bengaluru, Delhi, Pune, Chennai, Hyderabad, Kolkata, Ahmedabad, Mumbai)", "bengaluru marathon", 8100, "0-6",
  "delhi half marathon 9,900; pune marathon 8,100; mumbai marathon 8,100; chennai 6,600; tata mumbai 5,400; hyderabad 4,400; kolkata 3,600; ahmedabad 2,400", "Race pages", (3, 5, 2, 5, 5, 3), 5,
  "Aggregators, official sites, Facebook; no training content (checked earlier)."),
 ("K20", "Adjacent (race events)", "India race calendar", "marathons in india", 1900, "22",
  "upcoming marathons in india 1,000", "Calendar hub", (3, 4, 3, 3, 4, 3), 5,
  "ifinish, indiarunning, runindia, ahotu (checked earlier)."),
 ("K21", "Off-core", "Distance facts (marathon and half marathon distance)", "half marathon distance", 9900, "1-10",
  "marathon distance 8,100; marathon length km 2,400", "Answer queries", (3, 5, 2, 3, 2, 2), 3,
  "Fact questions; SERP not read; likely answered in the snippet."),
 ("K22", "Off-core", "Running shoes and gear", "best running shoes", 22200, "15",
  "best running shoes for men 60,500; best running machine 1,900", "Not a fit", (2, 5, 3, 1, 1, 2), 5,
  "Retailers and brands; high advertiser competition."),
 ("K23", "Positioning", "AI and adaptive coaching terms", "ai running coach", 10, "n/a",
  "strava alternative 90; running coach app 70", "Positioning page (below gate)", (5, 1, 4, 3, 3, 4), 5,
  "Small AI-coach sites publish comparisons."),
]

W = {"base": (.20, .15, .10, .15, .20, .20),
     "demand_heavy": (.15, .30, .10, .15, .15, .15),
     "ease_heavy": (.15, .10, .10, .25, .25, .15),
     "business_heavy": (.30, .10, .15, .10, .10, .25)}


def sc(s, w):
    return sum(a * b for a, b in zip(s, w))


rows = [(c, {k: round(sc(c[8], w), 2) for k, w in W.items()}) for c in C]
ranks = {}
for k in W:
    for i, (c, r) in enumerate(sorted(rows, key=lambda x: -x[1][k]), 1):
        ranks.setdefault(c[0], {})[k] = i


def tier(s):
    return 1 if s >= 4.0 else 2 if s >= 3.5 else 3 if s >= 3.0 else 4


with open("outputs/keyword_clusters_scored_v3.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["cluster_id", "fit", "cluster", "primary_keyword", "pool_volume_IN", "KD", "other_pools", "page_type",
                "relevance", "demand", "intent_fit", "competition_ease", "ranking_opportunity", "business_value",
                "score", "confidence", "tier", "volume_gate_1000", "rank_range_4_weightings", "serp_evidence"])
    for c, r in sorted(rows, key=lambda x: -x[1]["base"]):
        v = list(ranks[c[0]].values())
        w.writerow([c[0], c[1], c[2], c[3], c[4], c[5], c[6], c[7], *c[8], r["base"], c[9], tier(r["base"]),
                    "pass" if c[4] >= 1000 else "fail", f"{min(v)}-{max(v)}", c[10]])

for c, r in sorted(rows, key=lambda x: -x[1]["base"]):
    v = list(ranks[c[0]].values())
    print(c[0], "%.2f" % r["base"], "T%d" % tier(r["base"]), "gate", "pass" if c[4] >= 1000 else "FAIL", "%d-%d" % (min(v), max(v)), "|", c[1], "|", c[2][:46], "|", c[4])
