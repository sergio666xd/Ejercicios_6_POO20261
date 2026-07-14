from typing import overload, List

class ScientificArticle:

    @overload
    def __init__(self, title: str, author: str):
        ...

    @overload
    def __init__(self, title: str, author: str, keywords: List[str], publication: str, year: int):
        ...

    @overload
    def __init__(self, title: str, author: str, keywords: List[str], publication: str, year: int, abstract: str):
        ...


    def __init__(self, *args):
        total_args = len(args)
        
        if total_args == 2:
            self._init_first_constructor(*args)
        elif total_args == 5:
            self._init_second_constructor(*args)
        elif total_args == 6:
            self._init_third_constructor(*args)
        else:
            raise TypeError(
                f"Cannot instantiate ScientificArticle with {total_args} arguments. "
                "Expected 2, 5, or 6."
            )


    def _init_first_constructor(self, title: str, author: str):
        """Constructor 1: Only title and author."""
        self.title = title
        self.author = author
        self.keywords: List[str] = []
        self.publication = "Not specified"
        self.year = 0
        self.abstract = "No abstract"

    def _init_second_constructor(self, title: str, author: str, keywords: List[str], publication: str, year: int):
        """Constructor 2: Invokes the first (this) and adds more metadata."""
        self._init_first_constructor(title, author)
        self.keywords = keywords
        self.publication = publication
        self.year = year

    def _init_third_constructor(self, title: str, author: str, keywords: List[str], publication: str, year: int, abstract: str):
        """Constructor 3: Invokes the second (this) and adds the abstract."""
        self._init_second_constructor(title, author, keywords, publication, year)
        self.abstract = abstract


    def print_details(self):
        """Prints the scientific article data on the screen."""
        print("\n========================================")
        print("       SCIENTIFIC ARTICLE DETAILS")
        print("========================================")
        print(f"Title = {self.title}")
        print(f"Author = {self.author}")
        print("Keywords =")
        if self.keywords:
            for i, keyword in enumerate(self.keywords, 1):
                print(f"  {i}. {keyword}")
        else:
            print("  (None)")
        print(f"Publication = {self.publication}")
        print(f"Year = {self.year if self.year != 0 else 'Not specified'}")
        print(f"Abstract = {self.abstract}")
        print("========================================\n")

if __name__ == "__main__":
    
    print("Scientific Article Manager\n")
    print("Select how you want to register the scientific article:\n")
    print("1. Basic registration (Title and Author only)")
    print("2. Standard registration (Title, Author, 3 Keywords, Publication, and Year)")
    print("3. Complete registration (Title, Author, 3 Keywords, Publication, Year, and Abstract)")

    while True:
        try:
            option = int(input("\nEnter the number of the desired option: "))
            if option in [1, 2, 3]:
                break
            print("Please select a valid option (1, 2, or 3).")
        except ValueError:
            print("Please enter a valid number.")

    # Shared variables
    title = ""
    author = ""

    # ================= OPTION 1 =================
    if option == 1:
        title = input("Article title: ")
        author = input("Article author: ")
        
        # Instantiate using the first constructor (2 parameters)
        article = ScientificArticle(title, author)
        article.print_details()

    # ================= OPTION 2 =================
    elif option == 2:
        title = input("Article title: ")
        author = input("Article author: ")
        
        # Request exactly 3 keywords
        keywords_list = []
        print("Enter 3 keywords for the article:")
        for i in range(3):
            keyword = input(f"  Keyword {i+1}: ")
            keywords_list.append(keyword)
            
        publication = input("Publication name: ")
        
        while True:
            try:
                year = int(input("Publication year: "))
                break
            except ValueError:
                print("Please enter a valid year (integer number).")

        article = ScientificArticle(title, author, keywords_list, publication, year)
        article.print_details()

    # ================= OPTION 3 =================
    elif option == 3:
        title = input("Article title: ")
        author = input("Article author: ")
        
        keywords_list = []
        print("Enter 3 keywords for the article:")
        for i in range(3):
            keyword = input(f"  Keyword {i+1}: ")
            keywords_list.append(keyword)
            
        publication = input("Publication name: ")
        
        while True:
            try:
                year = int(input("Publication year: "))
                break
            except ValueError:
                print("Please enter a valid year (integer number).")
                
        abstract = input("Article abstract: ")

        article = ScientificArticle(title, author, keywords_list, publication, year, abstract)
        article.print_details()