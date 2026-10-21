import csv, os

os.makedirs("outputs", exist_ok=True)

# (id, name, primary keyword, primary vol, kd, secondary keywords with volume, intent, page type,
#  (relevance, demand, intent_fit, competition_ease, ranking_opportunity, business_value), confidence, evidence)
C = [
 ("C01", "India city marathons (Delhi HM, Bengaluru, Pune, Chennai, Hyderabad, Kolkata, Ahmedabad)", "delhi half marathon", 9900, 0,
  "bengaluru marathon 8100; pune marathon 8100; chennai marathon 6600; hyderabad marathon 4400; kolkata marathon 3600; ahmedabad marathon 2400; delhi half marathon 2026 1300; bengaluru marathon 2026 1000",
  "Informational (event info, registration)", "Race page + city hub", (4, 5, 3, 5, 5, 4), 4,
  "SERPs: aggregators, Facebook/Instagram, AIMS, stale pages; no training content. Orka catalog lacks these marquee races."),
 ("C02", "Mumbai marathon family (Tata Mumbai Marathon, 2027)", "mumbai marathon", 8100, 6,
  "tata mumbai marathon 5400; mumbai marathon 2027 1000; mumbai marathon registration 170",
  "Informational / transactional", "Race page + training guide", (4, 5, 3, 3, 4, 4), 4,
  "Official site plus BookMyShow, worldsmarathons, ahotu; no training content."),
 ("C03", "India race calendar and lists", "marathons in india", 1900, 22,
  "upcoming marathons in india 1000; marathon calendar india 210; half marathon india 210",
  "Informational (list)", "Calendar hub", (4, 4, 4, 3, 4, 4), 4,
  "ifinish, indiarunning, runindia, ahotu rank; one stale Olympics.com page."),
 ("C04", "Race-specific training plans (India)", "mumbai marathon training plan", None, None,
  "half marathon training plan india; marathon training plan india; marathon training plan in km 20",
  "Informational / plan", "Race-linked plan pages", (5, 2, 5, 5, 5, 5), 2,
  "Volume not returned by OpenSEO (below threshold or unavailable). SERP checks found no real week-by-week plan for Mumbai/Delhi/Bengaluru. Needs validation."),
 ("C05", "Marathon training plan (general and beginners)", "marathon training plan", 18100, 10,
  "marathon training plan for beginners 210 (KD71); marathon training plan pdf 210; how to prepare for a marathon 320; how to train for a marathon 320",
  "Informational / plan", "Plan hub + beginner plan", (5, 5, 5, 2, 3, 5), 4,
  "Hal Higdon, Nike, Runner's World, HOKA, GU; On India has an India page. India angle (km, heat) is the opening."),
 ("C06", "Half marathon training plans", "half marathon training plan", 1600, 10,
  "half marathon training plan for beginners 320; how to train for a half marathon 170; half marathon training plan 12 weeks 50",
  "Informational / plan", "Plan page", (5, 3, 5, 2, 3, 5), 4,
  "Injinji, Mottiv, Team RWB, On, PureGym, Runna."),
 ("C07", "10K and 5K plans, Couch to 5K", "10k training plan", 1900, 0,
  "5k training plan 1000; couch to 5k 1000; couch to 5k app 480; 10k training plan for beginners 110; running plan for beginners 480",
  "Informational / plan", "Plan pages", (4, 3, 5, 2, 3, 4), 4,
  "NHS and c25k own Couch to 5K; Mottiv, Runner's World, Decathlon Coach; Reddit ranks for beginner plan."),
 ("C08", "Goal-time plans (sub 4, sub 2, sub 50)", "sub 2 hour half marathon", 70, None,
  "sub 30 5k 170; sub 60 10k 40; sub 50 10k 20",
  "Informational / plan", "Goal-time plan pages", (5, 1, 5, 4, 4, 4), 3,
  "Low measured volume; sub-4 marathon queries were not returned by OpenSEO. Autocomplete shows many goal-time variants that fit Orka's goal-pace plans."),
 ("C09", "Pace calculators", "pace calculator", 8100, 33,
  "running pace calculator 2400 (KD34); half marathon pace calculator 90; 5k pace chart 70; 10k pace chart 70; running pace chart km 50",
  "Informational (tool)", "Calculator page", (4, 4, 5, 2, 3, 3), 4,
  "calculator.net, Active, Strava, McMillan. High competition for the head term."),
 ("C10", "Marathon pace calculator and pace charts", "marathon pace calculator", 390, 0,
  "marathon pace chart km 110; half marathon pace chart 140; marathon time calculator 70",
  "Informational (tool)", "Calculator page (km)", (5, 2, 5, 3, 4, 3), 4,
  "Small sites rank (goandrace, marathonballot, runhive, geeksonfeet)."),
 ("C11", "Race and marathon time predictor", "marathon time predictor", 30, None,
  "race time predictor 40; half marathon time calculator 30; marathon predictor 10; race predictor calculator 10",
  "Informational (tool)", "Existing predictor page", (5, 1, 5, 3, 3, 3), 3,
  "Tiny volume. Fetcheveryone, marathonguide, runcalcs rank. Existing tool at /tracker/marathon-time-predictor."),
 ("C12", "Heart rate zones and zone 2", "zone 2 running", 1300, 10,
  "heart rate zone calculator 320; zone 2 heart rate calculator 210; max heart rate calculator 320 (KD73); heart rate zones running 110",
  "Informational (tool / guide)", "Calculator + guide", (4, 3, 4, 4, 4, 3), 3,
  "Tiny tool sites and blogs rank for the calculator; zone 2 is blog-level (Juniper, Peloton)."),
 ("C13", "How to run faster, build endurance, start running", "how to run faster", 5400, 0,
  "how to build running endurance 3600; how to start running 2400; how to improve running stamina 480; running for beginners 320",
  "Informational (guide)", "Blog guides", (3, 5, 4, 3, 3, 3), 4,
  "Video-heavy, thin written pages for faster/endurance/stamina. REI, Runner's World, Nike for start running."),
 ("C14", "Running apps (head terms, India)", "running app", 4400, 34,
  "best running app 1000; nike run club 1300; runkeeper 590; running training app 70; couch to 5k app 480",
  "Commercial / navigational", "App comparison page", (5, 4, 3, 1, 2, 4), 4,
  "Strava, Play/App Store, Runkeeper dominate. Only one India listicle (thehigh5tribe)."),
 ("C15", "AI / adaptive coaching and app alternatives", "ai running coach", 10, None,
  "strava alternative 90 (KD50); running coach app 70; garmin coach 70; runna app review 30; nike run club alternative 10; ai running coach app 10; free running coach app 10",
  "Commercial", "Positioning landing + comparisons", (5, 1, 4, 3, 3, 4), 4,
  "Low volume today; small AI-coach sites publish comparison posts. Brand positioning, not traffic."),
 ("C16", "Missed training, taper and adaptive plans", "what to do if you miss a run in marathon training", None, None,
  "missed marathon training; how to taper for a marathon; half marathon taper 10",
  "Informational (guide)", "Blog guide", (5, 1, 4, 4, 4, 3), 2,
  "Volume not measured in OpenSEO; web-search SERPs show RunnersConnect, Running Channel, Human Kinetics. Needs validation."),
 ("C17", "HRV for runners", "what is hrv", 2900, 45,
  "hrv running 10; resting heart rate running 30; running recovery 260; overtraining running 10",
  "Informational (guide)", "Blog guide", (4, 3, 2, 1, 2, 2), 3,
  "Head term is medical-authority territory; runner-specific terms are tiny."),
 ("C18", "Marathon fueling and running nutrition", "running nutrition", 1000, 30,
  "marathon nutrition 20; half marathon fueling 10; how many gels for a marathon 10",
  "Informational (tool / guide)", "Calculator + guide", (4, 2, 4, 3, 3, 3), 3,
  "Head term has high advertiser competition; marathon-specific terms tiny. Existing fueling calculator."),
 ("C19", "Race readiness", "am i ready for a marathon", None, None,
  "how long to train for a marathon 20; first marathon 90; first half marathon 30",
  "Informational (quiz / guide)", "Existing quiz page", (5, 1, 4, 4, 3, 3), 2,
  "Volume not returned. Active and NIFS checklists rank. Existing quiz at /tracker/race-readiness-quiz."),
 ("C20", "Running shoes", "best running shoes", 22200, 15,
  "best running shoes for men 60500; nike running shoes 60500; asics running shoes 40500; best running shoes india 4400; best running shoes for beginners 590; running shoe finder 20",
  "Commercial / transactional", "Shoe finder tool", (2, 5, 3, 1, 1, 2), 4,
  "High advertiser competition; retailers and brands rank. Weak fit for Orka."),
 ("C21", "Running for weight loss", "running for weight loss", 1000, 19,
  "-", "Informational (guide)", "Blog guide", (2, 3, 3, 3, 3, 2), 3,
  "McMillan, Mottiv, YouTube; off-core audience."),
]

