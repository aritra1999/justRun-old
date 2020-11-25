import random, os, string, time
from subprocess import Popen, PIPE, run

def run_code(code, input, lang):
    slug = "media/code/" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
    command = ""
    ext = ""

    open(slug + ".in", "x").write(input)

    if lang == "c_cpp":
        ext = ".cpp"
        open(slug + ".cpp", "x").write(code)
        command = "g++ " + slug + ".cpp -o " + slug + " && ./" + slug + " <" + slug + ".in> " + slug + ".out"
    else:
        return ("error", "Invalid language!", None, None, None)


    # Execute Code
    print("Running  Command")
    timeStart = time.time()

    # try:
    #     print("Run Complete: ", result.stdout.readline().strip())
    # except:
    #     print("Found Error!")
        # return ("error", "Error in execution!", e.output, None, None)
    timeEnd = time.time() - timeStart

    # os.remove(slug + ".in")
    # os.remove(slug + ext)

    # try:
    #     os.remove(slug)
    # except:
    #     return ("error", "Error in execution!", None, None, None)


    # Getting Output
    # try: output = open(slug + ".out", "r").read()
    # except: return ("error", "Error in execution!", None, None, None)
    # os.remove(slug + ".out")


    # Return Ouput
    # return ("success", "Code Run Successful!", output, timeEnd, 243)
    return ("success", "Code Run Successful!", "Hello World", timeEnd, 243)