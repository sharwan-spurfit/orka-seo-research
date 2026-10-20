"""Phases 1, 2, 6, 10, 11, 12: analyst-written tables (manual judgments, evidence noted per row)."""
import csv, os
D = os.path.join(os.path.dirname(__file__), "..", "data")
def wr(f, head, rows):
    with open(os.path.join(D, f), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh); w.writerow(head); w.writerows(rows)

# ---- Phase 1: framework
wr("p1_framework.csv", ["item","definition"], [
["Market","India, English-language Google searches"],
["Product (assumption from landing-page repo)","Free adaptive AI running-training app (iOS/Android): plans from goal+race date, re-plans after missed runs, reads HRV/sleep/HR from Apple Watch, Garmin, COROS, WHOOP, Strava, Apple Health. Site has race catalog, free tools (marathon time predictor, fueling calculator, race-readiness quiz, shoe finder), blog, /download."],
["Goal of SEO","Installs of the free app; secondary: tool usage and race-catalog engagement that lead to installs"],
["Source rule","Free sources only (Google Autocomplete gl=in, Google Trends relative, manual SERP reading). No Ahrefs/Similarweb/paid credits."],
["Independence rule","Keywords are never filtered or weighted by the site's existing content or GSC rankings. Existing pages enter only in Phase 10 (mapping), after scoring."],
["Score scale","1-5 on seven dimensions; HIGHER IS ALWAYS BETTER (competition_ease 5 = weak SERP)."],
["relevance","How directly the query's need is solved by the product (5 = core, 1 = unrelated)"],
["demand","Search-interest proxy (1-4 from autocomplete breadth; Trends probe can override). NOT volume. 5 only with real evidence."],
["intent","Closeness to action: tool/commercial 5, plan-seeking/commercial-investigation 4, informational 3, navigational 1-2"],
["competition_ease","Manual SERP read: 5 = thin/low-authority/gap, 1 = big publishers + apps dominate"],
["opportunity","Quality of the content gap an Orka page could fill (5 = nobody answers it well)"],
["value","Likelihood a visitor converts to install / becomes an engaged user"],
["confidence","How much real evidence backs the scores (autocomplete-only = low)"],
["Base weights","relevance .20, demand .15, intent .15, competition .15, opportunity .15, value .15, confidence .05"],
["Weight tests","demand_heavy, value_heavy, low_competition, equal. A cluster is 'weight-sensitive' if its rank moves >4 places across sets."],
["Tiers (base score)","Tier 1 >=3.9, Tier 2 >=3.3, Tier 3 >=2.7, Tier 4 park <2.7"],
["LIMITS (stated plainly)","1) NO absolute search volumes anywhere. 2) SERP checks used a US-only search tool, not google.co.in; India SERPs will differ. 3) Autocomplete shows what Google suggests, not how often it is searched. 4) Google Trends could not be re-run from the cloud container (proxy returns 403); only the earlier 5-term probe exists. 5) Competition and opportunity are one analyst's manual ratings."],
])

# ---- Phase 2: competitors
C = "Competitor / market"
wr("p2_competitors.csv", ["name","type","domain_or_note","why_it_matters","seen_in"], [
["Runna","AI plan app","runna.com (Strava-owned since 2025)","Closest direct app; owns 'runna alternative' demand","earlier session SERPs"],
["Nike Run Club","App + publisher","nike.com","Ranks for generic plans and app queries","earlier session SERPs"],
["TrainAsONE","Adaptive plan app","trainasone.com","Direct adaptive-plan competitor","earlier session SERPs"],
["26weeks.ai","AI plan app","26weeks.ai","Direct AI-plan competitor","earlier session SERPs"],
["RunXP","App","","Direct competitor","earlier session SERPs"],
["SensAI","App","","Direct competitor","earlier session SERPs"],
["Edge","App","","Direct competitor","earlier session SERPs"],
["Garmin Coach","Device-native plans","garmin.com","Owns Garmin-plan queries; Training Readiness is a 'second opinion' (forum reading)","earlier + this session"],
["RunMotion / Runkeeper","Apps","","Generic running-app SERPs","earlier session SERPs"],
["Strava","Platform","strava.com","Owns 'strava alternative'; also integration partner","earlier session SERPs"],
["Kiprun Pacer","Free plan app","pacer.kiprun.com","Free-plan positioning overlaps Orka; India availability unconfirmed","this session SERP"],
["running.COACH","Plan app","","Pace/HR/power-based plans","this session SERP"],
["India Running (app)","India race app","apps.apple.com/in (India Running)","India-specific race + plans app","this session SERP"],
["FirstRun (MobieFit)","India C25K-style app","","Old (2015) India-specific app; status unclear","this session SERP"],
["marathon-index.com","Race-guide publisher","marathon-index.com","Has Mumbai/Delhi/Bangalore/Hyderabad race pages; Mumbai plan 'coming soon', Delhi plan gated behind sign-up","this session SERP"],
["fatmarathoner.com","Blog (India-angled)","fatmarathoner.com","Ranks for India heat plan and India shoes; main India-specific content rival","this session SERP"],
["Marathon Handbook","Publisher","marathonhandbook.com","Generic plans; free PDFs","earlier + this session"],
["Runner's World","Publisher","runnersworld.com","Generic plans, calculators","earlier session SERPs"],
["RunnersConnect","Coaching publisher","runnersconnect.com","Plans, calculators","earlier session SERPs"],
["TrainingPeaks / Finalsurge","Coaching platforms","trainingpeaks.com / finalsurge.com","Plan marketplaces","earlier session SERPs"],
["Omni Calculator","Calculators","omnicalculator.com","Pace/time calculators","earlier session SERPs"],
["marathons.com","Race directory","marathons.com","Race listings","earlier session SERPs"],
["Red Bull India","Brand content","redbull.com","India beginner plan content","earlier session SERPs"],
["Nuffield Health / On / Trainero","Generic 12-week half plans","nuffieldhealth.com, on.com/en-in, blog.trainero.com","Own '12 week half marathon plan' SERP","this session SERP"],
["Kissht / Urban Style Footwear","Commercial blogs","kissht.com, urbanstylefootwear.com","India shoe listicles; promotional, plus spam mirror pages","this session SERP"],
["Spam mirror domains","Noise","several","Copy generic content for shoes/plans; weak authority","both sessions"],
])

