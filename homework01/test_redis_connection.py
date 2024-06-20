import unittest
import redis

class TestRedisConnection(unittest.TestCase):
  def setUp(self):
    # 在每個測試案例執行前連接到Redis伺服器
    self.r = redis.Redis(host='localhost', port=6379, db=0)

  def tearDown(self):
    # 在每個測試案例執行後關閉Redis連線
    self.r.close()

  def test_set_and_get_value(self):
    # 測試設定鍵值對並取得值
    self.r.set('test_key', 'test_value')
    value = self.r.get('test_key')
    self.assertEqual(value, b'test_value')

if __name__ == '__main__':
  unittest.main()
