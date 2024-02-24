# Dataframe
for index, row in ted.iloc[range(0, 20), [ted.columns.get_loc('transcript'), ted.columns.get_loc('url')]].iterrows():
    print('"{transcript}", "{url}"'.format(transcript=row["transcript"], url=row["url"].replace("\n", "")))


# Series
for index, value in enumerate(corpus):
    print(f"Index: {index}, Value: {value}")

