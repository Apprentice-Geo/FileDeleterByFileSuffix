import os
import sys
from pathlib import Path
class FileDelBySuf:
    def __init__(self):
        self.suffixs=None
        self.dryRun=True

    def setSuffixs(self,suffixs):
        if isinstance(suffixs, str):
            self.suffixs = {suffixs}
        else:
            self.suffixs = set(list(suffixs))

    def setDryRun(self,dryRun):
        self.dryRun=dryRun
    
    def getSuffix(self,fileName):
        name=Path(fileName).name
        for suf in self.suffixs:
            if len(suf)>=len(name):
                continue
            elif suf.startswith('.'):
                if name.endswith(suf):
                    return True
        return None
    
    def deleter(self,path):
        if not self.getSuffix(path):
            return
        if self.dryRun:
            print(f"[Dry Run] Deleted {path}")
            return
        try:
            os.remove(path)
            print(f"Deleted {path}")
        except Exception as e:
            print(f"Failed to delete {path}:{e}")
            
    def fileTraversal(self,path):
        if os.path.isfile(path):
            self.deleter(path)
            return
        if not os.path.isdir(path):
            print(f"Not found: {path}")
            return
        for root,dirs,files in os.walk(path):
            for file in files:
                fullPath=os.path.join(root,file)
                self.deleter(fullPath)
