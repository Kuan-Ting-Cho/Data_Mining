import random
import numpy as np
import pandas as pd

attribute_dict1 = {}
#---------------實作的收穫-------------------#
attribute_dict1['Reward from homework'] = {
    '1': -2, '2': -2, '3': -1, '4': -1, '5': 0, '6': 0, '7': 1, '8': 1, '9': 2, '10': 2}
attribute_dict1['Course relevance'] = {
    'no correlation': -2, 'modestly correlated': -1, 'moderately correlated': 1, 'highly correlated': 2}
attribute_dict1['Interdisciplinary learning'] = {
    'no': -2, 'uncertain': -1, 'a little': 0, 'fifty-fifty': 1, 'often': 2}
attribute_dict1['Cooperation and Discussion'] = {
    'without cooperation': -2, 'seldom': -1, 'common': 0, 'often': 1, 'always': 2}
##----------------reward = 4項相加*2--------------------------##

attribute_dict2 = {}
#---------------時間成本-------------------#
attribute_dict2['Homework numbers'] = {
    '>=7': 2, '5-6': 1, '3-4': -1, '1-2': -2}
attribute_dict2['Scale'] = {'large': 2, 'medium to large': 1,
                            'medium': 0, 'small to medium': -1, 'small': -2}
attribute_dict2['Average time spent'] = {
    '>10 hr': 2, '5-10 hr': 1, '3-5 hr': 0, '1-3 hr': -1, '<1 hr': -2}
attribute_dict2['Homework deadlines'] = {
    'a month': 2, 'three week': 1, 'two weeks': 0, 'one weeks': -1, 'three days': -2}
##----------------time_cost = 4項相加--------------------------##

attribute_dict3 = {}
#---------------感受-------------------#
attribute_dict3['Step by step'] = {
    'no': -2, 'uncertain': -1, 'fifty-fifty': 0, 'roughly': 1, 'fully qualified': 2}
attribute_dict3['Feeling'] = {'bored': -2, 'worried': -2, 'impatient': -1,
                              'confused': -1, 'interested': 1, 'motivated': 1, 'inspired': 2, 'rewarding': 2}
attribute_dict3['Difficulty of implementation'] = {
    'super hard': -2, 'very easy': -1, 'simple': 0, 'difficult': 1, 'moderate': 2}
attribute_dict3['Difficulty in understanding'] = {
    'super hard': -2, 'very easy': -1, 'simple': 0, 'difficult': 1, 'moderate': 2}
##----------------feel = 4項相加--------------------------##

attribute_dict4 = {}
#---------------學生能力-------------------#
attribute_dict4['Student qualifications'] = {
    'low': -2, 'between low/middle': -1, 'middle': 0, 'between middle/high': 1, 'high': 2}
attribute_dict4['Student concentration'] = {
    'low': -2, 'between low/middle': -1, 'middle': 0, 'between middle/high': 1, 'high': 2}
attribute_dict4['Student responsibility'] = {
    'low': -2, 'between low/middle': -1, 'middle': 0, 'between middle/high': 1, 'high': 2}
attribute_dict4['Research relevance'] = {
    'low': -2, 'between low/middle': -1, 'middle': 0, 'between middle/high': 1, 'high': 2}
##----------------ability = 4項相加--------------------------##

# Absolutely Right Rules

#--------共有 16 個有效的 Attribute--------#
# reward*2 (<=-8 : 低  -8 < & < 8 : 中 >=8 : 高 )
# time_cost、feel、ability (<=-4 : 低  -4< & < 4 : 中 >=4 : 高 )

#--------five rules--------#
# Rule1 = reward*2>=8 & time_cost<=-6(時間成本低，收穫高)

# Rule2 = reward*2>=8 & feel>=6(感受好，收穫高)

# Rule3 = reward*2>=8 & ability>=6(學生能力高，收穫高)

# Rule4 = reward*2>=8 & 4>=time_cost>=0 & 6>=feel>=2 & 6>=ability>=2(時間成本適中，感受適中偏好，學生能力適中偏高，收穫高)

# Rule5 = reward*2>=8 & time_cost>=4 & 6>=feel>=2 & -2>=ability>=-6(時間成本高，感受適中偏好，學生能力適中偏低，收穫高)


def data_generator(attribute_dict, num, case):
    # 0: >=8 1: >=6 2: >=4 3: 2-6之間 4: 0-4之間 5:-2 - -6之間 6: <=-6 7:隨機
    caseset = [0, 1, 2, 3, 4, 5, 6, 7]
    df = pd.DataFrame(columns=attribute_dict.keys())
    score = []
    count = 0
    while count < num:
        a = []
        b = []
        for attribute in attribute_dict.keys():
            c = random.choice(list(attribute_dict[attribute].keys()))
            a.append(c)
            b.append(attribute_dict[attribute][c])
        if caseset[case] == 0:
            if sum(b)*2 >= 8:
                df.loc[len(df.index)] = a
                score.append(sum(b)*2)
                count += 1
        elif caseset[case] == 1:
            if sum(b) >= 6:
                df.loc[len(df.index)] = a
                score.append(sum(b))
                count += 1
        elif caseset[case] == 2:
            if sum(b) >= 4:
                df.loc[len(df.index)] = a
                score.append(sum(b))
                count += 1
        elif caseset[case] == 3:
            if 6 >= sum(b) and sum(b) >= 2:
                df.loc[len(df.index)] = a
                score.append(sum(b))
                count += 1
        elif caseset[case] == 4:
            if 4 >= sum(b) and sum(b) >= 0:
                df.loc[len(df.index)] = a
                score.append(sum(b))
                count += 1
        elif caseset[case] == 5:
            if sum(b) >= -6 and sum(b) <= -2:
                df.loc[len(df.index)] = a
                score.append(sum(b))
                count += 1
        elif caseset[case] == 6:
            if sum(b) <= -6:
                df.loc[len(df.index)] = a
                score.append(sum(b))
                count += 1
        elif caseset[case] == 7:
            df.loc[len(df.index)] = a
            score.append(sum(b))
            count += 1
    return df, np.array(score)


