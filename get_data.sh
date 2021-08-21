# data for chap02
wget https://nlp100.github.io/data/popular-names.txt -P /workspaces/NLP-100knock/data/chap02

# data for chap03
wget https://nlp100.github.io/data/jawiki-country.json.gz -P /workspaces/NLP-100knock/data/chap03 && gzip -d /workspaces/NLP-100knock/data/chap03/jawiki-country.json.gz

# data for chap04
wget https://nlp100.github.io/data/neko.txt -P /workspaces/NLP-100knock/data/chap04

# data for chap05
wget https://nlp100.github.io/data/ai.ja.zip -P /workspaces/NLP-100knock/data/chap05 && unzip -o /workspaces/NLP-100knock/data/chap05/ai.ja.zip -d /workspaces/NLP-100knock/data/chap05/

# data for chap06
wget https://archive.ics.uci.edu/ml/machine-learning-databases/00359/NewsAggregatorDataset.zip -P /workspaces/NLP-100knock/data/chap06 && unzip -o /workspaces/NLP-100knock/data/chap06/NewsAggregatorDataset.zip -d /workspaces/NLP-100knock/data/chap06/

# data for chap07
wget https://s3.amazonaws.com/dl4j-distribution/GoogleNews-vectors-negative300.bin.gz -P /workspaces/NLP-100knock/data/chap07 && gzip -d /workspaces/NLP-100knock/data/chap07/GoogleNews-vectors-negative300.bin.gz

# data for chap10
wget http://www.phontron.com/kftt/download/kftt-data-1.0.tar.gz -P /workspaces/NLP-100knock/data/chap10 && tar -xzf /workspaces/NLP-100knock/data/chap10/kftt-data-1.0.tar.gz -C /workspaces/NLP-100knock/data/chap10/

# additional data
wget https://nlp.stanford.edu/projects/jesc/data/raw.tar.gz -P /workspaces/NLP-100knock/data/chap10 && tar -xzf /workspaces/NLP-100knock/data/chap10/raw.tar.gz -C /workspaces/NLP-100knock/data/chap10/
