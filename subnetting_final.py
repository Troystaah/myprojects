import sys
def make_ip_num(ip_str) :                                                                                                                      #ip into integer
    octets = ip_str.split(".")
    for x in range(4):
        octets[x] = int(octets[x])
        octets[x] = octets[x]<<(24-(8*x))
    ip_num = (octets[3]+octets[2]+octets[1]+octets[0])
    return(ip_num)

def make_ip_str(ip_num):                                                                                                                #ip into string
    octets = []
    for x in range(4):
        octets.append(ip_num>>(24 - (8*x)) & 0xff)
        octets[x] = str(octets[x])
    address_str = octets[0] + "." + octets[1] + "." + octets[2] + "." + octets[3]                                                                                                 #joining the ip string together but with . to sepearate each bit
    return address_str

def calculate(ip_address_str, cidr) :                                                                                                          #calculate different segments ip
    ip_address_int = make_ip_num(ip_address_str)
    hostbits = 32 - cidr
    Network_id = (ip_address_int >> hostbits) << hostbits
    Network_id_str = make_ip_str(Network_id)
    First_host = Network_id + 1
    Broadcast = (((Network_id >> hostbits) + 1) << hostbits) - 1
    Last_host = Broadcast - 1
    return (ip_address_int, Network_id, First_host, Last_host, Broadcast)

def pretty_print(my_tuple) :                                                                                                                      #print formatted ips into dotted decimal format
    print("ip_address =", make_ip_str(my_tuple[0]))                                                                                 #print command in defined function is necessary
    print("Network_id =", make_ip_str(my_tuple[1]))
    print("First_host =", make_ip_str(my_tuple[2]))
    print("Last_host =", make_ip_str(my_tuple[3]))
    print("Broadcast =", make_ip_str(my_tuple[4]))
    return (0)

if __name__ ==  '__main__':
    ip_str = "192.168.30.125"
    cidr = 24
    if len(sys.argv) == 3:
            if sys.argv[2].isdigit():
                ip_str = str(sys.argv[1])
                cidr = int(sys.argv[2])
                print(ip_str, cidr)


    my_tuple = calculate(ip_str, cidr)
    pretty_print(my_tuple)                                                                                                                             #do not need print command for pretty_print
