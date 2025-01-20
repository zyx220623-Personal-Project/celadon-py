import os
import sys
def remove_aosp_for_celadon(file_path: str, file_end_path: str):
    file = open(file_path, "r")
    read = file.read().split("\n  <project ")
    file.close()
    file_end = ""
    a01 = 0
    for i in read:
        if "remote=" in i:
            if a01 != 0:file_end+="\n  <project "
            if "utf8" in i and a01 == 0:i = i.replace("utf8","utf-8")
            file_end+=i
        a01 += 1
    file = open(file_end_path,"w+")
    file.write(file_end)
    file.close()
    print("wrote")
def addlist(arg: list):
    re = ""
    len1 = len(arg)
    j = 0
    for i in arg:
        j += 1
        re+=i
        if j != len1:re+="."
    return re
def startMain(arg1, debug = False):
    arg2 = os.path.dirname(arg1)
    
    arg3: str = os.path.basename(arg1)
    arg4 = arg3.split(".")
    arg5 = addlist(arg4[:len(arg4)-1])
    arg6 = arg4[-1]
    arg7 = arg5+"_origin."+arg6
    arg8 = arg2 +"/"+ arg7
    if debug == False:
        os.rename(arg1,arg8)
        remove_aosp_for_celadon(arg8,arg1)
    else:
        print(arg2)
        print(arg7)
        print(arg8)
        print(arg1)
if "--debug" in sys.argv:startMain(sys.argv[1],True)
else:startMain(sys.argv[1])
    
            
