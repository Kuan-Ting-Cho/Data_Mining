# import numpy as npㄎㄎ
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn import tree
import graphviz
df_values1 = pd.read_csv('./input/data1.csv')
df_values2 = pd.read_csv('./input/data2.csv')
df_values3 = pd.read_csv('./input/data3.csv')
df_values4 = pd.read_csv('./input/data4.csv')
df_values5 = pd.read_csv('./input/data5.csv')
df_values_new1 = df_values1.iloc[:, 0:17]
df_values_new2 = df_values2.iloc[:, 0:19]
df_values_new3 = df_values3.iloc[:, 0:19]
df_values_new4 = df_values4.iloc[:, 0:19]
df_values_new5 = df_values5.iloc[:, 0:17]
#------------------不同data的input/output shape-----------------------------#
x1 = df_values_new1.iloc[:, :-1]
y1 = df_values_new1.iloc[:, -1]
x2 = df_values_new2.iloc[:, :-1]
y2 = df_values_new2.iloc[:, -1]
x3 = df_values_new3.iloc[:, :-1]
y3 = df_values_new3.iloc[:, -1]
x4 = df_values_new4.iloc[:, :-1]
y4 = df_values_new4.iloc[:, -1]
x5 = df_values_new4.iloc[:, :-1]
y5 = df_values_new4.iloc[:, -1]
print(f"Shape of data1 input: {x1.shape}")
print(f"Shape of data1 output: {y1.shape}")
print(f"Shape of data2 input: {x2.shape}")
print(f"Shape of data2 output: {y2.shape}")
print(f"Shape of data3 input: {x3.shape}")
print(f"Shape of data3 output: {y3.shape}")
print(f"Shape of data4 input: {x4.shape}")
print(f"Shape of data4 output: {y4.shape}")
#------------------不同data的train_test_split-----------------------------#
x_train1, x_vad1, y_train1, y_vad1 = train_test_split(
    x1, y1, test_size=0.3, random_state=1234)
print(f"Shape of data1 x_train: {x_train1.shape}")
print(f"Shape of data1 x_vad: {x_vad1.shape}")
print(f"Shape of data1 y_train: {y_train1.shape}")
print(f"Shape of data1 y_vad: {y_vad1.shape}")
x_train2, x_vad2, y_train2, y_vad2 = train_test_split(
    x2, y2, test_size=0.3, random_state=1234)
print(f"Shape of data2 x_train: {x_train2.shape}")
print(f"Shape of data2 x_vad: {x_vad2.shape}")
print(f"Shape of data2 y_train: {y_train2.shape}")
print(f"Shape of data2 y_vad: {y_vad2.shape}")
x_train3, x_vad3, y_train3, y_vad3 = train_test_split(
    x3, y3, test_size=0.3, random_state=1234)
print(f"Shape of data3 x_train: {x_train3.shape}")
print(f"Shape of data3 x_vad: {x_vad3.shape}")
print(f"Shape of data3 y_train: {y_train3.shape}")
print(f"Shape of data3 y_vad: {y_vad3.shape}")
x_train4, x_vad4, y_train4, y_vad4 = train_test_split(
    x4, y4, test_size=0.3, random_state=1234)
print(f"Shape of data4 x_train: {x_train4.shape}")
print(f"Shape of data4 x_vad: {x_vad4.shape}")
print(f"Shape of data4 y_train: {y_train4.shape}")
print(f"Shape of data4 y_vad: {y_vad4.shape}")
x_train5, x_vad5, y_train5, y_vad5 = train_test_split(
    x5, y5, test_size=0.3, random_state=1234)
#------------------不同data的型態轉換-----------------------------#
x_train1 = x_train1.astype('int')
x_vad1 = x_vad1.astype('int')
y_train1 = y_train1.astype('int')
y_vad1 = y_vad1.astype('int')
x_train2 = x_train2.astype('int')
x_vad2 = x_vad2.astype('int')
y_train2 = y_train2.astype('int')
y_vad2 = y_vad2.astype('int')
x_train3 = x_train3.astype('int')
x_vad3 = x_vad3.astype('int')
y_train3 = y_train3.astype('int')
y_vad3 = y_vad3.astype('int')
x_train4 = x_train4.astype('int')
x_vad4 = x_vad4.astype('int')
y_train4 = y_train4.astype('int')
y_vad4 = y_vad4.astype('int')
x_train5 = x_train5.astype('int')
x_vad5 = x_vad5.astype('int')
y_train5 = y_train5.astype('int')
y_vad5 = y_vad5.astype('int')
#------------------不同data的decision_tree-----------------------------#
dt_basic1 = tree.DecisionTreeClassifier(max_depth=7,criterion='entropy',random_state=1234)
dt_basic1.fit(x_train1,y_train1)
y_preds1 = dt_basic1.predict(x_vad1)

