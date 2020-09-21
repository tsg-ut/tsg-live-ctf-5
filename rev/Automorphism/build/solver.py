#!/usr/bin/env python3
# coding: utf-8
import angr
import claripy

import sys
if len(sys.argv)>1:
    p = angr.Project(sys.argv[1],auto_load_libs=False,main_opts={'base_addr':0x400000})
else:
    p = angr.Project("../dist/Automorphism",auto_load_libs=False,main_opts={'base_addr':0x400000})

input_len = 32
flag_chars = [claripy.BVS('flag_%d' % i, 8) for i in range(input_len)]
flag = claripy.Concat( *flag_chars + [claripy.BVV(b'\n')])

addr_main=p.loader.find_symbol('main').rebased_addr
addr_win=p.loader.find_symbol('win').rebased_addr

st = p.factory.full_init_state(
    args=['../dist/Automorphism'],
    add_options=({
        angr.options.ZERO_FILL_UNCONSTRAINED_MEMORY
    }),
    stdin=flag,
    addr=addr_main
)

for k in flag_chars:
    st.solver.add(k<0x7f)
    st.solver.add(k > 0x20)
st.solver.add(flag_chars[0]==ord('T'))
st.solver.add(flag_chars[1]==ord('S'))
st.solver.add(flag_chars[2]==ord('G'))
st.solver.add(flag_chars[3]==ord('L'))
st.solver.add(flag_chars[4]==ord('I'))
st.solver.add(flag_chars[5]==ord('V'))
st.solver.add(flag_chars[6]==ord('E'))
st.solver.add(flag_chars[7]==ord('{'))
st.solver.add(flag_chars[31]==ord('}'))

sm = p.factory.simulation_manager(st)

sm.explore(find=addr_win)

print(sm.found[0].posix.dumps(0))

