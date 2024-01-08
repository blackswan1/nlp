import spacy


stopwords = ['fifteen', 'noone', 'whereupon', 'could', 'ten', 'all', 'please', 'indeed', 'whole', 'beside', 'therein', 'using', 'but', 'very', 'already', 'about', 'no', 'regarding', 'afterwards', 'front', 'go', 'in', 'make', 'three', 'here', 'what', 'without', 'yourselves', 'which', 'nothing', 'am', 'between', 'along', 'herein', 'sometimes', 'did', 'as', 'within', 'elsewhere', 'was', 'forty', 'becoming', 'how', 'will', 'other', 'bottom', 'these', 'amount', 'across', 'the', 'than', 'first', 'namely', 'may', 'none', 'anyway', 'again', 'eleven', 'his', 'meanwhile', 'name', 're', 'from', 'some', 'thru', 'upon', 'whither', 'he', 'such', 'down', 'my', 'often', 'whether', 'made', 'while', 'empty', 'two', 'latter', 'whatever', 'cannot', 'less', 'many', 'you', 'ours', 'done', 'thus', 'since', 'everything', 'for', 'more', 'unless', 'former', 'anyone', 'per', 'seeming', 'hereafter', 'on', 'yours', 'always', 'due', 'last', 'alone', 'one', 'something', 'twenty', 'until', 'latterly', 'seems', 'were', 'where', 'eight', 'ourselves', 'further', 'themselves', 'therefore', 'they', 'whenever', 'after', 'among', 'when', 'at', 'through', 'put', 'thereby', 'then', 'should', 'formerly', 'third', 'who', 'this', 'neither', 'others', 'twelve', 'also', 'else', 'seemed', 'has', 'ever', 'someone', 'its', 'that', 'does', 'sixty', 'why', 'do', 'whereas', 'are', 'either', 'hereupon', 'rather', 'because', 'might', 'those', 'via', 'hence', 'itself', 'show', 'perhaps', 'various', 'during', 'otherwise', 'thereafter', 'yourself', 'become', 'now', 'same', 'enough', 'been', 'take', 'their', 'seem', 'there', 'next', 'above', 'mostly', 'once', 'a', 'top', 'almost', 'six', 'every', 'nobody', 'any', 'say', 'each', 'them', 'must', 'she', 'throughout', 'whence', 'hundred', 'not', 'however', 'together', 'several', 'myself', 'i', 'anything', 'somehow', 'or', 'used', 'keep', 'much', 'thereupon', 'ca', 'just', 'behind', 'can', 'becomes', 'me', 'had', 'only', 'back', 'four', 'somewhere', 'if', 'by', 'whereafter', 'everywhere', 'beforehand', 'well', 'doing', 'everyone', 'nor', 'five', 'wherein', 'so', 'amongst', 'though', 'still', 'move', 'except', 'see', 'us', 'your', 'against', 'although', 'is', 'became', 'call', 'have', 'most', 'wherever', 'few', 'out', 'whom', 'yet', 'be', 'own', 'off', 'quite', 'with', 'and', 'side', 'whoever', 'would', 'both', 'fifty', 'before', 'full', 'get', 'sometime', 'beyond', 'part', 'least', 'besides', 'around', 'even', 'whose', 'hereby', 'up', 'being', 'we', 'an', 'him', 'below', 'moreover', 'really', 'it', 'of', 'our', 'nowhere', 'whereby', 'too', 'her', 'toward', 'anyhow', 'give', 'never', 'another', 'anywhere', 'mine', 'herself', 'over', 'himself', 'to', 'onto', 'into', 'thence', 'towards', 'hers', 'nevertheless', 'serious', 'under', 'nine']

# Function to preprocess text
def preprocess(text):
    # Create Doc object
    doc = nlp(text, disable=['ner', 'parser'])
    # Generate lemmas
    lemmas = [token.lemma_ for token in doc]
    # Remove stopwords and non-alphabetic characters
    a_lemmas = [lemma for lemma in lemmas 
            if lemma.isalpha() and lemma not in stopwords]
    
    return ' '.join(a_lemmas)
  
# Apply preprocess to ted['transcript']
ted['transcript'] = ted['transcript'].apply(preprocess)
print(ted['transcript'])