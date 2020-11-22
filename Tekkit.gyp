class item():

    def __init__(self, name, num=0):
        self.name = name
        self.num = num

def mirror(x):
    glass = 3*x
    sn_fe_al = x
    glass = 0.5*glass
    sn_fe_al = 0.5*sn_fe_al
    print("You need",glass,"glass and",sn_fe_al,"tin/iron/aluminium ingots") 
    print("For",x,"mirrors")
    print("")

def piston(x):
    cobble = 4*x
    planks = 3*x
    iron = x
    redstone = x
    print("You need",cobble,"cobble,",planks,"wooden planks,",iron,"iron ingots, and",redstone,"redstone") 
    print("For",x,"pistons")
    print("")

def quartz_block(x):
    nether_quartz = 4*x
    print("You need",nether_quartz,"nether quartz")
    print("For",x,"quartz blocks")
    print("")

def copper_block(x):
    copper = 9*x
    print("You need",copper,"copper ingots") 
    print("For",x,"copper blocks")
    print("")

def glowstone_block(x):
    glowstone = 4*x
    print("You need",glowstone,"glowstone")
    print("For",x,"glowstone blocks")
    print("")

def iron_block(x):
    iron = 9*x
    print("You need",iron,"iron ingots")
    print("For",x,"iron blocks")
    print("")

def gold_block(x):
    gold = 9*x
    print("You need",gold,"gold ingots")
    print("For",x,"gold blocks")
    print("")

def diamond_block(x):
    diamond = 9*x
    print("You need",diamond,"diamons")
    print("For",x,"diamond blocks")
    print("")

def stick(x):
    planks = 2*x
    planks = 0.25*planks
    print("You need",planks,"wooden planks") 
    print("For",x,"sticks")
    print("")

def redstone_torch(x):
    stick = x
    redstone = x
    print("You need",stick,"sticks, and",redstone,"redstone") 
    print("For",x,"redstone torches")
    print("")

def redstone_repeater(x):
    stone = 3*x
    redstone_torch(2*x)
    redstone = x
    print("You need",stone,"stone, and",redstone,"redstone")
    print("For",x,"redstone repeaters")
    print("")

def clock(x):
    gold = 4*x
    redstone = 1*x
    print("You need",gold,"gold ingots, and",redstone,"redstone")
    print("For",x,"clocks")
    print("")

def redstone_lamp(x):
    redstone = 4*x
    glowstone_block(x)
    print("You need",redstone,"redstone")
    print("For",x,"redstone lamps")
    print("")

def pho_I(x):
    glass = 3*x
    lapis = 3*x
    mirror(3*x)
    print("You need",glass,"glass, and",lapis,"lapis lazuli") 
    print("For",x,"photovoltaic cell I's")
    print("")

def pho_II(x):
    pho_I(x)
    mirror(2*x)
    lapis = 3*x
    clay = 3*x
    print("You need",lapis,"lapis lazuli, and",clay,"clay")
    print("For",x,"photovoltaic cell II's")
    print("")

def pho_III(x):
    glass = 3*x
    glowstone = 3*x
    obsididan = 2*x
    pho_II(x)
    print("You need",glass,"glass,",glowstone,"glowstone dust, and",obsididan,"obisdian")
    print("For",x,"photovoltaic cell III's")
    print("")

def pho_IV(x):
    blaze_rod = 3*x
    glowstone = 2*x
    diamond_block(x)
    pho_III(x)
    quartz_block(2*x)
    print("You need",blaze_rod,"blaze rods, and",glowstone,"glowstone")
    print("For",x,"phtovoltaic cell IV's")
    print("")

def solar_I(x):
    planks = 5*x
    redstone = x
    mirror(3*x)
    print("You need",planks,"wooden planks and",redstone,"redstone") 
    print("For",x,"solar I's")
    print("")

def solar_II(x):
    solar_I(8*x)
    piston(x)
    print("For",x,"solar II's")
    print("")

def solar_III(x):
    solar_II(4*x)
    copper_block(x)
    redstone_repeater(x)
    pho_I(3*x)
    print("For",x,"solar III's")
    print("")

def solar_IV(x):
    solar_III(4*x)
    iron_block(x)
    clock(x)
    pho_II(3*x)
    print("For",x,"solar IV's")
    print("")

def solar_V(x):
    solar_IV(4*x)
    pho_III(3*x)
    gold_block(x)
    redstone_lamp(x)
    print("For",x,"solar V's")
    print("")
    
def solar_VI(x):
    solar_V(4*x)
    redstone_lamp(x)
    diamond_block(x)
    pho_IV(3*x)
    print("For",x,"solar VI's")
    print("")

def machine():

    m_c_e = {
        "zero":2,
        "one":3,
        "two":5,
        "three":8,
        "four":13,
        "five":20,
        "six":33,
        "seven":53,
        "eight":85,
        "nine":137,
        "ten":219,
        "eleven":351,
        "twelve":562,
        "thirteen":900,
        "fourteen":1441,
        "fifteen":2305,
        "sixteen":3689
        }
    e_f = {
        "zero":3,
        "one":4,
        "two":7,
        "three":12,
        "four":19,
        "five":31,
        "six":50,
        "seven":80,
        "eight":128,
        "nine":206,
        "ten":329,
        "eleven":527,
        "twelve":844,
        "thirteen":1351
        }

    energy_input = 2048
    num = []
    m_c_e_mach = 3
    e_f_mach = 1

    for i in m_c_e and e_f:
        x = m_c_e[i]
        y = e_f[i]
        w = (m_c_e_mach*x)+(e_f_mach*y)
        if w <= energy_input:
            z = energy_input - w
            num.append("x")
        else:
            print(z,"power left")
            break   
    print(len(num)-1,"overclockers each")

machine()