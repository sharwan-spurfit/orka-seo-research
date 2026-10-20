"""Phases 2-12 builder. Reads data/kw_clean.csv + autocomplete_raw.csv, writes data/*.csv.
Nothing here filters or weights by the site's existing content or GSC rankings.
"""
import csv, re, math, collections, os
D = os.path.join(os.path.dirname(__file__), "..", "data")
rd = lambda f: list(csv.DictReader(open(os.path.join(D, f), encoding="utf-8")))
def wr(f, head, rows):
    with open(os.path.join(D, f), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh); w.writerow(head); w.writerows(rows)

raw = {r["keyword"]: r for r in rd("autocomplete_raw.csv")}
kws = rd("kw_clean.csv")
allk = sorted(raw)

# ---------- topic clusters: (id, label, relevance, value, competition_ease, opportunity, confidence, intent, SERP evidence)
# All dimensions 1-5, HIGHER = BETTER (competition_ease 5 = weak SERP). Relevance/value are product-market judgments,
# competition/opportunity come from manual SERP reading (US-only), see p6_serp.csv.
CL = {
"india_race_plans": ("India race-specific training plans (Mumbai/Delhi/Bengaluru etc.)",5,5,4,5,3,"commercial-investigation","marathon-index Mumbai plan is 'coming soon'; Delhi plan gated; generic plans dominate"),
"india_heat": ("Training in Indian heat/humidity",5,4,4,5,2,"informational","only fatmarathoner + thin blogs; no sports-medicine source"),
"missed_training": ("Missed workouts / re-planning / return from injury",5,5,4,5,3,"informational","no dedicated tool-backed answer; mostly forum + generic blog"),
"ai_coach": ("AI / adaptive running coach apps",5,5,2,3,3,"commercial","Runna, TrainAsONE, 26weeks.ai, RunXP, SensAI + vendor listicles"),
"alternatives": ("Runna / Strava / Nike Run Club alternatives",5,5,3,4,3,"commercial","listicles by vendors; few honest comparisons"),
"running_app": ("Generic 'running app' / best running app",4,4,1,2,3,"commercial","Strava, Nike Run Club, Runkeeper, big publishers"),
"watch_integration": ("Garmin/COROS/Apple Watch/WHOOP training plans & sync",4,4,3,3,2,"commercial-investigation","brand help pages + forums"),
"watch_buying": ("Running watch buying",2,2,1,1,2,"commercial","retail + big review sites"),
"hrv": ("HRV for running / readiness decisions",5,4,3,4,3,"informational","blogs/forums; Garmin readiness is 'a second opinion'; single reading weak evidence"),
"hr_zones": ("Heart-rate zones / zone 2",3,3,1,1,3,"informational","Garmin, Polar, big publishers"),
"goal_time": ("Goal-time plans (sub-4 marathon, sub-2 half, sub-50 10k)",5,4,3,4,3,"commercial-investigation","fatmarathoner, Runner's World, forums; mixed quality"),
"time_predictor": ("Race time predictor / finish-time calculators",5,4,3,3,3,"tool","Runner's World, Omni Calculator, marathon-index, RunnersConnect"),
"pace_calc": ("Pace calculators / pace charts",4,3,1,1,3,"tool","Omni, Runner's World, countless calculators"),
"fueling": ("Marathon fueling / nutrition / gels",4,3,2,3,3,"informational","Maurten/GU/publisher pages; calculators exist"),
"taper": ("Marathon taper",4,3,2,2,3,"informational","Runner's World, Marathon Handbook"),
"long_run": ("Long run guidance",3,2,2,2,2,"informational","generic coaching blogs"),
"marathon_first": ("First marathon / beginner marathon",5,4,2,3,3,"informational","Nike, Runner's World, Marathon Handbook"),
"marathon_plan": ("Marathon training plan (generic)",5,4,1,2,3,"commercial-investigation","Nike, Marathon Handbook, Runner's World, Hal Higdon"),
"half_plan": ("Half marathon training plan (generic)",5,4,1,2,3,"commercial-investigation","Nuffield, On, Marathon Handbook, Trainero"),
"plan_10k_5k": ("5K / 10K training plans",4,4,2,2,2,"commercial-investigation","NHS/C25K, Runner's World, publishers"),
"c25k": ("Couch to 5K",3,3,1,1,2,"commercial-investigation","NHS + C25K apps"),
"plan_generic": ("Generic running training plan / program",4,4,1,2,2,"commercial-investigation","every publisher and app; unspecific"),
"beginner_running": ("Running for beginners / how to start",4,3,2,2,2,"informational","large publishers, health sites"),
"brand_plan": ("Named-method plans (Higdon, Hanson, Galloway, brand plans)",3,3,1,2,2,"commercial-investigation","method authors + brand sites"),
"race_readiness": ("Race readiness / am I ready",4,3,3,3,2,"tool","mostly forum threads; few quizzes"),
"india_race_calendar": ("India race calendar / events / registration",4,4,3,3,2,"navigational/informational","event aggregators, official sites"),
"india_race_info": ("India race results/winners/photos/coupons",2,1,1,1,2,"navigational","official sites; no product fit"),
"shoes_india": ("Running shoes for Indian runners (budget, beginners)",3,2,3,3,2,"commercial","commercial blogs, spam mirrors, fatmarathoner"),
"shoes_generic": ("Running shoes (generic)",2,2,1,1,3,"commercial","retail + big review sites"),
"hyrox_other": ("Hyrox/ultra/trail/other disciplines",2,2,2,2,1,"informational","adjacent; not core"),
"off_topic": ("Off-topic / non-running noise",1,1,1,1,5,"n/a","autocomplete noise (e.g. 'running stitch', 'race ready suspension')"),
}
OFF = re.compile(r"equilibrium|average cost|long run (cost|production|golf|zone$)|short run|tantrum|heater|quarkus|repair|race ready (?!quiz|test|calculator|checklist|score|readiness)|garage|alignments|detailing|\bmx\b|electric|green marathon|marathon (sports|x)\b|first light|captions?\b|vancouver|meal|lauriat|quotes|xarelto|stock|umamusume|karts?\\b|man india|series points|midwest|iberian|\\bxl\\b|territory|\\bjs\\b|administrator|app (name|design|login|ui)\\b|\\bgif\\b|\\brug\\b|8 year|second hand|motor|times of india|pvt|heat ?maps?|stitch|jsx|capture territory|marks? territory|dictation|long jump|zumba|spikes|suspension|wheels|mx207|clock|football|cost curve|demand curve|wealth|quotes|hangover|lauriat|lily|red\b|extra cushion|bike|\bman\b|honda|st jude|olympics|americans|photos? .*free|race ready (kendal|hcma|lap|side)", re.I)
def classify(k):
    if OFF.search(k): return "off_topic"
    if re.search(r"alternative|\bvs\b|versus|\brunna\b|nike run club|\bnrc\b|strava", k): return "alternatives"
    india = re.search(r"mumbai|delhi|bengaluru|bangalore|chennai|hyderabad|kolkata|pune|tata|airtel|wipro|india|aims|vadodara|chandigarh", k)
    if india:
        if re.search(r"result|winner|photo|coupon|history|expo|prize|bib|cut.?off|route map|sponsor|watch(es)?\b|certificate|\bapp\b|download", k): return "india_race_info"
        if re.search(r"shoe", k): return "shoes_india"
        if re.search(r"\bheat\b|humid|monsoon|weather|summer", k): return "india_heat"
        if re.search(r"train|plan|prepar|how to|schedule|beginner|week|tips|pace|diet|nutrition", k): return "india_race_plans"
        if re.search(r"shoe", k): return "shoes_india"
        return "india_race_calendar"
    if re.search(r"\bheat\b|humid|monsoon|hot weather", k) and not re.search(r"heatmap|calculator", k): return "india_heat"
    if re.search(r"miss(ed|ing)|skipp|back on track|injur|rest day|re-?plan|fell behind|behind on", k): return "missed_training"
    if re.search(r"alternative|vs\b|versus|\brunna\b|nike run club|\bnrc\b|strava", k): return "alternatives"
    if re.search(r"\bai\b|adaptive|ai coach|virtual coach|personali[sz]ed.*(plan|coach)|running coach", k): return "ai_coach"
    if re.search(r"hrv|readiness|recovery|sleep|resting heart", k): return "hrv"
    if re.search(r"zone 2|heart rate zone|hr zone|zones", k): return "hr_zones"
    if re.search(r"predictor|prediction|how fast can i run|finish time|time calculator", k): return "time_predictor"
    if re.search(r"pace (calculator|chart|converter)|calculator|converter", k): return "pace_calc"
    if re.search(r"fuel|nutrition|\bgels?\b|carb|hydrat|electrolyte|\beat\b", k): return "fueling"
    if re.search(r"taper", k): return "taper"
    if re.search(r"\bsub[ -]?\d|under \d|break(ing)? (\d|four|three|two)|\d hour marathon|negative split|in \d+ (weeks|months)", k) and not re.search(r"shoe", k): return "goal_time"
    if re.search(r"race readiness|ready to race|am i ready|are you ready", k): return "race_readiness"
    if re.search(r"hyrox|ultra|trail|utmb", k): return "hyrox_other"
    if re.search(r"garmin|coros|apple watch|whoop|polar|suunto|fitbit", k):
        return "watch_integration" if re.search(r"plan|coach|train|connect|sync|workout", k) else "watch_buying"
    if re.search(r"running watch|smart ?watch", k): return "watch_buying"
    if re.search(r"shoes?|sneakers|trainers|footwear", k): return "shoes_generic"
    if re.search(r"higdon|hanson|galloway|pfitzinger|jack daniels|nike|brooks|rei\b|lululemon|zwift|adidas|asics|garmin plan|runners world|runner's world|marathon handbook|hal ", k) and re.search(r"plan", k): return "brand_plan"
    if re.search(r"couch|c25k", k): return "c25k"
    if re.search(r"\bapp\b|apps\b", k): return "running_app"
    if re.search(r"long run", k): return "long_run"
    if re.search(r"first marathon|beginner.*marathon|marathon.*beginner|how to (run|train for) a marathon|marathon for beginners", k): return "marathon_first"
    if re.search(r"half", k): return "half_plan"
    if re.search(r"5k|10k|5 km|10 km", k): return "plan_10k_5k"
    if re.search(r"marathon|42", k): return "marathon_plan"
    if re.search(r"beginner|how to|start running|tips|run longer|lose weight", k): return "beginner_running"
    if re.search(r"plan|program|schedule|training|workout", k): return "plan_generic"
    return "off_topic"

