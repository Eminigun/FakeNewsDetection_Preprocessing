# Kütüphaneler
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re

# Veri yükleme
fake_news = pd.read_csv('fake_news.csv')
true_news = pd.read_csv('true_news.csv')

# Sahte ile gerçek haberler için 1 ve 0 etiketlerinin girilmesi
fake_news['label'] = 0
true_news['label'] = 1

# Sahte ve gerçek haberlerin birleştirilmesi
news = pd.concat([fake_news,true_news], axis=0)

# Boş veri olup olmadığının kontrolü
#print(news.isnull().sum())

# Title ile text özniteliklerinin birleştirilmesi
news['text'] = news['title'] + ' ' + news['text']

# Gereksiz tarih özniteliğinin ve boş olan eski title'ın silinmesi
news = news.drop(['date', 'title'], axis=1)

# Sahte ve gerçek haberlerin sırayla gelmemesi için karıştırılması
news = news.sample(frac=1)

# Karıştırıldıktan sonra oluşan index sayılarını düzenleme
news.reset_index(inplace=True)
news.drop(['index'], axis=1, inplace=True)

# Verilerin Ön İşlemesi
def word_operations(text):
    # Küçük harfe dönüştürülmesi
    text = text.lower()
    
    # Linklerin silinmesi
    text = re.sub(r'https?://\S+|www\.\S+', ' ', text)
    
    # HTML Taglerinin silinmesi
    text = re.sub(r'<.*?>', ' ', text)
    
    # Noktalama işaretlerinin silinmesi
    text = re.sub(r'[^\w\s]', ' ', text)
    
    # Sayıların silinmesi
    text = re.sub(r'\d', ' ', text)
    
    # Yeni satır karakterlerinin silinmesi (\n)
    text = re.sub(r'\n', ' ', text)
    
    # Sekme karakterlerinin silinmesi (\t)
    text = re.sub(r'\t', ' ', text)
    
    # Fazla boşlukların silinmesi
    text = re.sub(r'  ', ' ', text)
    
    # Özel karakterlerin silinmesi
    text = re.sub(r'[!@#$%^&*()_+-={}[]|:;"\'<>,.?/~\]', ' ', text)
    
    return text