# ---- Phase 6: SERP analysis (manual ratings; US-only tool)
H = ["query","cluster","competition_ease_1to5","dominant_result_types","gap_observed","evidence_date","evidence_strength","caveat"]
cav = "US-only search tool, not google.co.in"
wr("p6_serp.csv", H, [
["tata mumbai marathon training plan","india_race_plans",4,"marathon-index (plan 'coming soon'); one personal blog; Procam elite pages","No real race-specific plan; race date 17 Jan 2027 per search results","2026-10-20","this session, full read",cav],
["delhi half marathon training plan 12 weeks","india_race_plans",3,"marathon-index (gated), Nuffield, On (en-in), Trainero, Marathon Handbook","Delhi plan is gated; generic plans fill rest","2026-10-20","this session, full read",cav],
["marathon training plan india heat","india_heat",4,"marathontrainingacademy, fatmarathoner 12-week hot-weather plan, marathon-index weather pages, thin blogs","No sports-medicine source; the 10-20% per 10C pace figure is unsourced","2026-10-20","this session, full read",cav],
["best running shoes india under 5000","shoes_india",3,"Kissht, Urban Style Footwear, fatmarathoner, spam mirrors","Promotional lists; no honest fit-based guide","2026-10-20","this session, full read",cav],
["free running training plan app india","ai_coach",3,"FirstRun (2015), India Running, Kiprun Pacer, running.COACH","No modern free adaptive India app owns the query","2026-10-20","this session, full read",cav],
["garmin training readiness vs hrv adjust plan","hrv",3,"shoulditrain, rundida, the5krunner, TrainerRoad/Slowtwitch forums","Evidence mixed; single readings weak; no clear decision guide","2026-10-20","this session, full read",cav],
["marathon plan","marathon_plan",1,"Nike, Marathon Handbook, Runner's World","Saturated","earlier session","summary only (detail not retained)",cav],
["AI coach app","ai_coach",2,"Runna, TrainAsONE, 26weeks.ai, RunXP, SensAI + vendor listicles","Listicles by vendors","earlier session","summary only (detail not retained)",cav],
["India beginner plan","beginner_running",3,"Red Bull India, listicles","Some India angle","earlier session","summary only (detail not retained)",cav],
["marathon time predictor","time_predictor",3,"Runner's World, Omni Calculator, marathon-index","Calculators plentiful; few tied to plans","earlier session","summary only (detail not retained)",cav],
["marathon fueling calculator","fueling",2,"Maurten/GU/publishers, calculators","Calculators exist","earlier session","summary only (detail not retained)",cav],
["runna alternative / strava alternative","alternatives",3,"Vendor listicles","Few honest comparisons","earlier session","summary only (detail not retained)",cav],
["best running shoes india beginner","shoes_india",3,"Commercial blogs, spam mirrors","Honest India shoe guide missing","earlier session","summary only (detail not retained)",cav],
["sub 4 marathon plan","goal_time",3,"fatmarathoner, Runner's World, forums","Mixed quality","earlier session","summary only (detail not retained)",cav],
["missed week of training marathon","missed_training",4,"Forum threads, generic blogs","No tool-backed answer","earlier session","summary only (detail not retained)",cav],
["hrv running","hrv",3,"Blogs/forums; vendor pages","Single reading is weak evidence; decision guides missing","earlier session","summary only (detail not retained)",cav],
["mumbai marathon training plan","india_race_plans",4,"marathon-index placeholder, blogs","Race-specific plan missing","earlier session","summary only (detail not retained)",cav],
["india marathon calendar","india_race_calendar",3,"Event aggregators, official sites","Aggregators dominate","earlier session","summary only (detail not retained)",cav],
["pace calculator","pace_calc",1,"Omni, Runner's World, many calculators","Saturated","earlier session","summary only (detail not retained)",cav],
["12 week half marathon plan","half_plan",1,"Nuffield, On, Trainero, Marathon Handbook","Saturated","earlier + this session","summary + this session",cav],
["race readiness quiz","race_readiness",3,"Forum threads; few quizzes","Quiz format uncommon","earlier session","summary only (detail not retained)",cav],
["Not checked: all other 6,000+ keywords","(inherit cluster rating)","","","Cluster rating applied; confidence low","","none","Do not read per-keyword competition as measured"],
])

