import configparser

def readPropFiles():
    config = configparser.ConfigParser()
    config.read("config/mailService.ini")
    sections = config.sections()
    print (sections)
