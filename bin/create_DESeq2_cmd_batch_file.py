#!/usr/bin/env python

import os, sys
import argparse
from string import Template

parser = argparse.ArgumentParser()
parser.add_argument("--memory", help="amount of ram [default=50G]", type=str, default='50G')
parser.add_argument("--template", help="name of template file [default=DESeq2.R]", type=str, default="DESeq2.R")
parser.add_argument("--numberOfControls", help="the number of control samples", type=str, default=3)
parser.add_argument("--numberOfExperimentals", help="the number of experimental samples", type=str, default=3)
parser.add_argument("--org", help="organism annotation database name [default='org.Mm.eg.db']", type=str, default="org.Mm.eg.db")
parser.add_argument("--dbkey", help="type of database key to retrieve gene symbol [default='ENTREZID']", type=str, default="ENTREZID")
parser.add_argument("--gProfilerkey", help="organism code to use with g:Profiler [default='mmusculus']", type=str, default="mmusculus")
parser.add_argument("--queue", help="job queue to submit the job [default=bbc]", type=str, default="bbc")
parser.add_argument("--prefix", help="prefix for output files [default=DESeq2]", type=str, default="DESeq2")
parser.add_argument("--datafile", help="name of data file containing gene count data [default=gene_cnt_matrix.tab]", type=str, default="gene_cnt_matrix.tab")
parser.add_argument("--strand", help="is data stranded? If not, do nothing. If so, enter either 1 or 2. See STAR Manual, Section 7", type=int, default=0)
parser.add_argument("--aligndir", help="name of alignment directory [default=align]", type=str, default="align")

args = parser.parse_args()

wd = os.path.dirname(os.path.realpath(__file__))

template_file = open(wd + "/../templates/" + args.template, 'r').read()

s = Template(template_file)

new_t = s.substitute(memory=args.memory, cntCont=args.numberOfControls, cntExp=args.numberOfExperimentals, prefix=args.prefix, datafile=args.datafile,\
        orgdb=args.org, jobqueue=args.queue, dbkey=args.dbkey, gProfilerkey=args.gProfilerkey, strand=args.strand, aligndir=args.aligndir)

print new_t
