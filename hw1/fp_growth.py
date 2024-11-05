from utils import read_data, write_data
from utils import association_rule


def header_table(transaction_list, flatten_itemset, min_support):
    FreqDict = {}  # Header_Table
    item = list(set(flatten_itemset))
    for cand in item:
        count = 0
        for itemset in transaction_list:
            if (cand in itemset) == True:
                count += 1
        if count >= min_support*len(transaction_list):
            FreqDict[cand] = count/len(transaction_list)

    # 排序後型態為list，內有sublist
    FreqDict = sorted(FreqDict.items(), key=lambda item: item[1], reverse=True)
    FreqDict = [item for sublist in FreqDict for item in sublist]
    FreqDict = {FreqDict[i]: FreqDict[i + 1]
                for i in range(0, len(FreqDict), 2)}  # list->dict
    return FreqDict


def transaction_list_process(transaction_list, FreqDict):
    # 將 transaction_list 中非 Header_Table 的商品去除 ##
    for idx, itemset in enumerate(transaction_list):
        itemset_copy = itemset.copy()
        for item in itemset:
            if (item in FreqDict.keys()) == False:
                itemset_copy.remove(item)
        transaction_list[idx] = itemset_copy

    for idx, itemset in enumerate(transaction_list):  # 依 Header Table 排序 ##
        transaction_list[idx] = sorted(
            transaction_list[idx], key=lambda x: FreqDict[x], reverse=True)
    return transaction_list


class Node:
    def __init__(self, item, count=None, parent=None, children=None):
        self.item = item
        self.count = count
        self.parent = parent
        self.children = children


def FP_tree(transaction_list, FreqDict):
    HT_Ptr = {}  # Header_Table_Pointer Dictionary
    for i in FreqDict.keys():
        HT_Ptr[i] = []  # Initialize

    root = Node('root', 0)
    for itemset in transaction_list:

        p_n = root  # p_n 表示當前 Node
        for item in itemset:
            index = None
            if p_n.children != None:
                # 檢查 p_n 的 child 是否有同樣的 item
                for idx, i in enumerate(p_n.children):
                    if i.item == item:  # 有同樣的 item，紀錄 index，更新 child 的 count
                        index = idx
                        break

            if index != None:
                # p_n 的 child 有同樣的 item， 更新 child 的 count
                n_n = p_n.children[index]
                n_n.count = n_n.count + 1
                p_n = n_n  # 跳下個Node

            else:
                # p_n 沒有同樣的 item， 建立 n_n (next Node)， 在 Header_Table_Pointer 紀錄此 Node
                n_n = Node(item, 1, p_n)
                HT_Ptr[item].append(n_n)
                # p_n 加新 Node
                if p_n.children != None:
                    p_n.children.append(n_n)
                else:
                    p_n.children = [n_n]
                p_n = n_n  # 跳下個Node
    return HT_Ptr


def cond_pattern_base(HT_ptr):
    Cond_Pattern_Base = {}
    for i in HT_ptr.keys():
        Cond_Pattern_Base[i] = []  # Initialize

    for item in HT_ptr.keys():
        for node in HT_ptr[item]:
            p = node
            prefix = []
            while p.parent.item != 'root':
                prefix.insert(0, p.parent.item)
                p = p.parent

            if prefix != []:
                prefix.append(node.count)
                Cond_Pattern_Base[item].append(prefix)

    return Cond_Pattern_Base


