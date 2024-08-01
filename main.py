"""

    """

import pandas as pd
import vcf


def main():
    pass

    ##

    fp = '/var/genetics/ws/mahdimir/local/prj_data/40724_read_gt_from_VCF/inp/5816418_24053_0_0.dragen.hard-filtered.vcf.filtered.vcf'

    vcf_reader = vcf.Reader(open(fp, 'r'))

    ##
    i = 1
    for record in vcf_reader :
        print(record)
        i += 1

    print(i)


    ##

    fp = '/var/genetics/ws/mahdimir/local/prj_data/40701_Individual_WGS_filtering/inp/snps.lifted'

    df = pd.read_csv(fp, sep='\t', header=None)

    ##
    fp = '/var/genetics/ws/mahdimir/local/prj_data/40724_read_gt_from_VCF/inp/5816418_1.vcf'

    vcf_reader = vcf.Reader(open(fp, 'r'))

    ##
    i = 1
    for record in vcf_reader :
        print(record)
        # i += 1

    ##
    print(i)


    ##


    ##


    ##
