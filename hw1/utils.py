import csv


def kaggle_process(file, ans):
    f = open(file)
    lines = f.readlines()
    flatten_itemset = []

    for line in lines:
        line = line.split(',')
        itemset = []
        for idx, item in enumerate(line):
            itemset.append(item)
            if idx == len(line)-1:
                flatten_itemset.append(item.replace('\n', ''))
                break
            flatten_itemset.append(item)
        itemset[-1] = itemset[-1].replace('\n', '')
        ans.append(itemset)
    return ans, flatten_itemset


def testdata_process(file, ans):
    f = open(file)
    lines = f.readlines()
    before_transaction_id = ''
    itemset = []
    flatten_itemset = []

    for line in lines:
        line = line.split()
        transaction_id = line[1]
        item_id = line[2]

        if before_transaction_id == transaction_id:
            itemset.append(item_id)
        else:
            if itemset != []:
                ans.append(itemset)
            itemset = [item_id]

        flatten_itemset.append(item_id)

        before_transaction_id = transaction_id
    ans.append(itemset)

    return ans, flatten_itemset


def read_data(input_name):
    if 'testdata' in input_name:
        answers, flatten_itemset = testdata_process(input_name, [])
    elif 'kaggle' in input_name:
        answers, flatten_itemset = kaggle_process(input_name, [])

    return answers, flatten_itemset


def write_data(output_name, association_rule, value):
    output_name = output_name+'.csv'

    with open(output_name, 'w', newline='') as csvfile:
        # 定義欄位
        writer = csv.writer(csvfile)
        writer.writerow(['antecedent', 'consequent',
                         'support', 'confidence', 'lift'])
        for idx, rule in enumerate(association_rule):
            # 寫入資料
            writer.writerow(['{'+rule[0]+'}', '{'+rule[1]+'}',
                            value[idx][0], value[idx][1], value[idx][2]])
        csvfile.close()


def association_rule(Freq_pattern, min_conf):
    Apriori_rule = []
    value = []  # support confidence lift
    Freq_pattern_set = []
    for pattern in Freq_pattern.keys():
        Freq_pattern_set.append(set(pattern.split(',')))

    for A in Freq_pattern.keys():
        for B in Freq_pattern.keys():
            a = set(A.split(','))
            b = set(B.split(','))
            if len(list(a & b)) == 0:  # 沒有共同項:
                if (a | b) in Freq_pattern_set:
                    idx = Freq_pattern_set.index(a | b)

                    intersection = list(Freq_pattern.values())[idx]

                    support = intersection

                    confidence = intersection/Freq_pattern[A]

                    lift = confidence/Freq_pattern[B]
                    if confidence >= min_conf:
                        Apriori_rule.append([A, B])
                        value.append(['{:.3f}'.format(support), '{:.3f}'.format(
                            confidence), '{:.3f}'.format(lift)])
    print('length of Association rule : ', len(Apriori_rule))
    return Apriori_rule, value