# ---- Phase 10: keyword -> URL map. Existing pages come ONLY from the README; slugs are unknown, marked.
wr("p10_keyword_url_map.csv", ["cluster","primary_keyword","target_url","page_status","page_type","notes"], [
["alternatives","strava alternative","/alternatives/strava","new","comparison","One comparison per rival (Runna, Strava, NRC); honest, sourced; link to /download"],
["alternatives","runna alternative","/alternatives/runna","new","comparison",""],
["india_race_plans","tata mumbai marathon training plan","/races/tata-mumbai-marathon (race page, plan module) + blog guide","existing race page (slug to verify) + new guide","race page + guide","Date 17 Jan 2027 per search results; verify on official site"],
["india_race_plans","delhi half marathon training plan","/races/delhi-half-marathon (slug to verify)","existing race page + new section","race page","Repeat per major race (Bengaluru, Hyderabad, Chennai, Kolkata, Pune)"],
["goal_time","sub 2 half marathon","/blog/sub-2-half-marathon-plan","new","guide + CTA to predictor","also sub-4 marathon, sub-50 10k"],
["missed_training","garmin training plan missed workout","/blog/missed-a-run-how-to-adjust-training","new","guide","Demonstrates re-planning; CTA /download"],
["ai_coach","ai running coach","/ai-running-coach","new","landing","Core product page"],
["time_predictor","race time predictor","marathon time predictor tool (slug to verify)","existing tool","tool","Add explainer content, multi-distance variants"],
["india_heat","mumbai marathon weather","/blog/running-in-indian-heat","new","guide","Cite sources; flag the unsourced 10-20% per 10C figure"],
["hrv","hrv running","/blog/hrv-running-should-you-adjust-training","new","guide","Single reading is weak evidence; trend over days"],
["watch_integration","garmin training plans","/integrations/garmin (+ coros, apple-watch, whoop, strava)","new","integration pages",""],
["marathon_first","first marathon","/blog/first-marathon-guide","new","guide","Cluster is competitive; support piece"],
["plan_10k_5k","10k training plan","/blog/10k-training-plan","new","plan page","Support piece"],
["half_plan","half marathon training plan","/blog/half-marathon-training-plan","new","plan page","Tier 3"],
["running_app","running app","/ (home) and /download","existing","home","Brand/broad term; do not target with a blog post"],
["fueling","marathon nutrition","fueling calculator tool (slug to verify) + /blog/marathon-fueling","existing tool + new guide","tool + guide",""],
["race_readiness","race readiness","race-readiness quiz (slug to verify)","existing tool","tool","No autocomplete evidence; manual seed"],
["shoes_india","best running shoes for beginners india","shoe finder tool (slug to verify) + /blog/running-shoes-india","existing tool + new guide","tool + guide","Honest fit-based guide"],
["marathon_plan","marathon training plan","/blog/marathon-training-plan","new","plan page","Saturated; defer"],
["pace_calc","marathon pace calculator","/tools/pace-calculator","new","tool","Saturated; defer"],
["taper","marathon taper","/blog/marathon-taper","new","guide","Tier 3"],
["india_race_calendar","mumbai marathon","/races (catalog)","existing","catalog","Race pages carry calendar/info intent"],
["hr_zones / long_run / c25k / brand_plan / watch_buying / hyrox_other / india_race_info / shoes_generic","","none","parked","","Tier 4: no dedicated page"],
])

