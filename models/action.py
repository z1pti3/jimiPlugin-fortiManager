from Crypto.Cipher.AES import key_size
import jimi

from plugins.fortiManager.includes import fortiManager

class _fortiManagerConnect(jimi.action._action):
    host = str()
    username = str()
    password = str()
    protocol = "https"
    adom = "root"
    certificate_verify = True

    def doAction(self,data):
        host = jimi.helpers.evalString(self.host,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        username = jimi.helpers.evalString(self.username,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        if self.password.startswith("ENC") and self.password != "":
            password = jimi.auth.getPasswordFromENC(self.password)
        protocol = jimi.helpers.evalString(self.protocol,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        adom = jimi.helpers.evalString(self.adom,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        fortiManagerClass = fortiManager._fortiManager(host,username,password,adom,protocol,self.certificate_verify)
        if fortiManagerClass.sessionid:
            data["persistentData"]["fortiManager"] = fortiManager._fortiManager(host,username,password,adom,protocol,self.certificate_verify)
            return { "result" : True, "rc" : 200, "msg" : "FortiManager Object Created" }
        return { "result" : False, "rc" : 403, "msg" : "FortiManager Object Failed to Create" }

    def setAttribute(self,attr,value,sessionData=None):
        if attr == "password" and not value.startswith("ENC "):
            self.password = "ENC {0}".format(jimi.auth.getENCFromPassword(value))
            return True
        return super(_fortiManagerConnect, self).setAttribute(attr,value,sessionData=sessionData)

class _fortiManagerGetADOMS(jimi.action._action):

    def doAction(self,data):
        try:
            fortiManagerClass = data["persistentData"]["fortiManager"]
            adoms = fortiManager.getAdoms(fortiManagerClass)
            return { "result" : True, "rc" : 200, "msg" : "Success", "adoms" : adoms }
        except KeyError:
            return { "result" : False, "rc" : 403, "msg" : "No FortiManager Object Created. Make sure you have run fortiManagerConnect before this object." }

class _fortiManagerSetADOMS(jimi.action._action):
    adom = str()

    def doAction(self,data):
        adom = jimi.helpers.evalString(self.adom,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        try:
            fortiManagerClass = data["persistentData"]["fortiManager"]
            fortiManagerClass.set_adom(adom)
            return { "result" : True, "rc" : 200, "msg" : "Success" }
        except KeyError:
            return { "result" : False, "rc" : 403, "msg" : "No FortiManager Object Created. Make sure you have run fortiManagerConnect before this object." }

class _fortiManagerGetObjects(jimi.action._action):
    objectType = "address"

    def doAction(self,data):
        objectType = jimi.helpers.evalString(self.objectType,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        try:
            fortiManagerClass = data["persistentData"]["fortiManager"]
            objects = fortiManager.getObjects(fortiManagerClass,objectType)
            return { "result" : True, "rc" : 200, "msg" : "Success", "objects" : objects }
        except KeyError:
            return { "result" : False, "rc" : 403, "msg" : "No FortiManager Object Created. Make sure you have run fortiManagerConnect before this object." }

class _fortiManagerGetObject(jimi.action._action):
    objectType = "address"
    objectName = str()

    def doAction(self,data):
        objectType = jimi.helpers.evalString(self.objectType,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        objectName = jimi.helpers.evalString(self.objectName,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] }).replace("/","\\/")
        try:
            fortiManagerClass = data["persistentData"]["fortiManager"]
            objectItem = fortiManager.getObject(fortiManagerClass,objectType,objectName)
            return { "result" : True, "rc" : 200, "msg" : "Success", "object" : objectItem }
        except KeyError:
            return { "result" : False, "rc" : 403, "msg" : "No FortiManager Object Created. Make sure you have run fortiManagerConnect before this object." }

class _fortiManagerSetObject(jimi.action._action):
    objectType = "address"
    objectName = str()
    objectData = dict()

    def doAction(self,data):
        objectType = jimi.helpers.evalString(self.objectType,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        objectName = jimi.helpers.evalString(self.objectName,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] }).replace("/","\\/")
        objectData = jimi.helpers.evalDict(self.objectData,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        try:
            fortiManagerClass = data["persistentData"]["fortiManager"]
            result = fortiManager.setObject(fortiManagerClass,objectType,objectName,objectData)
            return { "result" : result, "rc" : 0, "msg" : "" }
        except KeyError:
            return { "result" : False, "rc" : 403, "msg" : "No FortiManager Object Created. Make sure you have run fortiManagerConnect before this object." }
