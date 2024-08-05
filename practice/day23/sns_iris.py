import seaborn as sns

# SSL 에러 해결
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

iris = sns.load_dataset('iris')
iris.species.value_counts()
iris.groupby("species").size()
