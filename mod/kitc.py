"""
Python global variable database for KIT - colors (corporate design)
-> initialize your color palette in every code
=====
"""
def init():
#%% Set global parameters
    global white, transparent, \
        black, gray90, gray80, gray75, gray70, gray60, gray50, gray40,\
                gray30, gray25, gray20, gray15, gray10, gray5,\
        green, green90, green80, green75, green70, green60, green50, green40,\
            green30, green25, green20, green15, green10, green5,\
        blue, blue90, blue80, blue75, blue70, blue60, blue50, blue40,\
            blue30, blue25, blue20, blue15, blue10, blue5,\
        red, red90, red80, red75, red70, red60, red50, red40,\
            red30, red25, red20, red15, red10, red5,\
        yellow, yellow90, yellow80, yellow75, yellow70, yellow60, yellow50, yellow40,\
            yellow30, yellow25, yellow20, yellow15, yellow10, yellow5,\
        orange, orange90, orange80, orange75, orange70, orange60, orange50, orange40,\
            orange30, orange25, orange20, orange15, orange10, orange5,\
        lightgreen, lightgreen90, lightgreen80, lightgreen75, lightgreen70, lightgreen60, lightgreen50, lightgreen40,\
            lightgreen30, lightgreen25, lightgreen20, lightgreen15, lightgreen10, lightgreen5,\
        purple, purple90, purple80, purple75, purple70, purple60, purple50, purple40,\
            purple30, purple25, purple20, purple15, purple10, purple5,\
        brown, brown90, brown80, brown75, brown70, brown60, brown50, brown40,\
            brown30, brown25, brown20, brown15, brown10, brown5,\
        cyan, cyan90, cyan80, cyan75, cyan70, cyan60, cyan50, cyan40,\
            cyan30, cyan25, cyan20, cyan15, cyan10, cyan5, \
        cycle_black_grey, cycle_color_all, cycle_color_main
                
