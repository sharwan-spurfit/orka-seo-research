from pytrends.request import TrendReq
import time,csv,warnings;warnings.filterwarnings("ignore")
terms=["running app","marathon training plan","half marathon training plan","10k training plan","5k training plan","running training plan","couch to 5k","marathon training plan for beginners","first marathon","how to train for a marathon","sub 4 marathon","sub 2 half marathon","sub 50 10k","running app","ai running coach","running coach app","best running app","strava alternative","runna","nike run club","garmin coach","marathon pace calculator","pace calculator","running pace calculator","marathon time predictor","race time predictor","half marathon pace chart","marathon fueling","marathon nutrition","marathon gel","running shoes","best running shoes","best running shoes for beginners","running shoes india","hrv running","heart rate zones running","zone 2 running","marathon taper","long run","mumbai marathon","delhi half marathon","bengaluru marathon","tata mumbai marathon","marathon india","marathon calendar india","running for beginners","how to start running","how to run longer without stopping","half marathon india","running plan after missing workouts","how to improve running pace"]
anchor="marathon"
p=TrendReq(hl='en-IN',tz=330,retries=1)
res={}
rest=[t for t in terms if t!=anchor]
for i in range(0,len(rest),4):
    b=rest[i:i+4]+[anchor]
    for a in range(3):
        try:
            p.build_payload(b,geo='IN',timeframe='today 12-m'); d=p.interest_over_time(); break
        except Exception as e:
            time.sleep(60); d=None
    if d is None: print("fail",b); continue
    m=d[b].mean(); sc=m[anchor]
    for t in rest[i:i+4]: res[t]=(m[t],sc)
    res[anchor]=(sc,sc)
    time.sleep(25)
# normalise to anchor=100
with open("trends_in.csv","w",newline="",encoding="utf-8") as f:
    w=csv.writer(f);w.writerow(["term","avg_interest_12m_IN","anchor_avg_in_batch","index_vs_marathon_100"])
    for t,(v,s) in res.items(): w.writerow([t,round(v,1),round(s,1),round(100*v/s,1) if s else ""])
print(open("trends_in.csv").read())
