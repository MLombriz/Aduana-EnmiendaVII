# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 12:37:07 2021

Merge TXT files

@author: santt
"""

filenames = ['C:/VIIEnmienda/TXTs/CAP_01_NOTAS', 
             'C:/VIIEnmienda/TXTs/CAP_01',
             'C:/VIIEnmienda/TXTs/CAP_02_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_02',
             'C:/VIIEnmienda/TXTs/CAP_03_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_03',
             'C:/VIIEnmienda/TXTs/CAP_04_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_04',
             'C:/VIIEnmienda/TXTs/CAP_05_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_05',
             'C:/VIIEnmienda/TXTs/CAP_06_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_06',
             'C:/VIIEnmienda/TXTs/CAP_07_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_07',
             'C:/VIIEnmienda/TXTs/CAP_08_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_09_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_10',
             'C:/VIIEnmienda/TXTs/CAP_10_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_11_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_12_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_13_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_14_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_15_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_15',
             'C:/VIIEnmienda/TXTs/CAP_16_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_17_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_18_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_19_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_19',
             'C:/VIIEnmienda/TXTs/CAP_20_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_21_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_22_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_23_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_24',
             'C:/VIIEnmienda/TXTs/CAP_24_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_25_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_26_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_27_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_27',
             'C:/VIIEnmienda/TXTs/CAP_28_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_29_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_29',
             'C:/VIIEnmienda/TXTs/CAP_30_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_30',
             'C:/VIIEnmienda/TXTs/CAP_31_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_31',
             'C:/VIIEnmienda/TXTs/CAP_32_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_33_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_34_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_35_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_36_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_37_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_38_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_39_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_40_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_41_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_42_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_43_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_44_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_44',
             'C:/VIIEnmienda/TXTs/CAP_45_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_45',
             'C:/VIIEnmienda/TXTs/CAP_46_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_47_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_48_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_49_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_49',
             'C:/VIIEnmienda/TXTs/CAP_50_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_51_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_52_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_52',
             'C:/VIIEnmienda/TXTs/CAP_53_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_54_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_54',
             'C:/VIIEnmienda/TXTs/CAP_55_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_55',
             'C:/VIIEnmienda/TXTs/CAP_56_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_56',
             'C:/VIIEnmienda/TXTs/CAP_57_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_57',
             'C:/VIIEnmienda/TXTs/CAP_58_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_58',
             'C:/VIIEnmienda/TXTs/CAP_59_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_59',
             'C:/VIIEnmienda/TXTs/CAP_60_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_60',
             'C:/VIIEnmienda/TXTs/CAP_61_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_61',
             'C:/VIIEnmienda/TXTs/CAP_62_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_62',
             'C:/VIIEnmienda/TXTs/CAP_63_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_63',
             'C:/VIIEnmienda/TXTs/CAP_64_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_64',
             'C:/VIIEnmienda/TXTs/CAP_65_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_65',
             'C:/VIIEnmienda/TXTs/CAP_66_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_66',
             'C:/VIIEnmienda/TXTs/CAP_67_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_67_',
             'C:/VIIEnmienda/TXTs/CAP_68_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_68',
             'C:/VIIEnmienda/TXTs/CAP_69_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_69',
             'C:/VIIEnmienda/TXTs/CAP_70_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_71_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_72_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_73_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_73',
             'C:/VIIEnmienda/TXTs/CAP_74_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_75_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_76_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_78_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_78',
             'C:/VIIEnmienda/TXTs/CAP_79_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_80_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_81_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_82_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_82',
             'C:/VIIEnmienda/TXTs/CAP_83_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_84_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_84',
             'C:/VIIEnmienda/TXTs/CAP_85_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_85',
             'C:/VIIEnmienda/TXTs/CAP_86_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_87_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_87',
             'C:/VIIEnmienda/TXTs/CAP_88_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_89_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_90_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_90',
             'C:/VIIEnmienda/TXTs/CAP_91_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_92_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_93_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_94_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_95_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_96_NOTAS',
             'C:/VIIEnmienda/TXTs/CAP_97_NOTAS'
             ]
with open('C:/VIIEnmienda/TXTs/Compilacion.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
                
