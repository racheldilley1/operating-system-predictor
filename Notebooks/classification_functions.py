import pandas as pd
import numpy as np

#modeling
from sklearn.model_selection import train_test_split, KFold, GridSearchCV, RandomizedSearchCV, cross_val_score
from sklearn.metrics import roc_auc_score, confusion_matrix, roc_curve, precision_score, recall_score, f1_score, fbeta_score, auc, log_loss
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import BernoulliNB, MultinomialNB, GaussianNB

# plotting
import matplotlib.pyplot as plt
import seaborn as sns

def multinomial_nb(X_train, y_train):
    nb = MultinomialNB()
    # gs = GridSearchCV(nb, cv=skf, param_grid=params, return_train_score=True)
    # #this helps with the way kf will generate indices below
    # X, y = np.array(X_train), np.array(y_train)
    # kf = KFold(n_splits=5, shuffle=True, random_state=23) #randomly shuffle before splitting
    # precision, recall, f1, fbeta, auc, logl, ac = [] , [], [], [], [], [], []

    # for train_ind, val_ind in kf.split(X, y):
    #     X_train, y_train = X[train_ind], y[train_ind]
    #     X_val, y_val = X[val_ind], y[val_ind]

    #     mnb = MultinomialNB()
    #     mnb.fit(X_train, y_train)

    #     metrics = calc_cv_scores(mnb, X_val, y_val)

    #     ac.append(metrics[0])
    #     precision.append(metrics[1])
    #     recall.append(metrics[2])
    #     f1.append(metrics[3])
    #     auc.append(metrics[5])
    #     logl.append(metrics[6])

    # print(f'Multinomial NB:\n')
    # get_scores(ac, precision, recall, f1, auc, logl)
    # plot_roc(y_val, X_val, mnb)
          
    return 'mnb'

def random_forest(X_train, y_train):

    rf = RandomForestClassifier()
    grid_param = {
                    'n_estimators': [100, 300, 500, 800, 1000],
                    'criterion': ['gini', 'entropy'],
                    'max_features': ['auto', 'sqrt', 'log2'],
                    'max_depth' : [4,5,6,7,8]
                }
    rs = RandomizedSearchCV(rf, param_distributions= grid_param, cv=5, n_iter=50, n_jobs=-1)
    rs.fit(X_train, y_train)

    metrics = calc_cv_scores(rs, X_train, y_train)

    ac = metrics[0]
    precision = metrics[1]
    recall = metrics[2] 
    f1 = metrics[3]
    auc = metrics[4]
    logl = metrics[5]

    print(f'Random Forest with params:\n')
    print(rs.best_params_)
    get_scores(ac, precision, recall, f1, auc, logl)
    plot_roc(y_train, X_train, rs)
          
    return rs

def decision_tree(X_train, y_train, depth):
    #this helps with the way kf will generate indices below
    # X, y = np.array(X_train), np.array(y_train)
    # kf = KFold(n_splits=5, shuffle=True, random_state=23) #randomly shuffle before splitting
    # precision, recall, f1, fbeta, auc, logl, ac = [] , [], [], [], [], [], []

    # for train_ind, val_ind in kf.split(X, y):
    #     X_train, y_train = X[train_ind], y[train_ind]
    #     X_val, y_val = X[val_ind], y[val_ind]

    #     dt = DecisionTreeClassifier(max_depth=depth)
    #     dt.fit(X_train, y_train)

    #     metrics = calc_scores(dt, X_val, y_val)

    #     ac.append(metrics[0])
    #     precision.append(metrics[1])
    #     recall.append(metrics[2])
    #     f1.append(metrics[3])
    #     auc.append(metrics[5])
    #     logl.append(metrics[6])

    # print(f'Decision Tree with max depth of {depth}:\n')
    # get_scores(ac, precision, recall, f1, auc, logl)
    # plot_roc(y_val, X_val, dt)
          
    return 'dt'

def logistic_model(X_train, y_train, regularization):
    #this helps with the way kf will generate indices below
    # X, y = np.array(X_train), np.array(y_train)
    # kf = KFold(n_splits=5, shuffle=True, random_state=23) #randomly shuffle before splitting
    # precision, recall, f1, fbeta, auc, logl , ac = [] , [], [], [], [], [], []

    # for train_ind, val_ind in kf.split(X, y):
    #     X_train, y_train = X[train_ind], y[train_ind]
    #     X_val, y_val = X[val_ind], y[val_ind]

    #     lm = LogisticRegression(C=regularization, max_iter=10000)
    #     lm.fit(X_train, y_train)

    #     metrics = calc_scores(lm, X_val, y_val)

    #     ac.append(metrics[0])
    #     precision.append(metrics[1])
    #     recall.append(metrics[2])
    #     f1.append(metrics[3])
    #     auc.append(metrics[5])
    #     logl.append(metrics[6])

    # print(f'logistic regression with C = {regularization}:\n')
    # get_scores(ac, precision, recall, f1, auc, logl)
    # plot_roc(y_val, X_val, lm)
          
    return 'lm'

