import csv

# OpenSEO/DataForSEO India, English, pulled 2026-10-21 for re-seeded (competitor-derived) keywords.
# Only rows with volume >= 20, plus notable 10-volume plan structures. Source: get_keyword_metrics.
D = """marathon training plans|18100|10
half marathon training plans|1600|10
running plan beginner|480|15
pace calculator marathon|390|47
how to train marathon|320|0
running program|320|75
running plan half marathon|320|11
running training plans|260|30
running training plan 5k|260|21
running exercise plan|210|26
running plan for 5k|210|19
beginner marathon training plan|210|71
running schedule half marathon|210|11
running eating plan|170|3
running meal plan|170|0
running nutrition plan|170|0
running plan|170|91
running planner|170|91
running plan lose weight|140|72
running plan weight loss|140|15
running program weight loss|140|16
running for fat loss plan|140|12
beginner 10k training plan|110|
how to train for running|110|4
running hiit program|90|
running training apps|90|66
bangalore marathon training|70|
marathon training in bangalore|70|
marathon training in mumbai|70|
ultra marathon training plan|70|
strength training vs running|50|
weight training vs running|50|
running plan marathon|40|14
running program marathon|40|
best running training app|40|58
boston marathon training plan|40|
16 week marathon training plan|40|
couch to 10k training plan|40|
running plan for 10k|30|0
advanced marathon training plan|30|
apps for marathon training|30|
first marathon training plan|30|
marathon training eating plan|30|
running program for 10k|30|
running training plan 10k|30|28
running workout plan pdf|30|
12 week marathon training plan|30|
sub 20 5k training plan|30|
10 mile training plan|20|
50k training plan|20|
couch to half marathon|20|
running lifting program|20|
marathon training plan km|20|
marathon training program km|20|
running training app free|20|
20 week marathon training plan|20|
8 week 10k training plan|20|
how to learn to run|20|62
8k training plan|10|
couch to marathon|10|
couch to full marathon|10|
intermediate marathon training plan|10|
easy marathon training plan|10|
best marathon training plan|10|
marathon training plan app|10|
learn to run schedule|10|
running in hot weather|10|
15k training plan free|0|"""

with open("data/openseo_reseed_metrics_IN.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["keyword", "monthly_volume_IN", "keyword_difficulty", "source", "date"])
    for line in D.split("\n"):
        k, v, kd = line.split("|")
        w.writerow([k, v, kd, "OpenSEO/DataForSEO get_keyword_metrics (loc 2356, en); ~590 re-seeded keywords checked, rows below 10 omitted", "2026-10-21"])
print("ok")
