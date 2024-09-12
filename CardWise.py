import sys
from tabulate import tabulate

class CC: 
    all_CCs: list = [] # List of dicts, format is below in __init__
    all_CCs_tabulate: list = [] # List of lists, formatted to be used in tabulate()
    all_CCs_tabulate_headers: list = ["Name", "Brand", "Type", "Annual Fee", "Benefits", "Credits"]
    
    def __init__(self, brand: str, name: str, ctype: str, af: int=0, credits: str | None=None, **kwargs: str | int | float): 
        self.brand = brand
        self.name = name
        self.type = ctype
        self.af = af
        self.credits = credits
        self.benefits = kwargs
        
        CC.all_CCs.append(
            {
                "brand": self.brand, "name": self.name, "type": self.type, "af": self.af, "benefits": self.benefits, "credits": self.credits
            }
        )
        
        if self.type == "cb": 
            tabulate_type = "Cash Back"
        if self.type == "points": 
            tabulate_type = "Points"
        if self.type == "misc": 
            tabulate_type = "Misc."

        if self.benefits == {}: 
            tabulate_benefits = "None"
        if self.benefits != {}: 
            ranked_benefits = CC.benefits_ranker(self.benefits)
            tabulate_benefits = ""
            for benefit_amount in ranked_benefits: 
                for benefit_name in ranked_benefits[benefit_amount]: 
                    benefit_name: str = benefit_name.replace("_", " ").title()
                    if self.type == "cb" and type(benefit_amount) == int: 
                        benefit_amount = f"{benefit_amount}%"
                    if self.type == "points" and type(benefit_amount) == int: 
                        benefit_amount = f"{benefit_amount}x"
                    tabulate_benefits = tabulate_benefits + f"{benefit_amount}: {benefit_name}\n"
        
        if self.credits == None: 
            tabulate_credits = "None"
        if self.credits != None: 
            tabulate_credits = ""
            credits_list = (self.credits).split(", ")
            for index in credits_list: 
                tabulate_credits = tabulate_credits + f"[*] {index}\n"

        CC.all_CCs_tabulate.append(
            [
                self.name, self.brand, tabulate_type, self.af, tabulate_benefits, tabulate_credits
            ]
        )

    def __str__(self): 
        name = self.name
        brand = self.brand
        ctype = self.type
        af = self.af
        ccredits = self.credits
        benefits = self.benefits
        
        ccredits = ccredits.split(", ")
        credits_str = ""
        for credit in ccredits: 
            credits_str = credits_str + f"    {credit} \n"

        benefits_str = ""
        for benefit in benefits: 
            benefitname: str = benefit.replace("_", " ").title() # "chase_travel" -> "Chase Travel"
            benefit_detail: str = str(benefits[benefit])
            benefits_str = benefits_str + f"    {benefitname}: {benefit_detail} \n"

        return (
            "---------------------------------------------------------------------------------------------------- \n"
            f"[*] Name: {name} \n"
            f"[*] Brand: {brand} \n"
            f"[*] Type: {ctype} \n"
            f"[*] Annual Fee: {af} \n"
            f"[*] Credits: \n"
            f"{credits_str}"
            f"[*] Benefits: \n"
            f"{benefits_str}"
            )

    @property
    def brand(self): 
        return self._brand
    @brand.setter
    def brand(self, brand: str): 
        brands = ["BofA", "Chase", "AmEx", "Citi", "CapOne"]
        if brand not in brands: 
            raise ValueError("Invalid brand")
        self._brand = brand

    @property
    def type(self): 
        return self._type
    @type.setter
    def type(self, type: str): 
        types = ["cb", "points", "misc"]
        if type not in types: 
            raise ValueError("Wrong CC type")
        self._type = type

    @property
    def benefits(self): 
        return self._benefits
    @benefits.setter
    def benefits(self, benefits: dict): 
        self._benefits = CC.benefits_sorter(self, benefits)

    # Alphabetical sorting of benefits. Automatically called by @benefits.setter and __init__.
    def benefits_sorter(self, benefits: dict) -> dict: 
        sorted_benefits_names: list = sorted(benefits)
        sorted_benefits = {benefit: benefits[benefit] for benefit in sorted_benefits_names}
        return sorted_benefits

    @classmethod
    def search(cls, **kwargs) -> dict: # Important note: search() returns a dict, NOT prints it
        name: str = kwargs.get("name", None)
        brand: str = kwargs.get("brand", None)
        ctype: str = kwargs.get("type", None) # Named ctype because Python keeps confusing it with type() lol
        af = kwargs.get("af", None)
        benefit: str | list = kwargs.get("benefit", None)
        name_results = {}
        brand_results = {}
        type_results = {}
        af_results = {}
        benefit_results = {}
        if name: # Note: When name is searched, no other parameters are considered. 
            for _ in range(len(CC.all_CCs)): 
                databaseName: str = CC.all_CCs[_]["name"] # This extra step is to preserve the special capitalization in the main database all_CCs
                if databaseName.lower() == name.lower(): 
                    name_results[f"{(CC.all_CCs[_]["brand"])} {(CC.all_CCs[_]["name"])}"] = CC.all_CCs[_]
            return name_results # Dict entry for specific card
        if brand: 
            for _ in range(len(CC.all_CCs)): 
                if CC.all_CCs[_]["brand"] == brand: 
                    brand_results[f"{(CC.all_CCs[_]["brand"])} {(CC.all_CCs[_]["name"])}"] = CC.all_CCs[_]
        if ctype: 
            for _ in range(len(CC.all_CCs)): 
                if CC.all_CCs[_]["type"] == ctype: 
                    type_results[f"{(CC.all_CCs[_]["brand"])} {(CC.all_CCs[_]["name"])}"] = CC.all_CCs[_]
        if af: 
            if type(af) == str: 
                intAF = int(af)
                for _ in range(len(CC.all_CCs)): 
                    if CC.all_CCs[_]["af"] == intAF: 
                        af_results[f"{(CC.all_CCs[_]["brand"])} {(CC.all_CCs[_]["name"])}"] = CC.all_CCs[_]
            if type(af) == tuple: 
                afMin, afMax = af
                for _ in range(len(CC.all_CCs)): 
                    if afMin <= CC.all_CCs[_]["af"] <= afMax: 
                        af_results[f"{(CC.all_CCs[_]["brand"])} {(CC.all_CCs[_]["name"])}"] = CC.all_CCs[_]
        if benefit: 
            if type(benefit) == str: 
                for _ in range(len(CC.all_CCs)): 
                    try: 
                        if CC.all_CCs[_]["benefits"][benefit] != None: 
                            benefit_results[f"{(CC.all_CCs[_]["brand"])} {(CC.all_CCs[_]["name"])}"] = CC.all_CCs[_]
                    except KeyError: # Happens when a card does not have the searched benefit as a listed category
                        pass
            if type(benefit) == list: 
                list_of_dicts: list = []
                for entry in benefit: 
                    dict_data: dict = {}
                    for _ in range(len(CC.all_CCs)): 
                        try: 
                            if CC.all_CCs[_]["benefits"][entry] != None: 
                                dict_data[f"{(CC.all_CCs[_]["brand"])} {(CC.all_CCs[_]["name"])}"] = CC.all_CCs[_] # ex. 
                        except KeyError: # Happens when a card does not have the searched benefit of a listed category
                            pass
                    list_of_dicts.append(dict_data)
                benefit_results: dict = CC.benefit_dict_creator(list_of_dicts)
        
        results = {}

        if not name: # Creating results (type: dict) = intersection of all x_results dicts. When name is searched, no other parameters are considered. 
            if brand and ctype and benefit and af: # 1234
                common = brand_results.keys() & type_results.keys()
                common = common & benefit_results.keys()
                common = common & af_results.keys()
                results = {_: brand_results[_] for _ in common}
            elif brand and ctype and benefit: # 123
                common = brand_results.keys() & type_results.keys()
                common = common & benefit_results.keys()
                results = {_: type_results[_] for _ in common}
            elif brand and ctype and af: # 124
                common = brand_results.keys() & type_results.keys()
                common = common & af_results.keys()
                results = {_: brand_results[_] for _ in common}
            elif brand and benefit and af: # 134
                common = brand_results.keys() & benefit_results.keys()
                common = common & af_results.keys()
                results = {_: brand_results[_] for _ in common}
            elif ctype and benefit and af: # 234
                common = type_results.keys() & benefit_results.keys()
                common = common & af_results.keys()
                results = {_: type_results[_] for _ in common}
            elif brand and ctype: # 12
                common = brand_results.keys() & type_results.keys()
                results = {_: brand_results[_] for _ in common}
            elif brand and benefit: # 13
                common = brand_results.keys() & benefit_results.keys()
                results = {_: brand_results[_] for _ in common}
            elif brand and af: # 14
                common = brand_results.keys() & af_results.keys()
                results = {_: brand_results[_] for _ in common}
            elif ctype and benefit: # 23
                common = type_results.keys() & benefit_results.keys()
                results = {_: type_results[_] for _ in common}
            elif ctype and af: # 24
                common = type_results.keys() & af_results.keys()
                results = {_: type_results[_] for _ in common}
            elif benefit and af: # 34
                common = benefit_results.keys() & af_results.keys()
                results = {_: benefit_results[_] for _ in common}
            elif brand: # 1
                results = brand_results
            elif ctype: # 2
                results = type_results
            elif benefit: # 3
                results = benefit_results
            elif af: # 4
                results = af_results

        return results
    
    # Returns properly formatted brand name when entered English standard brand names
    @classmethod
    def brand_standardizer(cls, brandname: str) -> str | None: 
        # Possible_inputs: ["Chase", "Bank of America", "BofA", "American Express", "AmEx", "Citi", "Capital One", "CapOne"]
        brandname = brandname.lower().strip()
        if brandname == "chase": 
            return "Chase"
        if brandname == "bank of america" or brandname == "bofa": 
            return "BofA"
        if brandname == "american express" or brandname == "amex": 
            return "AmEx"
        if brandname == "citi": 
            return "Citi"
        if brandname == "capital one" or brandname == "capone": 
            return "CapOne"
        if brandname == "": 
            return None
        else: 
            return "error"
    
    # Returns properly formatted type name when entered English standard type names
    @classmethod
    def type_standardizer(cls, typename: str) -> str | None: 
        # Possible_inputs = ["Cash Back", "CashBack", "cb", "Points", "Point", "Pts", "Pt", "Miscellaneous", "Misc", "Misc."]
        typename = typename.lower().strip()
        if typename == "cash back" or typename == "cashback" or typename == "cb": 
            return "cb"
        if typename == "points" or typename == "point" or typename == "pts" or typename == "pt": 
            return "points"
        if typename == "miscellaneous" or typename == "misc" or typename == "misc.": 
            return "misc"
        if typename == "": 
            return None
        else: 
            return "error"
        
    # Returns properly formatted benefit names when entered list of benefit names
    @classmethod
    def benefit_standardizer(cls, benefitlist: list[str]) -> list | None: 
        formatted_list = []
        for benefit in benefitlist: 
            formatted_benefit = benefit.lower().strip().replace(" ", "_")
            formatted_list.append(formatted_benefit)
        return formatted_list #sorted(formatted_list)

    # When passed in a list of dicts formatted [{"Card1": {contents1}, "Card2": {contents2}}, {"Card1": {contents1}, "Card3": {contents3}}], returns intersection dict formaatted {"Card1": {contents1}}
    @classmethod
    def benefit_dict_creator(cls, list_input: list[dict]) -> dict: 
        common: set = list_input[0].keys()
        
        for i in range(len(list_input) - 1): # If list_input has indexes 0, 1, 2, 3, range() will return 0, 1, 2
            common = common & list_input[i + 1].keys()
        results = {_: list_input[0][_] for _ in common}

        return results

    # When passed in a list formatted [["<name>", "<brand>", "<type>", "<af>", "<benefits>", "<credits>"], ...] for each CC, will return a table created by tabulate() that is ready to print
    @classmethod
    def table_formatter(cls, data: list) -> str: 
        table = tabulate(data, CC.all_CCs_tabulate_headers, tablefmt="rounded_grid")
        return table
    
    # When passed in a dict formatted {"<benefit>": "<amount>", ...}, will return a dict with keys ordered from <amount> greatest to least in format {<amount_int>: ["<benefit_1>, <benefit_2"], ...}
    @classmethod
    def benefits_ranker(cls, data: dict) -> dict: 
        ranked_benefits = {}
        for key in data: 
            key_amount = data[key]
            temp_list = []
            if type(key_amount) == str: 
                try: 
                    key_amount = int(key_amount.replace("x", ""))
                except ValueError: # Occurs when key_amount is a float like "18.5x"
                    key_amount = float(key_amount.replace("x", ""))
            try:
                if ranked_benefits[key_amount] != None: 
                    temp_list = ranked_benefits[key_amount]
            except KeyError: 
                ranked_benefits[key_amount] = []
                temp_list: list = ranked_benefits[key_amount]
            temp_list.append(key)
            ranked_benefits[key_amount] = temp_list
        sorted_keys = sorted(ranked_benefits, reverse=True)
        ranked_benefits = {a: ranked_benefits[a] for a in sorted_keys}
        return ranked_benefits
    
    # When passed in a CC.search() result, will return a str formatted by table_formatter() and tabulate() that's ready to print
    @classmethod
    def table_creator(cls, data: dict, benefit_preference_list: list=None, results_quantity: int=None) -> str: 
        if benefit_preference_list: 
            data = CC.results_order(data, benefit_preference_list, results_quantity)
        
        table_formatter_input = []
        for card in data: 
            brand: str = data[card]["brand"]
            name: str = data[card]["name"]
            ctype: str = data[card]["type"]
            af = data[card]["af"]
            benefits: dict = data[card]["benefits"]
            credits: str = data[card]["credits"]

            if ctype == "cb": 
                tabulate_type = "Cash Back"
            if ctype == "points": 
                tabulate_type = "Points"
            if ctype == "misc": 
                tabulate_type = "Misc."
            
            if benefits != {}: 
                ranked_benefits = CC.benefits_ranker(benefits)
                tabulate_benefits = ""
                for benefit_amount in ranked_benefits: 
                    for benefit_name in ranked_benefits[benefit_amount]: 
                        benefit_name: str = benefit_name.replace("_", " ").title()
                        if ctype == "cb" and type(benefit_amount) == int: 
                            benefit_amount = f"{benefit_amount}%"
                        if ctype == "points" and type(benefit_amount) == int: 
                            benefit_amount = f"{benefit_amount}x"
                        if ctype == "cb" and type(benefit_amount) == float: 
                            benefit_amount = f"{benefit_amount}%"
                        if ctype == "points" and type(benefit_amount) == float: 
                            benefit_amount = f"{benefit_amount}x"
                        tabulate_benefits = tabulate_benefits + f"{benefit_amount}: {benefit_name}\n"
            if benefits == {}: 
                tabulate_benefits = "None"

            if credits == None: 
                tabulate_credits = "None"
            if credits != None: 
                tabulate_credits = ""
                credits_list = credits.split(", ")
                for index in credits_list: 
                    tabulate_credits = tabulate_credits + f"[*] {index}\n"
            
            table_formatter_item = [name, brand, tabulate_type, af, tabulate_benefits, tabulate_credits]
            table_formatter_input.append(table_formatter_item)
        return CC.table_formatter(table_formatter_input)

    # When passed in a CC.search() result, will return a dict in the same format but with the results ordered by the first benefit in benefit_preference_list and possibly limited in quantity to results_quantity
    @classmethod
    def results_order(cls, search_results: dict, benefit_preference_list: list, results_quantity: int=None) -> dict: 
        ben_pref: str = benefit_preference_list[0] # Note: results_order() only orders results based on the first benefit listed in benefit_preference_list
        ranked_cards = {}
        for card in search_results: 
            ben_amt = search_results[card]["benefits"][ben_pref]
            temp_list: list = []
            if type(ben_amt) == str: 
                try: 
                    ben_amt = int(ben_amt.replace("x", ""))
                except ValueError: # When ben_amt is a float like 18.5
                    ben_amt = float(ben_amt.replace("x", ""))
            try: 
                if ranked_cards[ben_amt] != None: 
                    temp_list = ranked_cards[ben_amt]
            except KeyError: 
                ranked_cards[ben_amt] = []
                temp_list = ranked_cards[ben_amt]
            temp_list.append(card) # card = "Chase Sapphire Preferred"
            ranked_cards[ben_amt] = temp_list
        sorted_cards = sorted(ranked_cards, reverse=True)
        ranked_cards = {a: ranked_cards[a] for a in sorted_cards} # In format {<amount_int>: ["card_1", "card_2"], ...}
        
        ordered_results = {}
        for amount_int in ranked_cards: 
            for card in ranked_cards[amount_int]: 
                if results_quantity: 
                    while len(ordered_results) < results_quantity: 
                        ordered_results[card] = search_results[card]
                        break
                else: 
                    ordered_results[card] = search_results[card]

        return ordered_results

