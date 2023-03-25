def editorMiss(textInput):
    count =0
    for ch in textInput:
        if ((ch>='a' and ch<="z") or (ch>='A' and ch<='Z')):
            pass
        elif(ch>='0' and ch<=9):
            pass
        elif(ch==""):
            pass
        else:
            count=count+1
    return count
        