# finctopmns are bock Of codes  that run when called

def banner_grab(ip, port):
    """ Return A Banner String or None"""
    pass # if a functons is eclaed withno code block

def  is_valid_ip(ip):
    parts = ip.split(".") # split() method divides a string into a list or an Array
    if len(parts) != 4:  #  A valid Ip must have four section if the section are not equal to 4 then the Ip is not Valid
        return  False # retuen Fals
    return all(0 <= int(p)  <= 255 for p in parts) # check each of the sections if the number is not betwen the range 0 to 255 then  the IP is not vlaid  

print (is_valid_ip("192.168.6.1")) #True
print (is_valid_ip("999.1.1.1"))  # false