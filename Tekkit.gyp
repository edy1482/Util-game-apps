class solar():

    def mirror(self, x):
        glass = 3*x
        sn_fe_al = x
        glass = 0.5*glass
        sn_fe_al = 0.5*sn_fe_al
        print("You need",glass,"glass and",sn_fe_al,"tin/iron/aluminium ingots") 
        print("For",x,"mirrors")
        print("")

    def piston(self,x):
        cobble = 4*x
        planks = 3*x
        iron = x
        redstone = x
        print("You need",cobble,"cobble,",planks,"wooden planks,",iron,"iron ingots, and",redstone,"redstone") 
        print("For",x,"pistons")
        print("")
    
    def quartz_block(self,x):
        nether_quartz = 4*x
        print("You need",nether_quartz,"nether quartz")
        print("For",x,"quartz blocks")
        print("")

    def copper_block(self,x):
        copper = 9*x
        print("You need",copper,"copper ingots") 
        print("For",x,"copper blocks")
        print("")

    def glowstone_block(self,x):
        glowstone = 4*x
        print("You need",glowstone,"glowstone")
        print("For",x,"glowstone blocks")
        print("")
    
    def iron_block(self,x):
        iron = 9*x
        print("You need",iron,"iron ingots")
        print("For",x,"iron blocks")
        print("")

    def gold_block(self,x):
        gold = 9*x
        print("You need",gold,"gold ingots")
        print("For",x,"gold blocks")
        print("")

    def diamond_block(self,x):
        diamond = 9*x
        print("You need",diamond,"diamons")
        print("For",x,"diamond blocks")
        print("")

    def stick(self,x):
        planks = 2*x
        planks = 0.25*planks
        print("You need",planks,"wooden planks") 
        print("For",x,"sticks")
        print("")

    def redstone_torch(self,x):
        stick = x
        redstone = x
        print("You need",stick,"sticks, and",redstone,"redstone") 
        print("For",x,"redstone torches")
        print("")

    def redstone_repeater(self,x):
        stone = 3*x
        solar.redstone_torch(2*x)
        redstone = x
        print("You need",stone,"stone, and",redstone,"redstone")
        print("For",x,"redstone repeaters")
        print("")
    
    def clock(self,x):
        gold = 4*x
        redstone = 1*x
        print("You need",gold,"gold ingots, and",redstone,"redstone")
        print("For",x,"clocks")
        print("")

    def redstone_lamp(self,x):
        redstone = 4*x
        solar.glowstone_block(x)
        print("You need",redstone,"redstone")
        print("For",x,"redstone lamps")
        print("")

    def pho_I(self,x):
        glass = 3*x
        lapis = 3*x
        solar.mirror(3*x)
        print("You need",glass,"glass, and",lapis,"lapis lazuli") 
        print("For",x,"photovoltaic cell I's")
        print("")

    def pho_II(self,x):
        solar.pho_I(x)
        solar.mirror(2*x)
        lapis = 3*x
        clay = 3*x
        print("You need",lapis,"lapis lazuli, and",clay,"clay")
        print("For",x,"photovoltaic cell II's")
        print("")

    def pho_III(self,x):
        glass = 3*x
        glowstone = 3*x
        obsididan = 2*x
        solar.pho_II(x)
        print("You need",glass,"glass,",glowstone,"glowstone dust, and",obsididan,"obisdian")
        print("For",x,"photovoltaic cell III's")
        print("")

    def pho_IV(self,x):
        blaze_rod = 3*x
        glowstone = 2*x
        solar.diamond_block(x)
        solar.pho_III(x)
        solar.quartz_block(2*x)
        print("You need",blaze_rod,"blaze rods, and",glowstone,"glowstone")
        print("For",x,"phtovoltaic cell IV's")
        print("")

    def solar_I(self,x):
        planks = 5*x
        redstone = x
        solar.mirror(3*x)
        print("You need",planks,"wooden planks and",redstone,"redstone") 
        print("For",x,"solar I's")
        print("")

    def solar_II(self,x):
        solar.solar_I(8*x)
        solar.piston(x)
        print("For",x,"solar II's")
        print("")

    def solar_III(self,x):
        solar.solar_II(4*x)
        solar.copper_block(x)
        solar.redstone_repeater(x)
        solar.pho_I(3*x)
        print("For",x,"solar III's")
        print("")
    
    def solar_IV(self,x):
        solar.solar_III(4*x)
        solar.iron_block(x)
        solar.clock(x)
        solar.pho_II(3*x)
        print("For",x,"solar IV's")
        print("")
    
    def solar_V(self,x):
        solar.solar_IV(4*x)
        solar.pho_III(3*x)
        solar.gold_block(x)
        solar.redstone_lamp(x)
        print("For",x,"solar V's")
        print("")
    
    def solar_VI(self,x):
        solar.solar_V(4*x)
        solar.redstone_lamp(x)
        solar.diamond_block(x)
        solar.pho_IV(3*x)
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

    energy_input = 128
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