#%% Define KIT colors
    transparent = (1.0, 1.0, 1.0, 0.0)
    white = (1.0, 1.0, 1.0)
    
    black='#000000'
    gray90=(0.1, 0.1, 0.1)
    gray80=(0.2, 0.2, 0.2)
    gray75=(0.25, 0.25, 0.25)
    gray70=(0.3, 0.3, 0.3)
    gray60=(0.4, 0.4, 0.4)
    gray50=(0.5, 0.5, 0.5)
    gray40=(0.6, 0.6, 0.6)
    gray30=(0.7, 0.7, 0.7)
    gray25=(0.75, 0.75, 0.75)
    gray20=(0.8, 0.8, 0.8)
    gray15=(0.85, 0.85, 0.85)
    gray10=(0.9, 0.9, 0.9)
    gray5=(0.95, 0.95, 0.95)
    
    green='#009682'
    green90=(0.1, 0.6294, 0.5588)
    green80=(0.2, 0.6706, 0.6078)
    green75=(0.25, 0.6912, 0.6324)
    green70=(0.3, 0.7118, 0.6569)
    green60=(0.4, 0.7529, 0.7059)
    green50=(0.5, 0.7941, 0.7549)
    green40=(0.6, 0.8353, 0.8039)
    green30=(0.7, 0.8765, 0.8529)
    green25=(0.75, 0.8971, 0.8775)
    green20=(0.8, 0.9176, 0.902)
    green15=(0.85, 0.9382, 0.9265)
    green10=(0.9, 0.9588, 0.951)
    green5=(0.95, 0.9794, 0.9755)
    
    blue='#4664aa'
    blue90=(0.3471, 0.4529, 0.7)
    blue80=(0.4196, 0.5137, 0.7333)
    blue75=(0.4559, 0.5441, 0.75)
    blue70=(0.4922, 0.5745, 0.7667)
    blue60=(0.5647, 0.6353, 0.8)
    blue50=(0.6373, 0.6961, 0.8333)
    blue40=(0.7098, 0.7569, 0.8667)
    blue30=(0.7824, 0.8176, 0.9)
    blue25=(0.8186, 0.848, 0.9167)
    blue20=(0.8549, 0.8784, 0.9333)
    blue15=(0.8912, 0.9088, 0.95)
    blue10=(0.9275, 0.9392, 0.9667)
    blue5=(0.9637, 0.9696, 0.9833)
    
    red='#a22223'
    red90=(0.6718, 0.22, 0.2235)
    red80=(0.7082, 0.3067, 0.3098)
    red75=(0.7265, 0.35, 0.3529)
    red70=(0.7447, 0.3933, 0.3961)
    red60=(0.7812, 0.48, 0.4824)
    red50=(0.8176, 0.5667, 0.5686)
    red40=(0.8541, 0.6533, 0.6549)
    red30=(0.8906, 0.74, 0.7412)
    red25=(0.9088, 0.7833, 0.7843)
    red20=(0.9271, 0.8267, 0.8275)
    red15=(0.9453, 0.87, 0.8706)
    red10=(0.9635, 0.9133, 0.9137)
    red5=(0.9818, 0.9567, 0.9569)
    
    yellow='#fce500'
    yellow90=(0.9894, 0.9082, 0.1)
    yellow80=(0.9906, 0.9184, 0.2)
    yellow75=(0.9912, 0.9235, 0.25)
    yellow70=(0.9918, 0.9286, 0.3)
    yellow60=(0.9929, 0.9388, 0.4)
    yellow50=(0.9941, 0.949, 0.5)
    yellow40=(0.9953, 0.9592, 0.6)
    yellow30=(0.9965, 0.9694, 0.7)
    yellow25=(0.9971, 0.9745, 0.75)
    yellow20=(0.9976, 0.9796, 0.8)
    yellow15=(0.9982, 0.9847, 0.85)
    yellow10=(0.9988, 0.9898, 0.9)
    yellow5=(0.9994, 0.9949, 0.95)
    
    orange='#df9b1b'
    orange90=(0.8871, 0.6471, 0.1953)
    orange80=(0.8996, 0.6863, 0.2847)
    orange75=(0.9059, 0.7059, 0.3294)
    orange70=(0.9122, 0.7255, 0.3741)
    orange60=(0.9247, 0.7647, 0.4635)
    orange50=(0.9373, 0.8039, 0.5529)
    orange40=(0.9498, 0.8431, 0.6424)
    orange30=(0.9624, 0.8824, 0.7318)
    orange25=(0.9686, 0.902, 0.7765)
    orange20=(0.9749, 0.9216, 0.8212)
    orange15=(0.9812, 0.9412, 0.8659)
    orange10=(0.9875, 0.9608, 0.9106)
    orange5=(0.9937, 0.9804, 0.9553)
    
    lightgreen='#8cb63c'
    lightgreen90=(0.5941, 0.7424, 0.3118)
    lightgreen80=(0.6392, 0.771, 0.3882)
    lightgreen75=(0.6618, 0.7853, 0.4265)
    lightgreen70=(0.6843, 0.7996, 0.4647)
    lightgreen60=(0.7294, 0.8282, 0.5412)
    lightgreen50=(0.7745, 0.8569, 0.6176)
    lightgreen40=(0.8196, 0.8855, 0.6941)
    lightgreen30=(0.8647, 0.9141, 0.7706)
    lightgreen25=(0.8873, 0.9284, 0.8088)
    lightgreen20=(0.9098, 0.9427, 0.8471)
    lightgreen15=(0.9324, 0.9571, 0.8853)
    lightgreen10=(0.9549, 0.9714, 0.9235)
    lightgreen5=(0.9775, 0.9857, 0.9618)
    
    purple='#a3107c'
    purple90=(0.6753, 0.1565, 0.5376)
    purple80=(0.7114, 0.2502, 0.589)
    purple75=(0.7294, 0.2971, 0.6147)
    purple70=(0.7475, 0.3439, 0.6404)
    purple60=(0.7835, 0.4376, 0.6918)
    purple50=(0.8196, 0.5314, 0.7431)
    purple40=(0.8557, 0.6251, 0.7945)
    purple30=(0.8918, 0.7188, 0.8459)
    purple25=(0.9098, 0.7657, 0.8716)
    purple20=(0.9278, 0.8125, 0.8973)
    purple15=(0.9459, 0.8594, 0.9229)
    purple10=(0.9639, 0.9063, 0.9486)
    purple5=(0.982, 0.9531, 0.9743)

    brown='#a7822e'
    brown90=(0.6894, 0.5588, 0.2624)
    brown80=(0.7239, 0.6078, 0.3443)
    brown75=(0.7412, 0.6324, 0.3853)
    brown70=(0.7584, 0.6569, 0.4263)
    brown60=(0.7929, 0.7059, 0.5082)
    brown50=(0.8275, 0.7549, 0.5902)
    brown40=(0.862, 0.8039, 0.6722)
    brown30=(0.8965, 0.8529, 0.7541)
    brown25=(0.9137, 0.8775, 0.7951)
    brown20=(0.931, 0.902, 0.8361)
    brown15=(0.9482, 0.9265, 0.8771)
    brown10=(0.9655, 0.951, 0.918)
    brown5=(0.9827, 0.9755, 0.959)
    
    cyan='#23a1e0'
    cyan90=(0.2235, 0.6682, 0.8906)
    cyan80=(0.3098, 0.7051, 0.9027)
    cyan75=(0.3529, 0.7235, 0.9088)
    cyan70=(0.3961, 0.742, 0.9149)
    cyan60=(0.4824, 0.7788, 0.9271)
    cyan50=(0.5686, 0.8157, 0.9392)
    cyan40=(0.6549, 0.8525, 0.9514)
    cyan30=(0.7412, 0.8894, 0.9635)
    cyan25=(0.7843, 0.9078, 0.9696)
    cyan20=(0.8275, 0.9263, 0.9757)
    cyan15=(0.8706, 0.9447, 0.9818)
    cyan10=(0.9137, 0.9631, 0.9878)
    cyan5=(0.9569, 0.9816, 0.9939)
    