def intent_of(k, cl):
    if re.search(r"calculator|predictor|converter|pace chart|quiz|tool", k): return "tool"
    if re.search(r"\bapp\b|apps|download|alternative|\bvs\b|best .* (app|watch|shoes)|coach\b", k): return "commercial"
    if re.search(r"plan|schedule|program|pdf|template|workout", k): return "plan-seeking"
    if re.search(r"^(how|what|why|when|is|can|should|does)\b|tips|guide|mean|explained", k): return "informational"
    if cl in ("india_race_calendar", "india_race_info"): return "navigational/informational"
    return CL[cl][6]

# ---------- master DB (phases 3-4)
ext = collections.Counter()
for k in allk:
    ws = k.split()
    for n in range(1, len(ws)):  # count keywords that extend a shorter phrase
        ext[" ".join(ws[:n])] += 1
rows = []
seen_cl = {}
for k in allk:
    cl = classify(k); seen_cl[k] = cl
    r = raw[k]
    inclean = "yes"
    rows.append([k, cl, r["seed"], r["source"], r["date"], r["geo"], len(k.split()), ext.get(k, 0)])
wr("p3_master_keywords.csv", ["keyword","topic_cluster","seed","source","date","geo","word_count","autocomplete_extensions"], rows)

# ---------- cluster demand proxy (phase 5)
cnt = collections.Counter(seen_cl[k] for k in allk)
# Trends probe from earlier session (IN, 12m, relative index; marathon=45 on that probe's scale)
trends = [("marathon",45,"head term"),("running shoes",44,"shoes_generic/shoes_india"),("running app",5,"running_app"),
          ("mumbai marathon",2.4,"india_race_calendar"),("marathon training plan",0.0,"marathon_plan (reads ~0, i.e. below Trends threshold relative to 'marathon')")]
