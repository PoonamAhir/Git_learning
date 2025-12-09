from openpyxl import Workbook
workbook = Workbook()
worksheet = workbook.active

worksheet['A1'] = 'name'
worksheet['B1'] = 'place'
worksheet['C1'] = 'salary'
worksheet['D1'] = 'mail_id'

dataload = [
    ['poonam','walwa',100000,'punam@gmail.com'],
    ['kapil','belwale',200000,'kapil@gmail.com'],
    ['kamal','walwa',1500,'kamal@gmail.com']
]

for row in dataload:
    worksheet.append(row)

workbook.save('test.xlsx')