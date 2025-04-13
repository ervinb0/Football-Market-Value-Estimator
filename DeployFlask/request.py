import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={"age":25, "starts":57, "min":4117, "gls":28, "ast":11, "pos":3, "grade":4, "league":5, "club":42})

print(r.json())