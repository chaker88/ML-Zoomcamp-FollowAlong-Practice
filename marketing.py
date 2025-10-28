import requests

# url = 'http://localhost:9696/predict'
url = 'https://solitary-morning-661.fly.dev/predict' # I destroyed the deployment to avoid charges (check README for instructions to redeploy)
customer = {
    "gender": "male",
    "seniorcitizen": 1,
    "partner": "yes",
    "dependents": "no",
    "phoneservice": "no",
    "multiplelines": "no",
    "internetservice": "fiber_optic",
    "onlinesecurity": "no",
    "onlinebackup": "no",
    "deviceprotection": "no",
    "techsupport": "no",
    "streamingtv": "yes",
    "streamingmovies": "yes",
    "contract": "one_year",
    "paperlessbilling": "no",
    "paymentmethod": "credit_card_(automatic)",
    "tenure": 51,
    "monthlycharges": 20.35,
    "totalcharges": 152.1
}
response = requests.post(url, json=customer)
churn = response.json()

print("resonse:", churn)


if churn['churn_decision']:
    print('customer is likely to churn, send promo')
else:
    print('customer is not likely to churn')