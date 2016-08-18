# -*- coding: utf-8 -*-
from Bio import AlignIO
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-input", action=store, dest=input, type=str)
parser.add_argument("-output", action=store, dest=output, type=str)
args = parser.parse_args()

AlignIO.convert(args.input, "clustal", args.output, "phylip-relaxed")
