from Synergy.Synergy import *

userSelectCount = 4
ingredientNumber = 5
botSelect = "APPLE"
weightDP = {}
botChoiceList = []

weightDP[botSelect] = [-1]
weightDP['COCAINE'] = [Synergy[botSelect].value['COCAINE']]
weightDP['BANANA'] = [Synergy[botSelect].value['BANANA']]
weightDP['COKE'] = [Synergy[botSelect].value['COKE']]
weightDP['GUN'] = [Synergy[botSelect].value['GUN']]
botChoiceList.append(botSelect)
idx = 0

# 기능: 선택한 식재료를 기반으로 가장 큰 시너지 값을 가진 식재료를 리턴한다
# 출력: 가장 큰 시너지 값을 가진 식재료
def Greedy():
    greedDict = {}
    for name in Synergy.getSynergyList():
        greedDict[name] = max(weightDP[name])
        if (-1 in weightDP[name]): continue
    result = max(greedDict.values())

    for name in greedDict:
        if (greedDict[name] == result): 
            return name
        
# 기능: DP테이블에서 업데이트를 해야할 인덱스의 순서를 모두 업데이트한다
# 입력: 업데이트 해야할 인덱스
def updateDP(index):
    weightDP[botSelect].append(-1)
    # 시너지 재료들 전부를 순회합니다
    for name in Synergy.getSynergyList():
        # -1이 있으면 스킵
        if (-1 in weightDP[name]): continue
        sum = 0
        # 로봇이 선택한 명단과 선택할 재료를 연산
        for i in botChoiceList:
            sum += Synergy[name].value[i]
        weightDP[name].append(weightDP[botSelect][index - 1] + sum)

while (idx < userSelectCount - 1):
    botSelect = Greedy()
    botChoiceList.append(botSelect)
    updateDP(idx)
    idx += 1
    print(weightDP)
print(botChoiceList)