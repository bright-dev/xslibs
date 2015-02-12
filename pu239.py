from numpy import logspace
#############################
### General specifcations ###
#############################
reactor = "lwr1g"
plugins = ['xsgen.pre', 'xsgen.buk']
threads = 3
solver = 'openmc+origen'
formats = ('brightlite',)
burn_regions = 1     # Number of burnup annular regions.
burn_time = 365*3  # Number of days to burn the material [days]
time_step = 100      # Time step by which to increment the burn [days]
# burn_times = [0, 3, 100, 200, 300, 400, 500, 600, 700, 800, 900]

verbosity = 100

# Set isotopes to track
from xsgen.nuc_track import load, transmute
core_load_nucs = load            # Initial core loading nuclide list or file
core_transmute_nucs = transmute  # Transmutation tracking nuclide list or file
core_transmute_nucs = ['cf252', 'u235', 'u238', 'o16', 'h1']  # Transmutation tracking nuclide list or file

# Load stock template string from char
# Having this allows users to specify other templates
#from xsgen.templates.lwr import serpent
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
    942390: 1.0
    }

initial_U235 = [0.03, 0.05]

#sensitivity_mass_fractions = [1.1, 0.9]

fuel_chemical_form = {                 #Dictionary of initial fuel loading.
    "IHM": 1.0,
    }

fuel_form_mass_weighted = True  # Flag that determines if the fuel form should be mass weighted (True) or atom weighted (False)

k_particles   = 500      #Number of particles to run per kcode cycle
k_cycles      = 130       #Number of kcode cycles to run
k_cycles_skip = 30        #Number of kcode cycles to run but not tally at the begining.

# group_structure = [1.0e-9, 10]
group_structure = logspace(-9, 1, 10)

# Temperature
# Should be a positive multiple of 300 K (ie 300, 600, 900, etc)
temperature = 600

track_nucs = [
              "Pu239",
]
