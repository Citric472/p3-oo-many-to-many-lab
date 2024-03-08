class Book:
    def __init__(self, title):
        self.title = title

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]


class Author:
    def __init__(self, name):
        self.name = name

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Invalid author type")
        if not isinstance(book, Book):
            raise Exception("Invalid book type")
        if not isinstance(date, str):
            raise Exception("Invalid date type")
        if not isinstance(royalties, int):
            raise Exception("Invalid royalties type")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        self.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return sorted(cls.all, key=lambda x: (x.date, x.author.name, x.book.title)) if date else cls.all