wr("p5_trends_probe.csv", ["term","relative_index_IN_12m","maps_to","note"], [[a,b,c,"relative only; no absolute volume; from earlier local session. Re-run blocked in cloud container (proxy 403 to trends.google.com)"] for a,b,c in trends])
def dscore(n):  # autocomplete breadth proxy -> 1..4 (never 5 without Trends/volume evidence)
    return 1 if n < 20 else 2 if n < 80 else 3 if n < 250 else 4
trends_map = {"shoes_generic":5,"running_app":3,"india_race_calendar":2,"marathon_plan":1}
demand = {}
drows = []
for c in CL:
    n = cnt.get(c, 0); p = dscore(n)
    basis = "autocomplete breadth only"
    if c in trends_map:
        t = trends_map[c]; basis = f"Trends probe overrides breadth proxy (breadth={p})"; p = t
    demand[c] = p
    drows.append([c, CL[c][0], n, p, basis, "UNKNOWN (no source)", "low" if c not in trends_map else "low-medium"])
wr("p5_demand_by_cluster.csv", ["cluster","label","distinct_autocomplete_phrases","demand_score_1to5","basis","absolute_monthly_volume","confidence"], drows)

# ---------- keyword-level scoring (phases 7 & 9)
W = {"base":(.20,.15,.15,.15,.15,.15,.05),"demand_heavy":(.15,.30,.10,.10,.10,.20,.05),
     "value_heavy":(.25,.10,.15,.10,.10,.25,.05),"low_competition":(.15,.10,.10,.30,.25,.05,.05),
     "equal":(1/7,)*7}
