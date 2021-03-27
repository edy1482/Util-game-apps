class component():

    def __init__(self, name, employee, num=0, time=0):
        self.name = name
        self.employee = employee
        self.num = num
        self.time = time

components = {}

components['UI Comp'] = component('UI Comp', time=0.3, employee='Developer')
components['Backend Comp'] = component('Backend Comp', time=0.6, employee='Developer')
components['Network Comp'] = component('Network Comp', time=0.9, employee='Developer')
components['Database Comp'] = component('Database Comp', time=0.6, employee='Developer')
components['Video Comp'] = component('Video Comp', time=2.0, employee='Developer')
components['Semantic Comp'] = component('Semantic Comp', time=0.4, employee='Developer')
components['Smtp Comp'] = component('Smtp Comp', time=1.2, employee='Developer')
components['Encryption Comp'] = component('Encryption Comp', time=1.2, employee='Developer')
components['Filesystem Comp'] = component('Filesystem Comp', time=0.6, employee='Developer')
components['l18n Comp'] = component('l18n Comp', time=0.6, employee='Developer')
components['Search Alg Comp'] = component('Search Alg Comp', time=1.8, employee='Developer')
components['Compression Comp'] = component('Compression Comp', time=1.2, employee='Developer')

components['Blueprint Comp'] = component('Blueprint Comp', time=0.3, employee='Designer')
components['Wireframe Comp'] = component('Wireframe Comp', time=0.4, employee='Designer')
components['Graphics Comp'] = component('Graphics Comp', time=0.6, employee='Designer')
components['UI El'] = component('UI El', time=0.9, employee='Designer')
components['UI Set'] = component('UI Set', time=2.7, employee='Designer')
components['Responsive UI'] = component('Responsive UI', time=2.7, employee='Designer')
components['Doc Comp'] = component('Doc Comp', time=1.8, employee='Designer')
components['Design Guide'] = component('Design Guide', time=13.4, employee='Designer')

components['Interface Mod'] = component('Interface Mod', time=2.3, employee='Lead Developer')
components['Frontend Mod'] = component('Frontend Mod', time=4.4, employee='Lead Developer')
components['Backend Mod'] = component('Backend Mod', time=2.1, employee='Lead Developer')
components['Input Mod'] = component('Input Mod', time=0.9, employee='Lead Developer')
components['Storage Mod'] = component('Storage Mod', time=1.2, employee='Lead Developer')
components['Content Mod'] = component('Content Mod', time=5.7, employee='Lead Developer')
components['Video Mod'] = component('Video Mod', time=7.0, employee='Lead Developer')
components['Seo Mod'] = component('Seo Mod', time=3.7, employee='Lead Developer')
components['Email Mod'] = component('Email Mod', time=1.9, employee='Lead Developer')
components['Database Layer'] = component('Database Layer', time=2.2, employee='Lead Developer')
components['Notification Mod'] = component('Notification Mod', time=2.8, employee='Lead Developer')
components['Authentication Mod'] = component('Authentication Mod', time=3.4, employee='Lead Developer')
components['Pay Gate Mod'] = component('Pay Gate Mod', time=11.8, employee='Lead Developer')
components['Local Mod'] = component('Local Mod', time=3.9, employee='Lead Developer')
components['Search Mod'] = component('Search Mod', time=3.1, employee='Lead Developer')
components['Band Comp Mod'] = component('Band Comp Mod', time=2.8, employee='Lead Developer')
components['API Client Mod'] = component('API Client Mod', time=6.2, employee='Lead Developer')
components['Code Opt Mod'] = component('Code Opt Mod', time=13.9, employee='Lead Developer')

components['Virtual Hardware'] = component('Virtual Hardware', time=0.8, employee='SYS Admin')
components['Operating System'] = component('Operating System', time=0.8, employee='SYS Admin')
components['Firewall'] = component('Firewall', time=0.8, employee='SYS Admin')
components['Process Management'] = component('Process Management', time=1.2, employee='SYS Admin')
components['Continuous Integration'] = component('Continuous Integration', time=1.6, employee='SYS Admin')
components['Cron Job'] = component('Cron Job', time=0.6, employee='SYS Admin')
components['Virtual Container'] = component('Virtual Container', time=4.9, employee='SYS Admin')
components['Cluster'] = component('Cluster', time=22.4, employee='SYS Admin')
components['Swarm Management'] = component('Swarm Management', time=27.3, employee='SYS Admin')

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

def Code_Opt_Mod(x):
    components['Code Opt Mod'].num += x
    Backend_Mod(2*x)
    Frontend_Mod(2*x)
    Database_Layer(2*x)

def API_Client_Mod(x):
    components['API Client Mod'].num += x
    Backend_Mod(x)
    Database_Layer(x)
    components['Compression Comp'].num += 2*x

def UI_Set(x):
    components['UI Set'].num += x
    components['Wireframe Comp'].num += 2*x
    UI_El(2*x)

def UI_El(x):
    components['UI El'].num += x
    components['Blueprint Comp'].num += x
    components['Graphics Comp'].num += x

def Landing_Page(x):
    components['UI Comp'].num += x
    components['Backend Comp'].num += x
    components['Blueprint Comp'].num += x
    components['Graphics Comp'].num += x

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

def Live_Streaming(x):
    Backend_Mod(x)
    Frontend_Mod(x)
    components['Network Comp'].num += (4*x)

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

def DDOS(x):
    Code_Opt_Mod(x)
    API_Client_Mod(2*x)
    Swarm(x)
    components['Firewall'].num += 5*x

def Count():
    for i in components:
        if components[i].num == 0:
            pass
        else:
            print(components[i].name, ":", components[i].num, ":", components[i].employee)

def Prod():
    prod_times = {
        "dev" : 0,
        "designer": 0,
        "lead dev": 0,
        "SYS Ad": 0
    }
    employee_num = {
        "dev" : 0,
        "designer": 0,
        "lead dev": 0,
        "SYS Ad": 0
    }
    day_time = 7.0
    for i in components:
        if components[i].num == 0:
            pass
        else:
            if components[i].employee == 'Developer':
                prod_times['dev'] += components[i].num*components[i].time
            elif components[i].employee == 'Designer':
                prod_times["designer"] += components[i].num*components[i].time
            elif components[i].employee == 'Lead Developer':
                prod_times["lead dev"] += components[i].num*components[i].time
            elif components[i].employee == 'SYS Admin':
                prod_times["SYS Ad"] += components[i].num*components[i].time
    for i in prod_times and employee_num:
        if prod_times[i] == 0:
            pass
        else:
            employee_num[i] += 1
            if prod_times[i] > day_time:
                employ_diff = prod_times[i]/day_time
                employee_num[i] += round(employ_diff)
            elif prod_times[i] < day_time:
                pass
    total = 0
    for i in employee_num:
        total += employee_num[i]
    print(employee_num, 'total:', total)
               
DDOS(1)
Count()
Prod()