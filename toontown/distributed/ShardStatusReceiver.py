#Embedded file name: toontown.distributed.ShardStatusReceiver


class ShardStatusReceiver:

    def __init__(self, air):
        self.air = air
        self.shards = {}
        self.air.netMessenger.accept('shardStatus', self, self.handleShardStatus)
        self.air.netMessenger.send('queryShardStatus')

    def handleShardStatus(self, channel, status):
        self.shards.setdefault(channel, {}).update(status)

    def getShards(self):
        return self.shards
