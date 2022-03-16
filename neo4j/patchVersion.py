from neo4jUtil import getNeo4jConn
from neo4jMethod import addAuthorBookTypeRelations
# match (n) detach delete n  删库
# MATCH (n:`图书中文名`) RETURN count(*) 查询某一节点数量

# MATCH (n:`专业类型标签`{name:'科技'})-[]-()  RETURN count(*) 查询某一节点的关系数量
# MATCH (n:`专业类型标签`{name:'科技'})-[]-(m:`专业类型标签`)  RETURN m
if __name__ == "__main__":
    # 获取neo4j连接
    graphCon = getNeo4jConn()
    # 测试
    title = "最受欢迎的250本小说"
    tags = ["Top250"]
    # 科技
    title = "科技"
    tags = ["科普","互联网","科学","编程","交互设计","算法","用户体验","web","交互","通信","UE","神经网络","UCD","程序"]
    for tag in tags:
        addAuthorBookTypeRelations(graphCon,title,tag)
        print(tag,"创建完毕")
    # 经管
    title = "经管"
    tags = ["经济学","管理","经济","商业","金融","投资","营销","理财","创业","股票","广告","企业史","策划"]
    for tag in tags:
        addAuthorBookTypeRelations(graphCon,title,tag)
        print(tag,"创建完毕")
    # 生活
    title = "生活"
    tags = ["爱情","成长","生活","心理","女性","旅行","励志","教育",
            "摄影","职场","美食","游记","灵修","健康","情感","人际关系",
            "两性","养生","手工","家居","自助游"]
    for tag in tags:
        addAuthorBookTypeRelations(graphCon,title,tag)
        print(tag,"创建完毕")
    # 文化
    title = "文化"
    tags = ["历史", "心理学", "哲学", "社会学", "传记", "文化", "艺术", "社会",
            "政治", "设计", "政治学", "宗教", "建筑", "电影", "中国历史", "数学",
            "回忆录", "思想", "人物传记", "艺术史", "国学", "人文", "音乐", "绘画",
            "西方哲学", "戏剧", "近代史", "二战", "军事", "佛教", "考古", "自由主义",
            "美术"]
    for tag in tags:
        addAuthorBookTypeRelations(graphCon,title,tag)
        print(tag,"创建完毕")
    # 流行
    title = "流行"
    tags = ["漫画", "推理", "绘本", "悬疑", "东野圭吾", "青春", "科幻", "言情",
            "推理小说", "奇幻", "武侠", "日本漫画", "耽美", "科幻小说", "网络小说", "三毛",
            "韩寒", "亦舒", "阿加莎·克里斯蒂", "金庸", "穿越", "安妮宝贝", "魔幻", "轻小说",
            "郭敬明", "青春文学", "几米", "J.K.罗琳", "幾米", "张小娴", "校园", "古龙",
            "高木直子", "沧月", "余秋雨", "张悦然"]
    for tag in tags:
        addAuthorBookTypeRelations(graphCon,title,tag)
        print(tag,"创建完毕")
    # 文学
    title = "文学"
    tags =["小说","文学","外国文学","经典","中国文学","随笔","日本文学","散文",
            "村上春树","诗歌","童话","名著","儿童文学","古典文学","余华","王小波",
            "当代文学","杂文","张爱玲","外国名著","鲁迅","钱钟书","诗词","茨威格",
           "米兰·昆德拉","杜拉斯","港台"]
    for tag in tags:
        addAuthorBookTypeRelations(graphCon,title,tag)
        print(tag,"创建完毕")