from utils import read_data, write_data
from utils import association_rule


def Li_combination(set_list):
    set_list_next = []
    intersection = set()
    for set_item in set_list:
        intersection = intersection | set_item
    intersection_list = list(intersection)
    for set_item in set_list:
        temp_list = []
        idx_list = []
        for i in range(len(set_item)):
            idx_list.append(intersection_list.index(list(set_item)[i]))
        idx = max(idx_list)
        temp_list = intersection_list[idx+1:]
        if temp_list != []:
            for j in range(len(temp_list)):
                set_item_copy = set_item.copy()
                set_item_copy.add(temp_list[j])
                if set_item_copy not in set_list_next:
                    set_list_next.append(set_item_copy)
    return set_list_next


def Candidate(ans_set, del_cand):
    ans = []
    if list(del_cand) == [] or type(list(del_cand)[0]) == str:  # 處理空的del_cand 和 處理C1_del
        ans = ans_set
    else:  # 處理C2_del、C3_del
        for itemset in ans_set:
            if itemset not in del_cand:
                ans.append(list(itemset))
    return ans


def Candidate_i(Ci_cand, transaction_list):
    Ci = {}
    if Ci_cand != []:  # 無候選人，輸出空字典
        if type(Ci_cand[0]) == str:  # C1
            for cand in Ci_cand:
                count = 0
                for itemset in transaction_list:
                    if (cand in itemset) == True:
                        count += 1
                Ci[cand] = count/len(transaction_list)
        else:  # C2、C3...Ci
            for cand in Ci_cand:
                count = 0
                for itemset in transaction_list:
                    if set(cand).issubset(set(itemset)):
                        count += 1

                Ci[','.join(str(i) for i in cand)] = count / \
                    len(transaction_list)
    return Ci


def List_i(Ci, min_support):
    Ci_delete = []
    Ci_delete_key = []
    Ci_delete_set = []
    Ci_delete_set_next = []
    Li = Ci.copy()

    for key in Li.keys():  # 記錄小於min_support的選項
        if Li[key] < min_support:
            Ci_delete_key.append(key)
    for key in Ci_delete_key:  # 刪掉小於min_support的選項
        del Li[key]
        Ci_delete.append(key)

    # 將刪掉的選項轉成set
    if Ci_delete == []:  # 處理Ci_delete為空
        Ci_delete_set = []
    elif len(Ci_delete[0].split(',')) == 1:  # 處理C1_del
        Ci_delete_set = set(Ci_delete)
    else:  # 處理C2_del、C3_del...Ci_del
        for delete in Ci_delete:
            Ci_delete_set.append(set(delete.split(',')))
        Ci_delete_set_next = Li_combination(Ci_delete_set)
    return Li, Ci_delete_set_next


def Li_item_combination(List_i):
    Li_item = []
    for i in List_i.keys():
        Li_item.append(set(i.split(',')))
    Ci_all_cand = Li_combination(Li_item)
    return Ci_all_cand


def Frequency_pattern(transaction_list, flatten_itemset, min_support):
    Freq_pattern = {}
    Li_item = []
    Ci_cand = []
    Ci = {}
    Li = {}
    Ci_del = {}
    i = 0
    Stop = False
    while Stop == False:
        if i == 0:
            Ci_cand = list(set(flatten_itemset))
            Ci = Candidate_i(Ci_cand, transaction_list)
            Li, Ci_del = List_i(Ci, min_support)
            Freq_pattern.update(Li)
            i += 1
        else:
            Li_item_comb = Li_item_combination(Li)
            Ci_cand = Candidate(Li_item_comb, Ci_del)
            Ci = Candidate_i(Ci_cand, transaction_list)
            Li, Ci_del = List_i(Ci, min_support)
            if Li != {}:
                Freq_pattern.update(Li)
                i += 1
            else:
                Stop = True
    print('apriori Freq_Pattern : ', len(Freq_pattern))
    return Freq_pattern


def apriori(file, min_support, min_conf):
    transaction_list, flatten_itemset = read_data(file)
    Freq_pattern = Frequency_pattern(
        transaction_list, flatten_itemset, min_support)

    Apriori_Rule, Value = association_rule(Freq_pattern, min_conf)
    f = file.split('/')
    f[-1] = f[-1].replace('txt', '')
    Output_name = './output/'+f[-1]+'-apriori'
    write_data(Output_name, Apriori_Rule, Value)
