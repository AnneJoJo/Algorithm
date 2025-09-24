class DebtRecords(object): 
    def solution(self,debts):
        balance ={}
        for borrower,lender,amount in debts:
            balance[borrower] = balance.get(borrower, 0) - int(amount) 
            balance[lender] = balance.get(lender,0) + int(amount)
        maxdebt = min(balance.values()) 
        res=[]
        if maxdebt>=0:
            return res
        for country in balance:
            if maxdebt == balance[country]: 
                res.append(country)
        
        res.sort() 
        return res

debts = [['USA', 'Canada', 2], ['Canada', 'USA', 2], ['Mexico', 'Canada', 5],
         ['Canada', 'Mexico', 7],['USA', 'Canada', 4], ['USA', 'Mexico', 4]]   
d = DebtRecords()
print(d.solution(debts))