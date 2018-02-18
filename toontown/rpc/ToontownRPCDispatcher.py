#Embedded file name: toontown.rpc.ToontownRPCDispatcher
from direct.directnotify.DirectNotifyGlobal import directNotify
from toontown.toonbase import ToonPythonUtil as PythonUtil

class ToontownRPCDispatcher:
    notify = directNotify.newCategory('ToontownRPCDispatcher')

    def __init__(self, handler):
        self.handler = handler

    def dispatch(self, request):
        if not isinstance(request.method, basestring) or not isinstance(request.params, (tuple, list, dict)):
            request.error(-32600, 'Invalid Request')
            return
        method = getattr(self.handler, 'rpc_' + request.method, None)
        if method is None:
            request.error(-32601, 'Method not found')
            return
        token = None
        if isinstance(request.params, dict):
            token = request.params.get('token')
            del request.params['token']
        elif len(request.params) > 0:
            token = request.params[0]
            params = request.params[1:]
        if not isinstance(token, basestring):
            request.error(-32000, 'No token provided')
            return
        error = self.handler.authenticate(token, method)
        if error is not None:
            request.error(*error)
            return
        try:
            if isinstance(params, dict):
                request.result(method(**params))
            else:
                request.result(method(*params))
        except:
            request.error(-32603, PythonUtil.describeException())
