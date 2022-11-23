from Algorithm.Synergy.Synergy import *
#from Synergy.Synergy import *

#userSelectCount = 4
weightDP = {}
botChoiceList = [] # ingredient_robot

# 처음 선택으로 DP테이블 세팅
def initSynergy(botFirstSelect, botList):
    for name in Synergy.getSynergyList():
        if (name == botFirstSelect) :
            continue
        weightDP[name] = [Synergy[botFirstSelect].value[name]]
        weightDP[botFirstSelect] = [-1]
    botList.append(botFirstSelect)
        
# 기능: 선택한 식재료를 기반으로 가장 큰 시너지 값을 가진 식재료를 리턴한다
# 출력: 가장 큰 시너지 값을 가진 식재료
def Greedy():
    greedDict = {}
    for name in Synergy.getSynergyList():
        #print(name)
        if (-1 in weightDP[name]): 
            continue
        greedDict[name] = max(weightDP[name])
    result = max(greedDict.values())

    for name in greedDict:
        if (greedDict[name] == result): 
            botChoiceList.append(name)
            return name
        
# 기능: DP테이블에서 업데이트를 해야할 인덱스의 순서를 모두 업데이트한다
# 입력: 업데이트 해야할 인덱스
def updateDP(index, botSelect, botList):
    weightDP[botSelect].append(-1)
    # 시너지 재료들 전부를 순회합니다
    for name in Synergy.getSynergyList():
        # -1이 있으면 스킵
        if (-1 in weightDP[name]): 
            continue
        sum = 0
        # 로봇이 선택한 명단과 선택할 재료를 연산
        for i in botList:
            print(i)
            sum += Synergy[name].value[i]
        weightDP[name].append(weightDP[botSelect][index - 1] + sum)
        
temp_list = ['SESAME_OIL', 'KOCHUJANG', 'MAYONNAISE']
#Synergy["SESAME_OIL"]

def sumSynergy(list):
    sum = 0
    for standard in list:
 #       print(standard)
        for obj in list:
  #          print(obj)
            if (standard == obj):
                continue
            sum += Synergy[standard].value[obj]
    sum = (int)(sum / 2)
    return sum

print(sumSynergy(temp_list))