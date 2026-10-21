"""Merge OpenSEO tool output files (ranked keywords per competitor, keyword research expansions)
into one master table. Usage: python merge_openseo.py <tool-results dir>"""
import csv, glob, json, os, sys, collections

d = sys.argv[1]
rows = {}  # keyword -> dict


def add(kw, vol, kd, intent, source, rank=None, url=None, trend=None):
    r = rows.setdefault(kw, {"keyword": kw, "volume": None, "kd": None, "intent": "", "sources": set(), "ranks": [], "pages": set(), "trend": None})
    if vol is not None:
        r["volume"] = vol if r["volume"] is None else max(r["volume"], vol)
    if kd is not None:
        r["kd"] = kd
    if intent:
        r["intent"] = intent
    r["sources"].add(source)
    if rank is not None:
        r["ranks"].append((source, rank))
    if url:
        r["pages"].add(url)


for f in sorted(glob.glob(os.path.join(d, "mcp-2a21affa*get_ranked_keywords*.txt"))):
    try:
        j = json.load(open(f, encoding="utf-8"))
    except Exception:
        continue
    target = j.get("target", "?")
    for k in j.get("keywords", []):
        kd = k["keyword_data"]
        ki = kd.get("keyword_info", {})
        s = k.get("ranked_serp_element", {}).get("serp_item", {})
        add(kd["keyword"], ki.get("search_volume"), kd.get("keyword_properties", {}).get("keyword_difficulty"),
            kd.get("search_intent_info", {}).get("main_intent", ""), "competitor:" + target,
            s.get("rank_absolute"), s.get("url"))
    print(os.path.basename(f)[-24:], target, len(j.get("keywords", [])), "of", j.get("totalCount"))

for f in sorted(glob.glob(os.path.join(d, "mcp-2a21affa*research_keywords*.txt"))):
    j = json.load(open(f, encoding="utf-8"))
    for res in j.get("results", []):
        seed = res.get("seed", "?")
        for k in res.get("rows", []):
            add(k["keyword"], k.get("searchVolume"), k.get("keywordDifficulty"), k.get("intent", ""), "expansion:" + seed)
        print("research seed", seed, len(res.get("rows", [])))

out = os.path.join("data", "openseo_master_candidates.csv")
with open(out, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["keyword", "monthly_volume_IN", "keyword_difficulty", "intent", "n_sources", "sources", "best_rank_by_domain", "ranking_pages"])
    for r in sorted(rows.values(), key=lambda x: -(x["volume"] or 0)):
        best = {}
        for s, rk in r["ranks"]:
            best[s] = min(rk, best.get(s, 999))
        w.writerow([r["keyword"], r["volume"] if r["volume"] is not None else "", r["kd"] if r["kd"] is not None else "", r["intent"], len(r["sources"]),
                    "; ".join(sorted(r["sources"])), "; ".join("%s=%s" % (k.replace("competitor:", ""), v) for k, v in best.items()), " | ".join(sorted(r["pages"]))[:400]])
print(len(rows), "unique keywords ->", out)
