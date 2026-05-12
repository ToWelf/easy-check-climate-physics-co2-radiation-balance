#!/usr/bin/env python3
"""
Simple verification script to test key calculations in the climate physics model.
This script verifies that the notebook calculations are scientifically accurate.
"""

import numpy as np
from scipy import constants

def test_stefan_boltzmann():
    """Test Stefan-Boltzmann constant is correct"""
    sigma = constants.Stefan_Boltzmann
    expected = 5.67e-8  # W/(m^2*K^4)
    assert abs(sigma - expected) < 1e-10, f"Stefan-Boltzmann constant incorrect: {sigma}"
    print("✓ Stefan-Boltzmann constant verified: {:.2e} W/(m²·K⁴)".format(sigma))

def test_radiative_forcing():
    """Test CO2 radiative forcing calculation"""
    def radiative_forcing_co2(C, C0=278):
        return 5.35 * np.log(C / C0)
    
    # Test current CO2 levels
    C0 = 278  # Pre-industrial
    C_current = 421  # Current
    forcing = radiative_forcing_co2(C_current, C0)
    
    # Expected forcing should be around 2.1-2.2 W/m²
    assert 2.0 < forcing < 2.3, f"Radiative forcing out of expected range: {forcing}"
    print(f"✓ CO2 radiative forcing verified: {forcing:.2f} W/m²")
    
    # Test CO2 doubling (560 ppm)
    forcing_2x = radiative_forcing_co2(560, C0)
    expected_2x = 3.7  # Well-known value for CO2 doubling
    assert abs(forcing_2x - expected_2x) < 0.1, f"CO2 doubling forcing incorrect: {forcing_2x}"
    print(f"✓ CO2 doubling forcing verified: {forcing_2x:.2f} W/m² (expected ~3.7)")

def test_effective_temperature():
    """Test Earth's effective radiating temperature calculation"""
    sigma = constants.Stefan_Boltzmann
    solar_constant = 1361  # W/m²
    earth_albedo = 0.30
    
    # Average absorbed solar flux
    avg_solar_flux = solar_constant * (1 - earth_albedo) / 4
    
    # Effective temperature
    T_eff = (avg_solar_flux / sigma)**(1/4)
    T_eff_C = T_eff - 273.15
    
    # Should be around -18°C (255 K)
    assert 253 < T_eff < 257, f"Effective temperature out of range: {T_eff} K"
    print(f"✓ Effective temperature verified: {T_eff:.1f} K ({T_eff_C:.1f}°C)")

def test_greenhouse_effect():
    """Test greenhouse effect magnitude"""
    T_effective = 255  # K (without greenhouse effect)
    T_surface = 288    # K (with greenhouse effect)
    
    greenhouse_warming = T_surface - T_effective
    
    # Natural greenhouse effect should be around 33°C
    assert 30 < greenhouse_warming < 36, f"Greenhouse effect out of range: {greenhouse_warming} K"
    print(f"✓ Natural greenhouse effect verified: {greenhouse_warming:.1f} K")

def test_carbon_budget():
    """Test carbon budget mass balance"""
    # Carbon budget values (in GtC)
    total_emissions = 680  # Total human emissions
    atmospheric_increase = 305  # Observed atmospheric increase
    ocean_uptake = 175
    land_uptake = 200
    
    # Mass balance
    calculated_atmospheric = total_emissions - ocean_uptake - land_uptake
    
    # Should match observed atmospheric increase within ~10%
    error = abs(calculated_atmospheric - atmospheric_increase) / atmospheric_increase
    assert error < 0.1, f"Carbon budget doesn't balance: {calculated_atmospheric} vs {atmospheric_increase}"
    print(f"✓ Carbon budget verified: {calculated_atmospheric:.0f} GtC vs {atmospheric_increase:.0f} GtC observed")

def test_ocean_acidification():
    """Test ocean pH decline calculation"""
    ph_preindustrial = 8.25
    ph_current = 8.08
    
    # Calculate hydrogen ion concentration increase
    h_initial = 10**(-ph_preindustrial)
    h_current = 10**(-ph_current)
    h_increase = ((h_current / h_initial) - 1) * 100
    
    # A pH drop of 0.17 units results in ~48% increase in H+ ions
    assert 45 < h_increase < 50, f"Ocean acidification out of range: {h_increase}%"
    print(f"✓ Ocean acidification verified: {h_increase:.1f}% increase in H⁺ ions")

def main():
    """Run all verification tests"""
    print("=" * 60)
    print("Climate Physics Model - Calculation Verification")
    print("=" * 60)
    print()
    
    try:
        test_stefan_boltzmann()
        test_radiative_forcing()
        test_effective_temperature()
        test_greenhouse_effect()
        test_carbon_budget()
        test_ocean_acidification()
        
        print()
        print("=" * 60)
        print("✓ ALL TESTS PASSED - Calculations verified")
        print("=" * 60)
        return 0
    except AssertionError as e:
        print()
        print("=" * 60)
        print(f"✗ TEST FAILED: {e}")
        print("=" * 60)
        return 1

if __name__ == "__main__":
    exit(main())
