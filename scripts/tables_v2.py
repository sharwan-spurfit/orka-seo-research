import csv, os

os.makedirs("outputs", exist_ok=True)


def save(name, header, rows):
    with open("outputs/" + name, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


# Searches/month are India, English (OpenSEO/DataForSEO, 21 Oct 2026). KD = keyword difficulty.
URL_MAP = [
 ["Core plan", "/training-plans/marathon", "New", "marathon training plan (18,100; KD 10)",
  "marathon training plans and marathon prep schedule (same 18,100 pool); how to train marathon 320; marathon training schedule 210 (KD 52); beginner marathon training plan 210 (KD 71); marathon training plan pdf 210; marathon training tips 110; how to start marathon training 70; marathon training plan km 20",
  "Levels (beginner to advanced), 12/16/20-week variants, km paces, India heat and air quality, run-walk start, sub-4 goal, missed-week rule, taper, FAQ",
  "Hal Higdon, Nike, Runner's World, HOKA. The 'marathon training schedule' results are weak (Pinterest, Scribd, hubpages, a small India calculator).", "Flagship page"],
 ["Core plan", "/blog/how-to-run-a-marathon", "New guide (decide after drafting the plan page)", "how to run a marathon (18,100; KD 32, shares the pool with the plan page)",
  "how to run a half marathon 30", "First-timer guide: readiness, race week, pacing, fueling", "Weak results: GQ gallery, Reddit, Medium, RunnersConnect, a university PDF", "Guide; link to the plan page"],
 ["Core plan", "/training-plans/half-marathon", "New", "half marathon training plan (1,600; KD 10)",
  "half marathon training schedule 320; running plan half marathon 320; running schedule half marathon 210; half marathon training schedule for beginners 320; how to train for a half marathon 170 (KD 60)",
  "12-week beginner plan, sub-2 goal, taper", "Women's Running, On, PureGym, Runna, charity PDFs", "Plan page"],
 ["Core plan", "/training-plans/10k", "New", "10k training plan (1,900; KD 0)",
  "10k training schedule 1,900; beginner 10k training plan 110; running plan for 10k 30; running training plan 10k 30; 8 week 10k training plan 20",
  "8-week plan, sub-50 goal, progression from 5K", "Hal Higdon, charity PDFs, Nike, Strava, Decathlon Coach", "Plan page"],
 ["Core plan", "/training-plans/5k", "New", "5k training plan (1,000; KD 14)",
  "running training plan 5k 260; how to train for a 5k 260; running plan for 5k 210; sub 20 5k training plan 30",
  "6-8 week plan, sub-30 and sub-20 goals", "Mottiv, Runner's World, Under Armour, PDFs", "Plan page"],
 ["Core plan", "/training-plans", "New hub", "running training plans (260; KD 30)",
  "running plan beginner 480 (KD 15); running schedule for beginners 480 (KD 15); running training schedule 260; running exercise plan 210. Skip 'running plan' (170; KD 91) and 'running program' (320; KD 75)",
  "Chooser for distance and level; run-walk start for new runners", "Hal Higdon, Strava, Runner's World, Nike", "Hub for all plan pages"],
 ["Core plan (wave 2)", "/training-plans/couch-to-5k", "New", "couch to 5k (1,000; KD 33)",
  "couch to 10k training plan 40; how to learn to run 20; learn to run schedule 10", "Run-walk plan for absolute beginners", "NHS and c25k own the head term; competitive", "Plan page"],
 ["Tool (wave 2)", "/tools/marathon-pace-calculator", "New", "marathon pace calculator (390; KD 0)",
  "pace calculator marathon 390 (KD 47); half marathon pace chart 140; marathon pace chart km 110", "Km-first pace, splits, pace chart", "Small tool sites rank (goandrace, marathonballot, runhive)", "Tool; link to plan pages"],
 ["Tool (wave 2)", "/tools/heart-rate-zone-calculator + /blog/zone-2-running", "New", "zone 2 running (1,300; KD 10)",
  "heart rate zone calculator 320 (KD 26); zone 2 heart rate calculator 210", "Karvonen zones, zone 2 range, how to use them in a plan", "Tiny tool sites and blogs rank", "Tool + guide"],
 ["Guide (wave 3)", "/blog/how-to-run-faster, /blog/build-running-endurance, /blog/how-to-start-running", "New", "how to run faster (5,400; KD 0)",
  "how to build running endurance 3,600 (KD 23); how to start running 2,400 (KD 18); how to improve running stamina 480", "Written guides with a sample week", "Video-heavy and thin written results", "Guides; link to plan pages"],
 ["Core plan (wave 3)", "/training-plans/weight-loss", "New", "running plan weight loss (140; KD 15)",
  "running program weight loss 140; running for fat loss plan 140", "Beginner plan with weight-loss framing", "McMillan, Mottiv, TrainingPeaks", "Small page"],
 ["Tool (wave 3)", "/tools/pace-calculator", "New", "pace calculator (8,100; KD 33)", "running pace calculator 2,400 (KD 34)", "Km-first, India-friendly", "calculator.net, Active, Strava, McMillan", "Tool; competitive"],
 ["Existing", "/tracker/marathon-time-predictor", "Optimise", "marathon time predictor (30)", "race time predictor 40", "Link into plan pages", "Tiny volume", "Keep as an asset"],
 ["Existing", "/tracker/marathon-fueling-hydration-calculator", "Optimise", "running nutrition (1,000; KD 30)", "marathon nutrition 20", "Link from the marathon plan", "High advertiser competition", "Keep"],
 ["Existing", "/tracker/race-readiness-quiz", "Optimise", "am i ready for a marathon (no volume)", "-", "Link from plan pages", "No volume returned", "Keep"],
 ["Positioning", "/ai-running-coach + /compare/*", "New (brand, not traffic)", "ai running coach (10)",
  "strava alternative 90 (KD 50); running coach app 70; best running coach app 10 (KD 64)", "Honest comparison of adaptive-plan approaches", "Small AI-coach sites publish comparisons", "Conversion page"],
 ["Positioning (later)", "/blog/best-running-apps-india", "New", "running app (4,400; KD 34)", "best running app 1,000; nike run club 1,300", "India-focused roundup", "Strava and big apps dominate", "Low priority"],
 ["Adjacent: race events", "/races/[slug] for Delhi HM, Bengaluru, Pune, Chennai, Hyderabad, Kolkata, Ahmedabad, Tata Mumbai", "New pages (catalog lacks these races)", "delhi half marathon (9,900; KD 0)",
  "bengaluru marathon 8,100; pune marathon 8,100; mumbai marathon 8,100; chennai marathon 6,600; tata mumbai marathon 5,400; hyderabad marathon 4,400; kolkata marathon 3,600; ahmedabad marathon 2,400",
  "Date, distances, course, registration link, heat advice, link to the matching training plan", "Aggregators, Facebook/Instagram, AIMS, stale pages; no training content", "Event-information intent"],
 ["Adjacent: race events", "/races/india", "New hub", "marathons in india (1,900; KD 22)", "upcoming marathons in india 1,000; marathon calendar india 210; half marathon india 210",
  "Filter by month and distance; links to every India race", "ifinish, indiarunning, runindia, ahotu", "Hub"],
 ["Training concept (wave 3)", "/blog/tempo-runs-and-intervals", "New", "tempo run (1,900; KD 17)", "interval training running 1,600 (KD 15); intervals workout 1,600", "How and why, with a sample session in a plan week", "YouTube, Peloton, Under Armour, Running Warehouse; weak", "Guide; link to plan pages"],
 ["Training concept (wave 3)", "/blog/build-running-endurance", "New (already listed)", "how to build running endurance (3,600; KD 10-23)", "how to gain endurance in running 3,600", "Written guide with a sample week", "Peloton, strengthrunning, small blogs", "Guide"],
 ["App comparison (wave 2)", "/blog/best-running-apps-india", "New (moved earlier)", "running app (4,400; KD 34)", "best running app 1,000 (KD 19); running tracker app 1,000 (KD 47)", "India-focused roundup with honest criteria", "Reddit, Play Store, listicles; bhaagoindia roundup dates from 2022", "Comparison; leads to the app page"],
 ["Below the 1,000 gate", "Coach landing section on /ai-running-coach", "-", "running coach (590); running coach near me (590)", "-", "Mention coaching inside the AI coach page", "Local pack and personal sites; easy but small", "Brand, not traffic"],
 ["Section, not a page", "Sections inside the plan pages", "-", "goal times (sub 4 marathon 50; sub 2 half 70; sub 20 5k 30)",
  "levels and week lengths (16 week 40; 12 week 30; 20 week 20); race-specific plan sections (marathon training in mumbai 70; in bangalore 70); missed-week rule; readiness",
  "Each as a heading in the matching plan page", "Under 100 searches a month each", "Section only"],
 ["Skip", "-", "-", "50k plan 20; 10 mile plan 20; 8k plan 10; 15k plan 0; couch to marathon 10", "best running shoes (poor fit)", "-", "Negligible India volume or poor fit", "Do not build"],
]
save("keyword_to_url_map_v2.csv",
     ["group", "target_url", "status", "primary_keyword", "supporting_keywords", "include_in_page", "serp_note", "role"], URL_MAP)

ROADMAP = [
 ["A. Core plans", 1, "Marathon training plan", "/training-plans/marathon", "marathon training plan (18,100)", "Plan page",
  "16-20 week plan in km, four runs a week, India heat and air-quality notes, level and week-length sections", "Coach-reviewed plan content; India context", "Half, 10K and 5K pages; pace calculator; readiness quiz; fueling calculator; /download", "Position vs KD-10 competitors; app-install clicks"],
 ["A. Core plans", 2, "Half marathon training plan", "/training-plans/half-marathon", "half marathon training plan (1,600)", "Plan page", "12-week beginner plan; sub-2 goal", "Coach review", "Marathon and 10K pages", "Impressions and clicks"],
 ["A. Core plans", 3, "10K and 5K training plans", "/training-plans/10k, /training-plans/5k", "10k training plan (1,900); 5k training plan (1,000)", "Plan pages", "8-week 10K; 6-8 week 5K; goal-time sections", "Coach review", "Hub; couch to 5K", "Impressions and clicks"],
 ["A. Core plans", 4, "Training plans hub", "/training-plans", "running training plans (260); running plan beginner (480)", "Hub", "Chooser by distance and level; run-walk start", "Pages 1-3 published", "All plan pages", "Impressions; clicks to plan pages"],
 ["A. Core plans", 5, "How to run a marathon guide", "/blog/how-to-run-a-marathon", "how to run a marathon (18,100, shared pool)", "Guide", "First-timer guide; draft, then decide if it needs its own page", "Coach authored", "Marathon plan page", "Impressions; confirm it is not competing with the plan page"],
 ["A. Core plans", 6, "Couch to 5K plan", "/training-plans/couch-to-5k", "couch to 5k (1,000)", "Plan page", "Run-walk plan; India angle", "Coach review", "5K and hub", "Impressions (NHS and c25k dominate)"],
 ["A. Core plans", 7, "Marathon pace calculator", "/tools/marathon-pace-calculator", "marathon pace calculator (390)", "Tool", "Km-first pace and splits", "Engineering, reusing predictor logic", "Marathon and half pages", "Tool uses; top 10 for the term"],
 ["A. Core plans", 8, "Heart rate zone calculator and zone 2 guide", "/tools/heart-rate-zone-calculator", "zone 2 running (1,300)", "Tool + guide", "Karvonen zones; zone 2 range", "Engineering", "Plan pages", "Tool uses"],
 ["A. Core plans", 9, "Run-faster, endurance and start-running guides", "/blog/*", "how to run faster (5,400)", "Guides", "Written, with a sample week", "Coach authored", "Plan pages", "Clicks; time on page"],
 ["A. Core plans", 10, "Weight-loss running plan; pace calculator", "/training-plans/weight-loss, /tools/pace-calculator", "running plan weight loss (140); pace calculator (8,100)", "Plan + tool", "Small plan page; competitive tool", "Content + engineering", "Plan hub", "Impressions"],
 ["B. Adjacent: race events", 11, "Marquee India race pages (8 races)", "/races/[slug]", "delhi half marathon (9,900) and city variants", "Race pages", "Date, distances, course, registration link, heat advice, link to the matching training plan", "Race data added to the catalog", "Matching plan page; /races/india; /download", "Impressions and top-10 positions for city queries"],
 ["B. Adjacent: race events", 12, "India race calendar hub", "/races/india", "marathons in india (1,900)", "Hub", "Filter by month and distance", "Existing 54 India races plus new ones", "Every race page", "Impressions for calendar queries"],
 ["A. Core plans", 15, "Intervals and tempo runs guide", "/blog/tempo-runs-and-intervals", "tempo run (1,900)", "Guide", "How and why, with a sample session", "Coach authored", "Plan pages", "Clicks; time on page"],
 ["A. Core plans", 16, "Best running apps for India (moved to wave 2)", "/blog/best-running-apps-india", "running app (4,400)", "Comparison", "India-focused app roundup", "Fact check", "AI coach page, /download", "Impressions; app-install clicks"],
 ["C. Positioning", 13, "AI running coach page and comparisons", "/ai-running-coach, /compare/*", "ai running coach (10)", "Landing + comparisons", "Honest comparison of adaptive-plan approaches", "Fact-checked competitor claims", "Plan pages, /download", "Install conversion; brand queries"],
 ["C. Positioning", 14, "Best running apps for India", "/blog/best-running-apps-india", "running app (4,400)", "Comparison", "India-focused roundup", "Fact check", "AI coach page", "Impressions"],
]
save("content_roadmap_v2.csv",
     ["track", "order", "page", "target_url", "primary_keyword", "type", "brief", "needs", "internal_links", "success_metric"], ROADMAP)
print(len(URL_MAP), "url rows;", len(ROADMAP), "roadmap rows")
