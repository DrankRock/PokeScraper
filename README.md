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
<ins>*input*</ins>

![picture alt](https://github.com/DrankRock/PokeScraper/blob/main/gitRessources/Screenshot%20from%202021-11-20%2019-00-58.png "links.txt")

*command*

![picture alt](https://github.com/DrankRock/PokeScraper/blob/main/gitRessources/Screenshot%20from%202021-11-20%2019-03-22.png "command")

*links.csv*

![picture alt](https://github.com/DrankRock/PokeScraper/blob/main/gitRessources/Screenshot%20from%202021-11-20%2019-05-10.png "links.csv")

*linksStat.csv*

![picture alt](https://github.com/DrankRock/PokeScraper/blob/main/gitRessources/Screenshot%20from%202021-11-20%2019-05-50.png "linksStat.csv")


<details>
	<summary>Help</summary>
	<p>-- Pokemon CardMarket Scraper --<br>
usage: pokeScrap.0.2.py -i <input file or link> -o <outputfile> -s <statFile(optional)><br>
Precisions about the results :<br>
 _____________________<br>
|     minCondition    |<br>
|_____________________|<br>
| None = Poor         |<br>
| 6    = Played       |<br>
| 5    = Light Played |<br>
| 4    = Good         |<br>
| 3    = Excellent    |<br>
| 2    = Near Mint    |<br>
| 1    = Mint         |<br>
|_____________________|<br>
|      language       |<br>
|_____________________|<br>
| None = None         |<br>
| 1    = English      |<br>
| 2    = French       |<br>
| 3    = German       |<br>
| 4    = Spanish      |<br>
| 5    = Italian      |<br>
| 6    = S-Chinese    |<br>
| 7    = Japanese     |<br>
| 8    = Portuguese   |<br>
| 9    = Russian      |<br>
| 10   = Korean       |<br>
| 11   = T-Chinese    |<br>
| 12   = Dutch        |<br>
| 13   = Polish       |<br>
| 14   = Czech        |<br>
| 15   = Hungarian    |<br>
|_____________________|<br></p>
</details>
