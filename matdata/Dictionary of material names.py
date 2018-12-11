#list of function names
#list of full name
#list of lists of what properties there are

#easy to update and if the index mactch up....

#creat a class for the material that with a name entered can pull up info


#----------------------------------------------------#
#Example with two materials

function_names = ('Inconel_718','AL_ALY_1100')
full name = ('Inconel (UNS N107718)','3003F Aluminum (UNS A93003)')
data_included = ((True,True),(True,False))

class Materials_Data(object):

    def __init__(self, material_name):

        self.material_name = material_name


    #line to check if the material name is included in list or close to something

    #check what data is included

    #pull functions ... is T known? or will it be known....

    #the problem is that there are materials with multiple different types. they need to be combined or another way has to be looked at.
        
#Full names with their names in a dictionary

#function_name   : actual name
#updated with conductivity and lin expansion so far 12/10/2018
material_names = {"Inconel_718":"Inconel 718 (UNS N107718)", "AL_ALY_1100":"1100 Aluminum (UNS A91100)", "AL_ALY_3003":" 3003F Aluminum (UNS A93003)",
                  "AL_ALY_5083":"5083 Aluminum (UNS A95083)", "AL_ALY_6061":"6061-T6 Aluminum (UNS A96061)", "AL_ALY_6063":"6063-T5 Aluminum (UNS A96063)",
                  "Balsa_lowdensity":"Balsa (density = 6 lb/ft3)", "Balsa_highdensity":"Balsa (density = 11 lb/ft3)", "Beechwood_Phenolic_90":"Beechwood-Phenolic (cross-laminate [0/90], grain direction)",
                  "Beechwood_Phenolic_90":"Beechwood-Phenolic (cross-laminate [0/90], flatwise)", "Beryllium_Copper":"Beryllium Copper", "Apiezon_N":"Apiezon N",
                  "Beryllium":"Beryllium", "Brass":"Brass (UNS C26000)", "Copper_OFHC_50":"OFHC Copper (UNS C10100/C10200) RRR=50",
                  "Copper_OFHC_100":"OFHC Copper (UNS C10100/C10200) RRR=100", "Copper_OFHC_150":"OFHC Copper (UNS C10100/C10200) RRR=150", "Copper_OFHC_300":"OFHC Copper (UNS C10100/C10200) RRR=300",
                  "Copper_OFHC_500":"OFHC Copper (UNS C10100/C10200) RRR=500", "Fiberglass_Epoxy_Normal":"G-10 CR (Fiberglass Epoxy)(Normal Direction)", "Fiberglass_Epoxy_Warp":"G-10 CR (Fiberglass Epoxy) (Warp Direction)",
                  "Glass_Fabric_He_Warp":"Glass Fabric - Polyester (Helium, warp Direction)", "Glass_Fabric_N_Warp":"Glass Fabric - Polyester (Nitrogen, Warp Direction)",
                  "Glass_Fabric_N_Normal":"Glass Fabric - Polyester (Nitrogen, normal direction)", "Invar":"Invar (Fe-36Ni) (UNS K93600)","Lead":"Lead","Molybdenum":"Molybdenum",
                  "Fe_225_Ni":" Nickel Steel (Fe-2.25 Ni)","Fe_325_Ni":"Nickel Steel (Fe-3.25 Ni) (UNS S20103)","Fe_50_Ni":"Nickel Steel (Fe-5.0 Ni) (UNS S20153)", "Fe_90_Ni":"Nickel Steel (Fe-9.0 Ni) (UNS S21800)",
                  "Platinum":"Platinum","Nylon":"Polyamide (Nylon)","Mylar":"Polyethylene Terephthalate (Mylar)","Kapton":"Polyimide (Kapton)", "SS_304":"304 Stainless (UNS S30400)", "SS_304L":"304L Stainless (UNS S30403)",
                  "SS_310":"310 Stainless (UNS S31000)", "SS_316":"16 Stainless (UNS S31600)", "Teflon":"Teflon", "Ti_6AL_4V":"Ti 6Al 4V (UNS R56400)","Titanium_15_3_3_3":"Titanium 15-3-3-3 Composition: Bal Ti, 14.88% V, 3.13 Cr, 2.88 Sn, 3.00 Al",
                  "Kevlar_Fiber":"Kevlar 49 (Fiber)", "Kevlar_Composite":"Kevlar 49 (Composite)", "Beechwood_Phenolic_uflat":"Beechwood-Phenolic (unidirectional, flatwise)",
                  "Beechwood_Phenolic_ugrain":"Beechwood-Phenolic (unidirectional, grain direction)", "Beryllium_a":"Beryllium a-axis", "Beryllium_c":"Beryllium c-axis", "Beryllium_poly":"Beryllium Polycrystalline",
                  "Glass_Mat_Epoxy_chop":"Glass mat-epoxy (chopped strand mat)", "Glass_Mat_Epoxy_cont":"Glass mat-epoxy (continuous strand)", "PVC":"PVC (Polyvinyl Chloride)", "Sapphire":"Sapphire",
                  "PVC_20d":"Polyvinyl Chloride (PVC) density: 20.02 kg/m3 (=1.25 lb/ft3 air fill gas)","PVC_56d":"Polyvinyl Chloride (PVC) density: 56.06 kg/m3 (=3.5 lb/ft3 CO2 blown)","Polystyrene_31d":"Polystyrene density: 31.88 kg/m3 (=1.99 lb/ft3 Freon filled)",
                  "Polystyrene_32d":"Polystyrene density: 32.04 kg/m3 (=2.0 lb/ft3)","Polystyrene_49d":"Polystyrene density: 49.98 kg/m3 (=3.12 lb/ft3)","Polystyrene_99d":"Polystyrene density: 99.96 kg/m3 (=6.24 lb/ft3)",
                  "Polyurethane_31d":"Polyurethane density: 31.88 kg/m3 (=1.99 lb/ft3 Freon filled)","Polyurethane_32d":"Polyurethane density: 32.04 kg/m3 (=2.0 lb/ft3 CO2 Filled)","Polyurethane_49d":"Polyurethane density: 49.02 kg/m3 (=3.06 lb/ft3 He Filled)",
                  "Polyurethane_64d":"Polyurethane density: 64.08 kg/m3 (=4.00 lb/ft3 Freon filled)","Polystyrene_51":"Polystyrene density: 51.42 kg/m3 (=3.21 lb/ft3)", "Polystyrene_102":"Polystyrene density: 102.2 kg/m3 (=6.38 lb/ft3)"}
