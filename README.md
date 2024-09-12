# CardWise - HarvardX CS50P Final Project

An All-in-One Credit Card Tool for Searching, Selecting, and Comparing Major Credit Cards on the Market!


## Table of Contents

* [Description](#description)
* [Watch the Video Tutorial](#watch-the-video-tutorial)
* [Getting Started](#getting-started)
    * [Prerequisites](#prerequisites)
    * [Installation](#installation)
* [Usage](#usage)
    * [Starting the Program](#starting-the-program)
    * [CardFinder](#cardfinder)
    * [CardMatch](#cardmatch)
    * [CardVersus](#cardversus)
* [Project Design](#project-design)
    * [Imports](#imports)
    * [Class CC](#class-cc)
    * [Main() and Functions](#main-and-functions)
    * [CC Database](#cc-database)
* [Sources](#sources)

## Description

**CardWise** is a program designed in Python to simplify the process of choosing a new credit card. Credit cards are a key player in today's financial landscape, enabling secure cashless payments while offering consumers rewards. They are also an important source of credit history: one of the most important contributing factors to one's credit score. However, with the seemingly countless credit card offerings available from numerous banks, selecting one to apply for can feel overwhelming. **CardWise** has tools to help. 

* **CardFinder** allows the user to search for credit cards from the five largest U.S. banks using various criteria, such as name, brand, annual fee, benefits, and credits.
* **CardMatch** asks the user for their preferences on the aforementioned categories and intelligently ranks credit cards that fit the user's preferences in order of highest benefit multiplier to lowest. 
* **CardVersus** displays the qualities of two cards of the user's choice side-by-side so their respective pros and cons can be easily compared. 

These three tools are easily accessible by running the code and interacting with the program via the terminal window. As of this writing, **CardWise** utilizes credit card data that includes an exhaustive list of non-business credit cards offered by the five largest U.S. banks: Chase, Bank of America, American Express, Citi, and Capital One. Please note that while I did my best to provide current information on each credit card in this dataset, some card characteristics may not be accurate. In addition, please be forewarned that I did not intend this program to provide official financial guidance in any way whatsoever. 


## Watch the Video Tutorial
<a href="https://youtu.be/4gON3jbZu6o" target="_blank">
<img src="https://i9.ytimg.com/vi/4gON3jbZu6o/mqdefault.jpg?v=66e291df&sqp=CPCiircG&rs=AOn4CLCinc54m8LONeKVYfPZ89atYT9aog" alt="Watch the Video Tutorial" height="240" border="2">
</a> <br/>

Video Link: [https://youtu.be/4gON3jbZu6o](https://youtu.be/4gON3jbZu6o)


## Getting Started

### Prerequisites
* Python 3.10+
* Tabulate
    ```
    pip install tabulate
    ```

### Installation
1. Install git — Refer to the [git homepage](https://git-scm.com/download/mac) for instructions. 
2. Change the current working directory to the location where you want to install CardWise. 
3. Run the following command in your terminal window: 
    ```
    git clone https://github.com/wise615/cardwise.git
    ```
4. That's it! You should now have a local clone of the program repository. 


## Usage

Although usage of the program should be intuitive and mostly self-explanatory, continue reading to learn how to interact and use **CardWise**. 

### Starting the Program
Upon running the program, you will be greeted with the **CardWise** home screen, which looks like the following: 
```
Hi, welcome to CardWise! Please select which tool you would like to use or learn more about.
[1] CardFinder: Credit Card Search Engine
[2] CardMatch: Credit Card Selection Tool
[3] CardVersus: Credit Card Comparison Tool
[4] Exit
Enter Number: 
```
Enter the number of the tool you would like to use. Entering `4` will quit the program. 

### CardFinder
Entering `1` at the **CardWise** home screen will bring you to the **CardFinder** landing page, which looks like the following: 
```
CardFinder is a custom-built credit card search engine with a variety of available search criteria.
Please select which criteria to search for.
Hint: You can select multiple criteria by separating each number with a comma (ex. 1, 2, 3).
[1] Card Name
[2] Card Brand
[3] Card Type
[4] Card Benefits
[5] Card Annual Fee
[6] Return to CardWise Home Screen
[7] Exit
```
Next, enter any number or combination of numbers (formatted with a comma in between, like `1, 2, 3`) corresponding to the search criteria you would like to search for. Entering `4`, for example, will bring you this screen: 
```
CardFinder - Searching by card benefits.
Searchable benefits include but are not limited to: dining, gas, transit, groceries, travel, and streaming.
Hint: You can search for multiple benefits at the same time by separating them with a comma.
Card Benefits: 
```
You may be shown the screen above and/or up to 4 other screens depending on which search criteria you specified. If you entered `6`, you will be redirected to the **CardWise** home screen, while entering `7` will quit the program. If you press `Enter` without entering anything when prompted, the search will eventually fail and you will be redirected to the **CardFinder** landing page. <br/> 

Once you have entered all of the criteria you initially specified, the results of your search will be presented in the terminal window in a tabular format similar to that below. The height of the table will vary based on how many search results matched your search criteria, but the length of the window should fit on most full-landscape terminal windows. If the table's formatting appears to break, expand your terminal window horizontally. 
```
╭────────────────────┬─────────┬───────────┬──────────────┬──────────────────────┬──────────────────────────────────────────╮
│ Name               │ Brand   │ Type      │   Annual Fee │ Benefits             │ Credits                                  │
├────────────────────┼─────────┼───────────┼──────────────┼──────────────────────┼──────────────────────────────────────────┤
│ Sapphire Preferred │ Chase   │ Points    │           95 │ 5x: Chase Travel     │ [*] $150 in Partnership Benefits         │
│                    │         │           │              │ 3x: Dining           │ [*] $50 Annual Chase Travel Hotel Credit │
│                    │         │           │              │ 3x: Online Groceries │                                          │
│                    │         │           │              │ 3x: Streaming        │                                          │
│                    │         │           │              │ 2x: Travel           │                                          │
│                    │         │           │              │ 1x: All              │                                          │
├────────────────────┼─────────┼───────────┼──────────────┼──────────────────────┼──────────────────────────────────────────┤
│ Instacart          │ Chase   │ Cash Back │            0 │ 5%: Chase Travel     │ None                                     │
│                    │         │           │              │ 5%: Instacart        │                                          │
│                    │         │           │              │ 2%: Dining           │                                          │
│                    │         │           │              │ 2%: Gas              │                                          │
│                    │         │           │              │ 2%: Streaming        │                                          │
│                    │         │           │              │ 1%: All              │                                          │
╰────────────────────┴─────────┴───────────┴──────────────┴──────────────────────┴──────────────────────────────────────────╯
```
After presenting the search results, the program will return to the **CardFinder** landing page, allowing you to quickly perform another search, return to the **CardWise** home screen to choose another tool, or quit the program. 

### CardMatch
Entering `2` at the **CardWise** home screen will bring you to the **CardMatch** landing page, which looks like the following: 
```
CardMatch is a custom-built credit card selection tool that can help you find the card best fitting your needs.
Next, you will be asked to provide information on the brand, type, benefits, and annual fee of the card you want.
If you have no preference on a specific category, simply press Enter to advance to the next question.
CardMatch will be able to provide more refined suggestions if you enter more information.
However, CardMatch may not be able to recommend a card if you enter too many criteria. 
Note: Results are always sorted by the first preferred benefit you list, so if you skip that question, the results will not be sorted. 
[1] Continue
[2] Return to CardWise Home Screen
[3] Exit
Enter Number: 
```
If you enter `1` to continue, **CardMatch** will ask you a series of questions on your preferences for credit card brand, type, benefits, and annual fee. It will also ask you how many results you would like to view. <br/> 

The key difference between **CardMatch** and **CardFinder** is that while **CardFinder** will return, in no particular order, all of the credit card results matching the criteria you specify, **CardMatch** will return a user-chosen quantity of results ordered by each card's benefit multiplier (from greatest to least) for the first benefit specified by the user in their answer to the benefit preference question. This essentially "ranks" each card fitting the user's preferences, allowing convenient comparison between cards with similar characteristics. An example of how this works is below. 

> < **CardMatch** Landing Screen > <br/>
\>\>\> 1 (Continue) <br/> <br/>
< Brand Preference Question > <br/>
\>\>\> American Express <br/> <br/>
< Type Preference Question > <br/>
\>\>\> `Enter` (No typed input = No preference for card type) <br/> <br/>
< Benefit Preference Question> <br/>
\>\>\> Travel, Dining (Results will be ranked by the first benefit: Travel) <br/> <br/>
< Annual Fee Preference Question > <br/>
\>\>\> 0, 650 (Annual fees between $0 and $650) <br/> <br/>
< Quantity of Results Question > <br/>
\>\>\> 4 (You will only see the top 4 results) 

In **CardMatch**, you may press `Enter` without typing anything if you do not have a preference for a certain category. However, providing too few criteria may return search results that are too broad and do not fit your lifestyle very well. Pressing `Enter` with nothing typed for the quantity of results question will show you all of the results that match your preferences. The above interaction will print the following results: 

```
╭───────────────────────────┬─────────┬────────┬──────────────┬───────────────┬────────────────────────────────────────────────────────────────╮
│ Name                      │ Brand   │ Type   │   Annual Fee │ Benefits      │ Credits                                                        │
├───────────────────────────┼─────────┼────────┼──────────────┼───────────────┼────────────────────────────────────────────────────────────────┤
│ Hilton Honors Aspire      │ AmEx    │ Points │          550 │ 14x: Hilton   │ [*] Hilton Honors Diamond Status                               │
│                           │         │        │              │ 7x: Dining    │ [*] Up to $400 in annual Hilton Resort credits                 │
│                           │         │        │              │ 7x: Travel    │                                                                │
│                           │         │        │              │ 3x: All       │                                                                │
├───────────────────────────┼─────────┼────────┼──────────────┼───────────────┼────────────────────────────────────────────────────────────────┤
│ Green                     │ AmEx    │ Points │          150 │ 3x: Dining    │ [*] $199 annual CLEAR Plus credits                             │
│                           │         │        │              │ 3x: Transit   │                                                                │
│                           │         │        │              │ 3x: Travel    │                                                                │
├───────────────────────────┼─────────┼────────┼──────────────┼───────────────┼────────────────────────────────────────────────────────────────┤
│ Marriott Bonvoy Brilliant │ AmEx    │ Points │          650 │ 6x: Marriott  │ [*] Marriot Bonvoy Platinum Elite Status                       │
│                           │         │        │              │ 3x: Dining    │ [*] Up to $300 in annual dining statement credits              │
│                           │         │        │              │ 3x: Travel    │ [*] Annual Free Night Award                                    │
│                           │         │        │              │ 2x: All       │ [*] $120 statement credit for Global Entry/TSA PreCheck every  │
│                           │         │        │              │               │     4.5 years                                                  │
│                           │         │        │              │               │ [*] $100 in Marriott Bonvoy property credit                    │
├───────────────────────────┼─────────┼────────┼──────────────┼───────────────┼────────────────────────────────────────────────────────────────┤
│ Gold                      │ AmEx    │ Points │          325 │ 4x: Dining    │ [*] Up to $120 in annual Uber credits                          │
│                           │         │        │              │ 4x: Groceries │ [*] Up to $84 in annual Dunkin' credits                        │
│                           │         │        │              │ 3x: Travel    │                                                                │
╰───────────────────────────┴─────────┴────────┴──────────────┴───────────────┴────────────────────────────────────────────────────────────────╯
```
Please note that despite the 4th card (Gold) having a higher benefit multiplier on Dining, which was one of the search categories, the results are sorted only based on the first benefit entered (Travel). While this is an area of improvement to the code, for now, we recommend that you don't limit yourself to the first search result and take some time to explore the complete search results, using the presented order only as a place to start. <br/>

After presenting the search results, the program will return to the **CardMatch** landing page, allowing you to quickly perform another search, return to the **CardWise** home screen to choose another tool, or quit the program. 

### CardVersus
Entering `3` at the **CardWise** home screen will bring you to the **CardVersus** landing page, which looks like the following: 

```
CardVersus is a custom-built credit card comparison tool that allows you to compare two cards' characteristics side-by-side.
Next, you will be asked to enter the name of each card you want to compare.
If you are not sure which cards you would like to compare, we recommend you use one of CardWise's other tools first.
Note: Make sure to not include the brand name (ex. Enter "Sapphire Preferred" when searching for the Chase Sapphire Preferred Card).
[1] Continue
[2] Return to CardWise Home Screen
[3] Exit
Enter Number: 
```

If you enter `1` to continue, **CardVersus** will prompt you to enter the names of two cards you would like to compare. Please make sure to omit the card brand from the card name. In the rare case that a card name may be used by two or more companies (ex. Both American Express and Capital One have a card called "Platinum"), you will be asked to clarify the card brand. An example interaction may look like the following: 

> < **CardVersus** Landing Page > <br/>
\>\>\> 1 (Continue) <br/> <br/>
< Card 1 Name > <br/>
\>\>\> Sapphire Reserve <br/> <br/>
< Card 2 Name > <br/>
\>\>\> Platinum <br/> <br/>
< Clarifying Question: Enter `1` for American Express Platinum or `2` for Capital One Platinum > <br/>
\>\>\> 1

Some cards may have very specific names, so we recommend checking which name is stored in the program database by running a quick search if you have a card you want to compare in mind. Because different banks have different naming schemes for their credit card offerings, and some there was a level of standardization done to store the card data in the program, some names may not be identical to what is present on their respective bank's website. The above interaction will return the following table: 

```
╭──────────────────┬─────────┬────────┬──────────────┬──────────────────────────────────────────┬──────────────────────────────────────────────────────╮
│ Name             │ Brand   │ Type   │   Annual Fee │ Benefits                                 │ Credits                                              │
├──────────────────┼─────────┼────────┼──────────────┼──────────────────────────────────────────┼──────────────────────────────────────────────────────┤
│ Sapphire Reserve │ Chase   │ Points │          550 │ 10x: Chase Dining                        │ [*] $1000 in Partnership Benefits                    │
│                  │         │        │              │ 10x: Chase Travel Hotels And Car Rentals │ [*] $300 Annual Travel Credits                       │
│                  │         │        │              │ 5x: Chase Travel Flights                 │                                                      │
│                  │         │        │              │ 3x: Dining                               │                                                      │
├──────────────────┼─────────┼────────┼──────────────┼──────────────────────────────────────────┼──────────────────────────────────────────────────────┤
│ Platinum         │ AmEx    │ Points │          695 │ 5x: American Express Travel              │ [*] Up to $200 in annual hotel credits               │
│                  │         │        │              │ 5x: Travel                               │ [*] Up to $200 in annual Uber credits                │
│                  │         │        │              │ 1x: All                                  │ [*] Up to $155 in annual Walmart+ credits            │
│                  │         │        │              │                                          │ [*] Up to $200 in annual airline fee credits         │
│                  │         │        │              │                                          │ [*] American Express Global Lounge Collection Access │
│                  │         │        │              │                                          │ [*] Up to $240 in annual streaming credits           │
│                  │         │        │              │                                          │ [*] $199 in annual CLEAR Plus credits                │
╰──────────────────┴─────────┴────────┴──────────────┴──────────────────────────────────────────┴──────────────────────────────────────────────────────╯
```

After presenting the search results, the program will return to the **CardVersus** landing page, allowing you to quickly perform another search, return to the **CardWise** home screen to choose another tool, or quit the program. 

## Project Design
As this project is my final project submission for HarvardX's CS50P: Introduction to Programming with Python, I tried to incorporate most of the skills I learned through the course. On a broad scale, I used object-oriented programming to create a class `CC` (credit card), which handles all credit card (object) data and processing, while using procedural functional programming to outline the user interface, including text inputs and program functions. On a smaller scale, `CC` contains 10 methods along with several properties which interact with one another to dynamically create, read, analayze, and return `CC` object data stored in a master dictionary `CC.all_CCs`. Meanwhile, the functional part of the program heavily relies on conditional loops to collect user inputs and compare it against the `CC.all_CCs` database. Below is a very condensed roadmap of the 800+ lines of code this project comprises.

```Python
import sys
from tabulate import tabulate

class CC: 
    all_CCs: list = [] # When credit card (CC) objects are defined below, their information gets added to CC.all_CCs via __init__()

    def __init__(self, brand, name, ctype, af, credits, **kwargs): # **kwargs is later assigned to be the card's associated benefits
    
    ...
    
    @classmethod
    def search(cls, **kwargs) -> dict: # This is the core function of the entire program, returning a dict of the objects in CC.all_CCs that fit the specified **kwargs

    ...

    @classmethod
    def table_creator(cls, data, benefit_preference_list=None, results_quantity=None) -> str: # This utilizes several other class methods and tabulate() to return a printable str that presents the dict results from CC.search() in a legible table format

...

def main(): ... # main() only calls home_function() with exception handling, which I decided to make separate from main() to make the code more readable

def home_function(): ... # This is the "landing page" for the program, where users have the option to select which tool they would like to use or to exit the program via sys.exit() 

def cardfinder(): ... # cardfinder() primarily utilizes CC.search() to search for cards that fit any number of criteria set by the user

def cardmatch(): ... # cardmatch() also uses CC.search() but takes advantage of the optional arguments in CC.table_creator() to dynamically rank the search results from best to worst and present a user-specified amount of credit card suggestions that best fit their lifestyle

def cardversus(): ... # cardversus() allows users to specify two cards they are interested in to compare their details side-by-side

...

< CC Database > # 77 lines of code creating the 77 CC objects whose information is automatically stored in CC.all_CCs
```

Throughout the program, strong exception handling and thorough debugging combine to create a smooth user experience that gently prompts the user again for inputs with hints on formatting if an unexpected value is entered. In addition, the program runs continuously until intentionally stopped various breakpoints, offering the convenience of uninterrupted use without risking infinite loops. <br/>

Though not typically in the scope of a `README.md`, because this is an official submission for a course final project, I have included a description below of how each `@classmethod` and `function()` work in my project, as a sort of informal documentation and explanation of how my project functions. I have also included information about certain items of interest throughout the project. 

### Imports
```Python
import sys
from tabulate import tabulate
```
This program uses `sys.exit()` to terminate the program whenever the user enters that they want to "Exit" the program. `tabulate()` is used to format the returned data from `CC.search()` in a readable table. 

### Class CC
```Python
all_CCs: list = []
all_CCs_tabulate: list = []
all_CCs_tabulate_headers: list = ["Name", "Brand", "Type", "Annual Fee", "Benefits", "Credits"]
```
`CC.all_CCs` is later used as a master database of all `CC` object data and is referenced extensively throughout the rest of the project. `CC.all_CCs_tabulate` contains the same information as in `CC.all_CCs` but in a format printable with `tabulate()`. While it is not directly used in this project, it was used in a separate experimental file to test other `@classmethod`s in `CC`. `CC.all_CCs_tabulate_headers`, on the other hand, is used later in `CC.table_formatter` and is located here for convenient access. 

```Python
def __init__(self, brand: str, name: str, ctype: str, af: int=0, credits: str | None=None, **kwargs: str | int | float): ...
```
Called every time a new ``CC`` object is made in \<CC Database\>, `CC.__init__()` appends each credit card's data to `CC.all_CCs` and `CC.all_CCs_tabulate` as a `dict`. `brand=` corresponds to the card brand, `name=` to card name, `ctype=` to card type (`type` was not used for it's ambiguity with the built-in function `type()`), `af=` to card annual fee, `credits=` to card credits, and `**kwargs` to card benefits, which is also stored as a `dict`. 

```Python
def __str__(self): ...
```
While also not directly used in the project, `CC.__str__()` returns a string formatted to include each `CC` object's data in a easily legible format. This was used in a separate experimental file to test the function of the "getters" and "setters" coded as `@property` for each `CC` object's brand, type, and benefits. 

```Python
@property
def brand(self): ...
@brand.setter
def brand(self, brand: str): ...

@property
def type(self): ...
@type.setter
def type(self, type: str): ...

@property
def benefits(self): ...
@benefits.setter
def benefits(self, benefits: dict): ...
```
These "getters" and "setters" were used to provide a defense against potential errors in `CC` object creation in \<CC Database\>. 

```Python
def benefits_sorter(self, benefits: dict) -> dict: ...
```
This instance method provides alphabetical sorting of `benefits`, and is primarily used in `@benefits.setter` to standardize how benefit information is stored in `CC.all_CCs`. 

```Python
@classmethod
def search(cls, **kwargs) -> dict: ...
```
The heart of the whole project, `CC.search()` is designed to take optional arguments for `name`, `brand`, `type`, `af`, and `benefit`. For every argument provided, `CC.search()` searches through `CC.all_CCs` to ultimately return a `dict` of `dict`s of all cards in `CC.all_CCs` that contain the argument. Internally, it works by creating several `dict`s (one for each argument provided), then creating a `results` `dict` that is the intersection of every created `dict` via a dictionary comprehension. 

```Python
@classmethod
def brand_standardizer(cls, brandname: str) -> str | None: ...
```
When passed in a `str` that could be any of several ways to spell the names of the five banks whose credit cards are referenced throughout the project, `CC.brand_standardizer()` returns a formatted `str` that is compatible with `CC.search()` and other `@classmethod`s. 

```Python
@classmethod
def type_standardizer(cls, typename: str) -> str | None: 
```
When passed in a `str` that could be any of several ways to spell the three different types of credit cards that are referenced throughout the project, `CC.type_standardizer()` returns a formatted `str` that is compatible with `CC.search()` and other `@classmethod`s. 

```Python
@classmethod
def benefit_standardizer(cls, benefitlist: list[str]) -> list | None: 
```
When passed in a `list` of benefit names, such as what might be entered as an input by the user, `CC.benefit_standardizer()` returns a formatted `list` of benefit names that are compatible with `CC.search()` and other `@classmethod`s. 

```Python
@classmethod
def benefit_dict_creator(cls, list_input: list[dict]) -> dict: 
```
When passed in a `list` of `dict`s formatted as `[{"Card_1": {contents_1}, "Card_2": {contents_2}}, {"Card_1": {contents_1}, "Card_3": {contents_3}}]`, `CC.benefit_dict_creator()` returns an intersection `dict` formatted as `{"Card_1": {contents_1}}`. This is mostly used in `CC.search()` for the specific case in which a "benefit" argument is given as a list (ex. The user inputs multiple benefits to search for). 

```Python
@classmethod
def table_formatter(cls, data: list) -> str: 
```
When passed in a `list` formatted as `[["<name>", "<brand>", "<type>", "<af>", "<benefits>", "<credits>"], ...]` for each `CC`, `CC.table_formatter()` will return a table created by `tabulate()` that is ready to print. This is mostly used in `CC.table_creator()` to format information for printing to the terminal interface. 

```Python
@classmethod
def benefits_ranker(cls, data: dict) -> dict: 
```
When passed in a `dict` formatted as `{"<benefit>": "<amount>", ...}`, `CC.benefits_ranker()` will return a `dict` with its keys ordered from `<amount>` greatest to least in the format `{<amount_int>: ["<benefit_1>, <benefit_2"], ...}`. This is mainly used in `CC.table_creator()` to format information for printing to the terminal interface and in `CC.__init__()` to create the unused `CC.all_CCs_tabulate`. 

```Python
@classmethod
def table_creator(cls, data: dict, benefit_preference_list: list=None, results_quantity: int=None) -> str: 
```
When passed in a `CC.search()` result, `CC.table_creator()` will return a `str` formatted by `CC.table_formatter()` (essentially `tabulate()`) with each `CC`'s benefits ranked by `CC.benefit_ranker()` and the results ordered (and possibly limited in quantity) by `CC.results_order()`. This is a comprehensive `@classmethod` that handles both search result procesing and formatting. 

```Python
@classmethod
def results_order(cls, search_results: dict, benefit_preference_list: list, results_quantity: int=None) -> dict: 
```
When passed in a `CC.search()` result, `CC.results_order()` will return a `dict` in the same format but with the results ordered by the first benefit in `benefit_preference_list` and possibly limited in quantity to `results_quantity`. This is mainly used in `CC.table_creator()`, only being called if a `benefit_preference_list` is passed into `CC.table_creator()`, which is unnecessary for **CardFinder** and **CardVersus** to function, but is crucial to **CardMatch** working as intended. 

### Main() and Functions
```Python
def main(): 
    while True: 
        try: 
            home_function()
        except ValueError: 
            pass
        else: 
            sys.exit("An unexpected error occured in main()")
```
The `main()` function is simple by design. It only calls `home_function()`, and keeps doing so once `home_function()` is finished running (which should never happen by the design of each of the tool functions) or a `ValueError` is raised by an invalid input. 

```Python
def home_function(): 
    print(home_screen)
    answer = input("Enter Number: ").strip().removeprefix("[").removesuffix("]")
    match answer: 
        case "1": # CardFinder: Credit Card Search Engine
            cardfinder()
        case "2": # CardMatch: Credit Card Selection Tool
            cardmatch()
        case "3": # Credit Card Comparison Tool
            cardversus()
        case "4": # Exit
            sys.exit(exit_statement)
        case _: 
            raise ValueError("Invalid input from Home Function")
```
This prints the **CardWise** home screen, where the user can choose which tool they would like to use, or exit the program. In the case that the user enters an invalid input, a `ValueError` is raised and they are simply prompted to enter another number due to the recursive design of `main()`, from which `home_function()` is called. 

```Python
def cardfinder(): ...
```
This prints the **CardFinder** landing page, which is described in greater detail above in the [Usage: CardFinder](#cardfinder) section. 

```Python
def cardmatch(): ...
```
This prints the **CardMatch** landing page, which is described in greater detail above in the [Usage: CardMatch](#cardmatch) section. 

```Python
def cardversus(): ...
```
This prints the **CardVersus** landing page, which is described in greater detail above in the [Usage: CardVersus](#cardversus) section. 

```Python
def fx_benefits_ranker(data: dict) -> dict: 
    return CC.benefits_ranker(data)

def fx_benefit_dict_creator(list_input: list[dict]) -> dict: 
    return CC.benefit_dict_creator(list_input)

def fx_benefit_standardizer(benefitlist: list[str]) -> list | None: 
    return CC.benefit_standardizer(benefitlist)
```
These "functionize" several `@classmethod`s in `CC` so that they can be imported and tested in another file without explicitly importing `CC` into the other file. 

### CC Database
```Python
# CC Database
Chase_Sapphire_Preferred = CC("Chase", "Sapphire Preferred", "points", 95, credits="$150 in Partnership Benefits, $50 Annual Chase Travel Hotel Credit", dining="3x", travel="2x", chase_travel="5x", online_groceries="3x", streaming="3x", all="1x")
...
```
The final section of my program contains all of the credit card (`CC`) object data used to populate `CC.all_CCs` and related items. There is currently information for 77 credit cards from 5 banks. Although I initially debated whether to store this information in a `dict` or nested within a function, I opted to create a `class` instead because of several benefits it provided, including the ability to dynamically create different types of data using object-oriented programming, readability, usability, and that upon importing `class CC` into another project, the object data is still preserved and accessible. This final point made it convenient to test parts of my code in a separate experimental file and will allow spin-offs of this project to be able to access the credit card data I created unless deliberately overwritten. 


## Sources
The following sources were used to obtain information used to populate the `CC.all_CCs` database. APIs were not used and therefore there may be differences between the information currently published online and the hand-entered information being used in the **CardWise** program. All trademarks belong to their respective company and the information presented by **CardWise** should only be used for unofficial unverified informational purposes. 
* https://creditcards.chase.com/rewards-credit-cards
* https://www.bankofamerica.com/credit-cards/
* https://www.americanexpress.com/us/credit-cards/
* https://www.citi.com/credit-cards/compare/view-all-credit-cards
* https://www.capitalone.com/credit-cards/compare/
