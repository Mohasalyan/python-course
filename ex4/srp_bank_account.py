# Single Responsibility Principle (SRP)

accounts_list = []


class BankAccount:
    """
    BankAccount only handles account-related operations.
    """
    def __init__(self, account_no: str):
        self.account_no = account_no

    def get_account_number(self) -> str:
        return self.account_no


class AccountRepository:
    """
    Handles database-related actions (saving accounts).
    """
    @staticmethod
    def save(account: BankAccount) -> None:
        accounts_list.append(account)
        print(f"Success, saved account {account.get_account_number()} to DB")


# Example Usage
account = BankAccount("123456789")
repo = AccountRepository()
repo.save(account)
