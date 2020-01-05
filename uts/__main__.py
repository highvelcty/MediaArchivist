import io
import subprocess
import sys
import threading

class StreamMon(threading.Thread):
    def __init__(self, instream: io.TextIOWrapper, outstream: io.TextIOWrapper):
        super().__init__()
        self._instream = instream
        self._outstream = outstream

    def run(self):
        for line in self._instream:
            self._outstream.write(line)

def run(args):
    proc = subprocess.Popen(args, bufsize=1, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            universal_newlines=True)
    stdoutmon = StreamMon(proc.stdout, sys.stdout)
    stderrmon = StreamMon(proc.stderr, sys.stderr)
    stdoutmon.start()
    stderrmon.start()
    return_code = proc.wait()
    stdoutmon.join()
    stderrmon.join()

    return return_code

# Run unit testing with coverage
args = ['coverage', 'run', '-m', 'unittest']
args.extend(sys.argv[1:])
return_code = run(args)

# Report coverage
args = ['coverage', 'html']
coverage_report_return_code = run(args)
if coverage_report_return_code:
    raise Exception('return code %d on coverage report' % coverage_report_return_code)

sys.exit(return_code)
