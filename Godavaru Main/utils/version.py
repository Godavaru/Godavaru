def major():
    return "1"

def minor():
    return "5"

def patch():
    return "4"

def alpha():
    return False

def beta():
    return False

def getBotVersion():
    vers = "{}.{}.{}".format(major(), minor(), patch())
    if alpha() == True:
        botVers = vers+"_ALPHA"
    else:
        if beta() == True:
            botVers = vers+"_BETA"
        else:
            botVers = vers
    return botVers
