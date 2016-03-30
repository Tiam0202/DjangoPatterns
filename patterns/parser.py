##################################################################################
##################################################################################

from django.db import models


class Guy(models.Model):
    aid = models.IntegerField()


class Core(models.Model):
    guy = models.OneToOneField(to=Guy)
    time_out = models.IntegerField()
    step_time_out = models.IntegerField()


class Middle(models.Model):
    ip = models.GenericIPAddressField()
    domain = models.URLField(max_length=100)
    uid = models.IntegerField(max_length=100)
    active = models.BooleanField()


class Channel(models.Model):
    uid = models.CharField(max_length=100)
    priority = models.IntegerField()
    num_connects = models.IntegerField()
    core = models.ForeignKey(Core)
    hosts = models.ManyToManyField(to=Middle, through="Host")

    class Meta:
        ordering = ["priority"]


class Host(models.Model):
    priority = models.IntegerField()
    channel = models.ForeignKey(to=Channel)
    middle = models.ForeignKey(to=Middle)

    class Meta:
        ordering = ["priority"]


##################################################################################
##################################################################################


class CoreDispatcher:
    data = 0

    def __init__(self, data):
        self._data = data

    def get_core_model(self, aid, ms):
        pass


##################################################################################
##################################################################################

class ChannelState:
    def __init__(self, num_connects, hosts, priority):
        self.error_list = []
        self.hosts = hosts
        self.priority = priority
        self.num_connects = num_connects

    def get_active_host(self):
        return self.hosts.index(1)

    def update_hosts(self, hosts, force=False):
        if force:
            self.hosts = hosts
        else:
            self.hosts = [host for host in hosts if middle_validate(host)]

    def errors(self):
        return self.error_list

    def calculate_connects(self, time_out, increment):
        return self.num_connects * ((time_out / increment) ** 2)


class HttpChannel(ChannelState):
    uid = 0x0001

    def pack_channel_info(self):
        return "&".join([host.decode('utf-16') for host in self.hosts])

    @staticmethod
    def channel_info(stream):
        from struct import unpack
        unpack("h", stream[0:2]),
        unpack("b", stream[3:4]),
        unpack("h", stream[5:7]),

    @staticmethod
    def mids(stream):
        from struct import unpack
        mids = []
        while True:
            if len(stream) - stream.rfind("#") > 2:
                mid = unpack("h", stream[stream.rfind("#") + 1:])
                mids.append(mid)
        return mids


def middle_validate(host):
    try:
        if host.startswith('.'):
            Middle.objects.get(domain=host)
        else:
            Middle.objects.get(ip=host)
        return True
    except Exception as e:
        print(e.__class__.__name__)
        return False

##################################################################################
##################################################################################

    # guy = Guy(aid=111111)
    # guy.save()
    #
    # core = Core(guy=Guy.objects.get(id=1), time_out=5000, step_time_out=10)
    # core.save()
    #
    # middle = Middle(active=True, domain="for http", ip="8.8.8.8", uid=1234)
    # middle.save()
    #
    # channel = Channel(uid=1, core=Core.objects.get(id=1), num_connects=15, priority=1)
    # channel.save()
    #
    # host = Host(priority=1, channel=Channel.objects.get(id=1), middle=Middle.objects.get(id=1))
    # host.save()
