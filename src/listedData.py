import pandas as pd
import pickle

data = pd.read_csv("./src/data.csv")

playerNamesData = pd.DataFrame(data, columns=['PLAYER'])
playerNames = [i[0] for i in playerNamesData.values.tolist()]

with open('./src/dataFiles/playerNames.pkl', 'wb') as f:
    pickle.dump(playerNames, f)

clubsData = pd.DataFrame(data, columns=['CLUB'])
clubs = [i[0] for i in clubsData.values.tolist()]
with open('./src/dataFiles/clubs.pkl', 'wb') as f:
    pickle.dump(clubs, f)

positionData = pd.DataFrame(data, columns=['POS'])
position = [i[0] for i in positionData.values.tolist()]
with open('./src/dataFiles/position.pkl', 'wb') as f:
    pickle.dump(position, f)

overallData = pd.DataFrame(data, columns=['OVR'])
overall = [i[0] for i in overallData.values.tolist()]
with open('./src/dataFiles/overall.pkl', 'wb') as f:
    pickle.dump(overall, f)

paceData = pd.DataFrame(data, columns=['PAC'])
pace = [i[0] for i in paceData.values.tolist()]
with open('./src/dataFiles/pace.pkl', 'wb') as f:
    pickle.dump(pace, f)

shootingData = pd.DataFrame(data, columns=['SHO'])
shooting = [i[0] for i in shootingData.values.tolist()]
with open('./src/dataFiles/shooting.pkl', 'wb') as f:
    pickle.dump(shooting, f)

passingData = pd.DataFrame(data, columns=['PAS'])
passing = [i[0] for i in passingData.values.tolist()]
with open('./src/dataFiles/passing.pkl', 'wb') as f:
    pickle.dump(passing, f)

dribblingData = pd.DataFrame(data, columns=['DRI'])
dribbling = [i[0] for i in dribblingData.values.tolist()]
with open('./src/dataFiles/dribbling.pkl', 'wb') as f:
    pickle.dump(dribbling, f)

defendingData = pd.DataFrame(data, columns=['DEF'])
defending = [i[0] for i in defendingData.values.tolist()]
with open('./src/dataFiles/defending.pkl', 'wb') as f:
    pickle.dump(defending, f)

physicalData = pd.DataFrame(data, columns=['PHY'])
physical = [i[0] for i in physicalData.values.tolist()]
with open('./src/dataFiles/physical.pkl', 'wb') as f:
    pickle.dump(physical, f)