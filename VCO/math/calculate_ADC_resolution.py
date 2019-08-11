#!/usr/bin/env python3

print("ADC resolution calculator")
V_per_semitone = 1.0/12.0
print("\t1V/octave: 1 semitone = %8.5f V = %8.5f mV" % (V_per_semitone, 1000*V_per_semitone))
V_per_cent = V_per_semitone/100.0
print("\t%8.5f V (%8.5f mV) per cent" % (V_per_cent, 1000*V_per_cent))
ADC_input_range_V = 5.0
ADC_resolution_bits = 12.0
ADC_resolution_V = ADC_input_range_V/(2**ADC_resolution_bits)
print("\tADC: %d bits, %5.3f V input range:" % (ADC_resolution_bits, ADC_input_range_V))
ADC_resolution_cents = ADC_resolution_V/V_per_cent
print("\t\t%8.5f V/count = %8.5f cents/count" % (ADC_resolution_V,ADC_resolution_cents))

