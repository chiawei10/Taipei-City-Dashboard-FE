import pandas as pd

# 讀取 JSON 檔案
file_path = "C:/Users/Wenchi/Downloads/traffic111_110 (1).json"
df = pd.read_json(file_path)

# 將 'datetime' 欄位轉換為 datetime 格式
df['datetime'] = pd.to_datetime(df['datetime'])

# 抓出星期五同一天且是酒駕，並且發生時間在01:00-02:00的資料
friday_drunk_data_01_02 = df[(df['week'] == '五') & (df['drunk_driving'] == '酒駕') & (df['datetime'].dt.hour == 23)]

# 顯示結果
print(friday_drunk_data_01_02)

# 計算資料筆數
num_records = len(friday_drunk_data_01_02)
print(f"共有 {num_records} 筆資料符合條件。")
