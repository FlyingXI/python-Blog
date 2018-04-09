# encoding: utf-8
import tushare as ts
import json

result = ts.get_stock_basics()
print(result.shape)
result = result.head(2)
stockStr = result.to_json(orient='records', force_ascii=False)

myjson = json.loads(stockStr,encoding='utf8') #data是向 api请求的响应数据，data必须是字符串类型的
newjson = json.dumps(myjson, ensure_ascii=False)

print(myjson[0]['name'])
