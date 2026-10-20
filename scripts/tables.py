import csv, os

os.makedirs("outputs", exist_ok=True)


def save(name, header, rows):
    with open("outputs/" + name, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


# Phase 2: competitors
save("competitor_database.csv",
     ["domain_or_app", "type", "seen_for", "pages_or_assets_observed", "evidence_source"],
     [
      ["strava.com / Strava app", "Direct app + calculators", "running app, pace calculator, strava alternative, running plan for beginners", "App listings, /running-pace-calculator, /training-plans/running", "OpenSEO SERPs 2026-10-21"],
      ["Runna (runna.com)", "Direct app (Strava-owned)", "half marathon training plan, AI coach alternatives", "/training/half-marathon-plan", "OpenSEO and web search"],
      ["Nike Run Club (nike.com)", "Direct app + plans", "marathon training plan, nike run club, how to start running", "/running/marathon-training-plan, /nrc-app", "OpenSEO SERPs"],
      ["TrainAsONE, 26weeks.ai, RunXP, SensAI, Edge (findyouredge.app), Garmin Coach, RunMotion, RunCoach AI, fartlek.io", "Direct AI/adaptive coaching apps", "ai running coach, adaptive training plan", "Comparison posts, store listings", "Web search + OpenSEO ai running coach SERP"],
      ["runkeeper.com (ASICS)", "Direct app", "running app, runkeeper", "Homepage", "OpenSEO SERPs"],
      ["halhigdon.com", "Plan publisher", "marathon training plan, beginners, start running", "Novice 1 and 30/30 plans", "OpenSEO SERPs"],
      ["runnersworld.com (+UK, ZA)", "Editorial publisher", "marathon/5K plans, start running, zone 2", "Plan hubs, beginner guides", "OpenSEO SERPs"],
      ["marathonhandbook.com", "Editorial publisher", "10K plan database, HRV, time predictor", "Plan databases, calculators", "Web search"],
      ["mymottiv.com", "Plan publisher", "half/5K/10K plans, weight loss", "Free plan pages", "OpenSEO SERPs"],
      ["nhs.uk, c25k.com", "Couch to 5K owners", "couch to 5k", "NHS Better Health program", "OpenSEO SERPs"],
      ["on.com (incl. On India), hoka.com, asics.com, brooksrunning.com, nike.com", "Shoe-brand content", "marathon/half/10K plans", "Plan guides, PDFs", "OpenSEO SERPs"],
      ["calculator.net, active.com, mcmillanrunning.com, omnicalculator.com, goandrace.com, runhive.com, runandgrow.com", "Calculator/tool sites", "pace calculator, marathon pace calculator, HR zones, time predictor", "Tool pages", "OpenSEO SERPs"],
      ["fetcheveryone.com, marathonguide.com, runcalcs.com, kulg.io", "Predictor tool sites", "marathon time predictor", "Predictor pages", "OpenSEO SERPs"],
      ["ahotu.com, finishers.com, worldsmarathons.com, marathonmitra.com, racemart.in, ifinish.in, indiarunning.com, runindia.in, bhaagoindia.com, athlenic.com, racesregistrations.com, citywoofer.com", "Race aggregators (India and global)", "city marathon names, marathons in india, calendar", "Event and city listing pages", "OpenSEO SERPs"],
      ["aims-worldrunning.org, official race sites (tatamumbaimarathon.procam.in, bajajpunemarathon.com, jbgkolkatamarathon.com and others)", "Official race sources", "Delhi/Bengaluru/Hyderabad/Kolkata/Mumbai/Pune marathon", "Race info pages", "OpenSEO SERPs"],
      ["fatmarathoner.com, redbull.com/in-en, thehigh5tribe.com", "India editorial", "India beginner plans, calendars, best apps for runners in India", "India plan and calendar guides", "Web search + OpenSEO"],
      ["marathon-index.com", "Race plan aggregator", "Mumbai/Bangalore/Chennai training plan", "Race training-plan pages (week-by-week 'coming soon')", "Web search"],
      ["runnersconnect.net, therunningchannel.com, humankinetics.com", "Training-advice publishers", "missed marathon training", "Advice articles", "Web search"],
      ["peloton.com, juniper (myjuniper.com), kubios.com, mayoclinic.org", "Health and fitness publishers", "zone 2, HRV", "Explainers", "OpenSEO SERPs"],
     ])

# Phase 10: keyword-to-URL map
save("keyword_to_url_map.csv",
     ["cluster_id", "primary_keyword", "supporting_keywords", "target_url", "status", "page_purpose", "audience", "why_justified"],
     [
      ["C04", "mumbai marathon training plan", "half marathon training plan india; marathon training plan india; marathon training plan in km", "/races/[slug] training section + /training-plans/india-marathon-plan", "New + extend existing race pages", "Week-by-week plan tied to a specific race, with heat and km guidance, ending in 'build my plan in Orka'", "Runners entering an Indian race", "SERPs have no real race plan; ties to Orka's core product. Volume unverified, so validate with Search Console after launch."],
      ["C01", "delhi half marathon", "bengaluru marathon; pune marathon; chennai marathon; hyderabad marathon; kolkata marathon; ahmedabad marathon", "/races/[slug] for each marquee race", "New pages (catalog lacks these races)", "Race info + course + training CTA", "Entrants and followers of the race", "6 queries of 2,400-9,900/month, KD 0-5, aggregators and Facebook posts rank."],
      ["C02", "mumbai marathon", "tata mumbai marathon; mumbai marathon 2027; mumbai marathon registration", "/races/tata-mumbai-marathon", "New page", "Race info, 2027 date, training plan link", "Entrants", "8,100 + 5,400 + 1,000 per month, no training content in SERP."],
      ["C03", "marathons in india", "upcoming marathons in india; marathon calendar india; half marathon india", "/races (filter India) + /races/india", "Improve existing + new India hub", "Calendar hub for India, filterable by month and distance", "Runners choosing a race", "Existing 54 India races; aggregators rank."],
      ["C05", "marathon training plan", "marathon training plan for beginners; how to prepare for a marathon; how to train for a marathon", "/training-plans/marathon", "New page", "Beginner-to-sub-4 marathon plan in km with India heat notes", "First-time marathoners", "18,100/month, KD 10; competitors are global brands without India framing."],
      ["C06", "half marathon training plan", "half marathon training plan for beginners; how to train for a half marathon", "/training-plans/half-marathon", "New page", "12-week half plan", "First half runners", "1,600/month, KD 10."],
      ["C07", "10k training plan", "5k training plan; couch to 5k; running plan for beginners; 10k training plan for beginners", "/training-plans/10k and /training-plans/5k", "New pages", "10K and 5K plans", "Beginners", "1,900 and 1,000/month; no KD barrier for 10K."],
      ["C08", "sub 2 hour half marathon", "sub 30 5k; sub 60 10k; sub 50 10k; sub 4 marathon", "/training-plans/goal-times (one page per goal as volume proves)", "New hub, later split", "Goal-pace plans", "Time-goal runners", "Matches the product promise; start as one page to avoid thin duplicates."],
      ["C09", "pace calculator", "running pace calculator; half marathon pace calculator; 5k/10k pace chart", "/tools/pace-calculator", "New page", "Pace, time and distance calculator with km splits", "All runners", "8,100 + 2,400/month; head term competitive, so lead with km and India framing."],
      ["C10", "marathon pace calculator", "marathon pace chart km; half marathon pace chart; marathon time calculator", "/tools/marathon-pace-calculator", "New page", "Marathon split and pace chart", "Marathon runners", "KD 0; small sites rank."],
      ["C11", "marathon time predictor", "race time predictor; half marathon time calculator", "/tracker/marathon-time-predictor", "Existing page, optimise", "Predictor tool", "Race planners", "Tiny volume; keep as an asset and link into plans."],
      ["C12", "zone 2 running", "heart rate zone calculator; zone 2 heart rate calculator; heart rate zones running", "/tools/heart-rate-zone-calculator + guide", "New tool + blog guide", "HR zone calculator and zone 2 explainer", "Runners with watches", "1,300 + 320 + 210/month; tiny tool sites rank."],
      ["C13", "how to run faster", "how to build running endurance; how to start running; how to improve running stamina", "/blog/how-to-run-faster etc.", "New blog posts", "Written guides with real training content", "Beginners and improvers", "5,400 + 3,600 + 2,400/month; video-heavy or thin written results."],
      ["C14", "running app", "best running app; nike run club; runkeeper", "/blog/best-running-apps-india", "New comparison page", "Honest comparison, India focus", "App shoppers", "4,400 + 1,000/month; competitive, so lower priority."],
      ["C15", "ai running coach", "strava alternative; running coach app; garmin coach; runna app review", "/ai-running-coach + /compare/*", "New landing + comparison pages", "Positioning pages for the adaptive-plan promise", "Informed app shoppers", "Low volume, high intent and brand value."],
      ["C16", "what to do if you miss a run in marathon training", "marathon taper; how to taper for a marathon", "/blog/missed-training", "New blog post", "What to do after a missed week", "Existing runners", "Matches the product's differentiator. Volume unverified."],
      ["C18", "running nutrition", "marathon nutrition; half marathon fueling", "/tracker/marathon-fueling-hydration-calculator", "Existing page, optimise", "Fueling tool", "Marathon runners", "Marathon-specific volume tiny."],
      ["C19", "am i ready for a marathon", "how long to train for a marathon; first marathon", "/tracker/race-readiness-quiz", "Existing page, optimise", "Readiness quiz", "First-timers", "Volume unverified."],
      ["C20", "best running shoes", "best running shoes india; running shoe finder", "/tracker/shoe-finder", "Existing, no investment", "Shoe finder", "Shoppers", "Poor fit; high ad competition; skip."],
      ["C17", "what is hrv", "hrv running; running recovery", "/blog/hrv-for-runners", "Later blog post", "HRV explainer for runners", "Watch users", "Head term is authority-dominated; target runner-specific long tail only."],
     ])

# Phase 11: content roadmap
save("content_roadmap.csv",
     ["wave", "order", "page", "target_url", "primary_keyword", "type", "brief", "needs", "internal_links", "success_metric"],
     [
      [1, 1, "Marquee India race pages (Delhi HM, Bengaluru, Pune, Chennai, Hyderabad, Kolkata, Ahmedabad, Tata Mumbai)", "/races/[slug]", "delhi half marathon (and city variants)", "Race pages", "Official date, distances, course, cut-offs, registration link, heat advice, 'train for it' CTA", "Race data added to content/races.json", "/races, matching training plan, /download", "Impressions and top-10 positions for the city queries"],
      [1, 2, "India race calendar hub", "/races/india", "marathons in india", "Hub", "Filter by month and distance; link to every India race", "Existing 54 India races plus new marquee races", "Each race page", "Impressions for calendar queries"],
      [1, 3, "Race-linked training plans (Mumbai, Delhi HM first)", "/races/[slug]#plan", "mumbai marathon training plan", "Plan sections", "Week-by-week plan to race date with heat and km", "Coach review of plan content", "Race page, /download", "Impressions; check real volume in Search Console"],
      [2, 4, "Marathon training plan (beginners) in km", "/training-plans/marathon", "marathon training plan", "Plan page", "16-20 week plan, 4 days/week, India heat notes", "Coach review", "Race pages, predictor, readiness quiz", "Position vs KD-10 competitors; app installs"],
      [2, 5, "Half marathon plan; 10K plan; 5K plan", "/training-plans/half-marathon, /10k, /5k", "half marathon training plan", "Plan pages", "12-week half; 8-week 10K; Couch to 5K alternative", "Coach review", "Marathon plan, tools", "Impressions and clicks"],
      [2, 6, "Marathon pace calculator and pace calculator", "/tools/marathon-pace-calculator, /tools/pace-calculator", "marathon pace calculator", "Tools", "Km-first pace, splits, pace chart", "Engineering using existing predictor logic", "Plans, predictor", "Tool uses; top-10 for marathon pace calculator"],
      [3, 7, "Heart rate zone calculator and zone 2 guide", "/tools/heart-rate-zone-calculator", "zone 2 running", "Tool + guide", "Karvonen zones, zone 2 range", "Engineering", "Plans, AI coach page", "Tool uses"],
      [3, 8, "Guides: how to run faster, build endurance, start running", "/blog/*", "how to run faster", "Blog", "Written, practical, with sample week", "Coach authored", "Plans, /download", "Clicks; time on page"],
      [3, 9, "What to do after a missed week of training", "/blog/missed-training", "what to do if you miss a run in marathon training", "Blog", "Rules of thumb plus how Orka adapts", "Coach review", "AI coach page", "Impressions (validates volume)"],
      [4, 10, "AI running coach landing page and comparisons", "/ai-running-coach, /compare/*", "ai running coach", "Landing + comparisons", "Honest comparison of adaptive approaches", "Fact-checked competitor claims", "Download, plans", "Conversion to installs; brand queries"],
      [4, 11, "Best running apps for India", "/blog/best-running-apps-india", "best running app", "Comparison", "India-focused app roundup", "Fact check", "AI coach page", "Impressions"],
     ])

# Phase 12: measurement
save("measurement_framework.csv",
     ["metric", "source", "cadence", "what_it_tells_us", "action_trigger"],
     [
      ["Indexed pages and coverage", "Google Search Console", "Weekly", "Whether new pages are indexed", "Page not indexed after 14 days: inspect URL, fix, request indexing"],
      ["Impressions, clicks, CTR, avg position by page and query", "Google Search Console", "Weekly, monthly review", "Queries each page actually ranks for", "Position 8-20 with impressions: improve page; CTR under 2% at top 5: rewrite title"],
      ["Real volume for unverified clusters (C04, C16, C19)", "Search Console impressions", "Monthly", "Replaces missing volume estimates", "If impressions stay near zero after 60 days, demote the cluster"],
      ["Organic sessions and landing pages", "Google Analytics", "Weekly", "Traffic quality by page", "Low engagement: revise intent match"],
      ["Tool uses and CTA clicks", "Analytics events", "Weekly", "Whether pages turn visits into product use", "Low CTA click rate: change placement"],
      ["App install clicks from organic", "Analytics + store links", "Monthly", "Business outcome", "Compare clusters by installs per 1,000 sessions"],
      ["Keyword rank for tier-1 terms", "Search Console (and OpenSEO rank tracker if credits allow)", "Monthly", "Progress on priority terms", "Re-run SERP checks for stalled terms"],
      ["Assumption check", "This research vs Search Console", "Quarterly", "Where volume, difficulty or intent assumptions were wrong", "Update scoring and roadmap"],
     ])
print("ok")
