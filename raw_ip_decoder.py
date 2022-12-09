real_ip = input("enter the ip address: ")
decoded_octets = real_ip.split(".")
proto = "https://"
raw_ip = 0;
multip_order = 24
for octet in decoded_octets:
    raw_ip+=int(octet)*2**multip_order
    multip_order-=8
print(proto+str(raw_ip))
