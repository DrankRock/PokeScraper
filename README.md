# PokeScraper
pokemon cards price tracker from cardmarket links

---
## Current state :
This project is currently in developpment. It currently works if used in commande line. 
#### TODO :
->Make it work for all types of cards from CardMarket (Yu-Gi-Oh, Magic, etc). 

---
## Download :
```
# clone the repo
$ git clone https://github.com/DrankRock/PokeScraper.git
# change the working directory to PokeScraper
$ cd PokeScraper/
# download required packages
$ python -m pip install -r requirements.txt
```
---
## Usage :
`python3 pokeScrap.0.1.py -i <inputFile> -o <outputFile> -s <statFile>`
### Parameters :
***`-i or --input :`***

Input file containing on each line a link to a cardmarket card. 

***`-o or --output :`***

Output file, preferably a .csv file because the output will be written in csv format. For each line from the inputfile will be written a line containing :

`extension,number,name,min_price,price_trend,mean30d_price,language,sellerType,minCondition,isSigned,isFirstEd,isPlayset,isAltered,url`

***`-s or --stats :`***

Statistics file, preferably a csv file because the output will be written in csv format. At the end of the execution will be appended a line containing :

`current Time, sum of all the minimum prices, sum of all the trending prices, sum of all the "Mean 30 days" prices`

---
## Example :
*input*

![picture alt](https://github.com/DrankRock/PokeScraper/blob/main/gitRessources/Screenshot%20from%202021-11-20%2019-00-58.png "links.txt")
*command*

![picture alt](https://github.com/DrankRock/PokeScraper/blob/main/gitRessources/Screenshot%20from%202021-11-20%2019-03-22.png "links.txt")
