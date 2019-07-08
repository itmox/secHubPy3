import configparser

def parseConfig(path):
    config = configparser.ConfigParser()
    config.read(path)#path to the config file
    sections=config.sections()
    print  (sections)
   #a = all sections contained in the Config file
    for a in sections:
        print (a)
    #b= all keys contained in the section a
        for b in config[a]:
            print(b)
            #print the vaule
            print(b, config[a][b])