def knn_classification(X_train, y_train, k):
    #this helps with the way kf will generate indices below
    # X, y = np.array(X_train), np.array(y_train)
    # kf = KFold(n_splits=5, shuffle=True, random_state=23) #randomly shuffle before splitting
    # precision, recall, f1, fbeta, auc, logl, ac = [] , [], [], [], [], [], []

    # for train_ind, val_ind in kf.split(X, y):
    #     X_train, y_train = X[train_ind], y[train_ind]
    #     X_val, y_val = X[val_ind], y[val_ind]

    #     knn = KNeighborsClassifier(n_neighbors=k) #k nearest neighbors
    #     knn.fit(X_train, y_train)

    #     metrics = calc_cv_scores(knn, X_val, y_val)

    #     ac.append(metrics[0])
    #     precision.append(metrics[1])
    #     recall.append(metrics[2])
    #     f1.append(metrics[3])
    #     auc.append(metrics[5])
    #     logl.append(metrics[6])

    # print(f'KNN Classification with k = {k}:\n')
    # get_scores(ac, precision, recall, f1, auc, logl)
    # plot_roc(y_val, X_val, knn)
    return 'knn'

def calc_scores(model, X_val, y_val):

    preds = model.predict(X_val)
    y_val_enc = pd.get_dummies(y_val)
    probs = model.predict_proba(X_val)
    
    ac = round(model.score( X_val, y_val), 3)
    precision = (round(precision_score( y_val, preds, average='macro'), 3))
    recall = (round(recall_score( y_val, preds, average='macro'), 3))
    f1 = (round(f1_score( y_val, preds, average='macro'), 3))
    auc = (round(roc_auc_score( y_val_enc, probs, average='macro', multi_class='ovr'), 3))
    logl = (round(log_loss( y_val, probs), 3))

    return [ac, precision, recall, f1, auc, logl]

def calc_cv_scores(model, X_test, y_test):
    ac = round(cross_val_score(model, X_test, y_test, scoring='accuracy', cv=5).mean(), 3)
    precision = round(cross_val_score(model, X_test, y_test, scoring='precision_macro', cv=5).mean(), 3)
    recall = round(cross_val_score(model, X_test, y_test, scoring='recall_macro', cv=5).mean(), 3)
    f1 = round(cross_val_score(model, X_test, y_test, scoring='f1_macro', cv=5).mean(), 3)
    auc = round(cross_val_score(model, X_test, y_test, scoring='roc_auc_ovr', cv=5).mean(), 3)
    logl = round(cross_val_score(model, X_test, y_test, scoring='log_loss', cv=5).mean(), 3)

    return [ac, precision, recall, f1, auc, logl]

def get_scores(ac, precision, recall, f1, auc, logl):
    print(f'Accuracy: {np.mean(ac)},\n'
          f'Precision score: {np.mean(precision)},\n'
          f'Recall score: {np.mean(recall)},\n'
          f'f1 score: {np.mean(f1)},\n'
          f'ROC AUC score: {np.mean(auc)},\n'
          f'Log-loss: {np.mean(logl)},\n')

def conf_matrix(y_test, preds):

    conf = confusion_matrix(y_test, preds)
    plt.figure(figsize=(6,6))
    sns.heatmap(conf, cmap=plt.cm.get_cmap('Blues'), annot=True, square=True, fmt='d',
               xticklabels=['Linux', 'MacOS', 'Windows'],
               yticklabels=['Linux', 'MacOS', 'Windows'])

    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title('Confusion matrix')

def plot_roc(y_test, X_test, model):
    # Compute ROC curve and ROC area for each class
    fpr = dict()
    tpr = dict()
    roc_auc = dict()

    y_test_enc = pd.get_dummies(y_test)
    probs = model.predict_proba(X_test)

    for i in range(3):
        fpr[i], tpr[i], _ = roc_curve(y_test_enc.iloc[:, i], probs[:, i])
        roc_auc[i] = auc(fpr[i], tpr[i])

    plt.figure()
    op_sys = y_test_enc.columns
    colors = ['aqua', 'darkorange', 'cornflowerblue']
    for i, color, os in zip(range(3), colors, op_sys):
        plt.plot(fpr[i], tpr[i], color=color, lw=2,
                label='ROC curve of {0} (area = {1:0.2f})'
                ''.format(os, roc_auc[i]))

    plt.plot([0, 1], [0, 1], '--', lw=2)
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curves')
    plt.legend(loc="lower right")
    plt.show()




    