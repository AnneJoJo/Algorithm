class TransactionLogs(object)
    def solution(logs, threshold):
        """
        :type logs: List[str] :type threshold: int :rtype: List[str]
        """ 
        mp = collections.defaultdict(int) 
        for s in logs:
            x = s.split()
            sender =x[0]
            receiver = x[1]
            if sender == receiver :
                mp[sender]+=1 
            else:
                mp[sender]+=1 
                mp[receiver]+=1
        q=[]
        for user in mp:
            if mp[user]>=threshold: 
                q.append(user)
        q.sort() 
        return q