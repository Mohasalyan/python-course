# Dependency Inversion Principle (DIP)

from abc import ABC, abstractmethod


class Publisher(ABC):
    @abstractmethod
    def publish(self, news: str) -> None:
        pass


class NewsPaper(Publisher):
    def publish(self, news: str) -> None:
        print(f"{news} published today!")


class Reporter:
    """
    Reporter no longer depends directly on NewsPaper.
    It relies on the abstract Publisher interface.
    """
    def __init__(self, publisher: Publisher):
        self.publisher = publisher

    def publish(self, news: str) -> None:
        self.publisher.publish(news)


# Example Usage
news_paper = NewsPaper()
reporter = Reporter(news_paper)
reporter.publish("Breaking News!")  # "Breaking News! published today!"
