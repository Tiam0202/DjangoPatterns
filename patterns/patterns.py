# coding: utf-8
import random
import codecs


class ChannelCtrl:

    uid = 4096
    mod = u'First command'
    status = 1
    sequence = 8
    rw = "read"
    data_size = 0
    address = codecs.decode('ffffffff', 'hex')
    offset = 0

    def __init__(self, sequence, data_size=0, address=None, offset=None, rw=None, uid=None, mod=None, status=None):

        if sequence != self.sequence:
            self.sequence = sequence

        if uid and uid in range(4096, 39321):
            self.uid = uid

        if mod:
            self.mod = mod

        if address:
            self.address = address

        if offset:
            self.offset = offset

        if data_size:
            self.data_size = data_size

        if status:
            self.status = status

        if rw:
            self.rw = rw

    def __str__(self):
        head = len(self.mod)+8
        if head < 25:
            head = 25
        head = "="*head
        return "%s\nMOD: \"%s\";\nUID: %s;\nSEQ: %s;\nSTS: " \
               "%s;\nR\W: %s;\nLEN: %s;\nMEM: %s;\nOFF: %s;\n%s\n" \
               % (head, self.mod, hex(self.uid), hex(self.sequence),
                  self.status, self.rw, self.data_size, self.address,
                  hex(self.offset), head)








if __name__ == '__main__':
    cc = ChannelCtrl(sequence=8, uid=10001, mod='DNS module', status=2)
    print(cc)