def item_FP_tree(item, transaction_list, value):
    HT_Ptr = {}  # Header_Table_Pointer Dictionary
    root = Node('root', 0)
    for a, itemset in enumerate(transaction_list):

        p_n = root  # p_n 表示當前 Node
        for item in itemset:
            index = None
            if p_n.children != None:
                # 檢查 p_n 的 child 是否有同樣的 item
                for idx, i in enumerate(p_n.children):
                    if i.item == item:  # 有同樣的 item，紀錄 index，更新 child 的 count
                        index = idx
                        break

            if index != None:
                # p_n 的 child 有同樣的 item， 更新 child 的 count
                n_n = p_n.children[index]
                n_n.count += value[a]
                p_n = n_n  # 跳下個Node

            else:
                # p_n 沒有同樣的 item， 建立 n_n (next Node)， 在 Header_Table_Pointer 紀錄此 Node
                n_n = Node(item, value[a], p_n)
                if item not in HT_Ptr:
                    HT_Ptr[item] = []
                    HT_Ptr[item].append(n_n)
                else:
                    HT_Ptr[item].append(n_n)
                # p_n 加新 Node
                if p_n.children != None:
                    p_n.children.append(n_n)
                else:
                    p_n.children = [n_n]
                p_n = n_n  # 跳下個Node
    return HT_Ptr


def combinations(item, data, ans=[]):
    for i in range(len(data)):
        new_item = item.copy()
        new_data = data.copy()
        new_item.insert(-1, data[i])
        new_data = data[i+1:]
        ans.append(new_item)
        combinations(new_item, new_data, ans)
    return ans


def freq_pattern(Cond_Pattern_base, FreqDict, transaction_list, min_support):
    Freq_Pattern = {}
    for i in FreqDict.keys():  # Initialize
        Freq_Pattern[i] = []

    for item in Cond_Pattern_base.keys():
        item_list = []  # item 對應的
        value_list = []
        for i in range(len(Cond_Pattern_base[item])):
            j = len(Cond_Pattern_base[item][i])-1
            item_list.append(Cond_Pattern_base[item][i][0:j])
            value_list.append(Cond_Pattern_base[item][i][-1])
        # 根據每個item建Cond_FP_tree
        HT_Pointer = item_FP_tree(item, item_list, value_list)

        # Delete 小於 Min_support 的 HT_pointer
        Del_HT_item = []
        for i in HT_Pointer.keys():
            number = 0
            for node in HT_Pointer[i]:
                number += node.count
            if number < min_support*len(transaction_list):
                Del_HT_item.append(i)
        for i in Del_HT_item:
            del HT_Pointer[i]

        for i in HT_Pointer.keys():
            prefix_set = {}
            for node in HT_Pointer[i]:
                p = node
                prefix = []
                while p.parent.item != 'root':
                    prefix.insert(0, p.parent.item)
                    p = p.parent

                if i not in prefix_set:
                    prefix_set[i] = node.count
                else:
                    prefix_set[i] += node.count

                if prefix != []:
                    a = combinations([i], prefix, [])
                    for j in a:
                        k = ','.join(str(b) for b in j)
                        if k not in prefix_set:
                            prefix_set[k] = node.count
                        else:
                            prefix_set[k] += node.count
            for key in prefix_set.keys():
                if prefix_set[key] >= min_support*len(transaction_list):
                    l = prefix_set[key]/len(transaction_list)
                    m = key.split(',')
                    m.append(item)
                    k = ','.join(str(b) for b in m)
                    Freq_Pattern[k] = l
    Freq_Pattern.update(FreqDict)
    print('fp_growth Freq_Pattern : ', len(Freq_Pattern))
    return Freq_Pattern


def fp_growth(file, min_support, min_conf):
    transaction_list, flatten_itemset = read_data(file)
    FreqDict = header_table(transaction_list, flatten_itemset, min_support)
    transaction_list = transaction_list_process(transaction_list, FreqDict)
    HT_ptr = FP_tree(transaction_list, FreqDict)
    Cond_Pattern_Base = cond_pattern_base(HT_ptr)
    Freq_pattern = freq_pattern(
        Cond_Pattern_Base, FreqDict, transaction_list, min_support)
    Apriori_Rule, Value = association_rule(Freq_pattern, min_conf)
    f = file.split('/')
    f[-1] = f[-1].replace('txt', '')
    Output_name = './output/'+f[-1]+'-fp_growth'
    write_data(Output_name, Apriori_Rule, Value)