home_screen = (
    "------------------------------------------------------------------------------------------------------------------------ \n"
    "Hi, welcome to CardWise! Please select which tool you would like to use or learn more about. \n"
    "[1] CardFinder: Credit Card Search Engine \n"
    "[2] CardMatch: Credit Card Selection Tool \n"
    "[3] CardVersus: Credit Card Comparison Tool \n"
    "[4] Exit"
)

cardfinder_home_screen = (
    "------------------------------------------------------------------------------------------------------------------------ \n"
    "CardFinder is a custom-built credit card search engine with a variety of available search criteria. \n"
    "Please select which criteria to search for. \n"
    "Hint: You can select multiple criteria by separating each number with a comma (ex. 1, 2, 3). \n"
    "[1] Card Name \n"
    "[2] Card Brand \n"
    "[3] Card Type \n"
    "[4] Card Benefits \n"
    "[5] Card Annual Fee \n"
    "[6] Return to CardWise Home Screen \n"
    "[7] Exit"
)

cardmatch_home_screen = (
    "------------------------------------------------------------------------------------------------------------------------ \n"
    "CardMatch is a custom-built credit card selection tool that can help you find the card best fitting your needs. \n"
    "Next, you will be asked to provide information on the brand, type, benefits, and annual fee of the card you want. \n"
    "If you have no preference on a specific category, simply press Enter to advance to the next question. \n"
    "CardMatch will be able to provide more refined suggestions if you enter more information. \n"
    "However, CardMatch may not be able to recommend a card if you enter too many criteria. \n"
    "Note: Results are always sorted by the first preferred benefit you list, so if you skip that question, the results will not be sorted. \n"
    "[1] Continue \n"
    "[2] Return to CardWise Home Screen \n"
    "[3] Exit"
)

