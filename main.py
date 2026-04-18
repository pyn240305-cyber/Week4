import nltk
import re
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

# Input text
text = "Hello! My name is YEN_NHI24. I am 21 years old. My email is yen.nhi24@gmail.com"

# 1. Tokenization
tokens = word_tokenize(text)
print("Tokens:", tokens)

# 2. Lowercase
tokens = [word.lower() for word in tokens]
print("Lowercase:", tokens)

# 3. Remove stopwords
stop_words = set(stopwords.words('english'))
tokens = [word for word in tokens if word not in stop_words]
print("No Stopwords:", tokens)

# 4. Remove punctuation
tokens = [word for word in tokens if word not in string.punctuation]
print("No Punctuation:", tokens)

# 5. Regex Extraction
name = re.findall(r'YEN_NHI24', text)
age = re.findall(r'\d+', text)[0]
email = re.findall(r'[\w\.-]+@[\w\.-]+', text)

print("Name:", name[0])
print("Age:", age)
print("Email:", email[0])