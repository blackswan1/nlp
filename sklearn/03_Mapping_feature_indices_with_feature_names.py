# Create CountVectorizer object
vectorizer = CountVectorizer()

# Generate matrix of word vectors
bow_matrix = vectorizer.fit_transform(lion)

# Convert bow_matrix into a DataFrame
bow_df = pd.DataFrame(bow_matrix.toarray())

# Map the column names to vocabulary 
bow_df.columns = vectorizer.get_feature_names()

# Print bow_df
print(bow_df)




#<script.py> output:
#       an  decade  endangered  have  is  ...  lion  lions  of  species  the
#    0   0       0           0     0   1  ...     1      0   1        0    3
#    1   0       1           0     1   0  ...     0      1   1        0    0
#    2   1       0           1     0   1  ...     1      0   0        1    1