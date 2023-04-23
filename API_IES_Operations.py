from API_IES import DataList, Dataset

data = Dataset()
print('Enviando um request GET:')
print(data.get(data_id=1))
print(2*'\n')
print('Enviando um request DELETE:')
print(data.delete(data_id=1))

print(2*'\n')
#data.put()