# ---- Phase 11: roadmap
wr("p11_roadmap.csv", ["wave","priority","title","target_keyword","cluster","format","outline_points","internal_links","success_metric","effort"], [
[1,1,"Missed a run? How to re-plan your training","garmin training plan missed workout","missed_training","guide","What the research says about missed days; rules by days missed; worked examples; how Orka re-plans","/download, race pages, time predictor","Impressions, avg position, installs from page","M"],
[1,2,"Tata Mumbai Marathon training plan (17 Jan 2027)","tata mumbai marathon training plan","india_race_plans","race page + guide","Weeks-to-race builder; heat; course notes; verify date at official site","/races/*, predictor, /download","Position, clicks, installs","M"],
[1,3,"Delhi Half / Bengaluru / Hyderabad race plan sections","delhi half marathon training plan","india_race_plans","race page sections","Per-race heat, course profile, plan template","/races, guide","Clicks per race page","M"],
[1,4,"Strava alternative (honest comparison)","strava alternative","alternatives","comparison","Criteria table; where Strava wins; where Orka differs","/download, integrations","Position, installs","M"],
[1,5,"Runna alternative","runna alternative","alternatives","comparison","Price, adaptiveness, watch support, India availability","/download","Position, installs","M"],
[1,6,"Running in Indian heat and humidity","mumbai marathon weather","india_heat","guide","Acclimatisation, pacing by effort/HR, hydration, cite sources; flag unsourced rules of thumb","race pages, plans","Impressions, links","M"],
[2,7,"Sub-2 half marathon plan","sub 2 half marathon","goal_time","guide","Pace table in km, week structure, readiness check","predictor, /download","Position","M"],
[2,8,"Sub-4 marathon plan","sub 4 marathon","goal_time","guide","Same, marathon","predictor","Position","M"],
[2,9,"Sub-50 10k plan","sub 50 10k","goal_time","guide","","predictor","Position","S"],
[2,10,"AI running coach (landing)","ai running coach","ai_coach","landing","What adaptive means, evidence, limits","/download","Installs","M"],
[2,11,"HRV and running: should you change today's run?","hrv running","hrv","guide","Trend vs single reading; decision table; caveats","integrations","Position","M"],
[2,12,"Garmin / COROS / Apple Watch / WHOOP integration pages","garmin training plans","watch_integration","integration pages","What syncs, what adapts","/download","Installs","M"],
[2,13,"Race time predictor explainer + variants","race time predictor","time_predictor","tool enhancement","Method, accuracy limits, from 5k/10k/half","tools","Tool usage","S"],
[3,14,"First marathon guide","first marathon","marathon_first","guide","Support piece","plans","Position","M"],
[3,15,"10k training plan","10k training plan","plan_10k_5k","plan page","","","Position","M"],
[3,16,"Marathon fueling guide + calculator link","marathon nutrition","fueling","guide","","fueling tool","Tool usage","S"],
[3,17,"Best running shoes for beginners in India","best running shoes for beginners india","shoes_india","guide","Fit-based, no affiliate bias","shoe finder","Position","M"],
[3,18,"Half marathon training plan","half marathon training plan","half_plan","plan page","Saturated; differentiate with adaptive angle","","Position","M"],
[3,19,"Marathon taper","marathon taper","taper","guide","","plans","Position","S"],
[4,20,"Marathon training plan (generic)","marathon training plan","marathon_plan","plan page","Only after waves 1-3 show traction","","Position","L"],
])

# ---- Phase 12: measurement
wr("p12_measurement.csv", ["metric","source","cadence","baseline_method","target_direction","note"], [
["Impressions and clicks per cluster","Search Console (Queries x Pages, country=India)","weekly","Snapshot before each publish","up","Group queries by cluster rules in this repo"],
["Average position, target query","Search Console","weekly","Per-page baseline at publish","down","Position is noisy under 100 impressions"],
["Install clicks from organic landing pages","Analytics events on /download and store links","weekly","0 at launch","up","Define the event before launch"],
["Tool usage from organic","Analytics events (predictor, fueling, quiz, shoe finder)","weekly","Pre-launch usage","up",""],
["Indexing","Search Console page indexing","per publish","n/a","indexed in 2 weeks","Submit sitemap"],
["Backlinks / referring domains","Search Console Links report (free)","monthly","Snapshot","up","No paid tool"],
["Validation of demand","Compare Search Console impressions with Trends probe and autocomplete proxies","quarterly","This research","re-score clusters","First real demand data comes from Search Console after publishing"],
["Re-run research","Re-run autocomplete (scripts/ac.py) and Trends (scripts/tr.py, 60s gaps) from a machine with access","quarterly","This dataset","refresh",""],
])
print("ok")
