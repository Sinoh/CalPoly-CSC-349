# Tests 2-approximations of metric TSP.
# CSC 349, Assignment 8
# Given tests, Fall '19

import re
import os
import tempfile
import subprocess
import unittest

import graph


class TestTSP(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        compile()

    def test01_in1(self):
        out, err = run("in1.txt")
        msg = "Testing \"in1.txt\"; output to stderr, if any:\n%s" % err
        self.assertTrue(self.assertCycle(out, "in1.txt", msg) <= 42, msg)

    def test02_in2(self):
        out, err = run("in2.txt")
        msg = "Testing \"in2.txt\"; output to stderr, if any:\n%s" % err
        self.assertTrue(self.assertCycle(out, "in2.txt", msg) <= 6, msg)

    def test03_in3(self):
        out, err = run("in3.txt")
        msg = "Testing \"in3.txt\"; output to stderr, if any:\n%s" % err
        self.assertTrue(self.assertCycle(out, "in3.txt", msg) <= 16, msg)

    def assertCycle(self, out, graph_fname, msg):
        try:
            return parse_cycle(out, graph.read_graph(graph_fname))
        except Exception as e:
            raise AssertionError(msg) from e


def compile():
    """
    Compile a TSP approximation and ensure that all files are runnable
    """
    with open(os.devnull, "r") as dev_null:
        subprocess.call(
         "chmod +x *.sh && ./compile.sh",
         stdout = dev_null, stderr = dev_null,
         stdin = dev_null, shell = True)


def run(input_fname, _outs = {}, _errs = {}):
    """
    Run the TSP approximation and capture its output.
    :param input_fname: The name of an input file
    :return: A tuple containing the outputs to stdout and stderr
    """
    if input_fname not in _outs:
        try:
            with tempfile.TemporaryFile(mode = "w+") as out_file,\
                 tempfile.TemporaryFile(mode = "w+") as err_file,\
                 open(os.devnull, "r") as dev_null:

                subprocess.call(
                 "./run.sh %s" % input_fname,
                 stdout = out_file, stderr = err_file,
                 stdin = dev_null, shell = True)

                out_file.seek(0)
                _outs[input_fname] = out_file.read()
                err_file.seek(0)
                _errs[input_fname] = err_file.read()

        except Exception as e:
            if input_fname not in _outs:
                _outs[input_fname] = ""
            if input_fname not in _errs:
                _errs[input_fname] = "%s: %s" % (type(e).__name__, str(e))

    return (_outs[input_fname], _errs[input_fname])


def parse_cycle(raw_out, graph_g):
    """
    Parse a Hamiltonian cycle from raw output.
    :param raw_out: The raw output of the TSP approximation
    :param graph_g: The graph in which TSP was approximated
    :return: The weight of the cycle, raising an exception if not Hamiltonian
    """
    raw_cycle = re.match("^Hamiltonian cycle of weight (\d+):\s+"
                         "([\d\s,]+)\s+$", raw_out)

    try:
        weight = int(raw_cycle.group(1))
        cycle = [int(v) for v in re.split(",\s*", raw_cycle.group(2))]
        discovered = set()
    except Exception:
        raise RuntimeError("Failed to parse output.")

    for i in range(1, len(cycle)):
        if cycle[i] in discovered:
            raise ValueError("Cycle is not Hamiltonian.")
        elif cycle[i] not in graph_g:
            raise ValueError("Cycle contains nonexistent vertices.")
        else:
            discovered.add(cycle[i])
            weight -= graph_g[cycle[i - 1]][cycle[i]]

    if cycle[0] != cycle[-1]:
        raise ValueError("Cycle is not a cycle.")
    elif len(discovered) != len(graph_g.matrix):
        raise ValueError("Cycle is not Hamiltonian.")
    elif weight != 0:
        raise ValueError("Cycle does not match weight.")
    else:
        return int(raw_cycle.group(1))


if __name__ == "__main__":
    unittest.main()
