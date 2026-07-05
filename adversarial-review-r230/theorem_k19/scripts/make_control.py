# Vacuity control: base + a SINGLE defect unit, WITHOUT the 80 good-fiber units.
# If this is fast-UNSAT, the defect alone is contradictory (vacuous). Expect SAT/UNKNOWN.
import sys, os
B = r'C:\Users\Hpedr\Documents\conway-99-graph\adversarial-review-r230'
sys.path.insert(0, os.path.join(B, 'scratchpad'))
from honest_flip_cnf import build_base_cnf
cnf, labels, edge_vars, npv = build_base_cnf()
# ce1 defect: NOT edge((0,2),(0,3)) -> literal -<var>; find the var
# edge_vars maps? inspect
import json
# ce1 canonical: labels (0,2),(0,3), a C4 share-edge, absent -> negative unit
# reuse manifest var id: ce1 literal was for (0,2)-(0,3); from earlier log ce3=-12 (0,2)(1,2); need ce1
m = json.load(open(os.path.join(B,'scratchpad','ladder','g2prime','final','manifest_certfull.json')))
ce1 = m['certificates']['ce1']['defect_unit']['literal']
print('ce1 defect literal:', ce1)
cnf.append([ce1])  # base + ONLY the defect unit
out = os.path.join(B,'scratchpad','ladder','g2prime','final','control_ce1_defect_only.cnf')
cnf.to_file(out)
print('wrote', out, 'clauses', len(cnf.clauses))
