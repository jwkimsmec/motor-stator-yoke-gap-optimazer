import math

# Function to calculate motor parameters
def calculate_induction_motor_parameters():
    horsepower = 1  # in HP
    input_voltage = 110  # in Volts
    frequency = 60  # in Hz
    target_efficiency = 0.9  # efficiency
    synchronous_speed = 1746  # in RPM
    slip = 3  # percentage
    wire_gauge = "16 AWG"
    insulation_class = "F"
    full_load_torque = 5  # in Nm
    starting_torque = 6  # in Nm
    mount_type = "foot"
    stator_diameter = 0.06  # in meters
    core_diameter = 0.01  # in meters
    air_gap = 0.2  # in mm
    core_area = 20  # in cm^2
    enclosure = "TEFC"
    rotor_type = "squirrel cage"
    copper_bar_count = 24
    stator_slot_number = 36
    turns_per_slot = 20
    stator_to_yoke_gap = 0.008  # in meters (8 mm gap)

    watts_per_hp = 746  # 1 HP = 746 Watts
    power_factor = 0.85  # Estimated power factor for general induction motor
    stator_radius = stator_diameter / 2
    air_gap_m = air_gap / 1000  # Convert air gap to meters

    # Flux density and magnetic flux calculated based on gap optimization
    flux_density = 1.45  # Tesla (default optimized flux density)
    magnetic_flux = flux_density * core_area * 1e-4  # Weber (magnetic flux based on gap)
    
    # Mechanical power output
    output_power = horsepower * watts_per_hp  # Mechanical output power in watts
    input_power = output_power / target_efficiency  # Considering target efficiency
    rated_speed = synchronous_speed * (1 - (slip / 100))  # Rated speed at given slip
    running_current = input_power / (math.sqrt(3) * input_voltage * power_factor)  # For three-phase system
    starting_current = running_current * 5  # Typically 5 times running current during startup
    rotor_diameter = stator_diameter - 2 * air_gap_m  # Rotor diameter based on stator gap
    wire_diameter = 1.29  # mm (AWG 16 wire)
    total_turns = stator_slot_number * turns_per_slot  # Total turns in stator windings
    core_cross_sectional_area = core_area  # Core area
    thermal_overload_rating = running_current * 1.25  # Thermal overload rating (25% above full-load current)
    rated_torque = (output_power * 60) / (2 * math.pi * rated_speed)  # Torque based on rated power

    # Return motor parameters
    return {
        "Output Power (Watts)": output_power,
        "Input Power (Watts)": input_power,
        "Rated Speed (RPM)": rated_speed,
        "Running Current (Amps)": running_current,
        "Starting Current (Amps)": starting_current,
        "Rotor Diameter (m)": rotor_diameter,
        "Copper Wire Gauge": wire_gauge,
        "Copper Wire Diameter (mm)": wire_diameter,
        "Total Turns (Turns)": total_turns,
        "Turns per Slot": turns_per_slot,
        "Stator Slot Number": stator_slot_number,
        "Core Cross-Sectional Area (cm^2)": core_cross_sectional_area,
        "Thermal Overload Rating (Amps)": thermal_overload_rating,
        "Enclosure Type": enclosure,
        "Insulation Class": insulation_class,
        "Rotor Type": rotor_type,
        "Copper Bar Count": copper_bar_count,
        "Mount Type": mount_type,
        "Stator Diameter (m)": stator_diameter,
        "Core Diameter (m)": core_diameter,
        "Air Gap (m)": air_gap_m,
        "Full-Load Torque (Nm)": full_load_torque,
        "Rated Torque (Nm)": rated_torque,
        "Stator-to-Yoke Gap (m)": stator_to_yoke_gap,
        "Flux Density (T)": flux_density,
        "Magnetic Flux (Wb)": magnetic_flux
    }

# Save motor parameters to a file without optimization
def save_motor_parameters():
    motor_parameters = calculate_induction_motor_parameters()

    output_filepath = "/mnt/mot-yoke-gap.dat"
    with open(output_filepath, "w") as file:
        for parameter, value in motor_parameters.items():
            file.write(f"{parameter}: {value}\n")

    return output_filepath

# Call function to save motor parameters
save_motor_parameters()
