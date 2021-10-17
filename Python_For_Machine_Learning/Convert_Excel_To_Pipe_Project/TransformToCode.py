
import re
import numpy
from pandas.core.frame import DataFrame

class TransformToCode:

    def __init__(self, frameObj:DataFrame) -> None:
        self.frameObj = frameObj


    def acct_status_to_code(self, status:str)->str:
        if (len(str(status)) ==3) and (str(status) in ['001', '002', '003']):
            return status
        elif str(status) in ['1','2','3']:
            return str(status).zfill(3)
        elif str(status).lower() in ['open', 'opened', 'opn']:
            return '001'
        elif str(status).lower() in ['close', 'closed', 'cls']:
            return '002'
        elif str(status).lower() in ['written off', 'write off', 'writtenoff']:
            return '003'
        else:
            return '001'
        
    def currency_to_code(self, currency:str)->str:
        if (len(str(currency)) ==3) and (str(currency).lower() in ['ngn', 'usd', 'eur', 'gbp']):
            return currency.upper()
        elif (str(currency).lower() in ['naira', 'ng', 'n']) or re.match(r'na[a-z]*', str(currency).lower()) != None:
            return 'NGN'
        elif str(currency).lower() in ['us dollar', 'us']:
            return 'USD'
        elif str(currency).lower() in ['euro','europe']:
            return 'EUR'
        elif str(currency).lower() in ['pounds', 'pound']:
            return 'GBP'
        else:
            return currency.upper()

    def loan_classification_to_code(self, loan_classification)->str:
        """Takes in loan classification and returns the code corresponding to it. By default any loan classification not
        correctly specified is returned as watchlist-002"""
        if (len(str(loan_classification)) == 3) & (loan_classification in ['001', '002', '003', '004', '005']):
            return loan_classification
        elif str(loan_classification) in ['1', '2', '3', '4', '5']:
            return str(loan_classification).zfill(3)
        elif re.search('per', str(loan_classification).lower()) != None and str(loan_classification).lower() not in ['non performing', 'non-performing']:
            return '001'
        elif re.search('sub', str(loan_classification).lower()) != None or re.search('sub standard', str(loan_classification).lower()) != None:
            return '003'
        elif re.search('wat', str(loan_classification).lower()) != None or re.search(r'watchlist', str(loan_classification).lower()) != None:
            return '002'
        elif re.search('dou', str(loan_classification).lower()) != None or re.search(r'...dou[a-z]*', str(loan_classification).lower()) != None:
            return '004'
        elif re.search(r'l[a-z]*t', str(loan_classification).lower()) != None or re.search('loss', str(loan_classification).lower()) != None:
            return '005'
        else:
            return '002'
        
            
    def change_acct_status_to_code(self)->None:
        """"""
        self.frameObj[2] = self.frameObj[2].apply(lambda status_here: self.acct_status_to_code(status_here))

    def change_loan_classification_to_code(self)->None:
        """Change loan classification to code"""
        self.frameObj[18] = self.frameObj[18].apply(lambda loan_class: self.loan_classification_to_code(loan_class))

    def change_currency_to_code(self)->None:
        """Change currency column to code"""
        self.frameObj[9] = self.frameObj[9].apply(lambda currency: self.currency_to_code(currency))
    
    def change_account_status_date(self, date):
        self.frameObj[3] = date
        pass
    
    def reset_affected_column_heads(self):

        self.frameObj[2][0] = 'Account Status'
        self.frameObj[3][0] = 'Account status date'
        self.frameObj[9][0] = 'Loan Classification'
        self.frameObj[18][0] = 'Currency'