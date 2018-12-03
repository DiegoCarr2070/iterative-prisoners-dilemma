
team_name = 'Team Daniel Griffith' # We changed the names 
strategy_name = 'Genius'
strategy_description = "This strategy decides by always colluding, unless betrayed. If betrayed, then always betray. When always colluding randomly betray."
    # The description for the strategy was changed

def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

   
    if 'b' in their_history:
        return 'b'
    else:
            return 'c'
    if 'c' in my_history:
            return 'c'
''' This part of the code allows us to collude depending on if they betray or not'''


def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=1,
              result='b'):
         print 'Test passed'
    test_move(my_history='bbb',
              their_history='ccc', 
              my_score=1, 
              their_score=1,
              result='b')             