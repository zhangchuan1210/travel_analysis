from sqlalchemy import create_engine
import pandas as pd
import jieba
def travel_data_split():
    # 1. 建立数据库连接，读取数据并存储为 DataFrame 格式
    conn = create_engine("mysql+pymysql://root:123456@192.168.140.226:3306/travel_db")
    sql = "select comments from sight_comments"
    df1 = pd.read_sql(sql, conn)
    comments = df1.comments.values.tolist()
    # 2. 使用 jieba 分词模块进行分词处理
    comment_s = []
    for line in comments:
        ls = str(line)
        comment_cut = jieba.lcut(ls)
        comment_s.append(comment_cut)
    # 3. 读取不同类型的停用词，使用停用表
    stopwords = pd.read_excel("stopwords0.xlsx")
    baidu = "baidu_stopwords.txt"
    cn = "cn_stopwords.txt"
    hit = "hit_stopwords.txt"
    scu = "scu_stopwords.txt"
    # 将停用词表连接成列表
    stopwords = stopwords.stopword.values.tolist()
    baidu_stopwords = [line.strip() for line in open(baidu, 'r', encoding='utf-8').readlines()]
    cn_stopwords = [line.strip() for line in open(cn, 'r', encoding='utf-8').readlines()]
    hit_stopwords = [line.strip() for line in open(hit, 'r', encoding='utf-8').readlines()]
    scu_stopwords = [line.strip() for line in open(scu, 'r', encoding='utf-8').readlines()]
    stopwords[0:0] = baidu_stopwords
    stopwords[0:0] = cn_stopwords
    stopwords[0:0] = hit_stopwords
    stopwords[0:0] = scu_stopwords
    # 使用停用表处理评论分词
    comment_clean = []
    for line in comment_s:
        line_clean = []
        for word in line:
            if word not in stopwords:
                line_clean.append(word)
        comment_clean.append(line_clean)
    # 统计每个词语的个数，先去重
    title_clean_dist = []
    for line in comment_clean:
        line_dist = []
        for word in line:
            if word not in line_dist:
                line_dist.append(word)
        title_clean_dist.append(line_dist)
    # 将所有词语转换为一个 list
    allwords_clean_dist = []
    for line in title_clean_dist:
        for word in line:
            allwords_clean_dist.append(word)
    # 将词频清理转换成 DataFrame 格式并存储
    allwords_clean_dist = pd.DataFrame({"allwords": allwords_clean_dist})
    word_count = pd.DataFrame(allwords_clean_dist.allwords.value_counts()).reset_index()
    word_count.columns = ['word', 'count']
    word_count.to_sql("word_count", con=conn)