cardversus_home_screen = (
    "------------------------------------------------------------------------------------------------------------------------ \n"
    "CardVersus is a custom-built credit card comparison tool that allows you to compare two cards' characteristics side-by-side. \n"
    "Next, you will be asked to enter the name of each card you want to compare. \n"
    "If you are not sure which cards you would like to compare, we recommend you use one of CardWise's other tools first. \n"
    "Note: Make sure to not include the brand name (ex. Enter \"Sapphire Preferred\" when searching for the Chase Sapphire Preferred Card). \n"
    "[1] Continue \n"
    "[2] Return to CardWise Home Screen \n"
    "[3] Exit"
)

exit_statement = (
    "------------------------------------------------------------------------------------------------------------------------ \n"
    "Thank you for using CardWise \n"
)

def main(): 
    while True: 
        try: 
            home_function()
        except ValueError: 
            pass
        else: 
            sys.exit("An unexpected error occured in main()")

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

def cardfinder(): 
    while True: 
        try: 
            print(cardfinder_home_screen)
            answers: list = input("Enter Number: ").replace(" ", "").replace("[", "").replace("]", "").split(",") # Format ["1", "2", "3"]
            searchName = None
            searchBrand = None
            searchType = None
            searchBenefit = None
            searchBenefitList = None
            searchAF = None
            searchMin = None
            searchMax = None
            existsAF = False
            if "1" in answers: # Card Name
                print(
                    "------------------------------------------------------------------------------------------------------------------------ \n"
                    "CardFinder - Searching by card name. It is recommended to only use this function when you know the exact card name you are looking for. \n"
                    "Hint: Don't include the brand name (ex. Enter \"Sapphire Preferred\" when searching for the Chase Sapphire Preferred Card)."
                )
                searchName = input("Card Name: ").strip().replace("'", "").replace('"', '').title()
                valid_search_engine = True
            if "2" in answers: # Card Brand
                print(
                    "------------------------------------------------------------------------------------------------------------------------ \n"
                    "CardFinder - Searching by card brand. \n"
                    "Currently supported brands: Chase, Bank of America, Citi, American Express, Capital One. \n"
                    "Note: Currently, searching is limited to one brand at a time."
                )
                searchBrand = input("Card Brand: ")
                searchBrand = CC.brand_standardizer(searchBrand)
                valid_search_engine = True
            if "3" in answers: # Card Type
                print(
                    "------------------------------------------------------------------------------------------------------------------------ \n"
                    "CardFinder - Searching by card type. \n"
                    "Currently supported types: cash back, points, and misc. \n"
                    "Note: Currently, searching is limited to one type at a time."
                )
                searchType = input("Card Type: ")
                searchType = CC.type_standardizer(searchType)
                valid_search_engine = True
            if "4" in answers: # Card Benefits
                print(
                    "------------------------------------------------------------------------------------------------------------------------ \n"
                    "CardFinder - Searching by card benefits. \n"
                    "Searchable benefits include but are not limited to: dining, gas, transit, groceries, travel, and streaming. \n"
                    "Hint: You can search for multiple benefits at the same time by separating them with a comma. "
                )
                searchBenefit = input("Card Benefits: ")
                searchBenefitList = searchBenefit.split(",")
                searchBenefitList = CC.benefit_standardizer(searchBenefitList)
                valid_search_engine = True
            if "5" in answers: # Card Annual Fee
                print(
                    "------------------------------------------------------------------------------------------------------------------------ \n"
                    "CardFinder - Searching by card annual fee. \n"
                    "Please enter a number (ex. 0) or range of numbers separated by a comma (ex. 50, 100), omitting any dollar signs."
                )
                searchAF = input("Card Annual Fee: ").replace("'", "").replace('"', '').replace(" ", "") # Returns format "1" or "1,2"
                if len(searchAF.split(",")) == 1: # Case for when AF value is searched. type(searchAF) = str
                    searchAF_range = False
                    valid_search_engine = True
                    existsAF = True
                elif len(searchAF.split(",")) == 2: # Case for when AF range is searched. type(searchAF) = tuple
                    searchMin, searchMax = searchAF.split(",")
                    searchMin = int(searchMin)
                    searchMax = int(searchMax)
                    searchAF = (searchMin, searchMax)
                    searchAF_range = True
                    valid_search_engine = True
                    existsAF = True
                else: 
                    valid_search_engine = False
                    pass
            if "6" in answers: # Return to CardWise Home Screen
                valid_search_engine = False
                home_function()
            if "7" in answers: # Exit
                valid_search_engine = False
                sys.exit(exit_statement)

            if valid_search_engine == True: # Defensive coding
                if existsAF:
                    if searchAF_range == False: # Case for when AF value is searched. type(searchAF) = str
                        print(CC.table_creator(CC.search(name=searchName, brand=searchBrand, type=searchType, af=searchAF, benefit=searchBenefitList)))
                    if searchAF_range == True: # Case for when AF range is searched. type(searchAF) = tuple
                        print(CC.table_creator(CC.search(name=searchName, brand=searchBrand, type=searchType, af=searchAF, benefit=searchBenefitList)))
                else: 
                    print(CC.table_creator(CC.search(name=searchName, brand=searchBrand, type=searchType, benefit=searchBenefitList))) # Need to print because CC.search() only returns the dict
            else: 
                raise ValueError("Invalid input from CardFinder Home Screen")
        except ValueError: 
            pass

