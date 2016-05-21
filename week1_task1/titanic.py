import pandas

data = pandas.read_csv('titanic.csv', index_col='PassengerId')

#print headers
#print(data[:0])
#print first row
#print(data[:1])
#print columnt by index name
#print(data['Name'])
#print first 5 rows
#print(data.head())
#each value count
#print(data['Pclass'].value_counts())

#task 1
genderCounts = data['Sex'].value_counts()
print genderCounts['male'], genderCounts['female']

#task 2
dataSurvived = data['Survived']
print round(float(dataSurvived.value_counts()[1]) * 100 / float(dataSurvived.size), 2)

#task 3
dataPclass = data['Pclass']
print round(float(dataPclass.value_counts()[1] * 100) / float(dataPclass.size), 2)

#task 4
dataAge = data['Age']
print round(dataAge.sum() / dataAge.count(), 2), round(dataAge.median(), 2)

#task 5
dataSibSp = data['SibSp']
dataParch = data['Parch']
print round(dataSibSp.corr(dataParch, method='pearson'), 2)

#task 6
dataName = data['Name'].str.upper()
dataName = dataName.str.strip();
dataName = dataName.str.extract('(?P<Gender>MR\.\s|MRS\.\s|MISS.\s)(?P<Name>.*)')
womenNames = dataName[dataName['Gender'].isin(['MRS. ', 'MISS. '])]
print womenNames
print womenNames['Name'].value_counts()
