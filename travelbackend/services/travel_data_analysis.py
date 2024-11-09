from sqlalchemy import create_engine
import pandas as pd
from snownlp import SnowNLP

def travel_emotion_analysis():
     engine = create_engine("mysql+pymysql://root:123456@192.168.140.226:3306/travel_db")
     sql = "select comments from sight_comments"
     comment = pd.read_sql(sql, con=engine)
     reader = comment["comments"]
     xjb = [],mp = [],ms = [],values = []
     for line in reader:
         content = str(line)
         if '性价比' in content:
             xjb.append(content)
         if '门票' in content:
             mp.append(content)
         if '民宿' in content:
             ms.append(content)
         values.extend([xjb, mp, ms])
         j_value = [],z_value = [],x_value = []
         for v in values:
             j=0
             x=0
             z=0
             for i in v:
                 score = SnowNLP(i).sentiments
                 if score <= 0.3:
                     x+=1
                 elif 0.3 < score < 0.7:
                     z+=1
                 else:
                     j+=1
             j_value.append(j),z_value.append(z),x_value.append(x)
         words=['性价比','门票','民宿']
         c={}
         d=pd.DataFrame(c)
         d.to_sql(name='emotion',con=engine,if_exists='append',index=False)
