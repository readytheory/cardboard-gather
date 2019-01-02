def login_string(request) :
    try:
        if request.user.username in ('',None) :
            return 'Not Logged In | DECK '
        else:
            return "{} | DECK ".format(request.user.username)
    except Exception as e :
        return 'Login N/A | DECK'
    
        
