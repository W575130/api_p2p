import pymysql
# 建立数据库对象
host = 'localhost'
port = 3306
user = 'root'
pwd = 'root'
db = 'p2p'

# 查询语法
def readMSN(mobile):
    select_sql = 'select * from cyo_mobile_verify_code where mobile= {}'.format(mobile)
    # 建立sql连接对象
    conn = pymysql.connect(host=host, port=port, user=user, password=pwd, db=db)
    # 生成游标对象
    cur = conn.cursor()
    # 执行sql语句
    cur.execute(select_sql)
    # 查询sql结果
    data = cur.fetchone()
    return data[1]
    print(data)