def cardmatch(): 
    while True: 
        try: 
            print(cardmatch_home_screen)
            cont = input("Enter Number: ")
            if cont.strip() == "2": # Return to CardWise Home Screen
                home_function()
            elif cont.strip() == "3": # Exit
                sys.exit(exit_statement)
            elif cont.strip() == "1": # Continue to CardMatch
                brand_preference = input(
                    "Options for credit card brands include Chase, Bank of America, Citi, American Express, and Capital One. \n"
                    "Please enter your preferred card brand: "
                )
                brand_preference = CC.brand_standardizer(brand_preference)

                type_preference = input(
                    "------------------------------------------------------------------------------------------------------------------------ \n"
                    "Options for credit card types include Cash Back, Points, or Miscellaneous. \n"
                    "Neither cash back nor points cards have an inherent advantage over the other; the choice depends on lifestyle. \n"
                    "Note: Miscellaneous cards usually have promotional 0% APRs but no outstanding benefit. \n"
                    "Please enter your preferred card type: "
                )
                type_preference = CC.type_standardizer(type_preference)

                benefit_preference = input(
                    "------------------------------------------------------------------------------------------------------------------------ \n"
                    "Credit card benefits are rewards earned from card usage, typically in the form of either cash back or points. \n"
                    "Benefits may be earned by category spending, such as \"Dining\", or may be brand-specific, such as \"DoorDash\". \n"
                    "In addition, many cards allow you to earn points on \"All\" spending, even if it doesn't fit nicely in a category. \n"
                    "Finally, some cards may have multiple benefits while others may have none. \n"
                    "Some common benefits include but are not limited to: dining, gas, transit, groceries, travel, and streaming. \n"
                    "Results are always sorted by the first preferred benefit you list, so if you skip this question, the results will not be sorted. \n"
                    "Hint: You can search for multiple benefits at the same time by separating them with a comma. \n"
                    "Please enter your preferred benefits: "
                )
                benefit_preference_list: list = benefit_preference.split(",")
                benefit_preference_list = CC.benefit_standardizer(benefit_preference_list)

                af_preference = input(
                    "------------------------------------------------------------------------------------------------------------------------ \n"
                    "Credit cards have a wide range of annual fees, which are fees you must pay each year to keep the card. \n"
                    "Some high-end credit cards charge annual fees from under $100 to over $600, but many great cards have no fee. \n"
                    "In fact, most cash back cards do not charge an annual fee, which are more common among points cards meant for travel. \n"
                    "Generally, the higher the annual fee, the more benefits or credits the card comes with. \n"
                    "Hint: You can enter a range of annual fees by separating them with a comma (ex. 0, 100). \n"
                    "Please enter your preferred annual fee: "
                )
                af_preference = af_preference.replace("'", "").replace('"', '').replace(" ", "") # Returns format "1" or "1,2"
                if len(af_preference.split(",")) == 2: # Case for when AF range is searched. type(af_preference) = tuple
                    searchMin, searchMax = af_preference.split(",")
                    searchMin = int(searchMin)
                    searchMax = int(searchMax)
                    af_preference = (searchMin, searchMax)
                elif len(af_preference.split(",")) == 1: # Case for when AF value is searched. type(af_preference) = str
                    if af_preference == "": 
                        af_preference = None
                else: 
                    af_preference = None
                
                results_quantity = input(
                    "------------------------------------------------------------------------------------------------------------------------ \n"
                    "Finally, please enter the maximum amount of card results you would like to view. \n"
                    "CardMatch will automatically show the results in order of greatest benefit multiplier to least. \n"
                    "However, depending on your lifestyle, the card with the highest benefit multipliers might not always be the best card for you. \n"
                    "You can also choose to view all results by simply pressing Enter with no value entered. \n"
                    "Please enter the quantity of results to view: "
                ) 
                if results_quantity.strip() == "": 
                    results_quantity = None
                elif results_quantity.strip() != "":
                    results_quantity = int(results_quantity)
                
                search_results = CC.search(brand=brand_preference, type=type_preference, af=af_preference, benefit=benefit_preference_list)
                print(CC.table_creator(search_results, benefit_preference_list=benefit_preference_list, results_quantity=results_quantity))
            else: 
                raise ValueError("Invalid input from CardMatch Home Screen")
        except ValueError:
            pass

