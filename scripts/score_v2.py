"""Rescore v2: training-plan keywords are the core; race-event keywords are adjacent.
Volumes: OpenSEO/DataForSEO India English, pulled 2026-10-21 (first set + re-seed set).
Scores 1-5: relevance (fit to a running/marathon training-plan product), demand, intent_fit, competition_ease
(5 = easy), ranking_opportunity, business_value. Confidence is separate (5 = volume measured and SERPs read).
"""
import csv, os

os.makedirs("outputs", exist_ok=True)

# id, fit, name, primary kw, vol, kd, secondary (with volume), page type, scores, confidence, evidence
C = [
 ("C05", "Core plan", "Marathon training plan (head term and variants)", "marathon training plan", 18100, 10,
  "how to run a marathon 18100 (KD32); marathon training schedule 210 (KD52); how to train marathon 320; beginner marathon training plan 210 (KD71); marathon training plan pdf 210; marathon training tips 110",
  "Marathon plan hub + beginner section", (5, 5, 5, 2, 3, 5), 5,
  "Hal Higdon, Nike, Runner's World, HOKA, GU rank; On India has one India page. India angle (km, heat, working week) is the opening."),
 ("C07", "Core plan", "10K, 5K and Couch to 5K plans", "10k training plan", 1900, 0,
  "10k training schedule 1900; 5k training plan 1000; couch to 5k 1000; running plan beginner 480; running schedule for beginners 480; running training plan 5k 260; how to train for a 5k 260",
  "Plan pages (10K, 5K)", (5, 4, 5, 3, 3, 4), 5,
  "NHS and c25k own Couch to 5K; Mottiv, Runner's World, Decathlon Coach rank for plans; Reddit ranks for beginner plan."),
 ("C06", "Core plan", "Half marathon plans and schedules", "half marathon training plan", 1600, 10,
  "half marathon training schedule 320; running plan half marathon 320; running schedule half marathon 210; half marathon training schedule for beginners 320",
  "Half marathon plan page", (5, 3, 5, 2, 3, 5), 5,
  "Injinji, Mottiv, Team RWB, On, PureGym, Runna."),
 ("C04", "Core plan", "Race-specific and India-city training plans", "marathon training in mumbai", 70, None,
  "marathon training in bangalore 70; marathon training plan india (no volume); half marathon training plan india (no volume)",
  "Plan sections on race pages", (5, 1, 5, 5, 4, 5), 4,
  "Volume measured and tiny (70 each). SERP checks found no real week-by-week plan for Mumbai/Delhi/Bengaluru, so little competition, but little demand."),
 ("C24", "Core plan", "Weight-loss running plans", "running plan weight loss", 140, 15,
  "running program weight loss 140; running for fat loss plan 140; running plan lose weight 140 (KD72); running for weight loss 1000",
  "One plan page", (3, 2, 5, 4, 3, 2), 5,
  "Small, easy keywords; McMillan, Mottiv, TrainingPeaks rank. Off the core marathon audience."),
 ("C08", "Core plan", "Goal-time plans (sub 4, sub 2, sub 50, sub 20 5K)", "sub 4 marathon", 50, None,
  "sub 2 hour half marathon training plan 30; sub 20 5k training plan 30; sub 30 5k 170; sub 2 hour half marathon 70",
  "Goal-time sections in plan pages", (5, 1, 5, 4, 4, 4), 5,
  "Measured volume is tiny; fit as sections of the main plan pages."),
 ("C23", "Core plan", "Plan variants: levels and week lengths", "16 week marathon training plan", 40, None,
  "12 week marathon training plan 30; advanced marathon training plan 30; 20 week marathon training plan 20; intermediate marathon training plan 10",
  "Sections inside plan pages", (5, 1, 5, 4, 3, 3), 5,
  "Autocomplete shows hundreds of these phrases, but each is 10-40 searches a month."),
 ("C22", "Core plan", "Odd distances and ultra plans (8k, 15k, 10 mile, 50k)", "ultra marathon training plan", 70, None,
  "50k training plan 20; 10 mile training plan 20; 8k training plan 10; 15k training plan 0",
  "Skip as pages", (4, 1, 5, 4, 3, 2), 5,
  "Competitors cover them (Hal Higdon, Mottiv, TrainingPeaks) but India volume is negligible."),
 ("C09", "Tool", "Pace calculators", "pace calculator", 8100, 33,
  "running pace calculator 2400 (KD34); pace calculator marathon 390 (KD47); half marathon pace calculator 90; 5k/10k pace chart 70",
  "Calculator page", (4, 4, 5, 2, 3, 3), 5,
  "calculator.net, Active, Strava, McMillan. High competition for the head term."),
 ("C10", "Tool", "Marathon pace calculator and pace charts", "marathon pace calculator", 390, 0,
  "marathon pace chart km 110; half marathon pace chart 140; marathon time calculator 70",
  "Calculator page (km)", (5, 2, 5, 3, 4, 3), 5,
  "Small sites rank (goandrace, marathonballot, runhive, geeksonfeet)."),
 ("C12", "Tool", "Heart rate zones and zone 2", "zone 2 running", 1300, 10,
  "heart rate zone calculator 320; zone 2 heart rate calculator 210; max heart rate calculator 320 (KD73)",
  "Calculator + guide", (4, 3, 4, 4, 4, 3), 4,
  "Tiny tool sites and blogs rank for the calculator; zone 2 is blog-level."),
 ("C11", "Tool", "Race and marathon time predictor", "marathon time predictor", 30, None,
  "race time predictor 40; half marathon time calculator 30",
  "Existing predictor page", (5, 1, 5, 3, 3, 3), 4,
  "Tiny volume. Fetcheveryone, marathonguide, runcalcs rank."),
 ("C18", "Tool", "Marathon fueling and running nutrition", "running nutrition", 1000, 30,
  "running nutrition plan 170; marathon nutrition 20; half marathon fueling 10",
  "Calculator + guide", (3, 2, 4, 3, 3, 3), 4,
  "Head term has high advertiser competition; marathon-specific terms tiny."),
 ("C19", "Tool", "Race readiness", "am i ready for a marathon", None, None,
  "how long to train for a marathon 20; marathon readiness test (no volume)",
  "Existing quiz page", (5, 1, 4, 4, 3, 3), 4,
  "No volume returned for the main readiness queries."),
 ("C13", "Guide", "How to run faster, build endurance, start running", "how to run faster", 5400, 0,
  "how to build running endurance 3600; how to start running 2400; how to improve running stamina 480; running for beginners 320",
  "Blog guides", (3, 5, 4, 3, 3, 3), 5,
  "Video-heavy, thin written pages for faster/endurance/stamina. REI, Runner's World, Nike for start running."),
 ("C16", "Guide", "Missed training, taper and adaptive plans", "what to do if you miss a run", None, None,
  "missed long run marathon training (no volume); marathon training missed week (no volume); half marathon taper 10",
  "Blog guide", (5, 1, 4, 4, 4, 3), 4,
  "Main missed-training queries returned no volume; it is a product differentiator, not a traffic keyword."),
 ("C21", "Guide", "Running for weight loss (general)", "running for weight loss", 1000, 19,
  "-", "Blog guide", (2, 3, 3, 3, 3, 2), 4, "McMillan, Mottiv, YouTube; off-core audience."),
 ("C17", "Guide", "HRV for runners", "what is hrv", 2900, 45,
  "hrv running 10; resting heart rate running 30; running recovery 260",
  "Blog guide", (3, 3, 2, 1, 2, 2), 4,
  "Head term is medical-authority territory; runner-specific terms are tiny."),
 ("C14", "App / positioning", "Running apps (head terms, India)", "running app", 4400, 34,
  "best running app 1000; nike run club 1300; runkeeper 590; running training apps 90; best running training app 40",
  "App comparison page", (4, 4, 3, 1, 2, 4), 5,
  "Strava, Play/App Store, Runkeeper dominate. Only one India listicle (thehigh5tribe)."),
 ("C15", "App / positioning", "AI / adaptive coaching and app alternatives", "ai running coach", 10, None,
  "strava alternative 90 (KD50); running coach app 70; garmin coach 70; ai running plan 10; best running coach app 10 (KD64)",
  "Positioning landing + comparisons", (5, 1, 4, 3, 3, 4), 5,
  "Low volume today; small AI-coach sites publish comparison posts. Brand positioning, not traffic."),
 ("C01", "Adjacent (race events)", "India city marathons (Delhi HM, Bengaluru, Pune, Chennai, Hyderabad, Kolkata, Ahmedabad)", "delhi half marathon", 9900, 0,
  "bengaluru marathon 8100; pune marathon 8100; chennai marathon 6600; hyderabad marathon 4400; kolkata marathon 3600; ahmedabad marathon 2400",
  "Race page + city hub", (3, 5, 2, 5, 5, 3), 5,
  "Event-information intent. Aggregators, Facebook/Instagram, AIMS, stale pages rank; no training content."),
 ("C02", "Adjacent (race events)", "Mumbai marathon family (Tata Mumbai Marathon, 2027)", "mumbai marathon", 8100, 6,
  "tata mumbai marathon 5400; mumbai marathon 2027 1000; mumbai marathon registration 170",
  "Race page", (3, 5, 2, 3, 4, 3), 5,
  "Official site plus BookMyShow, worldsmarathons, ahotu; no training content."),
 ("C03", "Adjacent (race events)", "India race calendar and lists", "marathons in india", 1900, 22,
  "upcoming marathons in india 1000; marathon calendar india 210; half marathon india 210",
  "Calendar hub", (3, 4, 3, 3, 4, 3), 5,
  "ifinish, indiarunning, runindia, ahotu rank; one stale Olympics.com page."),
 ("C20", "Off-core", "Running shoes", "best running shoes", 22200, 15,
  "best running shoes for men 60500; nike running shoes 60500; asics running shoes 40500; best running shoes india 4400",
  "Shoe finder tool", (2, 5, 3, 1, 1, 2), 5,
  "High advertiser competition; retailers and brands rank. Weak fit for a plan product."),
]

