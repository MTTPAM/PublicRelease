#Embedded file name: toontown.rpc.ToontownRPCHandlerBase
import base64
from direct.directnotify.DirectNotifyGlobal import directNotify
import json
import time
UNKNOWN = 700
USER = 100
COMMUNITY_MANAGER = 200
MODERATOR = 300
ARTIST = 400
PROGRAMMER = 500
ADMINISTRATOR = 600
SYSTEM_ADMINISTRATOR = 700

class RPCMethod:

    def __init__(self, accessLevel = UNKNOWN):
        self.accessLevel = accessLevel

    def __call__(self, method):
        method.accessLevel = self.accessLevel
        return method


rpcmethod = RPCMethod

class ToontownRPCHandlerBase:
    notify = directNotify.newCategory('ToontownRPCHandlerBase')

    def __init__(self, air):
        self.air = air

    def authenticate(self, token, method):
        try:
            token = base64.b64decode(token)
        except TypeError:
            return (-32001, 'Token decode failure')

        if not token or len(token) % 16 != 0:
            return (-32002, 'Invalid token length')
        rpcServerSecret = config.GetString('rpc-server-secret', 'tta36f75jb74sl8g')
        if len(rpcServerSecret) > AES.block_size:
            self.notify.error('rpc-server-secret is too big!')
        elif len(rpcServerSecret) < AES.block_size:
            self.notify.error('rpc-server-secret is too small!')
        iv = token[:AES.block_size]
        cipherText = token[AES.block_size:]
        cipher = AES.new(rpcServerSecret, mode=AES.MODE_CBC, IV=iv)
        try:
            token = json.loads(cipher.decrypt(cipherText).replace('\x00', ''))
            if 'timestamp' not in token or not isinstance(token['timestamp'], int):
                raise ValueError
            if 'accesslevel' not in token or not isinstance(token['accesslevel'], int):
                raise ValueError
        except ValueError:
            return (-32003, 'Invalid token')

        if token['accesslevel'] < method.accessLevel:
            return (-32005, 'Insufficient access')