def rule_data_generator(attribute_dict1, attribute_dict2, attribute_dict3, attribute_dict4, num, caseset):
    data1, reward = data_generator(attribute_dict1, num, caseset[0])
    data2, time_cost = data_generator(attribute_dict2, num, caseset[1])
    data3, feel = data_generator(attribute_dict3, num, caseset[2])
    data4, ability = data_generator(attribute_dict4, num, caseset[3])
    df = pd.concat([data1, data2, data3, data4], axis=1)

    if caseset == [7, 7, 7, 7]:
        df['answer'] = 0
    else:
        df['answer'] = 1
    df['reward'] = reward
    df['time_cost'] = time_cost
    df['feel'] = feel
    df['ability'] = ability
    return df


#-----------Rule1-------------#
Rule1 = rule_data_generator(attribute_dict1, attribute_dict2, attribute_dict3,
                            attribute_dict4, 1000, [0, 6, 7, 7])
#-----------Rule2-------------#
Rule2 = rule_data_generator(attribute_dict1, attribute_dict2, attribute_dict3,
                            attribute_dict4, 1000, [0, 7, 1, 7])
#-----------Rule3-------------#
Rule3 = rule_data_generator(attribute_dict1, attribute_dict2, attribute_dict3,
                            attribute_dict4, 1000, [0, 7, 7, 1])
#-----------Rule4-------------#
Rule4 = rule_data_generator(attribute_dict1, attribute_dict2, attribute_dict3,
                            attribute_dict4, 1000, [0, 4, 3, 3])
#-----------Rule5-------------#
Rule5 = rule_data_generator(attribute_dict1, attribute_dict2, attribute_dict3,
                            attribute_dict4,  1000, [0, 2, 3, 5])
#-----------other data-------------#
Other_data = rule_data_generator(attribute_dict1, attribute_dict2,
                                 attribute_dict3, attribute_dict4, 5000, [7, 7, 7, 7])

df = pd.concat([Rule1, Rule2, Rule3, Rule4, Rule5, Other_data], axis=0)
df.reset_index(drop=True, inplace=True)

df.loc[df[(df['reward'] >= 8) & (df['time_cost'] <= -6)].index, 'answer'] = 1
df.loc[df[(df['reward'] >= 8) & (df['feel'] >= 6)].index, 'answer'] = 1
df.loc[df[(df['reward'] >= 8) & (df['ability'] >= 6)].index, 'answer'] = 1
df.loc[df[(df['reward'] >= 8) & (0 <= df['time_cost']) & (df['time_cost'] <= 4) & (
    2 <= df['ability']) & (df['ability'] <= 6) & (2 <= df['feel']) & (df['feel'] <= 6)].index, 'answer'] = 1
df.loc[df[(df['reward'] >= 8) & (df['time_cost'] >= 4) & (2 <= df['feel']) & (
    df['feel'] <= 6) & (-6 <= df['ability']) & (df['ability'] <= -2)].index, 'answer'] = 1


print('Rule1 numbers: ', len(
    df[(df['reward'] >= 8) & (df['time_cost'] <= -6)].index))
print('Rule2 numbers: ', len(
    df[(df['reward'] >= 8) & (df['feel'] >= 6)].index))
print('Rule3 numbers: ', len(
    df[(df['reward'] >= 8) & (df['ability'] >= 6)].index))
print('Rule4 numbers: ', len(df[(df['reward'] >= 8) & (0 <= df['time_cost']) & (df['time_cost'] <= 4) & (
    2 <= df['ability']) & (df['ability'] <= 6) & (2 <= df['feel']) & (df['feel'] <= 6)].index))
print('Rule5 numbers: ', len(df[(df['reward'] >= 8) & (df['time_cost'] >= 4) & (2 <= df['feel']) & (
    df['feel'] <= 6) & (-6 <= df['ability']) & (df['ability'] <= -2)].index))
print('Good homeworks numbers: ', len(df.loc[df['answer'] == 1]))
print('Bad homeworks numbers: ', len(df.loc[df['answer'] == 0]))

df_values = df.copy()
for attribute in attribute_dict1.keys():
    df_values[attribute] = df[attribute].map(attribute_dict1[attribute])
for attribute in attribute_dict2.keys():
    df_values[attribute] = df[attribute].map(attribute_dict2[attribute])
for attribute in attribute_dict3.keys():
    df_values[attribute] = df[attribute].map(attribute_dict3[attribute])
for attribute in attribute_dict4.keys():
    df_values[attribute] = df[attribute].map(attribute_dict4[attribute])

df.to_csv('./input/data1_with_words.csv', index=False)
df_values.to_csv('./input/data1.csv', index=False)
