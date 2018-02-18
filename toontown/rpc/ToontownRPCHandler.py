#Embedded file name: toontown.rpc.ToontownRPCHandler
import datetime
from direct.distributed.MsgTypes import CLIENTAGENT_EJECT
from direct.distributed.PyDatagram import PyDatagram
from direct.stdpy import threading2
import re
from otp.distributed import OtpDoGlobals
from toontown.distributed.ShardStatusReceiver import ShardStatusReceiver
from toontown.rpc.ToontownRPCHandlerBase import *
from toontown.suit.SuitInvasionGlobals import INVASION_TYPE_NORMAL
from toontown.toon import ToonDNA
from toontown.toonbase import TTLocalizer
from toontown.uberdog.ClientServicesManagerUD import executeHttpRequest

class ToontownRPCHandler(ToontownRPCHandlerBase):

    def __init__(self, air):
        ToontownRPCHandlerBase.__init__(self, air)
        self.shardStatus = ShardStatusReceiver(air)

    @rpcmethod(accessLevel=COMMUNITY_MANAGER)
    def rpc_ping(self, data):
        return data

    @rpcmethod(accessLevel=SYSTEM_ADMINISTRATOR)
    def rpc_queryObject(self, doId):
        result = []
        unblocked = threading2.Event()

        def callback(dclass, fields):
            if dclass is not None:
                dclass = dclass.getName()
            result.extend([dclass, fields])
            unblocked.set()

        self.air.dbInterface.queryObject(self.air.dbId, doId, callback)
        unblocked.wait()
        return result

    @rpcmethod(accessLevel=SYSTEM_ADMINISTRATOR)
    def rpc_updateObject(self, doId, dclassName, newFields, oldFields = None):
        if dclassName not in self.air.dclassesByName:
            dclassName += 'UD'
            if dclassName not in self.air.dclassesByName:
                return False
        dclass = self.air.dclassesByName[dclassName]
        if oldFields is None:
            self.air.dbInterface.updateObject(self.air.dbId, doId, dclass, newFields)
            return True
        result = [True]
        unblocked = threading2.Event()

        def callback(fields):
            if fields is not None:
                result[0] = False
            unblocked.set()

        self.air.dbInterface.updateObject(self.air.dbId, doId, dclass, newFields, oldFields=oldFields, callback=callback)
        unblocked.wait()
        return result[0]

    @rpcmethod(accessLevel=SYSTEM_ADMINISTRATOR)
    def rpc_setField(self, doId, dclassName, fieldName, args = []):
        if dclassName not in self.air.dclassesByName:
            dclassName += 'UD'
            if dclassName not in self.air.dclassesByName:
                return False
        dclass = self.air.dclassesByName[dclassName]
        datagram = dclass.aiFormatUpdate(fieldName, doId, doId, self.air.ourChannel, args)
        self.air.send(datagram)
        return True

    @rpcmethod(accessLevel=SYSTEM_ADMINISTRATOR)
    def rpc_messageChannel(self, channel, message):
        dclass = self.air.dclassesByName['ClientServicesManagerUD']
        datagram = dclass.aiFormatUpdate('systemMessage', OtpDoGlobals.OTP_DO_ID_CLIENT_SERVICES_MANAGER, channel, 1000000, [message])
        self.air.send(datagram)

    @rpcmethod(accessLevel=SYSTEM_ADMINISTRATOR)
    def rpc_messageAll(self, message):
        self.rpc_messageChannel(10, message)

    @rpcmethod(accessLevel=SYSTEM_ADMINISTRATOR)
    def rpc_messageShard(self, shardId, message):
        districtId = shardId + 1
        channel = districtId << 32 | 2
        self.rpc_messageChannel(channel, message)

    @rpcmethod(accessLevel=MODERATOR)
    def rpc_messageStaff(self, message):
        self.rpc_messageChannel(OtpDoGlobals.OTP_STAFF_CHANNEL, message)

    @rpcmethod(accessLevel=MODERATOR)
    def rpc_messageUser(self, userId, message):
        accountId = self.rpc_getUserAccountId(userId)
        if accountId is not None:
            self.rpc_messageAccount(accountId, message)

    @rpcmethod(accessLevel=MODERATOR)
    def rpc_messageAccount(self, accountId, message):
        channel = accountId + 4307852197888L
        self.rpc_messageChannel(channel, message)

    @rpcmethod(accessLevel=MODERATOR)
    def rpc_messageAvatar(self, avId, message):
        channel = avId + 4299262263296L
        self.rpc_messageChannel(channel, message)

    @rpcmethod(accessLevel=SYSTEM_ADMINISTRATOR)
    def rpc_kickChannel(self, channel, code, reason):
        datagram = PyDatagram()
        datagram.addServerHeader(channel, self.air.ourChannel, CLIENTAGENT_EJECT)
        datagram.addUint16(code)
        datagram.addString(reason)
        self.air.send(datagram)

    @rpcmethod(accessLevel=SYSTEM_ADMINISTRATOR)
    def rpc_kickAll(self, code, reason):
        self.rpc_kickChannel(10, code, reason)

    @rpcmethod(accessLevel=SYSTEM_ADMINISTRATOR)
    def rpc_kickShard(self, shardId, code, reason):
        districtId = shardId + 1
        channel = districtId << 32 | 2
        self.rpc_kickChannel(channel, code, reason)

    @rpcmethod(accessLevel=MODERATOR)
    def rpc_kickUser(self, userId, code, reason):
        accountId = self.rpc_getUserAccountId(userId)
        if accountId is not None:
            self.rpc_kickAccount(accountId, code, reason)

    @rpcmethod(accessLevel=MODERATOR)
    def rpc_kickAccount(self, accountId, code, reason):
        channel = accountId + 4307852197888L
        self.rpc_kickChannel(channel, code, reason)

    @rpcmethod(accessLevel=MODERATOR)
    def rpc_kickAvatar(self, avId, code, reason):
        channel = avId + 4299262263296L
        self.rpc_kickChannel(channel, code, reason)

    @rpcmethod(accessLevel=MODERATOR)
    def rpc_banUser(self, userId, duration, reason):
        if reason not in ('hacking', 'language', 'other'):
            return False
        self.air.writeServerEvent('ban', userId, duration, reason)
        if duration > 0:
            now = datetime.date.today()
            release = str(now + datetime.timedelta(hours=duration))
        else:
            release = '0000-00-00'
        executeHttpRequest('accounts/ban/', Id=userId, Release=release, Reason=reason)
        self.rpc_kickUser(userId, 152, reason)
        return True

    @rpcmethod(accessLevel=MODERATOR)
    def rpc_banAccount(self, accountId, duration, reason):
        userId = self.rpc_getAccountUserId(accountId)
        return self.rpc_banUser(userId, duration, reason)

    @rpcmethod(accessLevel=MODERATOR)
    def rpc_banAvatar(self, avId, duration, reason):
        userId = self.rpc_getAvatarUserId(avId)
        return self.rpc_banUser(userId, duration, reason)

    @rpcmethod(accessLevel=MODERATOR)
    def rpc_getUserAccountId(self, userId):
        if str(userId) in self.air.csm.accountDB.dbm:
            return int(self.air.csm.accountDB.dbm[str(userId)])

    @rpcmethod(accessLevel=MODERATOR)
    def rpc_getUserAvatars(self, userId):
        accountId = self.rpc_getUserAccountId(userId)
        if accountId is not None:
            return self.rpc_getAccountAvatars(accountId)

    @rpcmethod(accessLevel=MODERATOR)
    def rpc_getUserDeletedAvatars(self, userId):
        accountId = self.rpc_getUserAccountId(userId)
        if accountId is not None:
            return self.rpc_getAccountDeletedAvatars(accountId)

    @rpcmethod(accessLevel=MODERATOR)
    def rpc_getAccountUserId(self, accountId):
        dclassName, fields = self.rpc_queryObject(accountId)
        if dclassName == 'Account':
            return fields['ACCOUNT_ID']

    @rpcmethod(accessLevel=MODERATOR)
    def rpc_getAccountAvatars(self, accountId):
        dclassName, fields = self.rpc_queryObject(accountId)
        if dclassName == 'Account':
            return fields['ACCOUNT_AV_SET']

    @rpcmethod(accessLevel=MODERATOR)
    def rpc_getAccountDeletedAvatars(self, accountId):
        dclassName, fields = self.rpc_queryObject(accountId)
        if dclassName == 'Account':
            return fields['ACCOUNT_AV_SET_DEL']

    @rpcmethod(accessLevel=MODERATOR)
    def rpc_getAvatarUserId(self, avId):
        accountId = self.rpc_getAvatarAccountId(avId)
        if accountId is not None:
            return self.rpc_getAccountUserId(accountId)

    @rpcmethod(accessLevel=MODERATOR)
    def rpc_getAvatarAccountId(self, avId):
        dclassName, fields = self.rpc_queryObject(avId)
        if dclassName == 'DistributedToon':
            return fields['setDISLid'][0]

    @rpcmethod(accessLevel=MODERATOR)
    def rpc_getAvatarAvatars(self, avId):
        accountId = self.rpc_getAvatarAccountId(avId)
        if accountId is not None:
            return self.rpc_getAccountAvatars(accountId)

    @rpcmethod(accessLevel=MODERATOR)
    def rpc_getAvatarDeletedAvatars(self, avId):
        accountId = self.rpc_getAvatarAccountId(avId)
        if accountId is not None:
            return self.rpc_getAccountDeletedAvatars(accountId)

    @rpcmethod(accessLevel=MODERATOR)
    def rpc_getAvatarDetails(self, avId):
        dclassName, fields = self.rpc_queryObject(avId)
        if dclassName == 'DistributedToon':
            result = {}
            result['name'] = fields['setName'][0]
            dna = ToonDNA.ToonDNA()
            dna.makeFromNetString(fields['setDNAString'][0])
            result['species'] = ToonDNA.getSpeciesName(dna.head)
            result['head-color'] = dna.headColor
            result['max-hp'] = fields['setMaxHp'][0]
            result['online'] = avId in self.air.friendsManager.onlineToons
            return result

    @rpcmethod(accessLevel=MODERATOR)
    def rpc_findAvatarsByName(self, needle):
        if not config.GetBool('want-mongo-client', False):
            return []
        if not needle:
            return []
        self.air.mongodb.astron.objects.ensure_index('fields.setName')
        exp = re.compile('.*%s.*' % needle, re.IGNORECASE)
        result = self.air.mongodb.astron.objects.find({'fields.setName._0': exp})
        return [ avatar['_id'] for avatar in result ]

    @rpcmethod(accessLevel=USER)
    def rpc_listShards(self):
        return self.shardStatus.getShards()

    @rpcmethod(accessLevel=ADMINISTRATOR)
    def rpc_startInvasion(self, shardId, suitDeptIndex = None, suitTypeIndex = None, flags = 0, type = INVASION_TYPE_NORMAL):
        self.air.netMessenger.send('startInvasion', [shardId,
         suitDeptIndex,
         suitTypeIndex,
         flags,
         type])

    @rpcmethod(accessLevel=ADMINISTRATOR)
    def rpc_stopInvasion(self, shardId):
        self.air.netMessenger.send('stopInvasion', [shardId])

    @rpcmethod(accessLevel=MODERATOR)
    def rpc_approveName(self, avId):
        newFields = {'WishNameState': 'APPROVED'}
        oldFields = {'WishNameState': 'PENDING'}
        return self.rpc_updateObject(avId, 'DistributedToonUD', newFields, oldFields=oldFields)

    @rpcmethod(accessLevel=MODERATOR)
    def rpc_rejectName(self, avId):
        newFields = {'WishNameState': 'REJECTED'}
        oldFields = {'WishNameState': 'PENDING'}
        return self.rpc_updateObject(avId, 'DistributedToonUD', newFields, oldFields=oldFields)
