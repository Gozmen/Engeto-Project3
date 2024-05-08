# Elections Scraper
Projekt 3 pro Engeto Python Akademii

## Popis projektu
Cílem je extrahování výsledků parlamentních voleb v roce 2017 pro vybraný okres [z tohoto odkazu](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ) (Odkaz X ve sloupci "Výběr obce") a jejich uložení do csv souboru.\
Program projde všechny obce daného okresu a uloží do csv souboru hodnoty ve sloupcích "Kód obce", "Název obce", "Voliči v seznamu", "Vydané obálky", "Platné hlasy" a počty hlasů jednotlivých politických stran.

## Instalace knihoven
Knihovny použité v kódu jsou uložené v souboru requirements.txt. 
```
pip --version                    Kontrola verze pip package installeru
pip install requests             Instalace requests knihovny
pip install beautifulsoup4       Instalace beautifulsoup4 knihovny
pip install pandas               Instalace pandas knihovny
pip freeze > requirements.txt    Výpis seznamu knihoven do requirements.txt souboru
```
## Spuštění projektu
Soubor Projekt3.py se spouští z příkazového řádku a požaduje dva argumenty, které jsou podmíněny přímo v kódu programu a musí mít správné pořadí.
```
python Projekt3.py "<odkaz_uzemniho_celku>" "<vystupni_soubor.csv>"
```
Výstupem programu je .csv soubor s výsledky voleb.

## Ukázka projektu
Výsledky pro okres Blansko:
> 1. argument -> [https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6201]
> 2. argument -> Vysledky_Blansko.csv


Spuštění programu:
```
python Projekt3.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6201" "Vysledky_Blansko.csv"
```

Část běhu programu
> Downloading data from URL: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6201
> 
> Downloading data from URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=11&xobec=581291&xvyber=6201
> 
> Downloading data from URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=11&xobec=581313&xvyber=6201
> 
> Downloading data from URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=11&xobec=581330&xvyber=6201
> 
> ...
> 
> Data saved to file: Vysledky_Blansko.csv
> 
> Program completed: Projekt3.py

Ukázka chyby v případě použití neplatné URL adresy (v URL adrese chybí poslední znak, číslice 1)
>Downloading data from URL: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=620
>
>No links found, please check the URL.

Částečný výstup:
> Kód obce,Název obce,Voliči v seznamu,Vydané obálky,Platné hlasy,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,Radostné Česko,STAROSTOVÉ A NEZÁVISLÍ,Komunistická str.Čech a Moravy,Strana zelených,"ROZUMNÍ-stop migraci,diktát.EU",Strana svobodných občanů,Blok proti islam.-Obran.domova,Občanská demokratická aliance,Česká pirátská strana,Referendum o Evropské unii,TOP 09,ANO 2011,Dobrá volba 2016,SPR-Republ.str.Čsl. M.Sládka,Křesť.demokr.unie-Čs.str.lid.,Česká strana národně sociální,REALISTÉ,SPORTOVCI,Dělnic.str.sociální spravedl.,Svob.a př.dem.-T.Okamura (SPD),Strana Práv Občanů,Národ Sobě

> 581291,Adamov,3 668,2 157,2 138,208,3,5,222,0,76,241,37,18,28,1,7,208,5,63,565,5,14,117,2,10,3,6,278,15,1

> 581313,Bedřichov,205,155,153,16,0,2,10,0,3,4,0,3,8,0,0,13,0,6,51,0,1,17,0,0,1,0,18,0,0

> 581330,Benešov,538,382,382,28,0,0,43,0,9,45,4,5,6,0,0,24,0,11,92,0,0,74,0,2,0,1,36,2,0
