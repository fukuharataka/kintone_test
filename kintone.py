import requests
import json

# APIトークンを設定
api_token = "api_token"

# Kintoneのドメイン名
kintone_domain = "kintone_domain"

# アプリID
app_id = "0000"

# URLを構築
url = f"https://{kintone_domain}.kintone.com/k/v1/record.json"

# ヘッダー情報
headers = {
    "X-Cybozu-API-Token": api_token,
    "Content-Type": "application/json"
}

record ={}

data = {
    "app": app_id,
    "record": record
}

# POSTリクエストを実行
response = requests.post(url, headers=headers, data=json.dumps(data))

# レスポンスを表示
print(response.json())

