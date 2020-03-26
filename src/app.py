# Usage: python ./src/app.py ./data/src.txt ./data/result.txt
import sys
import os

if len(sys.argv) != 3:
    print("Usage: $python app.py <input file> <output file>")
    exit(1)

rfname = sys.argv[1]
wfname = sys.argv[2]
fcontents = ""

if os.path.exists(rfname):

    with open(rfname, "r") as readFile:
        fcontents = readFile.readlines()
        i = 1
        print("file contents:")
        for line in fcontents:
            print("  {}: {}".format(i, line))
            i = i + 1

    with open(wfname, "w") as writeFile:
        for line in fcontents:
            writeFile.write(line)
else:
    print("[error] file not found from container:{}".format(rfname))

print("Complete")