from enum import Enum

class Synergy(Enum):
    APPLE = {"BANANA": 1, "COKE": 3, "GUN": 7, "COCAINE": 2}
    COCAINE = {"APPLE": 2, "COKE": 4, "BANANA": 7, "GUN": 8}
    BANANA = {"APPLE": 3, "COCAINE": 7, "COKE": 4, "GUN": 1}
    COKE = {"APPLE": 3, "COCAINE": 5, "BANANA": 4, "GUN": 3}
    GUN = {"COCAINE": 2, "BANANA": 1, "COKE": 3, "APPLE": 0}
    
    def getSynergyList():
        return ['APPLE', 'COCAINE', 'BANANA', 'COKE', 'GUN']

userSelectCount = 4
ingredientNumber = 5
weightDP = {}

botChoiceList = []
botSelect = "APPLE"
weightDP[botSelect] = [-1]
weightDP['COCAINE'] = [Synergy[botSelect].value['COCAINE']]
weightDP['BANANA'] = [Synergy[botSelect].value['BANANA']]
weightDP['COKE'] = [Synergy[botSelect].value['COKE']]
weightDP['GUN'] = [Synergy[botSelect].value['GUN']]

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