''' Circular dominoes chain algorithm '''
def can_chain(dominoes, chain=[]):
    ''' Recursive function chaining matching dominos. Return the chain if no dominos are left and
    last number matches first or return None otherwise. ''' 
    if not dominoes:
        return chain
    last_num = chain[-1][-1] if chain else dominoes[0][-1]
    for i, dom in enumerate(dominoes):
        if last_num in dom:
            ret = can_chain( dominoes[:i] + dominoes[i+1:], chain + [dom if dom[0] == last_num else dom[::-1]])
            if ret and ret[0][0] == ret[-1][-1]:
                return ret
            
print(can_chain(
    [(3,5),(5,2),(2,1)]
                ))