dot_data1 = tree.export_graphviz(dt_basic1, 
              feature_names=x1.columns,
              class_names=['bad homework','good homework'],
              rounded = True, 
              special_characters = True,
              filled=True)

graph1 = graphviz.Source(dot_data1, format="png") 
graph1.render('decision_tree_data1_max_depth=7',view=False) #save image
accuracy_value1 = accuracy_score(y_vad1,y_preds1)

dt_basic2 = tree.DecisionTreeClassifier(max_depth=7,criterion='entropy',random_state=1234)
dt_basic2.fit(x_train2,y_train2)
y_preds2 = dt_basic2.predict(x_vad2)

dot_data2 = tree.export_graphviz(dt_basic2, 
              feature_names=x2.columns,
              class_names=['bad homework','good homework'],
              rounded = True, 
              special_characters = True,
              filled=True)

graph2 = graphviz.Source(dot_data2, format="png") 
graph2.render('decision_tree_data2_max_depth=7',view=False) #save image
accuracy_value2 = accuracy_score(y_vad2,y_preds2)

dt_basic3 = tree.DecisionTreeClassifier(max_depth=7,criterion='entropy',random_state=1234)
dt_basic3.fit(x_train3,y_train3)
y_preds3 = dt_basic3.predict(x_vad2)

dot_data3 = tree.export_graphviz(dt_basic3, 
              feature_names=x3.columns,
              class_names=['bad homework','good homework'],
              rounded = True, 
              special_characters = True,
              filled=True)

graph3 = graphviz.Source(dot_data3, format="png") 
graph3.render('decision_tree_data3_max_depth=7',view=False) #save image
accuracy_value3 = accuracy_score(y_vad3,y_preds3)

dt_basic4 = tree.DecisionTreeClassifier(max_depth=7,criterion='entropy',random_state=1234)
dt_basic4.fit(x_train4,y_train4)
y_preds4 = dt_basic4.predict(x_vad4)

dot_data4 = tree.export_graphviz(dt_basic4, 
              feature_names=x4.columns,
              class_names=['bad homework','good homework'],
              rounded = True, 
              special_characters = True,
              filled=True)

graph4 = graphviz.Source(dot_data4, format="png") 
graph4.render('decision_tree_data4_max_depth=7',view=False) #save image
accuracy_value4 = accuracy_score(y_vad4,y_preds4)

print('score of decision_tree_data1 model is : ',accuracy_value1)
print('score of decision_tree_data2 model is : ',accuracy_value2)
print('score of decision_tree_data3 model is : ',accuracy_value3)
print('score of decision_tree_data4 model is : ',accuracy_value4)
confusion_matrix4 = confusion_matrix(y_vad4,y_preds4)
print(classification_report(y_vad1,y_preds1, target_names=['Bad homeworks','Good homeworks']))
print(classification_report(y_vad2,y_preds2, target_names=['Bad homeworks','Good homeworks']))
print(classification_report(y_vad2,y_preds3, target_names=['Bad homeworks','Good homeworks']))
print(classification_report(y_vad4,y_preds4, target_names=['Bad homeworks','Good homeworks']))
#------------------不同data的random_forest -----------------------------#
rnd1 = RandomForestClassifier(n_estimators=100, max_depth=7, random_state=1234)
rnd1.fit(x_train1, y_train1)
y_preds1 = rnd1.predict(x_vad1)
accuracy_value1 = accuracy_score(y_vad4, y_preds1)

rnd2 = RandomForestClassifier(n_estimators=100, max_depth=7, random_state=1234)
rnd2.fit(x_train2, y_train2)
y_preds2 = rnd2.predict(x_vad2)
accuracy_value2 = accuracy_score(y_vad2, y_preds2)

rnd3 = RandomForestClassifier(n_estimators=100, max_depth=7, random_state=1234)
rnd3.fit(x_train3, y_train3)
y_preds3 = rnd3.predict(x_vad2)
accuracy_value3 = accuracy_score(y_vad2, y_preds3)