WN = ["relevance","demand","intent","competition_ease","opportunity","value","confidence"]
INT_SC = {"tool":5,"commercial":5,"plan-seeking":4,"commercial-investigation":4,"informational":3,"navigational/informational":2,"navigational":1,"n/a":1}
def kwscore(k, cl):
    lab, rel, val, comp, opp, conf, dint, _ = CL[cl]
    it = intent_of(k, cl); d = demand[cl]
    d = max(1, min(5, d + (1 if ext.get(k,0) >= 3 else 0) - (1 if len(k.split()) >= 7 else 0)))
    return it, [rel, d, INT_SC.get(it,3), comp, opp, val, conf]
def sc(v, w): return round(sum(a*b for a,b in zip(v,w)), 3)
krows = []
for k in allk:
    cl = seen_cl[k]
    it, v = kwscore(k, cl)
    krows.append([k, cl, it] + v + [sc(v, W["base"])])
wr("p7_p9_keyword_scores.csv", ["keyword","topic_cluster","intent_label","relevance","demand","intent_score","competition_ease","opportunity","value","confidence","score_base"], krows)

# ---------- cluster scoring + weight sensitivity
crows = []
cs = {}
for c,(lab,rel,val,comp,opp,conf,dint,ev) in CL.items():
    if c == "off_topic": continue
    v = [rel, demand[c], INT_SC.get(dint.split("/")[0], 3), comp, opp, val, conf]
    cs[c] = {n: sc(v, w) for n, w in W.items()}; cs[c]["v"] = v
rank = {n: {c:i+1 for i,c in enumerate(sorted(cs, key=lambda c:-cs[c][n]))} for n in W}
def tier(s): return "Tier 1" if s >= 3.9 else "Tier 2" if s >= 3.3 else "Tier 3" if s >= 2.7 else "Tier 4 (park)"
for c in sorted(cs, key=lambda c: -cs[c]["base"]):
    rr = [rank[n][c] for n in W]
    stab = "stable" if max(rr)-min(rr) <= 4 else "weight-sensitive"
    crows.append([c, CL[c][0], cnt[c]] + cs[c]["v"] + [cs[c][n] for n in W] + [tier(cs[c]["base"]), min(rr), max(rr), stab])
wr("p9_cluster_scores.csv", ["cluster","label","n_keywords"]+WN+[f"score_{n}" for n in W]+["tier_base","best_rank","worst_rank","rank_stability"], crows)

PRIM = {"missed_training":"garmin training plan missed workout","india_heat":"mumbai marathon weather",
        "india_race_plans":"tata mumbai marathon training plan","goal_time":"sub 2 half marathon","shoes_india":"best running shoes for beginners india",
        "brand_plan":"marathon training plan hal higdon","race_readiness":"race readiness (manual; autocomplete returned only unrelated 'Race Ready' brands)"}
# ---------- phase 8: primary/secondary per cluster
prow = []
for c in sorted(cs, key=lambda c:-cs[c]["base"]):
    items = [r for r in krows if r[1]==c and r[3] >= 3 and not r[0].startswith(" ")]
    items.sort(key=lambda r:(-r[4], -ext.get(r[0],0), len(r[0].split()), r[0]))
    prim = items[0][0] if items else ""
    sec = [r[0] for r in items[1:9]]
    if c in PRIM:  # curated: data-ranked pick was off-intent (analyst override, shown in column)
        prim = PRIM[c]; sec = [r[0] for r in items if r[0] != prim][:8]
    prow.append([c, CL[c][0], prim, "; ".join(sec), cnt[c]])
wr("p8_clusters.csv", ["cluster","label","primary_keyword","secondary_keywords","n_keywords"], prow)
print({c:cnt[c] for c in CL})
for r in crows: print(r[0], r[-5:], r[3:10])
