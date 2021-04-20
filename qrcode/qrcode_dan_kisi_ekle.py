import pyqrcode
import vobject

j = vobject.vCard()
o = j.add('fn')
o.value = "AAAA BBBB"

o = j.add('n')
o.value = vobject.vcard.Name( family='BBBB', given='AAAA' )

o = j.add('tel')
o.type_param = "cell"
o.value = '00112233445566

o=j.add('email')
o.type_param = 'INTERNET'
o.value = 'aaaabbbb@gmail.com'


data =j.serialize()


number = pyqrcode.create(data)
number.png('qrcode/xyz.png', scale=6)