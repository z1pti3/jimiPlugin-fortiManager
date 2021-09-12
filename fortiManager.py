import jimi

class _fortiManager(jimi.plugin._plugin):
    version = 0.1

    def install(self):
        # Register models
        jimi.model.registerModel("fortiManagerConnect","_fortiManagerConnect","_action","plugins.fortiManager.models.action")
        jimi.model.registerModel("fortiManagerGetADOMS","_fortiManagerGetADOMS","_action","plugins.fortiManager.models.action")
        jimi.model.registerModel("fortiManagerSetADOMS","_fortiManagerSetADOMS","_action","plugins.fortiManager.models.action")
        jimi.model.registerModel("fortiManagerGetObjects","_fortiManagerGetObjects","_action","plugins.fortiManager.models.action")
        jimi.model.registerModel("fortiManagerGetObject","_fortiManagerGetObject","_action","plugins.fortiManager.models.action")
        jimi.model.registerModel("fortiManagerSetObject","_fortiManagerSetObject","_action","plugins.fortiManager.models.action")
        return True

    def uninstall(self):
        # deregister models
        jimi.model.deregisterModel("fortiManagerConnect","_fortiManagerConnect","_action","plugins.fortiManager.models.action")
        jimi.model.deregisterModel("fortiManagerGetADOMS","_fortiManagerGetADOMS","_action","plugins.fortiManager.models.action")
        jimi.model.deregisterModel("fortiManagerSetADOMS","_fortiManagerSetADOMS","_action","plugins.fortiManager.models.action")
        jimi.model.deregisterModel("fortiManagerGetObjects","_fortiManagerGetObjects","_action","plugins.fortiManager.models.action")
        jimi.model.deregisterModel("fortiManagerGetObject","_fortiManagerGetObject","_action","plugins.fortiManager.models.action")
        jimi.model.deregisterModel("fortiManagerSetObject","_fortiManagerSetObject","_action","plugins.fortiManager.models.action")
        return True

    def upgrade(self,LatestPluginVersion):
        #if self.version < 0.2:
        return True
