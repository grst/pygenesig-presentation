from pygenesig.gini import GiniSignatureGenerator
from pygenesig.bioqc import BioQCSignatureTester
import os

config = {
    'expr_file': '/pstore/home/sturmg/projects/gtex-signatures/data_processed/v3/exprs_processed.npy',
    'target_file': '/pstore/home/sturmg/projects/gtex-signatures/data_processed/v3/target.csv',
    'rosetta_file': '/pstore/home/sturmg/projects/gtex-signatures/data_processed/v3/rosetta_processed.csv',
    'n_splits': 10,
    'signature_generator': GiniSignatureGenerator,
    'sg_kwargs': {"min_gini": .8, "max_rk": 3, "min_expr": 5, "max_rel_rk": None},
    'signature_tester': BioQCSignatureTester,
    'st_kwargs': {},
    'results_dir': './results'
}