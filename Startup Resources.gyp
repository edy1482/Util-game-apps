class component():

    def __init__(self, name, num=0):
        self.name = name
        self.num = num

components = {}
components['Interface Mod'] = component('Interface Mod')
components['Frontend Mod'] = component('Frontend Mod')
components['Backend Mod'] = component('Backend Mod')
components['Input Mod'] = component('Input Mod')
components['Storage Mod'] = component('Storage Mod')
components['Content Mod'] = component('Content Mod')
components['Video Mod'] = component('Video Mod')
components['Seo Mod'] = component('Seo Mod')
components['Email Mod'] = component('Email Mod')
components['Database Layer'] = component('Database Layer')
components['Notification Mod'] = component('Notification Mod')
components['Authentication Mod'] = component('Authentication Mod')

components['UI Comp'] = component('UI Comp')
components['Backend Comp'] = component('Backend Comp')
components['Network Comp'] = component('Network Comp')
components['Database Comp'] = component('Database Comp')
components['Video Comp'] = component('Video Comp')
components['Semantic Comp'] = component('Semantic Comp')
components['Smtp Comp'] = component('Smtp Comp')
components['Encryption Comp'] = component('Encryption Comp')
components['Filesystem Comp'] = component('Filesystem Comp')
components['l18n Comp'] = component('l18n Comp')
components['Search Alg Comp'] = component('Search Alg Comp')
components['Compression Comp'] = component('Compression Comp')

components['Blueprint Comp'] = component('Blueprint Comp')
components['Wireframe Comp'] = component('Wireframe Comp')
components['Graphics Comp'] = component('Graphics Comp')
components['UI El'] = component('UI El')
components['UI Set'] = component('UI Set')
components['Responsive UI'] = component('Responsive UI')

components['Virtual Hardware'] = component('Virtual Hardware')
components['Operating System'] = component('Operating System')
components['Firewall'] = component('Firewall')
components['Process Management'] = component('Process Management')
components['Continuous Integration'] = component('Continuous Integration')
components['Cron Job'] = component('Cron Job')
components['Virtual Container'] = component('Virtual Container')
components['Cluster'] = component('Cluster')
components['Swarm Management'] = component('Swarm Management')

def Frontend_Mod(x):
    components['Frontend Mod'].num += x
    UI_El(x)
    Interface_Mod(x)
    
def Interface_Mod(x):
    components['Interface Mod'].num += x
    UI_El(2*x)
    components['Wireframe Comp'].num += x

def Backend_Mod(x):
    components['Backend Mod'].num += x
    components['Backend Comp'].num += x
    components['Network Comp'].num += x

def Content_Mod(x):
    components['Content Mod'].num += x
    Frontend_Mod(x)
    Input_Mod(x)
    Backend_Mod(x)

def Input_Mod(x):
    components['Input Mod'].num += x 
    components['UI Comp'].num += x
    components['Backend Comp'].num += x

def Video_Mod(x):
    components['Video Mod'].num += x
    components['Video Comp'].num += x
    Frontend_Mod(x)
    Backend_Mod(x)

def Storage_Mod(x):
    components['Storage Mod'].num += x
    components['Filesystem Comp'].num += x
    components['Backend Comp'].num += x

def Email_Mod(x):
    components['Email Mod'].num += x
    components['Smtp Comp'].num += x
    components['Backend Comp'].num += x

def Database_Layer(x):
    components['Database Layer'].num += x
    components['Database Comp'].num += x
    components['Backend Comp'].num += x
    components['Network Comp'].num += x

def UI_Set(x):
    components['UI Set'].num += x
    components['Wireframe Comp'].num += 2*x
    UI_El(2*x)

def UI_El(x):
    components['UI El'].num += x
    components['Blueprint Comp'].num += x
    components['Graphics Comp'].num += x

def Count():
    for i in components:
        if components[i].num == 0:
            pass
        else:
            print(components[i].name,":",components[i].num)

def Video(x):
    Frontend_Mod(x)
    Video_Mod(x)

def Item_List(x):
    Backend_Mod(x)
    Frontend_Mod(x)
    Content_Mod(x)

def Sharing(x):
    Backend_Mod(2*x)
    Frontend_Mod(x)
    Input_Mod(x)
    Email_Mod(2*x)
    UI_Set(x)

def Offline(x):
    Backend_Mod(2*x)
    Frontend_Mod(x)
    Storage_Mod(2*x)
    Database_Layer(2*x)
    UI_Set(x)

def Virtual_Container(x):
    components['Virtual Container'].num += x
    components['Virtual Hardware'].num += x
    components['Operating System'].num += x
    components['Process Management'].num += x
    components['Continuous Integration'].num += x
    components['Cron Job'].num += x

def Cluster(x):
    components['Cluster'].num += x
    Virtual_Container(3*x)
    components['Firewall'].num += 10*x

def Swarm(x):
    components['Swarm Management'].num += x
    Cluster(x)
    Virtual_Container(x)

def XServer(x):
    Virtual_Container(7*x)
    Cluster(5*x)
    Swarm(5*x)

XServer(1)
Count()