import pandas as pd
import numpy as np
import string
import os
from bs4 import BeautifulSoup



def create_subject_dict(files):
    
    
    subject_dict = {}
    
    for subject in files.subject.unique():
        subject_dict[subject] = pd.Series([])
        file_list = list(files[files['subject'] == subject].filenames)


        for file in file_list:
            local_series = pd.Series(pd.read_csv(os.path.join('./glossary_terms', file))['term'].values)
            
            subject_dict[subject] = subject_dict[subject].append(local_series, ignore_index = True)

    
    return subject_dict


def glossary_preprocess(text):
    
    preprocessed = text.lower().translate(str.maketrans("", "", string.punctuation)).split()
    
    return preprocessed

def num_glossary_terms(row, file_df, subject_dict):
    
    
    subject = row.subject
    
    if subject != 'not_sure':
        glossary_terms = subject_dict[subject]

        row_words = glossary_preprocess(row.question)

        #set(glossary_terms).intersection(set(row_words))

        return len(set(glossary_terms).intersection(set(row_words)))
    
    return

def create_glossary_col(df):
    """
    returns dataframe with new column glossary_terms
    """
    
    files = pd.DataFrame(os.listdir('./glossary_terms'), columns = ['filenames'])
    
    files['subject'] = files.filenames.map({'introduction-sociology-2e_index_terms.csv': 'sociology',
           'principles-microeconomics-2e_index_terms.csv': 'economics',
           'anatomy-and-physiology_index_terms.csv': 'biology',
           'college-physics_index_terms.csv': 'physics',
           'principles-economics-2e_index_terms.csv': 'economics',
            'us-history_index_terms.csv': 'history',
            'principles-macroeconomics-2e_index_terms.csv': 'economics',
            'biology-ap-courses_index_terms.csv': 'biology',
            'college-physics-ap-courses_index_terms.csv': 'physics',
            'biology-2e_index_terms.csv': 'biology',
            'psychology-2e_index_terms.csv': 'psychology'
})
    
    subject_dict = create_subject_dict(files)
    
    df['glossary_terms'] = df.apply(lambda x: num_glossary_terms(x, files, subject_dict), axis = 1)
    
    return df

def clean_question(x):
    'takes in a row and passes it through beautiful soup'
    
    soup = BeautifulSoup(x, features="lxml")
    
    return soup.text

def preprocess_text(df):
    
    df['text'] = df.question.apply(lambda x: clean_question(x))
    
    df['text_length'] = df.text.str.len()

    df['num_words'] = df['text'].apply(lambda x: len(x.split()))
    
    return df


def preprocess_labels(df, class_mapping):
    
    df['blooms'] = df['blooms'].map(class_mapping)
    

    df['adj_label'] = df['blooms'] - 1
    
    return df
    
#def create_flesch_score()



def preprocess_dataset(df, class_mapping):
    
    df = df[df.book.notnull()]
    
    df['subject'] = df.book.map({'bio': 'biology', 'inbook-yes__bio__apbio': 'biology', 'apush': 'history',
                             'inbook-yes__phys__k12phys': 'physics', 'phys__k12phys': 'physics',
                             'bio__apbio': 'biology', 'cbio': 'biology', 'soc': 'sociology', 'anp': 'biology',
                             'phys': 'physics', 'econ__macro': 'economics', 'inbook-yes__apbio': 'biology',
                             'apbio':'biology', 'econ__micro':'economics',
                             'book:': 'not_sure', 'econ__micro__macro': 'economics', 'inbook-yes__k12phys': 'physics',
                             'k12phys': 'physics', 'inbook-yes__book:': 'not_sure'}
                            )
    
    
    #df['blooms'] = df['blooms'].map({1:1, 2:2, 3:2, 4:2, 5:2, 6:2})
    
    
    df = preprocess_labels(df, class_mapping)
    
    df = create_glossary_col(df)
    
    df = preprocess_text(df)
    
    
    return df
    
    


    