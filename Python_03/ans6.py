#!/usr/bin/env python3
dna = 'GATGGGATTggggttttccccTCCCATGTGCTCAAGACTGGCGCTaaaaGttttGAGCTTCTCaaaaGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCggggACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGccccCTCTGAGTCAGGAAACAttttCAGACCTATGGAAACTACTTCCTGaaaaCAACGTTCTGTccccCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTccccGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTccccCCGTGGccccTGCACCAGCAGCTCCTACACCGGCGGccccTGCACCAGccccCTCCTGGccccTGTCATCTTCTGTCCCTTCCCAGaaaaCCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTccccTGCCCTCAACAAGATGttttGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACAccccCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGccccCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGccccTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACttttCG'
dna_upper = dna.upper()
print("count of T&t in dna:", dna_upper.count('T'))
dna_upper_replace = dna_upper.replace('T', 'U')
dna_replace = dna.replace('T', 'U')
#print(dna_upper_replace)
#print(dna_replace)

dna_test = 'AATTGGCCA'
dna_test_AT = dna_test.count('A') + dna_test.count('T')
print("dna_test_AT:", dna_test_AT)

dna_upper_AT = dna_upper.count('A') + dna_upper.count('T')
print("dna_upper_AT:", dna_upper_AT)

sub_dna_upper = dna_upper[99:200]
print(len(sub_dna_upper))
print("count of G in dna_upper:",sub_dna_upper.count('G'))

#dna_upper_rev = dna_upper[::-1]
replace_A = sub_dna_upper.replace('A', 't')
replace_T = replace_A.replace('T', 'a')
replace_G = replace_T.replace('G', 'c')
replace_C = replace_G.replace('C', 'g')
dna_comp = replace_C.upper()
dna_comp_rev = dna_comp[::-1]

print("original dna:", dna_upper[0:11])
print("complement:", dna_comp[0:11])
#print(dna_comp[0:11])
str_a = "Original Sequence"
str_b = "Complement"
str_c = "Reverse Complement"
seq_5 = "{} 5'{} 3'"
seq_3 = "{} 3'{} 5'"
space = "{:<19}"
str_a_f = space.format(str_a)
str_b_f = space.format(str_b)
str_c_f = space.format(str_c)
print(seq_5.format(str_a_f,sub_dna_upper),'\n',seq_3.format(str_b_f,dna_comp),'\n',seq_5.format(str_c_f,dna_comp_rev))

#find the start position of an EcoRI site in the above DNA sequence( 5'...GAATTC...3')
start = sub_dna_upper.find('GAATTC') + 1
print("start position of an EcoRI:", start)
print("end position of an EcoRI:", start+5 )
