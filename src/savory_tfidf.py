
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import nltk.data
import numpy as np
import pandas as pd
import savory_orders
import savory_items
import savory_blends
import matplotlib.pyplot as plt
from sklearn.decomposition import NMF
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler




# There's a function for each section of the sprint as well as some additional
# helper functions.
def get_data_tfidf():
    return(pd.read_csv('../data/IngSpiceList.csv'))

def process_data_tfidf(spices,recipies):


    spice_ing = get_data_tfidf()
    # DO TFIDF TRANSFORMATION
    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform(spice_ing.spicelist).toarray()

    # FEATURE IMPORTANCES
    top_n(vectorizer, vectors, spice_ing.spicelist, 10)

    return vectors

    # RANKING
    # ranking(vectorizer, vectors, spice_ing.title,
    #         get_queries('queries.txt'), 3)

    # SUMMARIZATION
    # article = newsgroups.data[1599]  # can choose any article
    # summarization(article, categories, 3)


def top_n(vectorizer, vectors, data, n):
    '''
    Print out the top 10 words by three different sorting mechanisms:
        * average tf-idf score
        * total tf-idf score
        * highest TF score across corpus
    '''
    words = vectorizer.get_feature_names()

    # Top 10 words by average tfidf
    # Take the average of each column, denoted by axis=0
    avg = np.sum(vectors, axis=0) / np.sum(vectors > 0, axis=0)
    print ("top %d by average tf-idf" % n)
    print (get_top_values(avg, n, words))


    # Top 10 words by total tfidf
    total = np.sum(vectors, axis=0)
    print ("top %d by total tf-idf" % n)
    print (get_top_values(total, n, words))


    # Top 10 words by TF
    vectorizer2 = TfidfVectorizer(use_idf=False)
    # make documents into one giant document for this purpose
    vectors2 = vectorizer2.fit_transform([" ".join(data)]).toarray()
    print ("top %d by tf across all corpus" % n)
    print (get_top_values(vectors2[0], n, words))



def get_queries(filename):
    '''
    Return a list of strings of the queries in the file.
    '''
    queries = []
    with open('queries.txt') as f:
        for line in f:
            # horrible stuff to get out the query
            queries.append(line.split("   ")[1].split("20")[0].strip())
    return queries


def ranking(vectorizer, vectors, titles, queries, n):
    '''
    Print out the top n documents for each of the queries.
    '''
    tokenized_queries = vectorizer.transform(queries)
    cosine_similarities = linear_kernel(tokenized_queries, vectors)
    for i, query in enumerate(queries):
        print (query)
        print (get_top_values(cosine_similarities[i], 3, titles))



def summarize(article, sent_detector, n):
    '''
    Choose top n the sentences based on max tf-idf score.
    '''
    sentences = sent_detector.tokenize(article.strip())
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(sentences).toarray()
    # We are summing on axis=1 (total per row)
    total = np.sum(vectors, 1)
    lengths = np.array([len(sent) for sent in sentences])
    return get_top_values(total / lengths.astype(float), n, sentences)


def summarization(article, categories, n):
    '''
    Print top n sentences from the article.
    Print top n sentences from each category.
    '''
    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')

    # summarize an article
    print (summarize(article, sent_detector, n))


    # for cat in categories:
    #     newsgroup = fetch_20newsgroups(subset='train', categories=[cat])
    #     print (cat)
    #     # combine all articles into one string to summarize.
    #     print summarize("\n".join(newsgroup.data), sent_detector, n)


def get_top_values(lst, n, labels):
    '''
    INPUT: LIST, INTEGER, LIST
    OUTPUT: LIST

    Given a list of values, find the indices with the highest n values. Return
    the labels for each of these indices.

    e.g.
    lst = [7, 3, 2, 4, 1]
    n = 2
    labels = ["cat", "dog", "mouse", "pig", "rabbit"]
    output: ["cat", "pig"]
    '''
    return [labels[i] for i in np.argsort(lst)[-1:-n-1:-1]]


def fit_nmf(k,mat):
    nmf = NMF(n_components=k)
    nmf.fit(mat)
    W = nmf.transform(mat);
    H = nmf.components_;
    return nmf.reconstruction_err_

def fit_pca(k,mat):
    scaler = StandardScaler(copy=True, with_mean=True, with_std=True)
    # X_scaled = scaler.fit_transform(mat) # standardize data
    pca = PCA(n_components=k) #pca object
    X_pca = pca.fit_transform(mat)
    if(k ==2):
        fig, ax = plt.subplots(1, 1, figsize=(8, 6))
        ax.scatter(X_pca[:, 0], X_pca[:, 1], c='y',
                   cmap=plt.cm.Set1, edgecolor='k', s=10)
        ax.set_title("First two PCA directions")
        ax.set_xlabel("1st eigenvector (PC1)")
        ax.set_ylabel("2nd eigenvector (PC2)")
        plt.savefig('../images/PCA.png')
    return(X_pca)

if __name__ == '__main__':
    data = get_data_tfidf()
    items = savory_items.SItems()
    vectors = process_data_tfidf(items.spices,data)
    nmf = NMF(n_components=40)
    nmf.fit(vectors)
    W = nmf.transform(vectors);
    H = nmf.components_;
    print(W)
    # error = [fit_nmf(i,vectors) for i in range(1,60)]
    # plt.plot(range(1,60), error)
    # plt.xlabel('k')
    # plt.ylabel('Reconstruction Error')
    # plt.title('NMF')
    # plt.savefig('../images/Reconstruction.png')

    #fit_pca(2,vectors)
