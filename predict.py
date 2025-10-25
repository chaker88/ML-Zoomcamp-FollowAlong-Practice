import pickle
import sys
import json

with open("model.bin","rb") as f_in:
    pipeline = pickle.load(f_in)


customer = json.loads(sys.argv[1])
# customer= (
#     {'gender': 'male',
#  'seniorcitizen': 1,
#  'partner': 'yes',
#  'dependents': 'no',
#  'phoneservice': 'no',
#  'multiplelines': 'no',
#  'internetservice': 'fiber_optic',
#   'onlinesecurity': 'no',
#  'onlinebackup': 'no',
#  'deviceprotection': 'yes',
#  'techsupport': 'no',
#  'streamingtv': 'yes',
#  'streamingmovies': 'yes',
#  'contract': 'one_year',
#  'paperlessbilling': 'no',
#  'paymentmethod': 'credit_card_(automatic)',
#  'tenure': 12,
#  'monthlycharges': 20.35,
#  'totalcharges': 152.1}
# )


churn = pipeline.predict_proba(customer)[0,1]
print(churn)
if churn >=0.50:
    print("Let's send a promotion to the customer")
else:
    print("We don't need to send a promotion to the customer")
