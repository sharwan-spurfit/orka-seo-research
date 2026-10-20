# Orka Run: India SEO keyword research — brief and roadmap

Market: India, English. Free sources only. Date: 2026-10-20. Google Sheet: https://docs.google.com/spreadsheets/d/1jCDwY1JABbnksw1wKwQfeP2YR1b4K3614EpdHlDL7F0/edit All numbers trace to `data/*.csv` (built by `scripts/build_research.py`, `scripts/build_static.py`).

## Limits (read first)
1. **No absolute search volumes.** Nothing here is a monthly search count. Demand is a 1–4 proxy; a 5 needs real evidence.
2. **SERPs were read with a US-only search tool**, not google.co.in. India results will differ. Competition ratings are one analyst's judgment.
3. **Autocomplete is not volume.** It shows what Google suggests. About 530 of ~6,200 phrases are noise (e.g. "race ready go kart", "running stitch") and are kept in the database, scored low via the `off_topic` cluster.
4. **Google Trends could not be re-run** in this cloud session (the proxy returns 403 for trends.google.com). Only the earlier local 5-term probe exists: marathon 45, running shoes 44, running app 5, mumbai marathon 2.4, marathon training plan ~0 (relative, India, 12 months).
5. The autocomplete set found almost nothing for the three biggest SERP gaps (India race plans: 12 phrases, India heat: 4, missed training: 6). Those clusters are **bets on low-volume, high-fit queries**, not proven demand.
6. Rule kept: no keyword was filtered or weighted by the site's existing content or GSC rankings.

## Product assumptions (from the landing-page repo)
Free adaptive AI running-training app (iOS/Android). Plans from goal and race date, re-plans after missed runs, reads HRV/sleep/HR from Apple Watch, Garmin, COROS, WHOOP, Strava, Apple Health. Site has a race catalog, free tools (time predictor, fueling calculator, race-readiness quiz, shoe finder), blog and /download.

## Method (12 phases)
1 Framework → `p1_framework.csv` · 2 Competitors → `p2_competitors.csv` · 3–4 Universe and expansion → `p3_master_keywords.csv` (6,199 phrases, source and date per row) · 5 Demand → `p5_*` · 6 SERPs → `p6_serp.csv` (22 rows; 6 read in full this session, rest from earlier notes) · 7 Intent/relevance → `p7_p9_keyword_scores.csv` · 8 Clusters → `p8_clusters.csv` · 9 Scoring → `p9_cluster_scores.csv` · 10 URL map → `p10_keyword_url_map.csv` · 11 Roadmap → `p11_roadmap.csv` · 12 Measurement → `p12_measurement.csv`.

Scoring: 1–5 on relevance, demand, intent, competition (5 = weak SERP), opportunity, value, confidence. Base weights .20/.15/.15/.15/.15/.15/.05, tested against demand-heavy, value-heavy, low-competition and equal weights.

## Results
| Tier | Clusters (base score) |
|---|---|
| 1 | Runna/Strava/NRC alternatives (4.30) · India race-specific plans (4.00) · Goal-time plans, sub-4 / sub-2 half / sub-50 10k (4.00) |
| 2 | Missed training / re-planning (3.85) · AI running coach (3.85) · Race time predictor (3.85) · India heat (3.65) · HRV (3.55) · Watch integrations (3.45) · First marathon (3.40) · 5K/10K plans (3.30) |
| 3 | Half plan, running app, fueling, race readiness, generic marathon plan, India shoes, pace calc, taper, generic plan, beginner running, India race calendar |
| 4 park | Generic shoes, long run, C25K, named-method plans, HR zones, watch buying, Hyrox/other, India race results/photos |

Weight sensitivity: alternatives, India race plans, goal-time, time predictor, HRV, watch integrations, first marathon stay within 4 rank places across all weight sets. Missed training, AI coach, India heat and 5K/10K move more (see `p9_cluster_scores.csv`). Plan accordingly: the stable Tier 1 items go first.

## What the SERPs showed (US-only tool)
- Mumbai race page at marathon-index says its week-by-week plan is "coming soon"; Delhi plan is behind a sign-up. No real race-specific plan found. Tata Mumbai Marathon is listed for 17 Jan 2027 in search results; verify on the official site.
- India heat: fatmarathoner and thin blogs; no sports-medicine source. One "add 10–20% time per 10°C" rule is unsourced — do not repeat it unsourced.
- HRV: guidance is mixed; Garmin itself says Training Readiness is not designed to predict performance; HRV needs ~3 weeks of nightly data for a baseline. Write the guide around trends, not single readings.
- India shoe lists are promotional, with spam mirror pages.
- Generic marathon/half plans and pace calculators are saturated (Nike, Runner's World, Marathon Handbook, Nuffield, On, Omni).

## Roadmap
Full table with outlines, links and metrics: `p11_roadmap.csv`.
- **Wave 1 (publish first):** missed-run re-planning guide · Tata Mumbai Marathon plan · Delhi/Bengaluru/Hyderabad race-plan sections · Strava alternative · Runna alternative · Indian heat guide.
- **Wave 2:** sub-2 half, sub-4 marathon, sub-50 10k · AI running coach landing · HRV guide · watch integration pages · predictor explainer.
- **Wave 3:** first marathon, 10K plan, fueling, India shoes, half plan, taper.
- **Wave 4:** generic marathon plan, only if earlier waves show traction.

Keyword-to-URL mapping (`p10`) was done after scoring. Slugs for existing tools and race pages were not available in this repo and are marked "slug to verify".

## Measurement
Search Console (country India) by cluster: impressions, clicks, average position; analytics events for install clicks and tool use; indexing; referring domains. Real demand data arrives from Search Console after publishing; re-score clusters quarterly and re-run `scripts/tr.py` (60 s gaps) from a machine that can reach Trends. Full list: `p12_measurement.csv`.

## Open items
- Run Trends (relative interest) for the Tier 1–2 head terms from a machine with access.
- Re-check Tier 1–2 SERPs from an India vantage point.
- Confirm existing page slugs before finalising Phase 10.
