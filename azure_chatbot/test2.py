import requests,datetime,json


testData= {'tenant_id': '9255f64b-1818-42e5-ad78-f619a9a7b1e7', 
'user_id': '29:1htJmKwuNtPEggpMm5kJ73ht47oIbddUOeEh1r1DFpf7vJmh83_C7Q3sBnFcxS3EJv5hHqcu0Po3_-dMmfqnMfA', 
'todo':  {'todo_id': 'XkX3CFai7L', 'todo_name': 'rsgaefadea', 
'todo_date': '2021-08-25 23:30', 
'todo_contents': '', 'todo_update_date': '2021/08/05', 
'todo_completed': False, 'employee_id': '120734'}}

testData2= {'tenant_id': '010281b3-d5d6-4bc8-b561-bf4794b97036', 
'user_id': '29:1lNWDIz8Jn0YgoFx8LTJWrkqchAJb1Vg0bJK-PvHxe2FHzNXzFHYaeA0P9j58qQyPVVUCKUfpbZlBNcepHMaajg', 
'todo':  {'todo_id': 'XkX3CFai7L', 'todo_name': 'rsgaefadea', 
'todo_date': '2021-08-25 23:30', 
'todo_contents': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', 'todo_update_date': '2021/08/05', 
'todo_completed': False, 'employee_id': '120734'}}

r=requests.post('https://azure-bot-framework.herokuapp.com/api/v1/cron-messages',data=json.dumps(testData2))#

print(r.content.decode('utf-8'))