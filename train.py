from sklearn import svm
from sklearn import naive_bayes
from sklearn import lda

TRAINING_DATA_FILE = "train.csv"
NUM_CATEGORIES = 28

def process_training_examples(filename):
    X = []
    y = []
    with open(filename, 'r') as training_data:
        while True:
            line = training_data.readline().rstrip()
            if line == "":
                break
            data = [ float(x) for x in line.split(',') ]
            X.append(data[:-1])
            y.append(int(data[-1]))
    print("We have now processed all {} training examples".format(len(y)))
    return X, y

def train_linear_svm(X, y):
    clf = svm.LinearSVC(loss="l2", penalty="l1", dual=False, C=100.0)
    clf.fit(X, y)
    return clf

def train_rbf_svm(X, y):
    clf = svm.SVC(kernel="rbf", C=100.0)
    clf.fit(X, y)
    return clf

def train_naive_bayes(X, y):
    clf = naive_bayes.MultinomialNB()
    clf.fit(X, y)
    return clf

def train_lda(X, y):
    clf = lda.LDA()
    clf.fit(X, y)
    return clf

