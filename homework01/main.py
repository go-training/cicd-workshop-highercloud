import redis

# 連接到本機Redis伺服器
r = redis.Redis(host='localhost', port=6379, db=0)

# 設定鍵值對
r.set('key', 'value')

# 取得值
value = r.get('key')
print(value)