# weights: relevance, demand, intent_fit, competition_ease, ranking_opportunity, business_value
W = {
    "base": (.20, .15, .10, .15, .20, .20),
    "demand_heavy": (.15, .30, .10, .15, .15, .15),
    "ease_heavy": (.15, .10, .10, .25, .25, .15),
    "business_heavy": (.30, .10, .15, .10, .10, .25),
}


def score(s, w):
    return sum(a * b for a, b in zip(s, w))


rows = [(c, {k: round(score(c[8], w), 2) for k, w in W.items()}) for c in C]
ranks = {}
for k in W:
    for i, (c, r) in enumerate(sorted(rows, key=lambda x: -x[1][k]), 1):
        ranks.setdefault(c[0], {})[k] = i


def tier(s):
    return 1 if s >= 4.0 else 2 if s >= 3.5 else 3 if s >= 3.0 else 4


with open("outputs/keyword_clusters_scored.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["cluster_id", "cluster", "primary_keyword", "primary_volume_IN", "KD", "secondary_keywords_volume",
                "intent", "page_type", "relevance", "demand", "intent_fit", "competition_ease",
                "ranking_opportunity", "business_value", "opportunity_score_base", "confidence",
                "rank_base", "rank_demand_heavy", "rank_ease_heavy", "rank_business_heavy", "rank_range", "tier",
                "evidence"])
    for c, r in sorted(rows, key=lambda x: -x[1]["base"]):
        rk = ranks[c[0]]
        v = list(rk.values())
        w.writerow([c[0], c[1], c[2], c[3] if c[3] is not None else "unknown", c[4] if c[4] is not None else "n/a",
                    c[5], c[6], c[7], *c[8], r["base"], c[9], rk["base"], rk["demand_heavy"], rk["ease_heavy"],
                    rk["business_heavy"], f"{min(v)}-{max(v)}", tier(r["base"]), c[10]])

for c, r in sorted(rows, key=lambda x: -x[1]["base"]):
    print(c[0], r["base"], "T%d" % tier(r["base"]), "ranks", list(ranks[c[0]].values()), "conf", c[9], c[1][:45])