rnd4 = RandomForestClassifier(n_estimators=100, max_depth=7, random_state=1234)
rnd4.fit(x_train4, y_train4)
y_preds4 = rnd4.predict(x_vad4)
accuracy_value4 = accuracy_score(y_vad4, y_preds4)
print(classification_report(y_vad1, y_preds1,
      target_names=['Bad homeworks', 'Good homeworks']))
print(classification_report(y_vad2, y_preds2,
      target_names=['Bad homeworks', 'Good homeworks']))
print(classification_report(y_vad2, y_preds3,
      target_names=['Bad homeworks', 'Good homeworks']))
print(classification_report(y_vad4, y_preds4,
      target_names=['Bad homeworks', 'Good homeworks']))
# #------------------不同data的knn-----------------------------#
knn1 = KNeighborsClassifier(n_neighbors=43)
knn1.fit(x_train1, y_train1)
y_preds1 = knn1.predict(x_vad1)

knn2 = KNeighborsClassifier(n_neighbors=43)
knn2.fit(x_train2, y_train2)
y_preds2 = knn2.predict(x_vad2)

knn3 = KNeighborsClassifier(n_neighbors=43)
knn3.fit(x_train3, y_train3)
y_preds3 = knn3.predict(x_vad2)

knn4 = KNeighborsClassifier(n_neighbors=43)
knn4.fit(x_train4, y_train4)
y_preds4 = knn4.predict(x_vad4)

print(classification_report(y_vad1, y_preds1,
      target_names=['Bad homeworks', 'Good homeworks']))
print(classification_report(y_vad2, y_preds2,
      target_names=['Bad homeworks', 'Good homeworks']))
print(classification_report(y_vad2, y_preds3,
      target_names=['Bad homeworks', 'Good homeworks']))
print(classification_report(y_vad4, y_preds4,
      target_names=['Bad homeworks', 'Good homeworks']))
# #------------------不同data的k_means-----------------------------#
x_train1 = StandardScaler().fit_transform(x_train1)
x_vad1 = StandardScaler().fit_transform(x_vad1)
kmeans1 = KMeans(n_clusters=2, init='k-means++',
                 max_iter=100, n_init=10, random_state=1234)
kmeans1.fit(x_train1, y_train1)
y_preds1 = kmeans1.predict(x_vad1)

x_train2 = StandardScaler().fit_transform(x_train2)
x_vad2 = StandardScaler().fit_transform(x_vad2)
kmeans2 = KMeans(n_clusters=2, init='k-means++',
                 max_iter=100, n_init=10, random_state=1234)
kmeans2.fit(x_train2, y_train2)
y_preds2 = kmeans2.predict(x_vad2)

x_train3 = StandardScaler().fit_transform(x_train3)
kmeans3 = KMeans(n_clusters=2, init='k-means++',
                 max_iter=100, n_init=10, random_state=1234)
kmeans3.fit(x_train3, y_train3)
y_preds3 = kmeans3.predict(x_vad2)

x_train4 = StandardScaler().fit_transform(x_train4)
x_vad4 = StandardScaler().fit_transform(x_vad4)
kmeans4 = KMeans(n_clusters=2, init='k-means++',
                 max_iter=100, n_init=10, random_state=1234)
kmeans4.fit(x_train4, y_train4)
y_preds4 = kmeans4.predict(x_vad4)

x_train5 = StandardScaler().fit_transform(x_train5)
x_vad5 = StandardScaler().fit_transform(x_vad5)
kmeans5 = KMeans(n_clusters=2, init='k-means++',
                 max_iter=100, n_init=10, random_state=1234)
kmeans5.fit(x_train5, y_train5)
y_preds5 = kmeans5.predict(x_vad5)

print(classification_report(y_vad1, y_preds1,
      target_names=['Bad homeworks', 'Good homeworks']))
print(classification_report(y_vad2, y_preds2,
      target_names=['Bad homeworks', 'Good homeworks']))
print(classification_report(y_vad2, y_preds3,
      target_names=['Bad homeworks', 'Good homeworks']))
print(classification_report(y_vad4, y_preds4,
      target_names=['Bad homeworks', 'Good homeworks']))
print(classification_report(y_vad5, y_preds5,
      target_names=['Bad homeworks', 'Good homeworks']))
