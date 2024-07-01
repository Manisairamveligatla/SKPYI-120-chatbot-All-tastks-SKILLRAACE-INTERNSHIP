class Book:
    def __init__(self, title, author, publisher, price):
        self._title = title
        self._author = author
        self._publisher = publisher
        self._price = price
        self._royalty = 0

    # Getter and setter for title
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    # Getter and setter for author
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        self._author = author

    # Getter and setter for publisher
    @property
    def publisher(self):
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        self._publisher = publisher

    # Getter and setter for price
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    # Method to calculate royalty
    def royalty(self, copies_sold):
        if copies_sold <= 500:
            self._royalty = 0.10 * self._price * copies_sold
        elif copies_sold <= 1500:
            self._royalty = (0.10 * self._price * 500) + (0.125 * self._price * (copies_sold - 500))
        else:
            self._royalty = (0.10 * self._price * 500) + (0.125 * self._price * 1000) + (0.15 * self._price * (copies_sold - 1500))
        return self._royalty


class EBook(Book):
    def __init__(self, title, author, publisher, price, ebook_format):
        super().__init__(title, author, publisher, price)
        self._ebook_format = ebook_format

    # Getter and setter for ebook format
    @property
    def ebook_format(self):
        return self._ebook_format

    @ebook_format.setter
    def ebook_format(self, ebook_format):
        self._ebook_format = ebook_format

    # Override the royalty method to include GST deduction
    def royalty(self, copies_sold):
        base_royalty = super().royalty(copies_sold)
        gst_deduction = 0.12 * base_royalty
        self._royalty = base_royalty - gst_deduction
        return self._royalty


# Example usage
book = Book("Sample Book", "John Doe", "Sample Publisher", 20.0)
ebook = EBook("Sample EBook", "Jane Doe", "Sample Publisher", 15.0, "EPUB")

print("Book Royalty for 2000 copies sold: $", book.royalty(2000))
print("EBook Royalty for 2000 copies sold: $", ebook.royalty(2000))
