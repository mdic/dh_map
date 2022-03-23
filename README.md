# 
## Digital Humanities module 2021/2022 | LACOM - UniMoRe

### Disclaimer
This project concerns a severe and critical situation. It is **in no way meant to make fun of it, nor to take it lightly**.
On the contrary, it is meant to show how relevant and helpful digital approaches to anything human-related can be.

### Context
Our starting point is [Russia-Ukraine Monitor Map by Cen4infoRes](https://maphub.net/Cen4infoRes/russian-ukraine-monitor).
Have a look at it, and start taking notes as to:
- what it is
- what it contains
- what it does not contain

### Building our own project
We will first try to reproduce a rough version of the Russia-Ukraine Monitor Map by Cen4infoRes, based on data collected from Twitter. To achieve our goal, we will use the tools listed below. *Read what they do*, and have a *look at their documentations* to get a general understanding of **how they can help us**, and **how we should interact with them** (e.g. in which format should the data be passed to each tool?).

- [twint](https://github.com/twintproject/twint)
- [snscrape](https://github.com/JustAnotherArchivist/snscrape)
- [OpenRefine](https://openrefine.org/) | [Documentation](https://openrefine.org/documentation.html)
- [UMap](https://umap.openstreetmap.fr/en/) | [Documentation](https://wiki.openstreetmap.org/wiki/UMap/Guide)

[Scraping Tweets by Location in Python using snscrape](https://medium.com/swlh/how-to-scrape-tweets-by-location-in-python-using-snscrape-8c870fa6ec25) 

### Past meeting reports
These are available in the folder [reports](/reports).

### Our map

[Digital Humanities UniMoRe 2022](https://umap.openstreetmap.fr/en/map/digital-humanities-unimore-2022_735770)
The link with editor capabilities is shared on Teams!

### The data
Data is available in the [data](data/) folder, and it currently contains the following:

- `snscrape_since-20220316_random500.json`
collected on 22nd March 2022 using the command `snscrape --jsonl --progress twitter-search "geocode:50.233152,36.166992,200km since:2022-03-16"`, it is a random sample of 500 tweets (i.e.  JSON objects -> lines) from all the data collected during the scrape. The original file is too big to be included in this repo (240MB, while Github has a limit of 100MB per file), and you can find it [in our Team shared folder](https://unimore365.sharepoint.com/:f:/s/InsegnamentoPercorso_2021_12-261_2019_LCF-000051_S2_1_2021/ErjF2Jfty7RDsn0B44nnfhABkfS0o-sCtXCtppZACB0YAA?e=iBUqIR)