def cardversus(): 
    while True: 
        try: 
            print(cardversus_home_screen)
            cont = input("Enter Number: ")
            if cont.strip() == "2": # Return to CardWise Home Screen
                home_function()
            elif cont.strip() == "3": # Exit
                sys.exit(exit_statement)
            elif cont.strip() == "1": # Continue to CardVersus
                card_1 = input(
                    "------------------------------------------------------------------------------------------------------------------------ \n"
                    "Card 1: Please enter the name of the first card you would like to compare. \n"
                    "Note: Make sure to not include the brand name (ex. Enter \"Sapphire Preferred\" when searching for the Chase Sapphire Preferred Card). \n"
                    "Card 1 Name: "
                )
                card_1 = card_1.strip().title()
                if card_1 == "Platinum": 
                    clarification_1 = input(
                        "There are two cards named \"Platinum\": the American Express Platinum and Capital One Platinum. \n"
                        "Which one did you mean? \n"
                        "[1] American Express Platinum \n"
                        "[2] Capital One Platinum \n"
                        "Enter Number: "
                    )
                    if clarification_1.strip() == "1": 
                        card_1_search = CC.search(brand="AmEx", type="points", af="695")
                    if clarification_1.strip() == "2": 
                        card_1_search = CC.search(brand="CapOne", type="misc")
                else: 
                    card_1_search = CC.search(name=card_1)

                card_2 = input(
                    "------------------------------------------------------------------------------------------------------------------------ \n"
                    "Card 2: Please enter the name of the first card you would like to compare. \n"
                    "Note: Make sure to not include the brand name (ex. Enter \"Sapphire Preferred\" when searching for the Chase Sapphire Preferred Card). \n"
                    "Card 2 Name: "
                )
                card_2 = card_2.strip().title()
                if card_2 == "Platinum": 
                    clarification_2 = input(
                        "There are two cards named \"Platinum\": the American Express Platinum and Capital One Platinum. \n"
                        "Which one did you mean? \n"
                        "[1] American Express Platinum \n"
                        "[2] Capital One Platinum \n"
                        "Enter Number: "
                    )
                    if clarification_2.strip() == "1": 
                        card_2_search = CC.search(brand="AmEx", type="points", af="695")
                    if clarification_2.strip() == "2": 
                        card_2_search = CC.search(brand="CapOne", type="misc")
                else: 
                    card_2_search = CC.search(name=card_2)
                
                if card_1_search == {} or card_2_search == {}: 
                    print(
                        "------------------------------------------------------------------------------------------------------------------------ \n"
                        "At least one of the card names you entered was not valid. \n"
                        "Please check that the spelling was correct and/or that you did not include the brand name as part of the card name. \n"
                        "Note: Currently, CardWise only supports cards issued by Chase, Bank of America, Citi, American Express, and Capital One. "
                    )
                    raise ValueError("Invalid card name from CardVersus")
                
                combined_card_search = card_1_search | card_2_search
                print(CC.table_creator(combined_card_search))
            else: 
                raise ValueError("Invalid input from CardVersus Home Screen")
        except ValueError: 
            pass

