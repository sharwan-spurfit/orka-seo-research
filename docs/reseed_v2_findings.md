# Re-seed v2: competitor-derived seeds (2026-10-21)

Why: the first 40 seeds were written by me from Orka's features and my own knowledge. This pass starts only from "running and marathon training plans" and competitor taxonomies.

## Seed sources (85 seeds, `scripts/ac2.py`)
- Plan structure from Hal Higdon (sitemap), Runna, Nike, Strava, Marathon Handbook, Mottiv and TrainingPeaks (site pages and search results).
- Levels (novice, intermediate, advanced), walkers and senior plans, 8k / 15k / 10-mile / 50k plans, week-length plans, base training, post-marathon recovery, strength and 80/20 plans, weight-loss and trail plans, plan formats (pdf, free, app), competitor and alternative queries.
- India framing from Red Bull India, On India, Fat Marathoner, adidas India guides: heat, working professionals, air pollution.
- Not competitor-derived: the 3 India race-training seeds (mumbai, bangalore, delhi). They are mine.

## Result
- 6,125 raw phrases, 5,805 after cleaning (`data/autocomplete_raw_v2.csv`).
- Only 1,564 (27%) also appear in the first set. 4,241 are new (`data/new_keywords_v2_only.csv`). The seed list changes the keyword pool a lot.
- About 1,000 of the new phrases are competitor-brand queries (runna, nike run club, garmin coach). Only the "alternative", "review", "price" and "vs" forms are usable.

| Theme (non-brand) | All | New vs v1 | Examples |
| --- | --- | --- | --- |
| Week-length plans (8-24 weeks) | 752 | 676 | 8 week running plan; 12 week 8k training plan |
| Levels (novice, beginner, intermediate, advanced) | 623 | 521 | running program beginner; 8k training plan advanced |
| Couch-to, run-walk, learn to run | 537 | 288 | couch to marathon; learn to run plan |
| Strength, gym, 80/20 | 284 | 266 | running gym plan; 80/20 rule running |
| Trail, ultra, 50k | 277 | 270 | 50k training plan; 50k training schedule |
| Goal times (sub-x, PB, Boston) | 295 | 220 | sub 20 5k training plan; couch to boston marathon |
| Odd distances (8k, 15k, 10 mile) | 140 | 139 | 8k training plan; 15k training plan; 10 mile training plan |
| Weight loss | 102 | 96 | running plan weight loss; running for fat loss plan |
| India heat, pollution, working professionals | 20 | 20 | how to run in hot weather (very few) |
| India price / presence of competitors | n/a | n/a | runna india price; nike run club india |

## What it does not tell us
- Volume was not checked. OpenSEO credits ran out (the 11 left were below the minimum for a request). Autocomplete shows that people type these phrases, not how often.
- Candidates to verify first (no volume yet): 50k training plan, 8k training plan, 15k training plan, 10 mile training plan, couch to marathon, learn to run plan, running plan weight loss, running gym plan, novice / intermediate / advanced marathon training plan, 12 and 16 week marathon training plan, marathon taper, runna review / runna alternative.

## Effect on the target list
- The plan-keyword core is confirmed by volume already pulled: marathon training plan (18,100), 10k (1,900), half marathon (1,600), 5k (1,000), couch to 5k (1,000), running plan for beginners (480), marathon training plan pdf (210).
- The India city race keywords did not come out of this competitor-derived pass. They came from my seeds and are validated by volume, but they are event-information intent, not training-plan intent. Treat them as an adjacent opportunity, not the core of a training-plan product.
- New plan-structure ideas worth a page each if volume holds: odd-distance plans (8k, 15k, 10 mile, 50k), level-specific marathon plans, week-length variants, couch-to-marathon, strength-integrated plans, weight-loss running plan.

## Update: volumes checked (OpenSEO upgraded, ~590 re-seeded keywords, India, 2026-10-21)
`data/openseo_reseed_metrics_IN.csv` holds the rows with volume of 20 or more plus notable 10-volume plan structures.

- **The long tail is thin.** Nearly every new plan variant is 10-40 searches a month: 8k plan 10, 50k plan 20, 10 mile plan 20, couch to marathon 10, 16 week marathon plan 40, 12 week marathon plan 30, intermediate marathon plan 10, advanced marathon plan 30, sub 20 5k plan 30. They do not justify their own pages. Fold them into the main plan pages as sections.
- **Demand is in a few head terms.** marathon training plan(s) 18,100 (KD 10); 10k training plan 1,900; half marathon training plan(s) 1,600; 5k training plan 1,000; couch to 5k 1,000; running plan beginner 480; running plan half marathon 320; how to train marathon 320; running training plans 260; running training plan 5k 260.
- **Generic terms are hard or small.** "running plan" 170 at KD 91; "running program" 320 at KD 75; "beginner marathon training plan" 210 at KD 71.
- **Weight-loss plans are small but easy.** running plan weight loss 140 (KD 15); running program weight loss 140 (KD 16); running for fat loss plan 140 (KD 12).
- **India city training terms are tiny.** marathon training in Bangalore 70; marathon training in Mumbai 70. "Marathon training plan india" returned no volume.
- Google Ads groups close variants, so "marathon training plans" repeating 18,100 is the same pool as "marathon training plan".
- Total plan-keyword demand in India is roughly 25,000-30,000 searches a month, and about 18,000 of it is the single marathon head term.
