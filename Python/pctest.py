#coding=utf8
import struct
import binascii

uid1 = "868187020020125"
iccid1 = "8986031640200655519"

send_json_data = {"t":"1", "d":"%s" % uid1.encode("utf-8"), "iccid":"%s" % iccid1.encode("utf-8")}
#end_json_data = {"t":"1","d":"%s"%uid1.encode("utf-8")}
#send_json_data = json.dumps(json_data)
data_length = len(str(send_json_data))
print data_length

head = struct.pack("!2sHi","go",1,data_length)
print head

print head+str(send_json_data).encode("utf-8")

hex_data = binascii.b2a_hex(head+str(send_json_data).encode("utf-8"))

print hex_data
0