def fx_benefits_ranker(data: dict) -> dict: 
    return CC.benefits_ranker(data)

def fx_benefit_dict_creator(list_input: list[dict]) -> dict: 
    return CC.benefit_dict_creator(list_input)

def fx_benefit_standardizer(benefitlist: list[str]) -> list | None: 
    return CC.benefit_standardizer(benefitlist)

# CC Database
# Not including SUBs or business cards or variable statement credits
Chase_Sapphire_Preferred = CC("Chase", "Sapphire Preferred", "points", 95, credits="$150 in Partnership Benefits, $50 Annual Chase Travel Hotel Credit", dining="3x", travel="2x", chase_travel="5x", online_groceries="3x", streaming="3x", all="1x")
Chase_Sapphire_Reserve = CC("Chase", "Sapphire Reserve", "points", 550, credits="$1000 in Partnership Benefits, $300 Annual Travel Credits", chase_travel_hotels_and_car_rentals="10x", chase_travel_flights="5x", chase_dining="10x", dining="3x")
Chase_Freedom_Unlimited = CC("Chase", "Freedom Unlimited", "cb", all=1.5, dining=3, drugstores=3, chase_travel=5)
Chase_Freedom_Flex = CC("Chase", "Freedom Flex", "cb", category=5, chase_travel=5, dining=3, drugstores=3, all=1)
Chase_Freedom_Rise = CC("Chase", "Freedom Rise", "cb", all=1.5)
Chase_United_Explorer = CC("Chase", "United Explorer", "points", 95, credits="Free first checked bag, 2 United Club one-time passes per year, $100 statement credit for Global Entry/TSA Precheck/NEXUS \n    every 4 years", united_flights="7x", united_hotels="4x", united_all="2x", dining="2x", hotels="2x", all="1x")
Chase_United_Quest = CC("Chase", "United Quest", "points", 250, credits="Free first and second checked bags, $125 annual United purchase credit, Up to 10000 miles in award flight credits each year", united_flights="8x", united_hotels="4x", united_all="3x", travel="2x", dining="2x", streaming="2x", all="1x")
Chase_United_Gateway = CC("Chase", "United Gateway", "points", united_flights="7x", united_hotels="3x", united_all="2x", gas="2x", transit="2x", all="1x")
Chase_United_Club_Infinite = CC("Chase", "United Club Infinite", "points", 525, credits="Free first and second checked bags, United Club membership, Premier Access travel services, $100 statement credit for Global Entry/TSA PreCheck/NEXUS \n    every 4 years", united_flights="9x", united_hotels="4x", united_all="4x", travel="2x", dining="2x", all="1x")
Chase_Southwest_Rapid_Rewards_Plus = CC("Chase", "Southwest Rapid Rewards Plus", "points", 69, credits="3000 points every year, 2 EarlyBird Check-In each year, 10000 Companion Pass qualifying points boost each year", southwest_all="2x", rapid_rewards_travel="2x", transit="2x", streaming="2x", internet="2x", all="1x")
Chase_Southwest_Rapid_Rewards_Priority = CC("Chase", "Southwest Rapid Rewards Priority", "points", 149, credits="7500 points every year, $75 Southwest annual travel credit, 4 upgraded boardings per year, unlimited tier qualifying points, 10000 Companion Pass qualifying points boost each year", southwest_all="3x", rapid_rewards_travel="2x", transit="2x", internet="2x", streaming="2x", all="1x")
Chase_Southwest_Rapid_Rewards_Premier = CC("Chase", "Southwest Rapid Rewards Premier", "points", 99, credits="6000 points every year, 2 EarlyBird Check-In each year, unlimited tier qualifying points, 10000 Companion Pass qualifying points boost each year", southwest_all="3x", rapid_rewards_travel="2x", transit="2x", internet="2x", streaming="2x", all="1x")
Chase_Prime_Visa = CC("Chase", "Prime Visa", "cb", amazon=5, amazon_fresh=5, whole_foods=5, chase_travel=5, gas=2, dining=2, transit=2, all=1, amazon_prime_selection=10)
Chase_Amazon_Visa = CC("Chase", "Amazon Visa", "cb", amazon=3, amazon_fresh=3, whole_foods=3, chase_travel=3, gas=2, dining=2, transit=2, all=1)
Chase_Aeroplan = CC("Chase", "Aeroplan", "points", 95, credits="Free first checked bag, Priority Airport Services, Aeroplan 25K Status, 500 bonus points for every $2000 spent in a calendar month \n    up to 1500 points per month", groceries="3x", dining="3x", air_canada="3x", all="1x")
Chase_Marriott_Bonvoy_Boundless = CC("Chase", "Marriott Bonvoy Boundless", "points", 95, credits="Annual Free Night Award", marriott="17x", groceries="3x", gas="3x", dining="3x", all="2x")
Chase_Marriott_Bonvoy_Bountiful = CC("Chase", "Marriott Bonvoy Bountiful", "points", 250, credits="1000 bonus points per stay at Marriott Bonvoy hotels, Annual Free Night Award", marriott="18.5x", groceries="4x", dining="4x", all="2x")
Chase_Marriott_Bonvoy_Bold = CC("Chase", "Marriott Bonvoy Bold", "points", credits="Automatic Silver Elite Status", marriott="14x", groceries="2x", online_groceries="2x", internet="2x", streaming="2x")
Chase_Disney_Visa = CC("Chase", "Disney Visa", "cb", disney_store=10, disney_resorts=10, all=1)
Chase_Disney_Premier_Visa = CC("Chase", "Disney Premier Visa", "cb", 49, disney_store=10, disney_resorts=10, disney_plus=5, hulu=5, espn_plus=5, gas=2, groceries=2, dining=2, disney=2, all=1)
Chase_IHG_One_Rewards_Premier = CC("Chase", "IHG One Rewards Premier", "points", 99, credits="Automatic Platinum Elite Status, $100 statement credit and 10000 bonus points after spending \n    $20000 each calendar year, Anniversary Free Night", ihg_hotels="26x", ihg_resorts="26x", travel="5x", dining="5x", gas="5x", all="3x")
Chase_IHG_One_Rewards_Traveler = CC("Chase", "IHG One Rewards Traveler", "points", credits="Automatic Silver Elite Status, 10000 bonus points after spending $10000 each calendar year, Redeem 3 nights to get the 4th night free", ihg_hotels="17x", ihg_resorts="17x", dining="3x", utilities="3x", streaming="3x", gas="3x", all="2x")
Chase_World_of_Hyatt = CC("Chase", "World of Hyatt", "points", 95, credits="Annual Free Night Award, Extra Free Night after spending $15000 in a calendar year", hyatt_hotels="9x", dining="2x", travel="2x", transit="2x", gym="2x", all="1x")
Chase_British_Airways = CC("Chase", "British Airways", "points", 95, credits="Up to $600 in flight statement credits every year, Travel Together Ticket every calendar year after spending \n    $30000", british_airways_flights="3x", aer_lingus_flights="3x", iberia_flights="3x", hotels="2x", all="1x")
Chase_Aer_Lingus = CC("Chase", "Aer Lingus", "points", 95, credits="Economy Companion Ticket every calendar year after spending \n    $30000, Priority boarding", british_airways_flights="3x", aer_lingus_flights="3x", iberia_flights="3x", hotels="2x", all="1x")
Chase_Iberia = CC("Chase", "Iberia", "points", 95, credits="$1000 airfare discount voucher each calendar year after \n    spending $30000", iberia_flights="3x", british_airways_flights="3x", aer_lingus_flights="3x", hotels="2x", all="1x")
Chase_DoorDash_Rewards = CC("Chase", "DoorDash Rewards", "cb", credits="Complimentary DashPass Membership every year with $10000 in \n    annual card spend", doordash=4, dining=3, groceries=2, online_groceries=2, all=1)
Chase_Instacart = CC("Chase", "Instacart", "cb", instacart=5, chase_travel=5, dining=2, gas=2, streaming=2, all=1)
BofA_Customized_Cash_Rewards = CC("BofA", "Customized Cash Rewards", "cb", category=3, groceries=2, wholesale=2, all=1)
BofA_Unlimited_Cash_Rewards = CC("BofA", "Unlimited Cash Rewards", "cb", all=1.5)
BofA_BankAmericard = CC("BofA", "BankAmericard", "misc", credits="No penalty APR")
BofA_Travel_Rewards = CC("BofA", "Travel Rewards", "points", all=1.5)
BofA_Premium_Rewards = CC("BofA", "Premium Rewards", "points", 95, credits="$100 in airline incidental statement credits every year, $100 statement credit for Global Entry/TSA PreCheck every \n    four years", travel="2x", dining="2x", all="1.5x")
BofA_Premium_Rewards_Elite = CC("BofA", "Premium Rewards Elite", "points", 550, credits="Free Unlimited Access to airport lounges and experiences \n    worldwide, Up to 4 complimentary Priority Pass Select Memberships, Complimentary 24/7 Full-Service Concierge to book travel and \n    reservations, $300 in airline incident statement credits every year, $150 for lifestyle conveniences, $100 statement credit for Global Entry/TSA PreCheck every \n    four years", travel="2x", dining="2x", all="1.5x")
Citi_AAdvantage_Platinum_Select = CC("Citi", "AAdvantage Platinum Select", "points", 99, credits="First checked bag free on American Airlines, Preferred boarding on American Airlines", dining="2x", gas="2x", american_airlines="2x", all="1x")
Citi_Strata_Premier = CC("Citi", "Strata Premier", "points", 95, credits="$100 off a single hotel stay of $500 or more every year", citi_travel="10x", travel="3x", hotels="3x", dining="3x", groceries="3x", gas="3x", all="1x")
Citi_Double_Cash = CC("Citi", "Double Cash", "cb", all=2, citi_travel=5)
Citi_Custom_Cash = CC("Citi", "Custom Cash", "cb", category=5, all=1)
Citi_Rewards = CC("Citi", "Rewards+", "points", citi_travel="5x", groceries="2x", gas="2x", all="1x")
Citi_Simpicity = CC("Citi", "Simplicity", "misc", credits="No late fees and no penalty rate")
Citi_Diamond_Preferred = CC("Citi", "Diamond Preferred", "misc")
Citi_Costco_Anywhere = CC("Citi", "Costco Anywhere", "cb", gas=4, dining=3, travel=3, costco=2, all=1)
Citi_AAdvantage_World_Executive = CC("Citi", "AAdvantage World Executive", "points", 595, credits="First checked bag free on American Airlines, Up to $120 in annual Lyft credits, Up to $120 back on Grubhub purchases, Citi Entertainment, Complimentary priority check-in and screening, Dedicated Conceriege for travel & reservations, $100 statement credit for Global Entry/TSA PreCheck every \n    four years", american_airlines="4x", all="1x")
Citi_AAdvantage_MileUp = CC("Citi", "MileUp", "points", groceries="2x", online_groceries="2x", american_airlines="2x", all="1x")
Citi_Secured_Mastercard = CC("Citi", "Secured Mastercard", "misc")
Citi_ATNT_Points_Plus = CC("Citi", "AT&T Points Plus", "points", gas="3x", groceries="2x", online_groceries="2x", all="1x")
AmEx_Gold = CC("AmEx", "Gold", "points", 325, credits="Up to $120 in annual Uber credits, Up to $84 in annual Dunkin' credits", dining="4x", groceries="4x", travel="3x")
AmEx_Platinum = CC("AmEx", "Platinum", "points", 695, credits="Up to $200 in annual hotel credits, Up to $200 in annual Uber credits, Up to $155 in annual Walmart+ credits, Up to $200 in annual airline fee credits, American Express Global Lounge Collection Access, Up to $240 in annual streaming credits, $199 in annual CLEAR Plus credits", american_express_travel="5x", travel="5x", all="1x")
AmEx_Blue_Cash_Everyday = CC("AmEx", "Blue Cash Everyday", "cb", credits="Up to $84 in annual Disney Bundle credits", groceries=3, online_shopping=3, gas=3, all=1)
AmEx_Blue_Cash_Preferred = CC("AmEx", "Blue Cash Preferred", "cb", 95, groceries=6, streaming=6, transit=3, gas=3, all=1)
AmEx_Green = CC("AmEx", "Green", "points", 150, credits="$199 annual CLEAR Plus credits", travel="3x", transit="3x", dining="3x")
AmEx_Delta_SkyMiles_Reserve = CC("AmEx", "Delta SkyMiles Reserve", "points", 650, credits="Complimentary Delta Sky Club Access, Complimentary Access to the Centurion Lounge, $2500 Medallion Qualificiation Dollars each year, Annual Companion Certificate, Up to $240 in annual Resy credits, Up to $120 in annual rideshare credits, $200 in annual Delta Stays credits", delta="3x", hotels="3x", dining="2x", groceries="2x", all="1x")
AmEx_Cash_Magnet = CC("AmEx", "Cash Magnet", "cb", all=1.5)
AmEx_Delta_SkyMiles_Platinum = CC("AmEx", "Delta SkyMiles Platinum", "points", 350, credits="First checked bag free on Delta flights, $2500 Medallion Qualification Dollars each year, Annual Companion Certificate, $150 in annual Delta Stays credits, Up to $120 in annual rideshare credits, Up to $120 in annual Resy credits", delta="3x", all="1x")
AmEx_Delta_SkyMiles_Gold = CC("AmEx", "Delta SkyMiles Gold", "points", 150, credits="First checked bag free on Delta flights, $100 in annual Delta Stays credits, Priority boarding on Delta flights", dining="2x", groceries="2x", delta="2x", all="1x")
AmEx_EveryDay = CC("AmEx", "EveryDay", "cb", groceries=2, all=1)
AmEx_Hilton_Honors = CC("AmEx", "Hilton Honors", "points", credits="Hilton Honors Silver Status", hilton="7x", dining="5x", groceries="5x", gas="5x", all="3x")
AmEx_Hilton_Honors_Surpass = CC("AmEx", "Hilton Honors Surpass", "points", 150, credits="Hilton Honors Gold Status", hilton="12x", dining="6x", groceries="6x", gas="6x", online_shopping="4x", all="3x")
AmEx_Hilton_Honors_Aspire = CC("AmEx", "Hilton Honors Aspire", "points", 550, credits="Hilton Honors Diamond Status, Up to $400 in annual Hilton Resort credits", hilton="14x", dining="7x", travel="7x", all="3x")
AmEx_Marriott_Bonvoy_Bevy = CC("AmEx", "Marriott Bonvoy Bevy", "points", 250, credits="Marriott Bonvoy Gold Elite Status, Annual Free Night Award", marriott="6x", dining="4x", groceries="4x", all="2x")
AmEx_Marriott_Bonvoy_Brilliant = CC("AmEx", "Marriott Bonvoy Brilliant", "points", 650, credits="Marriot Bonvoy Platinum Elite Status, Up to $300 in annual dining statement credits, Annual Free Night Award, $120 statement credit for Global Entry/TSA PreCheck every \n    4.5 years, $100 in Marriott Bonvoy property credit", marriott="6x", dining="3x", travel="3x", all="2x")
AmEx_Delta_SkyMiles_Blue = CC("AmEx", "Delta SkyMiles Blue", "points", dining="2x", delta="2x", all="1x")
AmEx_EveryDay_Preferred = CC("AmEx", "EveryDay Preferred", "points", 95, groceries="3x", gas="3x", all="1x")
CapOne_Platinum = CC("CapOne", "Platinum", "misc")
CapOne_Venture_X = CC("CapOne", "Venture X", "points", 395, credits="$300 in annual travel credits, $100 in statement credits for Global Entry/TSA PreCheck, 10000 bonus miles each year, Complimentary access to airport lounges", capital_one_travel_hotels_and_rental_cars="10x", capital_one_travel_flights_and_rentals="5x", all="2x")
CapOne_Venture = CC("CapOne", "Venture", "points", 95, credits="$50 in experience credits every Lifestyle Collection stay, Up to $100 in statement credits for Global Entry/TSA \n    PreCheck, Hertz Five Star Status", capital_one_travel="5x", all="2x")
CapOne_VentureOne = CC("CapOne", "VentureOne", "points", capital_one_travel="5x", all="1.25x")
CapOne_Quicksilver = CC("CapOne", "Quicksilver", "cb", all="1.5x")
CapOne_SavorOne = CC("CapOne", "SavorOne", "cb", capital_one_travel=5, dining=3, entertainment=3, streaming=3, groceries=3, all=1)
CapOne_REI_CoOp = CC("CapOne", "REI Co-Op", "cb", rei=5, all=1.5)
CapOne_Pottery_Barn_Key_Rewards = CC("CapOne", "Pottery Barn Key Rewards", "cb", credits="$25 annual birthday reward", pottery_barn=5, williams_sonoma=5, west_elm=5, groceries=4, dining=4, food_delivery=4, all=1)
CapOne_West_Elm_Key_Rewards = CC("CapOne", "West Elm Key Rewards", "cb", credits="$25 annual birthday reward", pottery_barn=5, williams_sonoma=5, west_elm=5, groceries=4, dining=4, food_delivery=4, all=1)
CapOne_Williams_Sonoma_Key_Rewards = CC("CapOne", "Williams Sonoma Key Rewards", "cb", credits="$25 annual birthday reward", pottery_barn=5, williams_sonoma=5, west_elm=5, groceries=4, dining=4, food_delivery=4, all=1)
CapOne_The_Key_Rewards = CC("CapOne", "The Key Rewards", "cb", credits="$25 annual birthday reward", pottery_barn=5, williams_sonoma=5, west_elm=5, groceries=4, dining=4, food_delivery=4, all=1)
CapOne_Cabelas = CC("CapOne", "Cabela's CLUB Card", "cb", bass_pro_shops=5, cabelas=5, all=1)
CapOne_Bass_Pro_Shops = CC("CapOne", "Bass Pro Shops CLUB Card", "cb", bass_pro_shops=5, cabelas=5, all=1)
CapOne_BJs_One = CC("CapOne", "BJ's One Mastercard", "cb", bjs=3, all=1.5)
CapOne_BJs_One_Plus = CC("CapOne", "BJ's One+ Mastercard", "cb", bjs=5, all=2)

if __name__ == "__main__": 
    main()
