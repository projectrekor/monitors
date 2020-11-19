import base64
import gnupg

gpg = gnupg.GPG(gnupghome='/tmp/.gnupg')

# f = open('SHASUMS256.txt.sig', 'rb')

# encoded = base64.b64encode(data)
# verified = gpg.verify(encoded)

# sig = open('SHASUMS256.txt.sig', 'r')
# sig_data = sig.read()
# ver = open('SHASUMS256.txt', 'r')
# file_data = ver.read()
# verified = gpg.verify_file(sig_data, file_data)
stream = open("kubectl.asc", "rb")
verified = gpg.verify_file(stream)
print(verified.username)

# # mykey = gpg.search_keys('bgriggs@redhat.com', 'pool.sks-keyservers.net')
# # print(mykey)

# # Import GPG keys for node.js maintainers
# import_result = gpg.recv_keys(
#     'pool.sks-keyservers.net',
#     '4ED778F539E3634C779C87C6D7062848A1AB005C',
#     '94AE36675C464D64BAFA68DD7434390BDBE9B9C5',
#     '1C050899334244A8AF75E53792EF661D867B9DFA',
#     '71DCFD284A79C3B38668286BC97EC7A07EDE3FC1',
#     '8FCCA13FEF1D0C2E91008E09770F7A9A5AE15600',
#     'C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8',
#     'C82FA3AE1CBEDC6BE46B9360C43CEC45C17AB93C',
#     'DD8F2338BAE7501E3DD5AC78C273792F7D83545D',
#     'A48C2BEE680E841632CD4E44F07496B3EB3C1762',
#     '108F52B48DB57BB0CC439B2997B01419BD92F80A',
#     'B9E2F5981AA6E0CD28160D9FF13993A75599653C',
#     '9554F04D7259F04124DE6B476D5A82AC7E37093B',
#     'B9AE9905FFD7803F25714661B63B535A4C206CA9',
#     '77984A986EBC2AA786BC0F66B01FBB92821C587A',
#     '93C7E9E91B49E432C2F75674B0A78B0A6C481CF6',
#     '56730D5401028683275BD23C23EFEFE93C4CFFFE',
#     'FD3A5288F042B6850C66B31F09FE44734EB7990E',
#     '114F43EE0176B71C7BC219DD50A3051F888C628D',
#     '7937DFD2AB06298B2293C3187D33FF9D0246406D'
# )
# print(import_result.count)

# public_keys = gpg.list_keys()
# print(public_keys)

# # working!
# ascii_armored_public_keys = gpg.export_keys(
#     '4ED778F539E3634C779C87C6D7062848A1AB005C')

# message_bytes = ascii_armored_public_keys.encode('ascii')
# base64_bytes = base64.b64encode(message_bytes)
# base64_message = base64_bytes.decode('ascii')
# print(base64_message)