W = {
    "base": (.20, .15, .10, .15, .20, .20),
    "demand_heavy": (.15, .30, .10, .15, .15, .15),
    "ease_heavy": (.15, .10, .10, .25, .25, .15),
    "business_heavy": (.30, .10, .15, .10, .10, .25),
}


def sc(s, w):
    return sum(a * b for a, b in zip(s, w))


rows = [(c, {k: round(sc(c[8], w), 2) for k, w in W.items()}) for c in C]
ranks = {}
for k in W:
    for i, (c, r) in enumerate(sorted(rows, key=lambda x: -x[1][k]), 1):
        ranks.setdefault(c[0], {})[k] = i


def tier(s):
    return 1 if s >= 4.0 else 2 if s >= 3.5 else 3 if s >= 3.0 else 4


with open("outputs/keyword_clusters_scored_v2.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["cluster_id", "fit", "cluster", "primary_keyword", "primary_volume_IN", "KD", "secondary_keywords_volume",
                "page_type", "relevance", "demand", "intent_fit", "competition_ease", "ranking_opportunity",
                "business_value", "opportunity_score", "confidence", "traffic_target", "rank_base", "rank_demand_heavy",
                "rank_ease_heavy", "rank_business_heavy", "rank_range", "tier", "evidence"])
    for c, r in sorted(rows, key=lambda x: -x[1]["base"]):
        rk = ranks[c[0]]
        v = list(rk.values())
        w.writerow([c[0], c[1], c[2], c[3], c[4] if c[4] is not None else "unknown", c[5] if c[5] is not None else "n/a",
                    c[6], c[7], *c[8], r["base"], c[9], ("yes" if c[8][1] >= 2 and c[1] != "Off-core" else "no: section or differentiator, measured volume under 100" if c[8][1] <= 1 else "no"), rk["base"], rk["demand_heavy"], rk["ease_heavy"],
                    rk["business_heavy"], f"{min(v)}-{max(v)}", tier(r["base"]), c[10]])

for c, r in sorted(rows, key=lambda x: -x[1]["base"]):
    print(c[0], "%.2f" % r["base"], "T%d" % tier(r["base"]), list(ranks[c[0]].values()), "conf", c[9], "|", c[1], "|", c[2][:48])
