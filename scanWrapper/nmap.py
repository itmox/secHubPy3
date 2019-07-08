import scan_wrapper_template

class nmap(scan_wrapper_template):
    def ___init___(self, name="a"):
        print (name)


    def start(self, ip, config, ):
        # nmap -oX outputfile.xml 192.168.1.1
        output_as_xml_parameter = '-oX'

