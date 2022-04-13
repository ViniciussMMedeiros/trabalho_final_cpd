import pandas as pd

data = pd.read_csv("./src/data.csv")

playerNamesData = pd.DataFrame(data, columns=['PLAYER'])
playerNames = [i[0] for i in playerNamesData.values.tolist()]

clubsData = pd.DataFrame(data, columns=['CLUB'])
clubs = [i[0] for i in clubsData.values.tolist()]

positionData = pd.DataFrame(data, columns=['POS'])
position = [i[0] for i in positionData.values.tolist()]

overallData = pd.DataFrame(data, columns=['OVR'])
overall = [i[0] for i in overallData.values.tolist()]

paceData = pd.DataFrame(data, columns=['PAC'])
pace = [i[0] for i in paceData.values.tolist()]

shootingData = pd.DataFrame(data, columns=['SHO'])
shooting = [i[0] for i in shootingData.values.tolist()]

passingData = pd.DataFrame(data, columns=['PAS'])
passing = [i[0] for i in passingData.values.tolist()]

dribblingData = pd.DataFrame(data, columns=['DRI'])
dribbling = [i[0] for i in dribblingData.values.tolist()]

defendingData = pd.DataFrame(data, columns=['DEF'])
defending = [i[0] for i in defendingData.values.tolist()]

physicalData = pd.DataFrame(data, columns=['PHY'])
physical = [i[0] for i in physicalData.values.tolist()]

#################### IMPRIMINDO PARA VERIFICAR SE OS DADOS FORAM CAPTURADOS CORRETAMENTE DO ARQUIVO PARA AS LISTAS ####################
dataArr = []
dataArr.append(playerNames)
dataArr.append(clubs)
dataArr.append(position)
dataArr.append(overall)
dataArr.append(pace)
dataArr.append(shooting)
dataArr.append(passing)
dataArr.append(dribbling)
dataArr.append(defending)
dataArr.append(physical)

for data in dataArr:
    print("\n\n", data)
#######################################################################################################################################