#############################
### General specifcations ###
#############################
reactor = "lwr1g"
plugins = ['bright.xsgen.pre', 'bright.xsgen.buk']
solver = 'openmc+origen'
formats = ('brightlite',)
formats = ()
burn_regions = 1     # Number of burnup annular regions.
burn_time = 6 * 365  # Number of days to burn the material [days]    
time_step = 100      # Time step by which to increment the burn [days]

verbosity = 100

# Set isotopes to track
from bright.xsgen.nuc_track import load, transmute
core_load_nucs = load            # Initial core loading nuclide list or file
core_transmute_nucs = transmute  # Transmutation tracking nuclide list or file


# Load stock template string from char
# Having this allows users to specify other templates
#from bright.xsgen.templates.lwr import serpent
#xs_gen_template = serpent.xs_gen
#burnup_template = serpent.burnup


################################
### Unit Cell Sepcifications ###
################################
fuel_cell_radius = 0.410
void_cell_radius = 0.4185
clad_cell_radius = 0.475
unit_cell_pitch  = 0.65635 * 2.0 
unit_cell_height = 10.0

#fuel_density = [10.7, 10.7*0.9, 10.7*1.1]   # Denisty of Fuel
#fuel_density = [10.7*0.95, 10.7*1.05]   # Denisty of Fuel
fuel_density = 10.7
clad_density = 5.87                         # Cladding Density
cool_density = 0.73                         # Coolant Density

fuel_specific_power = 40.0 / 1000.0   # Power garnered from fuel [W / g]


###########################
### MCNPX Specification ###
###########################
# LEU
initial_heavy_metal = {     # Initial heavy metal mass fraction distribution
    922350: 0.04, 
    922380: 0.96, 
    }

#initial_U235 = [0.02, 0.04, 0.06]
initial_U235 = [0.03, 0.05]

#sensitivity_mass_fractions = [1.1, 0.9]

# UOX
fuel_chemical_form = {                 #Dictionary of initial fuel loading. 
    80160: 2.0, 
    "IHM": 1.0, 
    }	

fuel_form_mass_weighted = True  # Flag that determines if the fuel form should be mass weighted (True) or atom weighted (False)

k_particles   = 500      #Number of particles to run per kcode cycle
k_cycles      = 130       #Number of kcode cycles to run
k_cycles_skip = 30        #Number of kcode cycles to run but not tally at the begining.

group_structure = [1.0e-09, 10]

# Temperature
# Should be a positive multiple of 300 K (ie 300, 600, 900, etc)
temperature = 600

